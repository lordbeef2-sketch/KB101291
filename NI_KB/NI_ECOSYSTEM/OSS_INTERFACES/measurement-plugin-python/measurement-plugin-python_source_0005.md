# NI OSS SOURCE SNAPSHOT: measurement-plugin-python

<!--NI_OSS_SNAPSHOT repo=ni/measurement-plugin-python commit=2e57ec3e5bd703abc8690f8a46df62b28f0380e2 -->

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_datatypeinfo.py sha256=3ac130930a180e36b6810f546fc1abaaa897bddacec3d69688787c17b37618c5 bytes=4018 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_datatypeinfo.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_datatypeinfo.py`
- sha256: `3ac130930a180e36b6810f546fc1abaaa897bddacec3d69688787c17b37618c5`
- bytes: 4018

````python
from __future__ import annotations

from typing import NamedTuple

from google.protobuf import type_pb2
from ni.protobuf.types import array_pb2, xydata_pb2

from ni_measurement_plugin_sdk_service.measurement.info import (
    DataType,
    TypeSpecialization,
)


class DataTypeInfo(NamedTuple):
    """Class that represents the information for each of the :any:`DataType` enum values."""

    grpc_field_type: type_pb2.Field.Kind.ValueType
    """`Field.Kind` associated with the :any:`DataType`."""

    repeated: bool
    """Whether the :any:`DataType` is a repeated field."""

    type_specialization: TypeSpecialization = TypeSpecialization.NoType
    """Specific type when :any:`grpc_field_type` can have more than one use."""

    message_type: str = ""
    """The gRPC full name of the message type. 
    
    Required when :any:`grpc_field_type` is `Kind.TypeMessage`.
    Ignored for any other :any:`grpc_field_type` value.
    """


def get_type_info(data_type: DataType) -> DataTypeInfo:
    """Get information about a DataType."""
    data_type_info = _DATATYPE_TO_DATATYPEINFO_LOOKUP.get(data_type)
    if data_type_info is None:
        raise Exception(f"Data type information not found '{data_type}'")
    return data_type_info


_DATATYPE_TO_DATATYPEINFO_LOOKUP = {
    DataType.Int32: DataTypeInfo(type_pb2.Field.TYPE_INT32, False),
    DataType.Int64: DataTypeInfo(type_pb2.Field.TYPE_INT64, False),
    DataType.UInt32: DataTypeInfo(type_pb2.Field.TYPE_UINT32, False),
    DataType.UInt64: DataTypeInfo(type_pb2.Field.TYPE_UINT64, False),
    DataType.Float: DataTypeInfo(type_pb2.Field.TYPE_FLOAT, False),
    DataType.Double: DataTypeInfo(type_pb2.Field.TYPE_DOUBLE, False),
    DataType.Boolean: DataTypeInfo(type_pb2.Field.TYPE_BOOL, False),
    DataType.String: DataTypeInfo(type_pb2.Field.TYPE_STRING, False),
    DataType.Pin: DataTypeInfo(type_pb2.Field.TYPE_STRING, False, TypeSpecialization.Pin),
    DataType.Path: DataTypeInfo(type_pb2.Field.TYPE_STRING, False, TypeSpecialization.Path),
    DataType.Enum: DataTypeInfo(type_pb2.Field.TYPE_ENUM, False, TypeSpecialization.Enum),
    DataType.DoubleXYData: DataTypeInfo(
        type_pb2.Field.TYPE_MESSAGE,
        False,
        message_type=xydata_pb2.DoubleXYData.DESCRIPTOR.full_name,
    ),
    DataType.Double2DArray: DataTypeInfo(
        type_pb2.Field.TYPE_MESSAGE,
        False,
        message_type=array_pb2.Double2DArray.DESCRIPTOR.full_name,
    ),
    DataType.String2DArray: DataTypeInfo(
        type_pb2.Field.TYPE_MESSAGE,
        False,
        message_type=array_pb2.String2DArray.DESCRIPTOR.full_name,
    ),
    DataType.IOResource: DataTypeInfo(
        type_pb2.Field.TYPE_STRING, False, TypeSpecialization.IOResource
    ),
    DataType.Int32Array1D: DataTypeInfo(type_pb2.Field.TYPE_INT32, True),
    DataType.Int64Array1D: DataTypeInfo(type_pb2.Field.TYPE_INT64, True),
    DataType.UInt32Array1D: DataTypeInfo(type_pb2.Field.TYPE_UINT32, True),
    DataType.UInt64Array1D: DataTypeInfo(type_pb2.Field.TYPE_UINT64, True),
    DataType.FloatArray1D: DataTypeInfo(type_pb2.Field.TYPE_FLOAT, True),
    DataType.DoubleArray1D: DataTypeInfo(type_pb2.Field.TYPE_DOUBLE, True),
    DataType.BooleanArray1D: DataTypeInfo(type_pb2.Field.TYPE_BOOL, True),
    DataType.StringArray1D: DataTypeInfo(type_pb2.Field.TYPE_STRING, True),
    DataType.PinArray1D: DataTypeInfo(type_pb2.Field.TYPE_STRING, True, TypeSpecialization.Pin),
    DataType.PathArray1D: DataTypeInfo(type_pb2.Field.TYPE_STRING, True, TypeSpecialization.Path),
    DataType.EnumArray1D: DataTypeInfo(type_pb2.Field.TYPE_ENUM, True, TypeSpecialization.Enum),
    DataType.DoubleXYDataArray1D: DataTypeInfo(
        type_pb2.Field.TYPE_MESSAGE,
        True,
        message_type=xydata_pb2.DoubleXYData.DESCRIPTOR.full_name,
    ),
    DataType.IOResourceArray1D: DataTypeInfo(
        type_pb2.Field.TYPE_STRING, True, TypeSpecialization.IOResource
    ),
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_dotenvpath.py sha256=43d48f60c334e4f3b869bc32793eba69f4dc785c38d2c997675c7d55c094bd9a bytes=2381 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_dotenvpath.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_dotenvpath.py`
- sha256: `43d48f60c334e4f3b869bc32793eba69f4dc785c38d2c997675c7d55c094bd9a`
- bytes: 2381

````python
from __future__ import annotations

import inspect
import sys
import traceback
from pathlib import Path


def get_dotenv_search_path() -> Path:
    """Get the search path for loading the `.env` file."""
    # Prefer to load the `.env` file from the current directory or its parents.
    # If the current directory doesn't have a `.env` file, fall back to the
    # script/EXE path or the TestStand code module path.
    cwd = Path.cwd()
    if not _has_dotenv_file(cwd):
        if script_or_exe_path := _get_script_or_exe_path():
            return script_or_exe_path.resolve().parent
        if caller_path := _get_caller_path():
            return caller_path.resolve().parent
    return cwd


def _has_dotenv_file(dir: Path) -> bool:
    """Check whether the dir or its parents contains a `.env` file."""
    return (dir / ".env").exists() or any((p / ".env").exists() for p in dir.parents)


def _get_script_or_exe_path() -> Path | None:
    """Get the path of the top-level script or PyInstaller EXE, if possible."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable)

    main_module = sys.modules.get("__main__")
    if main_module:
        script_path = getattr(main_module, "__file__", "")
        if script_path:
            return Path(script_path)

    return None


def _get_caller_path() -> Path | None:
    """Get the path of the module calling into this package, if possible."""
    package_path = _get_package_path()
    for frame, _ in traceback.walk_stack(inspect.currentframe()):
        if frame.f_code.co_filename:
            module_path = Path(frame.f_code.co_filename)
            if _exists(module_path) and not module_path.is_relative_to(package_path):
                return module_path

    return None


# Path.exists() throws OSError when the path has invalid file characters.
# https://github.com/python/cpython/issues/79487
if sys.version_info >= (3, 10):

    def _exists(path: Path) -> bool:
        return path.exists()

else:

    def _exists(path: Path) -> bool:
        import os

        return os.path.exists(path)


def _get_package_path() -> Path:
    """Get the path of this package."""
    package = sys.modules[__package__]
    assert package.__file__ and package.__file__.endswith("__init__.py")
    return Path(package.__file__).parent
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_featuretoggles.py sha256=a6d47360c3be39b85c38f8f18fdc54af116625af2499ccab9067bae2c8b93bf0 bytes=4723 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_featuretoggles.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_featuretoggles.py`
- sha256: `a6d47360c3be39b85c38f8f18fdc54af116625af2499ccab9067bae2c8b93bf0`
- bytes: 4723

````python
"""Measurement plug-in feature toggles."""

from __future__ import annotations

import functools
import sys
from enum import Enum
from typing import TYPE_CHECKING, Callable, TypeVar

from ni_measurement_plugin_sdk_service._configuration import _PREFIX, _config

if TYPE_CHECKING:
    if sys.version_info >= (3, 10):
        from typing import ParamSpec
    else:
        from typing_extensions import ParamSpec

    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self

    _P = ParamSpec("_P")
    _T = TypeVar("_T")


# Based on the recipe at https://docs.python.org/3/howto/enum.html
class _OrderedEnum(Enum):
    def __ge__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value >= other.value
        return NotImplemented

    def __gt__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value > other.value
        return NotImplemented

    def __le__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value <= other.value
        return NotImplemented

    def __lt__(self, other: Self) -> bool:
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented


class CodeReadiness(_OrderedEnum):
    """Indicates whether code is ready to be supported."""

    RELEASE = 0
    NEXT_RELEASE = 1
    INCOMPLETE = 2
    PROTOTYPE = 3


def _init_code_readiness_level() -> CodeReadiness:
    if _config(f"{_PREFIX}_ALLOW_INCOMPLETE", default=False, cast=bool):
        return CodeReadiness.INCOMPLETE
    elif _config(f"{_PREFIX}_ALLOW_NEXT_RELEASE", default=False, cast=bool):
        return CodeReadiness.NEXT_RELEASE
    else:
        return CodeReadiness.RELEASE


# This is not public because `from _featuretoggles import CODE_READINESS_LEVEL`
# is incompatible with the patching performed by the use_code_readiness mark.
_CODE_READINESS_LEVEL = _init_code_readiness_level()


def get_code_readiness_level() -> CodeReadiness:
    """Get the current code readiness level.

    You can override this in tests by specifying the ``use_code_readiness``
    mark.
    """
    return _CODE_READINESS_LEVEL


class FeatureNotSupportedError(Exception):
    """The feature is not supported at the current code readiness level."""


class FeatureToggle:
    """A run-time feature toggle."""

    name: str
    """The name of the feature."""

    readiness: CodeReadiness
    """The code readiness at which this feature is enabled."""

    def __init__(self, name: str, readiness: CodeReadiness) -> None:
        """Initialize the feature toggle."""
        assert name == name.upper()
        self.name = name
        self.readiness = readiness
        self._is_enabled_override = None
        # Only read the env var at initialization time.
        if _config(f"{_PREFIX}_ENABLE_{name}", default=False, cast=bool):
            self._is_enabled_override = True

    @property
    def is_enabled(self) -> bool:
        """Indicates whether the feature is currently enabled.

        You can enable/disable features in tests by specifying the
        ``enable_feature_toggle`` or ``disable_feature_toggle`` marks.
        """
        if self._is_enabled_override is not None:
            return self._is_enabled_override
        return self.readiness <= get_code_readiness_level()

    def _raise_if_disabled(self) -> None:
        if self.is_enabled:
            return

        env_vars = f"{_PREFIX}_ENABLE_{self.name}"
        if self.readiness in [CodeReadiness.NEXT_RELEASE, CodeReadiness.INCOMPLETE]:
            env_vars += f" or {_PREFIX}_ALLOW_{self.readiness.name}"
        message = (
            f"The {self.name} feature is not supported at the current code readiness level. "
            f" To enable it, set {env_vars}."
        )
        raise FeatureNotSupportedError(message)


def requires_feature(
    feature_toggle: FeatureToggle,
) -> Callable[[Callable[_P, _T]], Callable[_P, _T]]:
    """Decorator specifying that the function requires the specified feature toggle."""

    def decorator(func: Callable[_P, _T]) -> Callable[_P, _T]:
        @functools.wraps(func)
        def wrapper(*args: _P.args, **kwargs: _P.kwargs) -> _T:
            feature_toggle._raise_if_disabled()
            return func(*args, **kwargs)

        return wrapper

    return decorator


# --------------------------------------
# Define feature toggle constants here:
# --------------------------------------
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/__init__.py sha256=9da9076a478eb814667429df925f5cc90229a052bd1899130f4a245e86fb668e bytes=284 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/__init__.py`
- sha256: `9da9076a478eb814667429df925f5cc90229a052bd1899130f4a245e86fb668e`
- bytes: 284

````python
"""Internal modules and classes for Measurement Framework."""

import sys

import ni.protobuf


# Redirect old imports of the stubs that used to be defined here to their new location.
sys.modules["ni_measurement_plugin_sdk_service._internal.stubs.ni.protobuf"] = ni.protobuf
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/discovery_client.py sha256=36fbe62397031eaf9a0bd76e054bfb605bdbab78ebd57a41233118395a9db8a8 bytes=527 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/discovery_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/discovery_client.py`
- sha256: `36fbe62397031eaf9a0bd76e054bfb605bdbab78ebd57a41233118395a9db8a8`
- bytes: 527

````python
"""Redirect internal discovery client API to the public API."""

import warnings

from deprecation import DeprecatedWarning
from ni.measurementlink.discovery.v1.client import DiscoveryClient, ServiceLocation

__all__ = ["DiscoveryClient", "ServiceLocation"]

warnings.warn(
    DeprecatedWarning(
        "ni_measurement_plugin_sdk_service._internal.discovery_client",
        deprecated_in="1.3.0",
        removed_in=None,
        details="Use ni_measurement_plugin_sdk_service.discovery instead.",
    ),
)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/grpc_servicer.py sha256=98fd9a8de896fc9c8f74e0219ffd05773e902e0b08962be7854903fd96e20f7c bytes=18078 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/grpc_servicer.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/grpc_servicer.py`
- sha256: `98fd9a8de896fc9c8f74e0219ffd05773e902e0b08962be7854903fd96e20f7c`
- bytes: 18078

````python
"""gRPC servicers for each version of the measurement service interface."""

from __future__ import annotations

import collections.abc
import contextlib
import inspect
import pathlib
import warnings
import weakref
from collections.abc import Generator
from contextvars import ContextVar
from typing import Any, Callable

import grpc
from google.protobuf import any_pb2
from ni.measurementlink.discovery.v1.client import ServiceInfo
from ni.measurementlink.measurement.v1 import (
    measurement_service_pb2 as v1_measurement_service_pb2,
    measurement_service_pb2_grpc as v1_measurement_service_pb2_grpc,
)
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni.measurementlink.sessionmanagement.v1.client import PinMapContext

from ni_measurement_plugin_sdk_service._internal.parameter import decoder, encoder
from ni_measurement_plugin_sdk_service._internal.parameter.metadata import (
    ParameterMetadata,
)
from ni_measurement_plugin_sdk_service.measurement import WrongMessageTypeWarning
from ni_measurement_plugin_sdk_service.measurement.info import MeasurementInfo


class MeasurementServiceContext:
    """Accessor for the measurement service's context-local state."""

    def __init__(
        self,
        grpc_context: grpc.ServicerContext,
        pin_map_context: PinMapContext,
        owner: weakref.ReferenceType[object] | None,
    ) -> None:
        """Initialize the measurement service context."""
        self._grpc_context = grpc_context
        self._pin_map_context = pin_map_context
        self._is_complete = False
        self._owner = owner

    def mark_complete(self) -> None:
        """Mark the current RPC as complete."""
        self._is_complete = True

    @property
    def grpc_context(self) -> grpc.ServicerContext:
        """Get the context for the RPC."""
        return self._grpc_context

    @property
    def owner(self) -> object:
        """The owner of the server (e.g. measurement service)."""
        if self._owner is None:
            return None
        return self._owner()  # dereference weak ref

    @property
    def pin_map_context(self) -> PinMapContext:
        """Get the pin map context for the RPC."""
        return self._pin_map_context

    def add_cancel_callback(self, cancel_callback: Callable[[], None]) -> None:
        """Add a callback that is invoked when the RPC is canceled."""

        def grpc_callback() -> None:
            if not self._is_complete:
                cancel_callback()

        self._grpc_context.add_callback(grpc_callback)

    def cancel(self) -> None:
        """Cancel the RPC."""
        if not self._is_complete:
            self._grpc_context.cancel()

    @property
    def time_remaining(self) -> float:
        """Get the time remaining for the RPC."""
        return self._grpc_context.time_remaining()

    def abort(self, code: grpc.StatusCode, details: str) -> None:
        """Aborts the RPC."""
        try:
            self._grpc_context.abort(code, details)
        except Exception as e:
            # If gRPC raises an empty exception, replace it with an RpcError.
            # This allows our logging interceptors to query the code/details.
            if type(e) is Exception:
                raise CustomRpcError(code, details) from e
            raise


class CustomRpcError(grpc.RpcError):
    """A custom exception class for handling gRPC RPC errors.

    gRPC's built-in RpcError is not directly configurable in Python, so this class
    enables the creation of custom RPC errors with specific error codes.
    """

    def __init__(self, code: grpc.StatusCode, details: str) -> None:
        """Initialize a CustomRpcError instance."""
        self._code = code
        self._details = details

    def code(self) -> grpc.StatusCode:
        """Get the gRPC status code."""
        return self._code

    def details(self) -> str:
        """Get the gRPC status details."""
        return self._details


measurement_service_context: ContextVar[MeasurementServiceContext] = ContextVar(
    "measurement_service_context"
)


def _get_mapping_by_parameter_name(
    mapping_by_id: dict[int, Any], measure_function: Callable[[], None]
) -> dict[str, Any]:
    """Transform a mapping by id into a mapping by parameter name (i.e. kwargs)."""
    signature = inspect.signature(measure_function)
    mapping_by_variable_name = {}
    for i, parameter in enumerate(signature.parameters.values(), start=1):
        mapping_by_variable_name[parameter.name] = mapping_by_id[i]
    return mapping_by_variable_name


def _serialize_outputs(
    output_metadata: dict[int, ParameterMetadata], outputs: Any, service_name: str
) -> any_pb2.Any:
    if isinstance(outputs, collections.abc.Sequence):
        return any_pb2.Any(
            value=encoder.serialize_parameters(output_metadata, outputs, service_name),
            type_url="type.googleapis.com/" + service_name,
        )
    elif outputs is None:
        raise ValueError(f"Measurement function returned None")
    else:
        raise TypeError(
            f"Measurement function returned value with unsupported type: {type(outputs)}"
        )


def frame_metadata_dict(
    parameter_list: list[ParameterMetadata],
) -> dict[int, ParameterMetadata]:
    """Create a metadata dictionary."""
    metadata_dict = {}
    for i, parameter in enumerate(parameter_list, start=1):
        metadata_dict[i] = parameter
    return metadata_dict


class MeasurementServiceServicerV1(v1_measurement_service_pb2_grpc.MeasurementServiceServicer):
    """Measurement v1 servicer."""

    def __init__(
        self,
        measurement_info: MeasurementInfo,
        configuration_parameter_list: list[ParameterMetadata],
        output_parameter_list: list[ParameterMetadata],
        measure_function: Callable,
        owner: object,
        service_info: ServiceInfo,
    ) -> None:
        """Initialize the measurement v1 servicer."""
        super().__init__()
        self._configuration_metadata = frame_metadata_dict(configuration_parameter_list)
        self._output_metadata = frame_metadata_dict(output_parameter_list)
        self._measurement_info = measurement_info
        self._measure_function = measure_function
        self._owner = weakref.ref(owner) if owner is not None else None  # avoid reference cycle
        self._service_info = service_info
        self._configuration_parameters_message_type = service_info.service_class + ".Configurations"
        self._outputs_message_type = service_info.service_class + ".Outputs"

    def GetMetadata(  # noqa: N802 - function name should be lowercase
        self, request: v1_measurement_service_pb2.GetMetadataRequest, context: grpc.ServicerContext
    ) -> v1_measurement_service_pb2.GetMetadataResponse:
        """RPC API to get measurement metadata."""
        measurement_details = v1_measurement_service_pb2.MeasurementDetails(
            display_name=self._measurement_info.display_name, version=self._measurement_info.version
        )

        measurement_signature = v1_measurement_service_pb2.MeasurementSignature(
            configuration_parameters_message_type=self._configuration_parameters_message_type,
            outputs_message_type=self._outputs_message_type,
        )

        for field_number, configuration_metadata in self._configuration_metadata.items():
            configuration_parameter = v1_measurement_service_pb2.ConfigurationParameter(
                field_number=field_number,
                name=configuration_metadata.display_name,
                repeated=configuration_metadata.repeated,
                type=configuration_metadata.type,
                annotations=configuration_metadata.annotations,
            )
            measurement_signature.configuration_parameters.append(configuration_parameter)

        measurement_signature.configuration_defaults.value = encoder.serialize_default_values(
            self._configuration_metadata, self._configuration_parameters_message_type
        )

        for field_number, output_metadata in self._output_metadata.items():
            output_parameter = v1_measurement_service_pb2.Output(
                field_number=field_number,
                name=output_metadata.display_name,
                type=output_metadata.type,
                repeated=output_metadata.repeated,
            )
            measurement_signature.outputs.append(output_parameter)

        metadata_response = v1_measurement_service_pb2.GetMetadataResponse(
            measurement_details=measurement_details,
            measurement_signature=measurement_signature,
            user_interface_details=None,
        )

        for ui_file_path in self._measurement_info.ui_file_paths:
            ui_details = v1_measurement_service_pb2.UserInterfaceDetails(
                file_url=pathlib.Path(ui_file_path).as_uri()
            )
            metadata_response.user_interface_details.append(ui_details)

        return metadata_response

    def Measure(  # noqa: N802 - function name should be lowercase
        self, request: v1_measurement_service_pb2.MeasureRequest, context: grpc.ServicerContext
    ) -> v1_measurement_service_pb2.MeasureResponse:
        """RPC API that executes the registered measurement method."""
        self._validate_parameters(request)
        mapping_by_id = decoder.deserialize_parameters(
            self._configuration_metadata,
            request.configuration_parameters.value,
            self._configuration_parameters_message_type,
        )
        mapping_by_variable_name = _get_mapping_by_parameter_name(
            mapping_by_id, self._measure_function
        )
        pin_map_context = PinMapContext._from_grpc(request.pin_map_context)
        token = measurement_service_context.set(
            MeasurementServiceContext(context, pin_map_context, self._owner)
        )
        try:
            return_value = self._measure_function(**mapping_by_variable_name)
            if isinstance(return_value, collections.abc.Generator):
                with contextlib.closing(return_value) as output_iter:
                    outputs = None
                    try:
                        while True:
                            outputs = next(output_iter)
                    except StopIteration as e:
                        if e.value is not None:
                            outputs = e.value
                    return self._serialize_response(outputs)
            else:
                return self._serialize_response(return_value)
        finally:
            measurement_service_context.get().mark_complete()
            measurement_service_context.reset(token)

    def _serialize_response(
        self,
        outputs: Any,
    ) -> v1_measurement_service_pb2.MeasureResponse:
        return v1_measurement_service_pb2.MeasureResponse(
            outputs=_serialize_outputs(self._output_metadata, outputs, self._outputs_message_type)
        )

    def _validate_parameters(self, request: v1_measurement_service_pb2.MeasureRequest) -> None:
        expected_type = "type.googleapis.com/" + self._configuration_parameters_message_type
        actual_type = request.configuration_parameters.type_url
        if actual_type != expected_type:
            warnings.warn(
                f"Wrong message type. Expected {expected_type!r} but got {actual_type!r}",
                WrongMessageTypeWarning,
            )


class MeasurementServiceServicerV2(v2_measurement_service_pb2_grpc.MeasurementServiceServicer):
    """Measurement v2 servicer."""

    def __init__(
        self,
        measurement_info: MeasurementInfo,
        configuration_parameter_list: list[ParameterMetadata],
        output_parameter_list: list[ParameterMetadata],
        measure_function: Callable,
        owner: object,
        service_info: ServiceInfo,
    ) -> None:
        """Initialize the measurement v2 servicer."""
        super().__init__()
        self._configuration_metadata = frame_metadata_dict(configuration_parameter_list)
        self._output_metadata = frame_metadata_dict(output_parameter_list)
        self._measurement_info = measurement_info
        self._measure_function = measure_function
        self._owner = weakref.ref(owner) if owner is not None else None  # avoid reference cycle
        self._service_info = service_info
        self._configuration_parameters_message_type = service_info.service_class + ".Configurations"
        self._outputs_message_type = service_info.service_class + ".Outputs"

    def GetMetadata(  # noqa: N802 - function name should be lowercase
        self, request: v2_measurement_service_pb2.GetMetadataRequest, context: grpc.ServicerContext
    ) -> v2_measurement_service_pb2.GetMetadataResponse:
        """RPC API to get measurement metadata."""
        measurement_details = v2_measurement_service_pb2.MeasurementDetails(
            display_name=self._measurement_info.display_name, version=self._measurement_info.version
        )

        measurement_signature = v2_measurement_service_pb2.MeasurementSignature(
            configuration_parameters_message_type=self._configuration_parameters_message_type,
            outputs_message_type=self._outputs_message_type,
        )

        for field_number, configuration_metadata in self._configuration_metadata.items():
            configuration_parameter = v2_measurement_service_pb2.ConfigurationParameter(
                field_number=field_number,
                name=configuration_metadata.display_name,
                repeated=configuration_metadata.repeated,
                type=configuration_metadata.type,
                annotations=configuration_metadata.annotations,
                message_type=configuration_metadata.message_type,
            )
            measurement_signature.configuration_parameters.append(configuration_parameter)

        measurement_signature.configuration_defaults.value = encoder.serialize_default_values(
            self._configuration_metadata, self._configuration_parameters_message_type
        )

        for field_number, output_metadata in self._output_metadata.items():
            output_parameter = v2_measurement_service_pb2.Output(
                field_number=field_number,
                name=output_metadata.display_name,
                type=output_metadata.type,
                repeated=output_metadata.repeated,
                annotations=output_metadata.annotations,
                message_type=output_metadata.message_type,
            )
            measurement_signature.outputs.append(output_parameter)

        metadata_response = v2_measurement_service_pb2.GetMetadataResponse(
            measurement_details=measurement_details,
            measurement_signature=measurement_signature,
            user_interface_details=None,
        )

        for ui_file_path in self._measurement_info.ui_file_paths:
            ui_details = v2_measurement_service_pb2.UserInterfaceDetails(
                file_url=pathlib.Path(ui_file_path).as_uri()
            )
            metadata_response.user_interface_details.append(ui_details)

        return metadata_response

    def Measure(  # noqa: N802 - function name should be lowercase
        self, request: v2_measurement_service_pb2.MeasureRequest, context: grpc.ServicerContext
    ) -> Generator[v2_measurement_service_pb2.MeasureResponse]:
        """RPC API that executes the registered measurement method."""
        self._validate_parameters(request)
        mapping_by_id = decoder.deserialize_parameters(
            self._configuration_metadata,
            request.configuration_parameters.value,
            self._configuration_parameters_message_type,
        )
        mapping_by_variable_name = _get_mapping_by_parameter_name(
            mapping_by_id, self._measure_function
        )
        pin_map_context = PinMapContext._from_grpc(request.pin_map_context)
        token = measurement_service_context.set(
            MeasurementServiceContext(context, pin_map_context, self._owner)
        )
        try:
            return_value = self._measure_function(**mapping_by_variable_name)
            if isinstance(return_value, collections.abc.Generator):
                with contextlib.closing(return_value) as output_iter:
                    try:
                        while True:
                            outputs = next(output_iter)
                            yield self._serialize_response(outputs)
                    except StopIteration as e:
                        if e.value is not None:
                            yield self._serialize_response(e.value)
            else:
                yield self._serialize_response(return_value)
        finally:
            measurement_service_context.get().mark_complete()
            measurement_service_context.reset(token)

    def _serialize_response(self, outputs: Any) -> v2_measurement_service_pb2.MeasureResponse:
        return v2_measurement_service_pb2.MeasureResponse(
            outputs=_serialize_outputs(self._output_metadata, outputs, self._outputs_message_type)
        )

    def _validate_parameters(self, request: v2_measurement_service_pb2.MeasureRequest) -> None:
        expected_type = "type.googleapis.com/" + self._configuration_parameters_message_type
        actual_type = request.configuration_parameters.type_url
        if actual_type != expected_type:
            warnings.warn(
                f"Wrong message type. Expected {expected_type!r} but got {actual_type!r}",
                WrongMessageTypeWarning,
            )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/__init__.py sha256=38d9f7a2b06b2023ba6115813d852c5b6e1eaa3a1f5d317d36660cde0680f071 bytes=58 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/__init__.py`
- sha256: `38d9f7a2b06b2023ba6115813d852c5b6e1eaa3a1f5d317d36660cde0680f071`
- bytes: 58

````python
"""Contains modules related to Measurement parameter."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/_get_type.py sha256=b02eec0ed68a48a4f14bfa2b92c43d91b0621c0b5eebcd59304511e737dbce85 bytes=1638 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/_get_type.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/_get_type.py`
- sha256: `b02eec0ed68a48a4f14bfa2b92c43d91b0621c0b5eebcd59304511e737dbce85`
- bytes: 1638

````python
from __future__ import annotations

from typing import Any

from google.protobuf.descriptor_pb2 import FieldDescriptorProto
from google.protobuf.type_pb2 import Field

_TYPE_DEFAULT_MAPPING = {
    Field.TYPE_FLOAT: float(),
    Field.TYPE_DOUBLE: float(),
    Field.TYPE_INT32: int(),
    Field.TYPE_INT64: int(),
    Field.TYPE_UINT32: int(),
    Field.TYPE_UINT64: int(),
    Field.TYPE_BOOL: bool(),
    Field.TYPE_STRING: "",
    Field.TYPE_ENUM: int(),
}

_PYTHON_DEFAULT_TYPES = {type(value) for value in _TYPE_DEFAULT_MAPPING.values()}

TYPE_FIELD_MAPPING = {
    Field.TYPE_FLOAT: FieldDescriptorProto.TYPE_FLOAT,
    Field.TYPE_DOUBLE: FieldDescriptorProto.TYPE_DOUBLE,
    Field.TYPE_INT32: FieldDescriptorProto.TYPE_INT32,
    Field.TYPE_INT64: FieldDescriptorProto.TYPE_INT64,
    Field.TYPE_UINT32: FieldDescriptorProto.TYPE_UINT32,
    Field.TYPE_UINT64: FieldDescriptorProto.TYPE_UINT64,
    Field.TYPE_BOOL: FieldDescriptorProto.TYPE_BOOL,
    Field.TYPE_STRING: FieldDescriptorProto.TYPE_STRING,
    Field.TYPE_ENUM: FieldDescriptorProto.TYPE_ENUM,
    Field.TYPE_MESSAGE: FieldDescriptorProto.TYPE_MESSAGE,
}


def get_type_default(
    value_type: Field.Kind.ValueType, repeated: bool, default_value_type: type | None = None
) -> Any:
    """Get the default value for the give type."""
    if repeated:
        return list()
    if (
        value_type == Field.TYPE_MESSAGE
        and default_value_type not in _PYTHON_DEFAULT_TYPES
        and default_value_type is not None
    ):
        return default_value_type()
    return _TYPE_DEFAULT_MAPPING.get(value_type)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/decoder.py sha256=eed1e3230f3a28fb1a39819567c20d1830025e6a2a180df01ebfdc4a157ffc8d bytes=2341 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/decoder.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/decoder.py`
- sha256: `eed1e3230f3a28fb1a39819567c20d1830025e6a2a180df01ebfdc4a157ffc8d`
- bytes: 2341

````python
from __future__ import annotations

"""Parameter Serializer."""

from typing import Any

from google.protobuf import descriptor_pool, message_factory
from google.protobuf.descriptor_pb2 import FieldDescriptorProto

from ni_measurement_plugin_sdk_service._internal.parameter.metadata import (
    ParameterMetadata,
)
from ni_measurement_plugin_sdk_service._internal.parameter.serialization_descriptors import (
    is_protobuf,
)


def deserialize_parameters(
    parameter_metadata_dict: dict[int, ParameterMetadata],
    parameter_bytes: bytes,
    service_name: str,
) -> dict[int, Any]:
    """Deserialize the bytes of the parameter based on the metadata.

    Args:
        parameter_metadata_dict (Dict[int, ParameterMetadata]): Parameter metadata by ID.

        parameter_bytes (bytes): Byte string to deserialize.

        service_name (str): Unique service name.

    Returns:
        Dict[int, Any]: Deserialized parameters by ID.
    """
    pool = descriptor_pool.Default()
    message_proto = pool.FindMessageTypeByName(service_name)
    message_instance = message_factory.GetMessageClass(message_proto)()
    parameter_values = {}

    message_instance.ParseFromString(parameter_bytes)
    for i in message_proto.fields_by_number.keys():
        parameter_metadata = parameter_metadata_dict[i]
        field_name = parameter_metadata.field_name
        value = getattr(message_instance, field_name)

        if parameter_metadata.type == FieldDescriptorProto.TYPE_ENUM:
            parameter_values[i] = _deserialize_enum_parameter(value, parameter_metadata)
        elif (
            parameter_metadata.type == FieldDescriptorProto.TYPE_MESSAGE
            and not parameter_metadata.repeated
            and value.ByteSize() == 0
        ):
            parameter_values[i] = None
        else:
            parameter_values[i] = value
    return parameter_values


def _deserialize_enum_parameter(field_value: Any, metadata: ParameterMetadata) -> Any:
    """Convert enum into their user defined enum type."""
    enum_type = metadata.enum_type
    if is_protobuf(enum_type):
        return field_value

    assert enum_type is not None
    if metadata.repeated:
        return [enum_type(value) for value in field_value]
    return enum_type(field_value)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/encoder.py sha256=550cb68ce11fe7c9b2ae23601902240848774e5f7f5c422384045b72728739b4 bytes=3089 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/encoder.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/encoder.py`
- sha256: `550cb68ce11fe7c9b2ae23601902240848774e5f7f5c422384045b72728739b4`
- bytes: 3089

````python
"""Parameter Serializer."""

from __future__ import annotations

from collections.abc import Sequence
from enum import Enum
from typing import Any

from google.protobuf import descriptor_pool, message_factory
from google.protobuf.descriptor_pb2 import FieldDescriptorProto

from ni_measurement_plugin_sdk_service._internal.parameter._get_type import (
    get_type_default,
)
from ni_measurement_plugin_sdk_service._internal.parameter.metadata import (
    ParameterMetadata,
)


def serialize_parameters(
    parameter_metadata_dict: dict[int, ParameterMetadata],
    parameter_values: Sequence[Any],
    service_name: str,
) -> bytes:
    """Serialize the parameter values in same order based on the metadata_dict.

    Args:
        parameter_metadata_dict (Dict[int, ParameterMetadata]): Parameter metadata by ID.

        parameter_values (Sequence[Any]): Parameter values to serialize.

        service_name (str): Unique service name.

    Returns:
        bytes: Serialized byte string containing parameter values.
    """
    pool = descriptor_pool.Default()
    message_proto = pool.FindMessageTypeByName(service_name)
    message_instance = message_factory.GetMessageClass(message_proto)()

    for i, parameter in enumerate(parameter_values, start=1):
        parameter_metadata = parameter_metadata_dict[i]
        field_name = parameter_metadata.field_name
        parameter = _get_enum_values(param=parameter)
        default_value = get_type_default(parameter_metadata.type, parameter_metadata.repeated)

        # Doesn't assign default values or None values to fields
        if parameter != default_value and parameter is not None:
            if parameter_metadata.repeated:
                getattr(message_instance, field_name).extend(parameter)
            elif parameter_metadata.type == FieldDescriptorProto.TYPE_MESSAGE:
                getattr(message_instance, field_name).CopyFrom(parameter)
            else:
                setattr(message_instance, field_name, parameter)
    return message_instance.SerializeToString()


def serialize_default_values(
    parameter_metadata_dict: dict[int, ParameterMetadata], service_name: str
) -> bytes:
    """Serialize the Default values in the Metadata.

    Args:
        parameter_metadata_dict (Dict[int, ParameterMetadata]): Configuration metadata.

        service_name (str): Unique service name.

    Returns:
        bytes: Serialized byte string containing default values.
    """
    default_value_parameter_array = [
        parameter.default_value for parameter in parameter_metadata_dict.values()
    ]
    return serialize_parameters(
        parameter_metadata_dict, default_value_parameter_array, service_name
    )


def _get_enum_values(param: Any) -> Any:
    """Get's value of an enum."""
    if param == []:
        return param
    if isinstance(param, list) and isinstance(param[0], Enum):
        return [x.value for x in param]
    elif isinstance(param, Enum):
        return param.value
    return param
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/metadata.py sha256=9cd6f00066c0ac42a171e364cdfa9faaf6400b3e8db5ddb4daf73eb5f85f06ce bytes=8326 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/metadata.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/metadata.py`
- sha256: `9cd6f00066c0ac42a171e364cdfa9faaf6400b3e8db5ddb4daf73eb5f85f06ce`
- bytes: 8326

````python
"""Contains classes that represents metadata."""

from __future__ import annotations

import json
from collections.abc import Iterable
from enum import Enum
from typing import TYPE_CHECKING, Any, NamedTuple, Union

from google.protobuf import type_pb2

from ni_measurement_plugin_sdk_service._annotations import (
    ENUM_VALUES_KEY,
    TYPE_SPECIALIZATION_KEY,
)
from ni_measurement_plugin_sdk_service._internal.parameter._get_type import (
    get_type_default,
)
from ni_measurement_plugin_sdk_service.measurement.info import TypeSpecialization

if TYPE_CHECKING:
    from google.protobuf.internal.enum_type_wrapper import _EnumTypeWrapper

    SupportedEnumType = Union[type[Enum], _EnumTypeWrapper]

_VALID_CHARS = set(" ().,;:!?-_'+")


class ParameterMetadata(NamedTuple):
    """Class that represents the metadata of parameters."""

    display_name: str
    """The display name of the parameter."""

    type: type_pb2.Field.Kind.ValueType
    """The datatype of the parameter represented by the gRPC field enum."""

    repeated: bool
    """Indicates whether the parameter is a scalar or 1D array.
    
    True for 1D array and false for scalar."""

    default_value: Any
    """The default value of the parameter."""

    annotations: dict[str, str]
    """Represents a set of annotations on the type."""

    message_type: str = ""
    """The gRPC full name of the message type. 
    
    Required when 'type' is Kind.TypeMessage. Ignored for any other 'type'.
    """

    field_name: str = ""
    """display_name in snake_case format."""

    enum_type: SupportedEnumType | None = None
    """Enum type of parameter"""

    @staticmethod
    def initialize(
        display_name: str,
        type: type_pb2.Field.Kind.ValueType,
        repeated: bool,
        default_value: Any,
        annotations: dict[str, str],
        message_type: str = "",
        enum_type: SupportedEnumType | None = None,
    ) -> ParameterMetadata:
        """Initialize ParameterMetadata with field_name."""
        _validate_display_name(display_name)
        underscore_display_name = display_name.replace(" ", "_")

        if all(char.isalnum() or char == "_" for char in underscore_display_name):
            field_name = underscore_display_name
        else:
            field_name = "".join(
                char for char in underscore_display_name if char.isalnum() or char == "_"
            )
        parameter_metadata = ParameterMetadata(
            display_name,
            type,
            repeated,
            default_value,
            annotations,
            message_type,
            field_name,
            enum_type,
        )
        _validate_default_value_type(parameter_metadata)
        return parameter_metadata


def _validate_display_name(display_name: str) -> None:
    """Validate and raise exception if 'display_name' has invalid characters.

    Raises:
        ValueError: If display_name has invalid characters.
    """
    if not display_name:
        raise ValueError("The display name cannot be an empty string.")
    elif not display_name[0].isalpha():
        raise ValueError(f"The first character in display name '{display_name}' must be a letter.")
    elif not all(char in _VALID_CHARS or char.isalnum() for char in display_name):
        raise ValueError(f"There are invalid characters in display name '{display_name}'.")


def _validate_default_value_type(parameter_metadata: ParameterMetadata) -> None:
    """Validate and raise exception if the default value does not match the type info.

    Args:
        parameter_metadata (ParameterMetadata): Parameter metadata

    Raises:
        TypeError: If default value does not match the Datatype.
    """
    default_value = parameter_metadata.default_value
    if default_value is None:
        return None

    expected_type = type(
        get_type_default(parameter_metadata.type, parameter_metadata.repeated, type(default_value))
    )
    display_name = parameter_metadata.display_name
    enum_values_annotation = get_enum_values_annotation(parameter_metadata)

    if parameter_metadata.repeated:
        if not isinstance(default_value, list):
            raise TypeError(f"The default value '{default_value}' is not a list.")
        if len(default_value) > 0:
            expected_element_type = type(
                get_type_default(parameter_metadata.type, False, type(default_value[0]))
            )
            _validate_default_value_type_for_repeated_type(
                default_value,
                expected_type,
                expected_element_type,
                enum_values_annotation,
                display_name,
            )
    else:
        _validate_default_value_type_for_scalar_type(
            default_value, expected_type, enum_values_annotation, display_name
        )
    return None


def _validate_default_value_type_for_scalar_type(
    default_value: object, expected_type: type, enum_values_annotation: str, display_name: str
) -> None:
    """Validate and raise exception if the default value does not match the type info."""
    if enum_values_annotation:
        user_enum_dict = json.loads(enum_values_annotation)
        _validate_default_value_type_for_enum_type(
            default_value, user_enum_dict, enum_values_annotation, display_name
        )
    else:
        _validate_default_value_type_for_basic_type(default_value, expected_type, display_name)


def _validate_default_value_type_for_repeated_type(
    default_value: Iterable[object],
    expected_type: type,
    expected_element_type: type,
    enum_values_annotation: str,
    display_name: str,
) -> None:
    """Validate and raise exception if the default value does not match the type info."""
    if not isinstance(default_value, expected_type):
        raise TypeError(
            f"Unexpected type {type(default_value)} in the default value for '{display_name}'. Expected type: {expected_type}."
        )

    if enum_values_annotation:
        user_enum_dict = json.loads(enum_values_annotation)
        for element in default_value:
            _validate_default_value_type_for_enum_type(
                element, user_enum_dict, enum_values_annotation, display_name
            )
    else:
        for element in default_value:
            _validate_default_value_type_for_basic_type(
                element, expected_element_type, display_name
            )


def _validate_default_value_type_for_basic_type(
    default_value: object,
    expected_type: type,
    display_name: str,
) -> None:
    if not isinstance(default_value, expected_type):
        if expected_type is float and isinstance(default_value, int):
            return None
        raise TypeError(
            f"Unexpected type {type(default_value)} in the default value for '{display_name}'. Expected type: {expected_type}."
        )


def _validate_default_value_type_for_enum_type(
    default_value: object,
    user_enum: dict[str, int],
    enum_values_annotation: str,
    display_name: str,
) -> None:
    if not _is_valid_enum_value(default_value, user_enum):
        raise TypeError(
            f"Invalid default value, `{default_value}`, for enum parameter '{display_name}'. Expected values: `{enum_values_annotation}`."
        )


def get_enum_values_annotation(parameter_metadata: ParameterMetadata) -> str:
    """Gets the value for the "ni/enum.values" annotation if it exists.

    Args:
        parameter_metadata (ParameterMetadata): Parameter metadata

    Returns:
        str: The value of "ni/enum.values" annotation
    """
    if parameter_metadata.annotations.get(TYPE_SPECIALIZATION_KEY) == TypeSpecialization.Enum.value:
        return parameter_metadata.annotations.get(ENUM_VALUES_KEY, "")
    else:
        return ""


def _is_valid_enum_value(enum_value: object, user_enum: dict[str, int]) -> bool:
    if isinstance(enum_value, Enum):
        return enum_value.name in user_enum and user_enum[enum_value.name] == enum_value.value
    elif isinstance(enum_value, int):
        return enum_value in user_enum.values()
    else:
        return False
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/serialization_descriptors.py sha256=035acd619630e856533606f6e1a4087bf887cc916b13d1e4ad62908f7a51bd0a bytes=4456 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/serialization_descriptors.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/parameter/serialization_descriptors.py`
- sha256: `035acd619630e856533606f6e1a4087bf887cc916b13d1e4ad62908f7a51bd0a`
- bytes: 4456

````python
"""Serialization Descriptors."""

from __future__ import annotations

from enum import Enum, EnumMeta
from json import loads
from typing import TYPE_CHECKING, Union

from google.protobuf.descriptor_pb2 import (
    DescriptorProto,
    FieldDescriptorProto,
    FileDescriptorProto,
)
from google.protobuf.descriptor_pool import DescriptorPool

from ni_measurement_plugin_sdk_service._annotations import ENUM_VALUES_KEY
from ni_measurement_plugin_sdk_service._internal.parameter._get_type import (
    TYPE_FIELD_MAPPING,
)
from ni_measurement_plugin_sdk_service._internal.parameter.metadata import (
    ParameterMetadata,
)

if TYPE_CHECKING:
    from google.protobuf.internal.enum_type_wrapper import _EnumTypeWrapper

    SupportedEnumType = Union[type[Enum], _EnumTypeWrapper]


def is_protobuf(enum_type: SupportedEnumType | None) -> bool:
    """Finds if 'enum_type' is a protobuf or a python enum."""
    return hasattr(enum_type, "ValueType")


def _get_enum_type_name(metadata: ParameterMetadata) -> str:
    """Get's enum type name from a 'parameter_metadata'."""
    enum_type = metadata.enum_type
    if enum_type is None:
        raise ValueError("Enum type cannot be None in ParameterMetadata.")

    if is_protobuf(enum_type) and not isinstance(enum_type, EnumMeta):
        return enum_type.DESCRIPTOR.name
    return enum_type.__name__


def _create_enum_type_class(
    file_descriptor: FileDescriptorProto,
    metadata: ParameterMetadata,
    field_descriptor: FieldDescriptorProto,
) -> None:
    """Implement a enum class in 'file_descriptor'."""
    enum_dict = loads(metadata.annotations[ENUM_VALUES_KEY])
    enum_type_name = _get_enum_type_name(metadata)

    if enum_type_name not in [file_enum.name for file_enum in file_descriptor.enum_type]:
        enum_descriptor = file_descriptor.enum_type.add()
        enum_descriptor.name = enum_type_name
        for name, number in enum_dict.items():
            enum_value_descriptor = enum_descriptor.value.add()
            enum_value_descriptor.name = f"{enum_type_name}_{name}"
            enum_value_descriptor.number = number
    field_descriptor.type_name = enum_type_name


def _create_field(
    message_proto: DescriptorProto, metadata: ParameterMetadata, index: int
) -> FieldDescriptorProto:
    """Implement a field in 'message_proto'."""
    field_descriptor = message_proto.field.add()
    field_descriptor.number = index
    field_descriptor.name = metadata.field_name
    field_descriptor.type = TYPE_FIELD_MAPPING[metadata.type]

    if metadata.repeated:
        field_descriptor.label = FieldDescriptorProto.LABEL_REPEATED
        field_descriptor.options.packed = True
    else:
        field_descriptor.label = FieldDescriptorProto.LABEL_OPTIONAL

    if metadata.type == FieldDescriptorProto.TYPE_MESSAGE:
        field_descriptor.type_name = metadata.message_type
    return field_descriptor


def _create_message_type(
    parameter_metadata: list[ParameterMetadata],
    message_name: str,
    file_descriptor: FileDescriptorProto,
) -> None:
    """Creates a message type with fields intialized in 'file_descriptor'."""
    message_proto = file_descriptor.message_type.add()
    message_proto.name = message_name

    # Initialize the message with fields defined
    for i, metadata in enumerate(parameter_metadata):
        field_descriptor = _create_field(
            message_proto=message_proto, metadata=metadata, index=i + 1
        )
        if metadata.type == FieldDescriptorProto.TYPE_ENUM:
            _create_enum_type_class(
                file_descriptor=file_descriptor,
                metadata=metadata,
                field_descriptor=field_descriptor,
            )


def create_file_descriptor(
    service_name: str,
    output_metadata: list[ParameterMetadata],
    input_metadata: list[ParameterMetadata],
    pool: DescriptorPool,
) -> None:
    """Creates two message types in one file descriptor proto."""
    try:
        pool.FindFileByName(service_name)
    except KeyError:
        file_descriptor = FileDescriptorProto()
        file_descriptor.name = service_name
        file_descriptor.package = service_name
        _create_message_type(input_metadata, "Configurations", file_descriptor)
        _create_message_type(output_metadata, "Outputs", file_descriptor)
        pool.Add(file_descriptor)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/_internal/service_manager.py sha256=10bdedc33fe4544c86c19d36902fe2e7362b7014c0dd484835b41407530f8781 bytes=6149 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/_internal/service_manager.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/_internal/service_manager.py`
- sha256: `10bdedc33fe4544c86c19d36902fe2e7362b7014c0dd484835b41407530f8781`
- bytes: 6149

````python
from __future__ import annotations

import logging
from typing import Callable

import grpc
from deprecation import deprecated
from google.protobuf import descriptor_pool
from grpc.framework.foundation import logging_pool
from ni.measurementlink.discovery.v1.client import (
    DiscoveryClient,
    ServiceInfo,
    ServiceLocation,
)
from ni.measurementlink.measurement.v1 import (
    measurement_service_pb2_grpc as v1_measurement_service_pb2_grpc,
)
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni_grpc_extensions.loggers import ServerLogger

from ni_measurement_plugin_sdk_service._internal.grpc_servicer import (
    MeasurementServiceServicerV1,
    MeasurementServiceServicerV2,
)
from ni_measurement_plugin_sdk_service._internal.parameter.metadata import (
    ParameterMetadata,
)
from ni_measurement_plugin_sdk_service._internal.parameter.serialization_descriptors import (
    create_file_descriptor,
)
from ni_measurement_plugin_sdk_service.measurement.info import MeasurementInfo

_logger = logging.getLogger(__name__)
_V1_INTERFACE = "ni.measurementlink.measurement.v1.MeasurementService"
_V2_INTERFACE = "ni.measurementlink.measurement.v2.MeasurementService"


class GrpcService:
    """Manages the gRPC server lifetime and registration."""

    def __init__(self, discovery_client: DiscoveryClient | None = None) -> None:
        """Initialize the service."""
        self._discovery_client = discovery_client or DiscoveryClient()
        self._server: grpc.Server | None = None
        self._service_location: ServiceLocation | None = None
        self._registration_id = ""

    @property
    @deprecated(
        deprecated_in="1.3.0-dev0",
        details="This property should not be public and will be removed in a later release.",
    )
    def discovery_client(self) -> DiscoveryClient:
        """Client for accessing the NI Discovery Service."""
        return self._discovery_client

    @property
    @deprecated(
        deprecated_in="1.3.0-dev0",
        details="Use service_location instead.",
    )
    def port(self) -> str:
        """The insecure port."""
        return self.service_location.insecure_port

    @property
    @deprecated(
        deprecated_in="1.3.0-dev0",
        details="This property should not be public and will be removed in a later release.",
    )
    def server(self) -> grpc.Server | None:
        """The gRPC server."""
        return self._server

    @property
    def service_location(self) -> ServiceLocation:
        """The location of the service on the network."""
        if self._service_location is None:
            raise RuntimeError("Measurement service not running")
        return self._service_location

    def start(
        self,
        measurement_info: MeasurementInfo,
        service_info: ServiceInfo,
        configuration_parameter_list: list[ParameterMetadata],
        output_parameter_list: list[ParameterMetadata],
        measure_function: Callable,
        owner: object = None,
    ) -> str:
        """Start the gRPC server and register it with the discovery service.

        Returns:
            The insecure port.
        """
        interceptors: list[grpc.ServerInterceptor] = []
        if ServerLogger.is_enabled():
            interceptors.append(ServerLogger())
        self._server = grpc.server(
            logging_pool.pool(max_workers=10),
            interceptors=interceptors,
            options=[
                ("grpc.max_receive_message_length", -1),
                ("grpc.max_send_message_length", -1),
            ],
        )
        create_file_descriptor(
            service_name=service_info.service_class,
            output_metadata=output_parameter_list,
            input_metadata=configuration_parameter_list,
            pool=descriptor_pool.Default(),
        )
        for interface in service_info.provided_interfaces:
            if interface == _V1_INTERFACE:
                servicer_v1 = MeasurementServiceServicerV1(
                    measurement_info,
                    configuration_parameter_list,
                    output_parameter_list,
                    measure_function,
                    owner,
                    service_info,
                )
                v1_measurement_service_pb2_grpc.add_MeasurementServiceServicer_to_server(
                    servicer_v1, self._server
                )
            elif interface == _V2_INTERFACE:
                servicer_v2 = MeasurementServiceServicerV2(
                    measurement_info,
                    configuration_parameter_list,
                    output_parameter_list,
                    measure_function,
                    owner,
                    service_info,
                )
                v2_measurement_service_pb2_grpc.add_MeasurementServiceServicer_to_server(
                    servicer_v2, self._server
                )
            else:
                raise ValueError(
                    f"Unknown interface was provided in the .serviceconfig file: {interface}"
                )
        host = "[::1]"
        port = str(self._server.add_insecure_port(f"{host}:0"))
        address = f"http://{host}:{port}"
        self._server.start()
        _logger.info("Measurement service listening on: %s", address)

        self._service_location = ServiceLocation("localhost", port, "")
        self._registration_id = self._discovery_client.register_service(
            service_info, self.service_location
        )
        return port

    def stop(self) -> None:
        """Unregister and stop the gRPC server."""
        if self._registration_id:
            self._discovery_client.unregister_service(self._registration_id)
        if self._server is not None:
            self._server.stop(5)

        self._registration_id = ""
        self._server = None
        self._service_location = None
        _logger.info("Measurement service closed.")
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/discovery/__init__.py sha256=c8e530e896d21edc83ee5839d9eea6e18d42c5e31df8df633b28c7fbd89ae1d3 bytes=501 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/discovery/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/discovery/__init__.py`
- sha256: `c8e530e896d21edc83ee5839d9eea6e18d42c5e31df8df633b28c7fbd89ae1d3`
- bytes: 501

````python
"""Compatibility API for accessing the NI Discovery Service.

The public API for accessing the NI Discovery Service has moved to the
:mod:`ni.measurementlink.discovery.v1.client` package.

The :mod:`ni_measurement_plugin_sdk_service.discovery` subpackage provides
compatibility with existing applications and will be deprecated in a future
release.
"""

from ni.measurementlink.discovery.v1.client import DiscoveryClient, ServiceLocation

__all__ = ["DiscoveryClient", "ServiceLocation"]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/grpc/__init__.py sha256=9c715f3cd4e55aa43916f98f341b92f61155ef7c7f6cb4815a78a3bbc6586b96 bytes=309 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/grpc/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/grpc/__init__.py`
- sha256: `9c715f3cd4e55aa43916f98f341b92f61155ef7c7f6cb4815a78a3bbc6586b96`
- bytes: 309

````python
"""Compatibility API for gRPC extensions.

The public gRPC extensions API has moved to the :external+ni_grpc_extensions:doc:`index` package.

The :mod:`ni_measurement_plugin_sdk_service.grpc` subpackage provides
compatibility with existing applications and will be deprecated in a future
release.
"""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/grpc/channelpool.py sha256=55317f5844a168ce626ccb84c0a3aed6cbb6ea756ca09fb6f8f042fffd9c1623 bytes=419 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/grpc/channelpool.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/grpc/channelpool.py`
- sha256: `55317f5844a168ce626ccb84c0a3aed6cbb6ea756ca09fb6f8f042fffd9c1623`
- bytes: 419

````python
"""Compatibility API for gRPC channel pool.

The :obj:`GrpcChannelPool` class has moved to the :mod:`ni_grpc_extensions.channelpool`
submodule.

The :mod:`ni_measurement_plugin_sdk_service.grpc.channelpool` submodule provides
compatibility with existing applications and will be deprecated in a future
release.
"""

from ni_grpc_extensions.channelpool import GrpcChannelPool

__all__ = ["GrpcChannelPool"]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/grpc/loggers.py sha256=ea0da6aafa92c8a11ed78d41a01f8bcb2deff0eeb3de27931f1aa8a71a7b7f87 bytes=444 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/grpc/loggers.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/grpc/loggers.py`
- sha256: `ea0da6aafa92c8a11ed78d41a01f8bcb2deff0eeb3de27931f1aa8a71a7b7f87`
- bytes: 444

````python
"""Compatibility API for gRPC logging interceptors.

The gRPC logging interceptor classes have moved to the :mod:`ni_grpc_extensions.loggers`
submodule.

The :mod:`ni_measurement_plugin_sdk_service.grpc.loggers` submodule provides
compatibility with existing applications and will be deprecated in a future
release.
"""

from ni_grpc_extensions.loggers import ClientLogger, ServerLogger

__all__ = ["ClientLogger", "ServerLogger"]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/measurement/__init__.py sha256=9bf6b5c808d1c23a9f777aee69fb134683611b69b3e29569c77ae95d4168a760 bytes=142 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/measurement/__init__.py`
- sha256: `9bf6b5c808d1c23a9f777aee69fb134683611b69b3e29569c77ae95d4168a760`
- bytes: 142

````python
"""Measurement Framework Package."""


class WrongMessageTypeWarning(RuntimeWarning):
    """Wrong message type received."""

    pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/measurement/client_support.py sha256=ac231e97ea1704dde857b4dc595a04a8a1fc3e7c3205876aba39be68dcc7ee29 bytes=3935 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/measurement/client_support.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/measurement/client_support.py`
- sha256: `ac231e97ea1704dde857b4dc595a04a8a1fc3e7c3205876aba39be68dcc7ee29`
- bytes: 3935

````python
"""Support functions for the Measurement Plug-In Client."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Any

from google.protobuf.descriptor_pb2 import FieldDescriptorProto

from ni_measurement_plugin_sdk_service._annotations import TYPE_SPECIALIZATION_KEY
from ni_measurement_plugin_sdk_service._internal.parameter.decoder import (
    deserialize_parameters as _internal_deserialize_parameters,
)
from ni_measurement_plugin_sdk_service._internal.parameter.encoder import (
    serialize_parameters as _internal_serialize_parameters,
)
from ni_measurement_plugin_sdk_service._internal.parameter.metadata import (
    ParameterMetadata,
)
from ni_measurement_plugin_sdk_service._internal.parameter.serialization_descriptors import (
    create_file_descriptor,
)
from ni_measurement_plugin_sdk_service.measurement.info import TypeSpecialization

__all__ = [
    "create_file_descriptor",
    "deserialize_parameters",
    "ParameterMetadata",
    "serialize_parameters",
]


def deserialize_parameters(
    parameter_metadata_dict: dict[int, ParameterMetadata],
    parameter_bytes: bytes,
    message_name: str,
    *,
    convert_paths: bool = True,
) -> Sequence[Any]:
    """Deserialize parameter bytes into separate parameter values.

    Args:
        parameter_metadata_dict: Parameter metadata by ID.

        parameter_byte: Byte string to deserialize.

        message_name: gRPC message name (e.g. f"{service_class}.Outputs").

        convert_paths: Specifies whether to convert path parameters to pathlib.Path.

    Returns:
        Deserialized parameter values, ordered by ID.
    """
    parameter_values = _internal_deserialize_parameters(
        parameter_metadata_dict, parameter_bytes, message_name
    )

    for id in parameter_values.keys():
        metadata = parameter_metadata_dict[id]
        if (
            convert_paths
            and metadata.type == FieldDescriptorProto.TYPE_STRING
            and metadata.annotations
            and metadata.annotations.get(TYPE_SPECIALIZATION_KEY) == TypeSpecialization.Path.value
        ):
            if metadata.repeated:
                parameter_values[id] = [Path(value) for value in parameter_values[id]]
            else:
                parameter_values[id] = Path(parameter_values[id])

    if parameter_metadata_dict:
        result = [None] * max(parameter_metadata_dict.keys())
    else:
        result = []

    for k, v in parameter_values.items():
        result[k - 1] = v

    return result


def serialize_parameters(
    parameter_metadata_dict: dict[int, ParameterMetadata],
    parameter_values: Sequence[Any],
    message_name: str,
) -> bytes:
    """Serialize parameter values into a parameter byte string.

    Args:
        parameter_metadata_dict: Parameter metadata by ID.

        parameter_values: Parameter values to serialize, ordered by ID.

        message_name: gRPC message name (e.g. f"{service_class}.Configurations").

    Returns:
        Serialized byte string containing parameter values.
    """
    new_parameter_values = list(parameter_values)

    for id in parameter_metadata_dict.keys():
        index = id - 1
        metadata = parameter_metadata_dict[id]
        if (
            metadata.type == FieldDescriptorProto.TYPE_STRING
            and metadata.annotations
            and metadata.annotations.get(TYPE_SPECIALIZATION_KEY) == TypeSpecialization.Path.value
        ):
            if metadata.repeated:
                new_parameter_values[index] = [str(value) for value in parameter_values[index]]
            else:
                new_parameter_values[index] = str(parameter_values[index])

    return _internal_serialize_parameters(
        parameter_metadata_dict, new_parameter_values, message_name
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/measurement/info.py sha256=498083e1995ccff02a71da5c8cf5d0682a7c0c01eb88c45438e5c43094d8883a bytes=1627 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/measurement/info.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/measurement/info.py`
- sha256: `498083e1995ccff02a71da5c8cf5d0682a7c0c01eb88c45438e5c43094d8883a`
- bytes: 1627

````python
"""Measurement service metadata classes and enums."""

from __future__ import annotations

import enum
from pathlib import Path
from typing import NamedTuple

from ni.measurementlink.discovery.v1.client import ServiceInfo

__all__ = ["ServiceInfo", "MeasurementInfo", "TypeSpecialization", "DataType"]


class MeasurementInfo(NamedTuple):
    """A named tuple providing information about a measurement."""

    display_name: str
    """The user visible name of the measurement."""

    version: str
    """The current version of the measurement."""

    ui_file_paths: list[Path]
    """Absolute paths to user interface files for the measurement (e.g. ``.measui`` or ``.vi``
    files)."""


class TypeSpecialization(enum.Enum):
    """Enum that represents the type specializations for measurement parameters."""

    NoType = ""
    Pin = "pin"
    Path = "path"
    Enum = "enum"
    IOResource = "ioresource"


class DataType(enum.Enum):
    """Enum that represents the supported data types."""

    Int32 = 0
    Int64 = 1
    UInt32 = 2
    UInt64 = 3
    Float = 4
    Double = 5
    Boolean = 6
    String = 7
    Pin = 8
    Path = 9
    Enum = 10
    DoubleXYData = 11
    IOResource = 12
    Double2DArray = 13
    String2DArray = 14

    Int32Array1D = 100
    Int64Array1D = 101
    UInt32Array1D = 102
    UInt64Array1D = 103
    FloatArray1D = 104
    DoubleArray1D = 105
    BooleanArray1D = 106
    StringArray1D = 107
    PinArray1D = 108
    PathArray1D = 109
    EnumArray1D = 110
    DoubleXYDataArray1D = 111
    IOResourceArray1D = 112
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/measurement/service.py sha256=fc78d9319c178b867ce48cbda6f63471c8221962ce100b5686a1f9551c4c9ece bytes=25209 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/measurement/service.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/measurement/service.py`
- sha256: `fc78d9319c178b867ce48cbda6f63471c8221962ce100b5686a1f9551c4c9ece`
- bytes: 25209

````python
"""Framework to host measurement service."""

from __future__ import annotations

import json
import sys
import threading
import warnings
from collections.abc import Iterable
from enum import Enum, EnumMeta
from os import path
from pathlib import Path
from types import TracebackType
from typing import (
    Any,
    Callable,
    Literal,
    TYPE_CHECKING,
    TypeVar,
    Union,
)

import grpc
from deprecation import deprecated
from google.protobuf.descriptor import EnumDescriptor
from ni.measurementlink.discovery.v1.client import (
    DiscoveryClient,
    ServiceInfo,
    ServiceLocation,
)
from ni.measurementlink.sessionmanagement.v1.client import (
    MultiSessionReservation,
    PinMapContext,
    SessionManagementClient,
    SingleSessionReservation,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool  # re-export

from ni_measurement_plugin_sdk_service import _datatypeinfo
from ni_measurement_plugin_sdk_service._annotations import (
    ENUM_VALUES_KEY,
    TYPE_SPECIALIZATION_KEY,
)
from ni_measurement_plugin_sdk_service._internal import grpc_servicer
from ni_measurement_plugin_sdk_service._internal.parameter import (
    metadata as parameter_metadata,
)
from ni_measurement_plugin_sdk_service._internal.service_manager import GrpcService
from ni_measurement_plugin_sdk_service.measurement.info import (
    DataType,
    MeasurementInfo,
    TypeSpecialization,
)

if TYPE_CHECKING:
    from google.protobuf.internal.enum_type_wrapper import _EnumTypeWrapper

    if sys.version_info >= (3, 10):
        from typing import TypeGuard
    else:
        from typing_extensions import TypeGuard

    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self

    SupportedEnumType = Union[type[Enum], _EnumTypeWrapper]


class MeasurementContext:
    """Proxy for the Measurement Service's context-local state."""

    @property
    def grpc_context(self) -> grpc.ServicerContext:
        """Get the context for the RPC."""
        return grpc_servicer.measurement_service_context.get().grpc_context

    @property
    def pin_map_context(self) -> PinMapContext:
        """Get the pin map context for the RPC."""
        return grpc_servicer.measurement_service_context.get().pin_map_context

    def add_cancel_callback(self, cancel_callback: Callable[[], None]) -> None:
        """Add a callback which is invoked when the RPC is canceled."""
        grpc_servicer.measurement_service_context.get().add_cancel_callback(cancel_callback)

    def cancel(self) -> None:
        """Cancel the RPC."""
        grpc_servicer.measurement_service_context.get().cancel()

    @property
    def time_remaining(self) -> float:
        """Get the time remaining for the RPC."""
        return grpc_servicer.measurement_service_context.get().time_remaining

    def abort(self, code: grpc.StatusCode, details: str) -> None:
        """Aborts the RPC."""
        grpc_servicer.measurement_service_context.get().abort(code, details)

    @property
    def _measurement_service(self) -> MeasurementService:
        owner = grpc_servicer.measurement_service_context.get().owner
        assert isinstance(owner, MeasurementService)
        return owner

    def reserve_session(
        self,
        pin_or_relay_names: str | Iterable[str],
        timeout: float | None = 0.0,
    ) -> SingleSessionReservation:
        """Reserve a single session.

        Reserve the session matching the given pins, sites, and instrument type ID and return
        the information needed to create or access the session.

        Args:
            pin_or_relay_names: One or multiple pins, pin groups, relays, or relay groups to
                use for the measurement.

            timeout: Timeout in seconds.

                Allowed values: 0 (non-blocking, fails immediately if resources cannot be
                reserved), -1 (infinite timeout), or any other positive numeric value (wait for
                that number of seconds)

        Returns:
            A reservation object with which you can query information about the session and
            unreserve it.
        """
        if not pin_or_relay_names:
            raise ValueError("You must specify at least one pin or relay name.")
        return self._measurement_service.session_management_client.reserve_session(
            context=self.pin_map_context, pin_or_relay_names=pin_or_relay_names, timeout=timeout
        )

    def reserve_sessions(
        self,
        pin_or_relay_names: str | Iterable[str],
        timeout: float | None = 0.0,
    ) -> MultiSessionReservation:
        """Reserve multiple sessions.

        Reserve sessions matching the given pins, sites, and instrument type ID and return the
        information needed to create or access the sessions.

        Args:
            pin_or_relay_names: One or multiple pins, pin groups, relays, or relay groups to use
                for the measurement.

            timeout: Timeout in seconds.

                Allowed values: 0 (non-blocking, fails immediately if resources cannot be
                reserved), -1 (infinite timeout), or any other positive numeric value (wait for
                that number of seconds)

        Returns:
            A reservation object with which you can query information about the sessions and
            unreserve them.
        """
        if not pin_or_relay_names:
            raise ValueError("You must specify at least one pin or relay name.")
        return self._measurement_service.session_management_client.reserve_sessions(
            context=self.pin_map_context, pin_or_relay_names=pin_or_relay_names, timeout=timeout
        )


_F = TypeVar("_F", bound=Callable)


class MeasurementService:
    """Class that supports registering and hosting a python function as a gRPC service."""

    def __init__(
        self,
        service_config_path: Path,
        version: str = "",
        ui_file_paths: list[Path] = [],
        service_class: str | None = None,
    ) -> None:
        """Initialize the Measurement Service object.

        Uses the specified .serviceconfig file, version, and UI file paths
        to initialize a Measurement Service object.

        Args:
            service_config_path (Path): Path to the .serviceconfig file.

            version (str): Version of the measurement service. Do not use this
                parameter.  Instead, specify the "version" field in the
                .serviceconfig file. Default value is "".

            ui_file_paths (List[Path]): List of paths to supported UIs.
                Default value is [].

            service_class (str): The service class from the .serviceconfig to use.
                Default value is None, which will use the first service in the
                .serviceconfig file.

        """
        if not path.exists(service_config_path):
            raise RuntimeError(f"File does not exist. {service_config_path}")

        with open(service_config_path, encoding="utf-8-sig") as service_config_file:
            service_config = json.load(service_config_file)

        if service_class is None:
            service = next(iter(service_config["services"]), None)
        else:
            service = next(
                (s for s in service_config["services"] if s["serviceClass"] == service_class), None
            )
        if not service:
            raise RuntimeError(
                f"Service class '{service_class}' not found in '{service_config_file}'"
            )

        if version:
            warnings.warn(
                "The 'version' constructor parameter is deprecated. Specify the version using the 'version' field in the .serviceconfig file instead.",
                DeprecationWarning,
            )
        config_version = service.get("version")
        if version and config_version is None:
            version = ""
        if config_version is not None:
            if version and version != config_version:
                raise RuntimeError(
                    f"Version mismatch: .serviceconfig version is '{config_version}', but version parameter is '{version}'.",
                )
            version = config_version

        # Note: sphinx-autoapi uses the public attributes' type hints and docstrings.
        self.measurement_info: MeasurementInfo = MeasurementInfo(
            display_name=service["displayName"],
            version=version,
            ui_file_paths=ui_file_paths,
        )
        """Information about the measurement performed by this service."""

        def convert_value_to_str(value: object) -> str:
            if isinstance(value, str):
                return value
            return json.dumps(value, separators=(",", ":"))

        self.service_info: ServiceInfo = ServiceInfo(
            display_name=service["displayName"],
            service_class=service["serviceClass"],
            description_url=service["descriptionUrl"],
            provided_interfaces=service["providedInterfaces"],
            versions=[version],
            annotations={
                key: convert_value_to_str(value)
                for key, value in service.get("annotations", {}).items()
            },
        )
        """Information about this service."""

        self.context: MeasurementContext = MeasurementContext()
        """Accessor for context-local state."""

        self._configuration_parameter_list: list[parameter_metadata.ParameterMetadata] = []
        self._output_parameter_list: list[parameter_metadata.ParameterMetadata] = []
        self._measure_function: Callable = self._raise_measurement_method_not_registered

        self._initialization_lock = threading.RLock()
        self._channel_pool: GrpcChannelPool | None = None
        self._discovery_client: DiscoveryClient | None = None
        self._grpc_service: GrpcService | None = None
        self._session_management_client: SessionManagementClient | None = None

    def _raise_measurement_method_not_registered(self) -> Any:
        raise RuntimeError(
            "Measurement method not registered. Use the register_measurement decorator to register it."
        )

    @property
    def channel_pool(self) -> GrpcChannelPool:
        """Pool of gRPC channels used by the service."""
        if self._channel_pool is None:
            with self._initialization_lock:
                if self._channel_pool is None:
                    self._channel_pool = GrpcChannelPool()
        return self._channel_pool

    @property
    def discovery_client(self) -> DiscoveryClient:
        """Client for accessing the NI Discovery Service."""
        if self._discovery_client is None:
            with self._initialization_lock:
                if self._discovery_client is None:
                    self._discovery_client = DiscoveryClient(grpc_channel_pool=self.channel_pool)
        return self._discovery_client

    @property
    @deprecated(
        deprecated_in="1.3.0-dev0",
        details="This property should not be public and will be removed in a later release.",
    )
    def configuration_parameter_list(self) -> list[Any]:
        """List of configuration parameters."""
        return self._configuration_parameter_list

    @property
    @deprecated(
        deprecated_in="1.3.0-dev0",
        details="This property should not be public and will be removed in a later release.",
    )
    def grpc_service(self) -> GrpcService | None:
        """The gRPC service object. This is a private implementation detail."""
        return self._grpc_service

    @property
    @deprecated(
        deprecated_in="1.3.0-dev0",
        details="This property should not be public and will be removed in a later release.",
    )
    def measure_function(self) -> Callable:
        """Registered measurement function."""
        return self._measure_function

    @property
    @deprecated(
        deprecated_in="1.3.0-dev0",
        details="This property should not be public and will be removed in a later release.",
    )
    def output_parameter_list(self) -> list[Any]:
        """List of output parameters."""
        return self._output_parameter_list

    @property
    def service_location(self) -> ServiceLocation:
        """The location of the service on the network."""
        with self._initialization_lock:
            if self._grpc_service is None:
                raise RuntimeError("Measurement service not running")
            return self._grpc_service.service_location

    @property
    def session_management_client(self) -> SessionManagementClient:
        """Client for accessing the measurement plug-in session management service."""
        if self._session_management_client is None:
            with self._initialization_lock:
                if self._session_management_client is None:
                    self._session_management_client = SessionManagementClient(
                        discovery_client=self.discovery_client,
                        grpc_channel_pool=self.channel_pool,
                    )
        return self._session_management_client

    def register_measurement(self, measurement_function: _F) -> _F:
        """Register a function as the measurement function for a measurement service.

        To declare a measurement function, use this idiom::

            @measurement_service.register_measurement
            @measurement_service.configuration("Configuration 1", ...)
            @measurement_service.configuration("Configuration 2", ...)
            @measurement_service.output("Output 1", ...)
            @measurement_service.output("Output 2", ...)
            def measure(configuration1, configuration2):
                ...
                return (output1, output2)

        See also: :func:`.configuration`, :func:`.output`
        """
        self._measure_function = measurement_function
        return measurement_function

    def configuration(
        self,
        display_name: str,
        type: DataType,
        default_value: Any,
        *,
        instrument_type: str = "",
        enum_type: SupportedEnumType | None = None,
    ) -> Callable[[_F], _F]:
        """Add a configuration parameter to a measurement function.

        This decorator maps the measurement service's configuration parameters
        to Python positional parameters. To add multiple configuration parameters
        to the same measurement function, use this decorator multiple times.
        The order of decorator calls must match the order of positional parameters.

        See also: :func:`.register_measurement`

        Args:
            display_name: Display name of the configuration.

            type: Data type of the configuration.

            default_value: Default value of the configuration.

            instrument_type:
                Filter pins by instrument type. This is only supported when configuration type
                is DataType.IOResource or DataType.Pin (deprecated).

                For NI instruments, use instrument type id constants defined by
                :py:mod:`ni_measurement_plugin_sdk_service.session_management`, such as
                :py:const:`~ni_measurement_plugin_sdk_service.session_management.INSTRUMENT_TYPE_NI_DCPOWER`
                or
                :py:const:`~ni_measurement_plugin_sdk_service.session_management.INSTRUMENT_TYPE_NI_DMM`.

                For custom instruments, use the instrument type id defined in the pin map file.

            enum_type:
                Defines the enum type associated with this configuration parameter. This is only
                supported when configuration type is DataType.Enum or DataType.EnumArray1D.

        Returns:
            Callable that takes in Any Python Function
            and returns the same python function.
        """
        if type == DataType.Pin:
            warnings.warn(
                "DataType.Pin is deprecated. Use DataType.IOResource instead.", DeprecationWarning
            )
        if type == DataType.PinArray1D:
            warnings.warn(
                "DataType.PinArray1D is deprecated. Use DataType.IOResourceArray1D instead.",
                DeprecationWarning,
            )
        if type in [
            DataType.Double2DArray,
            DataType.DoubleXYData,
            DataType.DoubleXYDataArray1D,
            DataType.String2DArray,
        ]:
            raise ValueError(f"{type} is not supported for configuration parameters.")
        data_type_info = _datatypeinfo.get_type_info(type)
        annotations = self._make_annotations_dict(
            data_type_info.type_specialization, instrument_type=instrument_type, enum_type=enum_type
        )
        parameter = parameter_metadata.ParameterMetadata.initialize(
            display_name,
            data_type_info.grpc_field_type,
            data_type_info.repeated,
            default_value,
            annotations,
            data_type_info.message_type,
            enum_type,
        )
        self._configuration_parameter_list.append(parameter)

        def _configuration(func: _F) -> _F:
            return func

        return _configuration

    def output(
        self,
        display_name: str,
        type: DataType,
        *,
        enum_type: SupportedEnumType | None = None,
    ) -> Callable[[_F], _F]:
        """Add an output parameter to a measurement function.

        This decorator maps the measurement service's output parameters to
        the elements of the tuple returned by the measurement function.
        To add multiple output parameters to the same measurement function,
        use this decorator multiple times.
        The order of decorator calls must match the order of elements
        returned by the measurement function.

        See also: :func:`.register_measurement`

        Args:
            display_name: Display name of the output.

            type: Data type of the output.

            enum_type:
                Defines the enum type associated with this configuration parameter. This is only
                supported when configuration type is DataType.Enum or DataType.EnumArray1D.

        Returns:
            Callable that takes in Any Python Function and
            returns the same python function.
        """
        if type == DataType.Pin:
            warnings.warn(
                "DataType.Pin is deprecated. Use DataType.IOResource instead.", DeprecationWarning
            )
        if type == DataType.PinArray1D:
            warnings.warn(
                "DataType.PinArray1D is deprecated. Use DataType.IOResourceArray1D instead.",
                DeprecationWarning,
            )
        data_type_info = _datatypeinfo.get_type_info(type)
        annotations = self._make_annotations_dict(
            data_type_info.type_specialization, enum_type=enum_type
        )
        parameter = parameter_metadata.ParameterMetadata.initialize(
            display_name,
            data_type_info.grpc_field_type,
            data_type_info.repeated,
            None,
            annotations,
            data_type_info.message_type,
            enum_type,
        )
        self._output_parameter_list.append(parameter)

        def _output(func: _F) -> _F:
            return func

        return _output

    def host_service(self) -> MeasurementService:
        """Host the registered measurement method as a gRPC measurement service.

        Returns:
            MeasurementService: Context manager that can be used with a with-statement to close
            the service.

        Raises:
            Exception: If register measurement methods not available.
        """
        with self._initialization_lock:
            if self._measure_function is self._raise_measurement_method_not_registered:
                self._raise_measurement_method_not_registered()
            if self._grpc_service is not None:
                raise RuntimeError("Measurement service already running.")

            self._grpc_service = GrpcService(self.discovery_client)
            self._grpc_service.start(
                self.measurement_info,
                self.service_info,
                self._configuration_parameter_list,
                self._output_parameter_list,
                self._measure_function,
                owner=self,
            )
            return self

    def _make_annotations_dict(
        self,
        type_specialization: TypeSpecialization,
        *,
        instrument_type: str = "",
        enum_type: SupportedEnumType | None = None,
    ) -> dict[str, str]:
        annotations: dict[str, str] = {}
        if type_specialization == TypeSpecialization.NoType:
            return annotations

        annotations[TYPE_SPECIALIZATION_KEY] = type_specialization.value
        if type_specialization == TypeSpecialization.Pin:
            if instrument_type != "" or instrument_type is not None:
                annotations["ni/pin.instrument_type"] = instrument_type
        if type_specialization == TypeSpecialization.IOResource:
            if instrument_type != "" or instrument_type is not None:
                annotations["ni/ioresource.instrument_type"] = instrument_type
        if type_specialization == TypeSpecialization.Enum:
            if enum_type is not None:
                annotations[ENUM_VALUES_KEY] = self._enum_to_annotations_value(enum_type)
            else:
                raise ValueError("enum_type is required for enum parameters.")

        return annotations

    def _enum_to_annotations_value(self, enum_type: SupportedEnumType) -> str:
        enum_values = {}
        # For protobuf enums, enum_type is an instance of EnumTypeWrapper at run time, so passing
        # it to issubclass() would raise an error.
        if self._is_protobuf_enum(enum_type):
            if 0 not in enum_type.values():
                raise ValueError("The enum does not have a value for 0.")
            for name, value in enum_type.items():
                enum_values[name] = value
        elif isinstance(enum_type, EnumMeta):
            if not any(member.value == 0 for member in enum_type):
                raise ValueError("The enum does not have a value for 0.")
            for member in enum_type:
                enum_values[member.name] = member.value
        return json.dumps(enum_values)

    def _is_protobuf_enum(self, enum_type: SupportedEnumType) -> TypeGuard[_EnumTypeWrapper]:
        # Use EnumDescriptor to check for protobuf enums at run time without using
        # google.protobuf.internal.
        return isinstance(getattr(enum_type, "DESCRIPTOR", None), EnumDescriptor)

    def close_service(self) -> None:
        """Stop the gRPC measurement service.

        This method stops the gRPC server, unregisters with the discovery service, and cleans up
        the cached discovery client and gRPC channel pool.

        After calling close_service(), you may call host_service() again.

        Exiting the measurement service's runtime context automatically calls close_service().
        """
        with self._initialization_lock:
            if self._grpc_service is not None:
                self._grpc_service.stop()
            if self._channel_pool is not None:
                self._channel_pool.close()

            self._grpc_service = None
            self._channel_pool = None
            self._discovery_client = None

    def __enter__(self: Self) -> Self:
        """Enter the runtime context related to the measurement service."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> Literal[False]:
        """Exit the runtime context related to the measurement service."""
        self.close_service()
        return False

    def get_channel(self, provided_interface: str, service_class: str = "") -> grpc.Channel:
        """Return gRPC channel to specified service.

        Args:
            provided_interface (str): The gRPC Full Name of the service.

            service_class (str): The service "class" that should be matched.

        Returns:
            grpc.Channel: A channel to the gRPC service.

        Raises:
            Exception: If service_class is not specified and there is more than one matching service
                registered.
        """
        service_location = self.discovery_client.resolve_service(provided_interface, service_class)
        return self.channel_pool.get_channel(service_location.insecure_address)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/pin_map/__init__.py sha256=b300dabc1ece1a97ed225f298b8263372658dcb6f60fd68720c7f14e4ce90c16 bytes=447 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/pin_map/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/pin_map/__init__.py`
- sha256: `b300dabc1ece1a97ed225f298b8263372658dcb6f60fd68720c7f14e4ce90c16`
- bytes: 447

````python
"""Compatibility API for accessing the NI Pin Map Service.

The public API for accessing the NI Pin Map Service has moved to the
:mod:`ni.measurementlink.pinmap.v1.client` package.

The :mod:`ni_measurement_plugin_sdk_service.pin_map` subpackage provides
compatibility with existing applications and will be deprecated in a future
release.
"""

from ni.measurementlink.pinmap.v1.client import PinMapClient

__all__ = ["PinMapClient"]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/py.typed sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/py.typed

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/py.typed`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````text

````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/session_management/__init__.py sha256=b259d33ce1623b9d4bca44f05d8f011343c5227069ba67e97d7d919904d7c0d3 bytes=2722 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/session_management/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/session_management/__init__.py`
- sha256: `b259d33ce1623b9d4bca44f05d8f011343c5227069ba67e97d7d919904d7c0d3`
- bytes: 2722

````python
"""Compatibility API for accessing the NI Session Management Service.

The public API for accessing the NI Session Management Service has moved to the
:mod:`ni.measurementlink.sessionmanagement.v1.client` package.

The :mod:`ni_measurement_plugin_sdk_service.session_management` subpackage
provides compatibility with existing applications and will be deprecated in a
future release.
"""

from ni.measurementlink.sessionmanagement.v1.client import (
    GRPC_SERVICE_CLASS,
    GRPC_SERVICE_INTERFACE_NAME,
    INSTRUMENT_TYPE_NI_DAQMX,
    INSTRUMENT_TYPE_NI_DCPOWER,
    INSTRUMENT_TYPE_NI_DIGITAL_PATTERN,
    INSTRUMENT_TYPE_NI_DMM,
    INSTRUMENT_TYPE_NI_FGEN,
    INSTRUMENT_TYPE_NI_HSDIO,
    INSTRUMENT_TYPE_NI_MODEL_BASED_INSTRUMENT,
    INSTRUMENT_TYPE_NI_RELAY_DRIVER,
    INSTRUMENT_TYPE_NI_RFMX,
    INSTRUMENT_TYPE_NI_RFPM,
    INSTRUMENT_TYPE_NI_RFSA,
    INSTRUMENT_TYPE_NI_RFSG,
    INSTRUMENT_TYPE_NI_SCOPE,
    INSTRUMENT_TYPE_NI_SWITCH_EXECUTIVE_VIRTUAL_DEVICE,
    INSTRUMENT_TYPE_NONE,
    SITE_SYSTEM_PINS,
    BaseReservation,
    ChannelMapping,
    Connection,
    MultiplexerSessionContainer,
    MultiplexerSessionInformation,
    MultiSessionReservation,
    PinMapContext,
    SessionInformation,
    SessionInitializationBehavior,
    SessionManagementClient,
    SingleSessionReservation,
    TypedConnection,
    TypedConnectionWithMultiplexer,
    TypedMultiplexerSessionInformation,
    TypedSessionInformation,
)

__all__ = [
    "GRPC_SERVICE_CLASS",
    "GRPC_SERVICE_INTERFACE_NAME",
    "INSTRUMENT_TYPE_NONE",
    "INSTRUMENT_TYPE_NI_DCPOWER",
    "INSTRUMENT_TYPE_NI_HSDIO",
    "INSTRUMENT_TYPE_NI_RFSA",
    "INSTRUMENT_TYPE_NI_RFMX",
    "INSTRUMENT_TYPE_NI_RFSG",
    "INSTRUMENT_TYPE_NI_RFPM",
    "INSTRUMENT_TYPE_NI_DMM",
    "INSTRUMENT_TYPE_NI_DIGITAL_PATTERN",
    "INSTRUMENT_TYPE_NI_SCOPE",
    "INSTRUMENT_TYPE_NI_FGEN",
    "INSTRUMENT_TYPE_NI_DAQMX",
    "INSTRUMENT_TYPE_NI_RELAY_DRIVER",
    "INSTRUMENT_TYPE_NI_MODEL_BASED_INSTRUMENT",
    "INSTRUMENT_TYPE_NI_SWITCH_EXECUTIVE_VIRTUAL_DEVICE",
    "SITE_SYSTEM_PINS",
    "BaseReservation",
    "ChannelMapping",
    "Connection",
    "MultiplexerSessionInformation",
    "MultiplexerSessionContainer",
    "MultiSessionReservation",
    "PinMapContext",
    "SessionInformation",
    "SessionInitializationBehavior",
    "SessionManagementClient",
    "SingleSessionReservation",
    "TypedConnection",
    "TypedConnectionWithMultiplexer",
    "TypedMultiplexerSessionInformation",
    "TypedSessionInformation",
]

Client = SessionManagementClient
"""Alias for compatibility with code that uses session_management.Client."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/session_management/_reservation.py sha256=047eca68352aa93b96d30d51b02288d069bad137a24c5139674db00b2b7fd594 bytes=325 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/session_management/_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/session_management/_reservation.py`
- sha256: `047eca68352aa93b96d30d51b02288d069bad137a24c5139674db00b2b7fd594`
- bytes: 325

````python
from ni.measurementlink.sessionmanagement.v1.client import (
    BaseReservation,
    MultiplexerSessionContainer,
    MultiSessionReservation,
    SingleSessionReservation,
)

__all__ = [
    "BaseReservation",
    "MultiplexerSessionContainer",
    "MultiSessionReservation",
    "SingleSessionReservation",
]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/ni_measurement_plugin_sdk_service/session_management/_types.py sha256=7a5c6ce7fbbc0925f377565a76871f93437389203c97559ab491754213e746c9 bytes=673 -->
## FILE: packages/service/ni_measurement_plugin_sdk_service/session_management/_types.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/ni_measurement_plugin_sdk_service/session_management/_types.py`
- sha256: `7a5c6ce7fbbc0925f377565a76871f93437389203c97559ab491754213e746c9`
- bytes: 673

````python
from ni.measurementlink.sessionmanagement.v1.client import (
    ChannelMapping,
    Connection,
    MultiplexerSessionInformation,
    PinMapContext,
    SessionInformation,
    SessionInitializationBehavior,
    TypedConnection,
    TypedConnectionWithMultiplexer,
    TypedMultiplexerSessionInformation,
    TypedSessionInformation,
)

__all__ = [
    "ChannelMapping",
    "Connection",
    "MultiplexerSessionInformation",
    "PinMapContext",
    "SessionInformation",
    "SessionInitializationBehavior",
    "TypedConnection",
    "TypedConnectionWithMultiplexer",
    "TypedMultiplexerSessionInformation",
    "TypedSessionInformation",
]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/poetry.lock sha256=de481d8aefe87c431288461f12dc1065984646c26fbc31f03e12cf2a3cc119c7 bytes=248178 -->
## FILE: packages/service/poetry.lock

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/poetry.lock`
- sha256: `de481d8aefe87c431288461f12dc1065984646c26fbc31f03e12cf2a3cc119c7`
- bytes: 248178

````text
# This file is automatically @generated by Poetry 2.4.1 and should not be changed by hand.

[[package]]
name = "alabaster"
version = "0.7.16"
description = "A light, configurable Sphinx theme"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version == \"3.10\""
files = [
    {file = "alabaster-0.7.16-py3-none-any.whl", hash = "sha256:b46733c07dce03ae4e150330b975c75737fa60f0a7c591b6c8bf4928a28e2c92"},
    {file = "alabaster-0.7.16.tar.gz", hash = "sha256:75a8b99c28a5dad50dd7f8ccdd447a121ddb3892da9e53d1ca5cca3106d58d65"},
]

[[package]]
name = "alabaster"
version = "1.0.0"
description = "A light, configurable Sphinx theme"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
markers = "python_version >= \"3.11\""
files = [
    {file = "alabaster-1.0.0-py3-none-any.whl", hash = "sha256:fc6786402dc3fcb2de3cabd5fe455a2db534b371124f1f21de8731783dec828b"},
    {file = "alabaster-1.0.0.tar.gz", hash = "sha256:c00dca57bca26fa62a6d7d0a9fcce65f3e026e9bfe33e9c538fd3fbb2144fd9e"},
]

[[package]]
name = "astroid"
version = "4.0.3"
description = "An abstract syntax tree for Python with inference support."
optional = false
python-versions = ">=3.10.0"
groups = ["docs"]
files = [
    {file = "astroid-4.0.3-py3-none-any.whl", hash = "sha256:864a0a34af1bd70e1049ba1e61cee843a7252c826d97825fcee9b2fcbd9e1b14"},
    {file = "astroid-4.0.3.tar.gz", hash = "sha256:08d1de40d251cc3dc4a7a12726721d475ac189e4e583d596ece7422bc176bda3"},
]

[package.dependencies]
typing-extensions = {version = ">=4", markers = "python_version < \"3.11\""}

[[package]]
name = "babel"
version = "2.17.0"
description = "Internationalization utilities"
optional = false
python-versions = ">=3.8"
groups = ["docs"]
files = [
    {file = "babel-2.17.0-py3-none-any.whl", hash = "sha256:4d0b53093fdfb4b21c92b5213dba5a1b23885afa8383709427046b21c366e5f2"},
    {file = "babel-2.17.0.tar.gz", hash = "sha256:0c54cffb19f690cdcc52a3b50bcbf71e07a808d1c80d549f2459b9d2cf0afb9d"},
]

[package.extras]
dev = ["backports.zoneinfo ; python_version < \"3.9\"", "freezegun (>=1.0,<2.0)", "jinja2 (>=3.0)", "pytest (>=6.0)", "pytest-cov", "pytz", "setuptools", "tzdata ; sys_platform == \"win32\""]

[[package]]
name = "bandit"
version = "1.9.4"
description = "Security oriented static analyser for python code."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "bandit-1.9.4-py3-none-any.whl", hash = "sha256:f89ffa663767f5a0585ea075f01020207e966a9c0f2b9ef56a57c7963a3f6f8e"},
    {file = "bandit-1.9.4.tar.gz", hash = "sha256:b589e5de2afe70bd4d53fa0c1da6199f4085af666fde00e8a034f152a52cd628"},
]

[package.dependencies]
colorama = {version = ">=0.3.9", markers = "platform_system == \"Windows\""}
PyYAML = ">=5.3.1"
rich = "*"
stevedore = ">=1.20.0"
tomli = {version = ">=1.1.0", optional = true, markers = "python_version < \"3.11\" and extra == \"toml\""}

[package.extras]
baseline = ["GitPython (>=3.1.30)"]
sarif = ["jschema-to-python (>=1.2.3)", "sarif-om (>=1.0.4)"]
test = ["beautifulsoup4 (>=4.8.0)", "coverage (>=4.5.4)", "fixtures (>=3.0.0)", "flake8 (>=4.0.0)", "pylint (==1.9.4)", "stestr (>=2.5.0)", "testscenarios (>=0.5.0)", "testtools (>=2.3.0)"]
toml = ["tomli (>=1.1.0) ; python_version < \"3.11\""]
yaml = ["PyYAML"]

[[package]]
name = "better-diff"
version = "0.1.4"
description = "A simple library for printing better diffs based on the stdlib unified_diff format."
optional = false
python-versions = "<4.0,>=3.8"
groups = ["dev"]
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
groups = ["dev"]
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
name = "cachetools"
version = "7.0.6"
description = "Extensible memoizing collections and decorators"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "cachetools-7.0.6-py3-none-any.whl", hash = "sha256:4e94956cfdd3086f12042cdd29318f5ced3893014f7d0d059bf3ead3f85b7f8b"},
    {file = "cachetools-7.0.6.tar.gz", hash = "sha256:e5d524d36d65703a87243a26ff08ad84f73352adbeafb1cde81e207b456aaf24"},
]

[[package]]
name = "certifi"
version = "2026.1.4"
description = "Python package for providing Mozilla's CA Bundle."
optional = false
python-versions = ">=3.7"
groups = ["main", "docs"]
files = [
    {file = "certifi-2026.1.4-py3-none-any.whl", hash = "sha256:9943707519e4add1115f44c2bc244f782c0249876bf51b6599fee1ffbedd685c"},
    {file = "certifi-2026.1.4.tar.gz", hash = "sha256:ac726dd470482006e014ad384921ed6438c457018f4b3d204aea4281258b2120"},
]
markers = {main = "extra == \"drivers\" or extra == \"nidaqmx\""}

[[package]]
name = "charset-normalizer"
version = "3.4.4"
description = "The Real First Universal Charset Detector. Open, modern and actively maintained alternative to Chardet."
optional = false
python-versions = ">=3.7"
groups = ["main", "docs"]
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
markers = {main = "extra == \"drivers\" or extra == \"nidaqmx\""}

[[package]]
name = "click"
version = "8.3.1"
description = "Composable command line interface toolkit"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev", "docs"]
files = [
    {file = "click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6"},
    {file = "click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a"},
]
markers = {main = "extra == \"drivers\" or extra == \"nidaqmx\""}

[package.dependencies]
colorama = {version = "*", markers = "platform_system == \"Windows\""}

[[package]]
name = "colorama"
version = "0.4.6"
description = "Cross-platform colored terminal text."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=2.7"
groups = ["main", "dev", "docs"]
files = [
    {file = "colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6"},
    {file = "colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44"},
]
markers = {main = "platform_system == \"Windows\" and (extra == \"drivers\" or extra == \"nidaqmx\")", docs = "platform_system == \"Windows\" or sys_platform == \"win32\""}

[[package]]
name = "coverage"
version = "7.13.2"
description = "Code coverage measurement for Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "coverage-7.13.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:f4af3b01763909f477ea17c962e2cca8f39b350a4e46e3a30838b2c12e31b81b"},
    {file = "coverage-7.13.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:36393bd2841fa0b59498f75466ee9bdec4f770d3254f031f23e8fd8e140ffdd2"},
    {file = "coverage-7.13.2-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:9cc7573518b7e2186bd229b1a0fe24a807273798832c27032c4510f47ffdb896"},
    {file = "coverage-7.13.2-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:ca9566769b69a5e216a4e176d54b9df88f29d750c5b78dbb899e379b4e14b30c"},
    {file = "coverage-7.13.2-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9c9bdea644e94fd66d75a6f7e9a97bb822371e1fe7eadae2cacd50fcbc28e4dc"},
    {file = "coverage-7.13.2-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:5bd447332ec4f45838c1ad42268ce21ca87c40deb86eabd59888859b66be22a5"},
    {file = "coverage-7.13.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:7c79ad5c28a16a1277e1187cf83ea8dafdcc689a784228a7d390f19776db7c31"},
    {file = "coverage-7.13.2-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:76e06ccacd1fb6ada5d076ed98a8c6f66e2e6acd3df02819e2ee29fd637b76ad"},
    {file = "coverage-7.13.2-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:49d49e9a5e9f4dc3d3dac95278a020afa6d6bdd41f63608a76fa05a719d5b66f"},
    {file = "coverage-7.13.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:ed2bce0e7bfa53f7b0b01c722da289ef6ad4c18ebd52b1f93704c21f116360c8"},
    {file = "coverage-7.13.2-cp310-cp310-win32.whl", hash = "sha256:1574983178b35b9af4db4a9f7328a18a14a0a0ce76ffaa1c1bacb4cc82089a7c"},
    {file = "coverage-7.13.2-cp310-cp310-win_amd64.whl", hash = "sha256:a360a8baeb038928ceb996f5623a4cd508728f8f13e08d4e96ce161702f3dd99"},
    {file = "coverage-7.13.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:060ebf6f2c51aff5ba38e1f43a2095e087389b1c69d559fde6049a4b0001320e"},
    {file = "coverage-7.13.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c1ea8ca9db5e7469cd364552985e15911548ea5b69c48a17291f0cac70484b2e"},
    {file = "coverage-7.13.2-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:b780090d15fd58f07cf2011943e25a5f0c1c894384b13a216b6c86c8a8a7c508"},
    {file = "coverage-7.13.2-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:88a800258d83acb803c38175b4495d293656d5fac48659c953c18e5f539a274b"},
    {file = "coverage-7.13.2-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6326e18e9a553e674d948536a04a80d850a5eeefe2aae2e6d7cf05d54046c01b"},
    {file = "coverage-7.13.2-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:59562de3f797979e1ff07c587e2ac36ba60ca59d16c211eceaa579c266c5022f"},
    {file = "coverage-7.13.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:27ba1ed6f66b0e2d61bfa78874dffd4f8c3a12f8e2b5410e515ab345ba7bc9c3"},
    {file = "coverage-7.13.2-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:8be48da4d47cc68754ce643ea50b3234557cbefe47c2f120495e7bd0a2756f2b"},
    {file = "coverage-7.13.2-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:2a47a4223d3361b91176aedd9d4e05844ca67d7188456227b6bf5e436630c9a1"},
    {file = "coverage-7.13.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:c6f141b468740197d6bd38f2b26ade124363228cc3f9858bd9924ab059e00059"},
    {file = "coverage-7.13.2-cp311-cp311-win32.whl", hash = "sha256:89567798404af067604246e01a49ef907d112edf2b75ef814b1364d5ce267031"},
    {file = "coverage-7.13.2-cp311-cp311-win_amd64.whl", hash = "sha256:21dd57941804ae2ac7e921771a5e21bbf9aabec317a041d164853ad0a96ce31e"},
    {file = "coverage-7.13.2-cp311-cp311-win_arm64.whl", hash = "sha256:10758e0586c134a0bafa28f2d37dd2cdb5e4a90de25c0fc0c77dabbad46eca28"},
    {file = "coverage-7.13.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:f106b2af193f965d0d3234f3f83fc35278c7fb935dfbde56ae2da3dd2c03b84d"},
    {file = "coverage-7.13.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:78f45d21dc4d5d6bd29323f0320089ef7eae16e4bef712dff79d184fa7330af3"},
    {file = "coverage-7.13.2-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:fae91dfecd816444c74531a9c3d6ded17a504767e97aa674d44f638107265b99"},
    {file = "coverage-7.13.2-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:264657171406c114787b441484de620e03d8f7202f113d62fcd3d9688baa3e6f"},
    {file = "coverage-7.13.2-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ae47d8dcd3ded0155afbb59c62bd8ab07ea0fd4902e1c40567439e6db9dcaf2f"},
    {file = "coverage-7.13.2-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:8a0b33e9fd838220b007ce8f299114d406c1e8edb21336af4c97a26ecfd185aa"},
    {file = "coverage-7.13.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:b3becbea7f3ce9a2d4d430f223ec15888e4deb31395840a79e916368d6004cce"},
    {file = "coverage-7.13.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:f819c727a6e6eeb8711e4ce63d78c620f69630a2e9d53bc95ca5379f57b6ba94"},
    {file = "coverage-7.13.2-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:4f7b71757a3ab19f7ba286e04c181004c1d61be921795ee8ba6970fd0ec91da5"},
    {file = "coverage-7.13.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:b7fc50d2afd2e6b4f6f2f403b70103d280a8e0cb35320cbbe6debcda02a1030b"},
    {file = "coverage-7.13.2-cp312-cp312-win32.whl", hash = "sha256:292250282cf9bcf206b543d7608bda17ca6fc151f4cbae949fc7e115112fbd41"},
    {file = "coverage-7.13.2-cp312-cp312-win_amd64.whl", hash = "sha256:eeea10169fac01549a7921d27a3e517194ae254b542102267bef7a93ed38c40e"},
    {file = "coverage-7.13.2-cp312-cp312-win_arm64.whl", hash = "sha256:2a5b567f0b635b592c917f96b9a9cb3dbd4c320d03f4bf94e9084e494f2e8894"},
    {file = "coverage-7.13.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:ed75de7d1217cf3b99365d110975f83af0528c849ef5180a12fd91b5064df9d6"},
    {file = "coverage-7.13.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:97e596de8fa9bada4d88fde64a3f4d37f1b6131e4faa32bad7808abc79887ddc"},
    {file = "coverage-7.13.2-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:68c86173562ed4413345410c9480a8d64864ac5e54a5cda236748031e094229f"},
    {file = "coverage-7.13.2-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:7be4d613638d678b2b3773b8f687537b284d7074695a43fe2fbbfc0e31ceaed1"},
    {file = "coverage-7.13.2-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d7f63ce526a96acd0e16c4af8b50b64334239550402fb1607ce6a584a6d62ce9"},
    {file = "coverage-7.13.2-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:406821f37f864f968e29ac14c3fccae0fec9fdeba48327f0341decf4daf92d7c"},
    {file = "coverage-7.13.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:ee68e5a4e3e5443623406b905db447dceddffee0dceb39f4e0cd9ec2a35004b5"},
    {file = "coverage-7.13.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:2ee0e58cca0c17dd9c6c1cdde02bb705c7b3fbfa5f3b0b5afeda20d4ebff8ef4"},
    {file = "coverage-7.13.2-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:6e5bbb5018bf76a56aabdb64246b5288d5ae1b7d0dd4d0534fe86df2c2992d1c"},
    {file = "coverage-7.13.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:a55516c68ef3e08e134e818d5e308ffa6b1337cc8b092b69b24287bf07d38e31"},
    {file = "coverage-7.13.2-cp313-cp313-win32.whl", hash = "sha256:5b20211c47a8abf4abc3319d8ce2464864fa9f30c5fcaf958a3eed92f4f1fef8"},
    {file = "coverage-7.13.2-cp313-cp313-win_amd64.whl", hash = "sha256:14f500232e521201cf031549fb1ebdfc0a40f401cf519157f76c397e586c3beb"},
    {file = "coverage-7.13.2-cp313-cp313-win_arm64.whl", hash = "sha256:9779310cb5a9778a60c899f075a8514c89fa6d10131445c2207fc893e0b14557"},
    {file = "coverage-7.13.2-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:e64fa5a1e41ce5df6b547cbc3d3699381c9e2c2c369c67837e716ed0f549d48e"},
    {file = "coverage-7.13.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:b01899e82a04085b6561eb233fd688474f57455e8ad35cd82286463ba06332b7"},
    {file = "coverage-7.13.2-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:838943bea48be0e2768b0cf7819544cdedc1bbb2f28427eabb6eb8c9eb2285d3"},
    {file = "coverage-7.13.2-cp313-cp313t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:93d1d25ec2b27e90bcfef7012992d1f5121b51161b8bffcda756a816cf13c2c3"},
    {file = "coverage-7.13.2-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:93b57142f9621b0d12349c43fc7741fe578e4bc914c1e5a54142856cfc0bf421"},
    {file = "coverage-7.13.2-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:f06799ae1bdfff7ccb8665d75f8291c69110ba9585253de254688aa8a1ccc6c5"},
    {file = "coverage-7.13.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:7f9405ab4f81d490811b1d91c7a20361135a2df4c170e7f0b747a794da5b7f23"},
    {file = "coverage-7.13.2-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:f9ab1d5b86f8fbc97a5b3cd6280a3fd85fef3b028689d8a2c00918f0d82c728c"},
    {file = "coverage-7.13.2-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:f674f59712d67e841525b99e5e2b595250e39b529c3bda14764e4f625a3fa01f"},
    {file = "coverage-7.13.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:c6cadac7b8ace1ba9144feb1ae3cb787a6065ba6d23ffc59a934b16406c26573"},
    {file = "coverage-7.13.2-cp313-cp313t-win32.whl", hash = "sha256:14ae4146465f8e6e6253eba0cccd57423e598a4cb925958b240c805300918343"},
    {file = "coverage-7.13.2-cp313-cp313t-win_amd64.whl", hash = "sha256:9074896edd705a05769e3de0eac0a8388484b503b68863dd06d5e473f874fd47"},
    {file = "coverage-7.13.2-cp313-cp313t-win_arm64.whl", hash = "sha256:69e526e14f3f854eda573d3cf40cffd29a1a91c684743d904c33dbdcd0e0f3e7"},
    {file = "coverage-7.13.2-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:387a825f43d680e7310e6f325b2167dd093bc8ffd933b83e9aa0983cf6e0a2ef"},
    {file = "coverage-7.13.2-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:f0d7fea9d8e5d778cd5a9e8fc38308ad688f02040e883cdc13311ef2748cb40f"},
    {file = "coverage-7.13.2-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:e080afb413be106c95c4ee96b4fffdc9e2fa56a8bbf90b5c0918e5c4449412f5"},
    {file = "coverage-7.13.2-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:a7fc042ba3c7ce25b8a9f097eb0f32a5ce1ccdb639d9eec114e26def98e1f8a4"},
    {file = "coverage-7.13.2-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d0ba505e021557f7f8173ee8cd6b926373d8653e5ff7581ae2efce1b11ef4c27"},
    {file = "coverage-7.13.2-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:7de326f80e3451bd5cc7239ab46c73ddb658fe0b7649476bc7413572d36cd548"},
    {file = "coverage-7.13.2-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:abaea04f1e7e34841d4a7b343904a3f59481f62f9df39e2cd399d69a187a9660"},
    {file = "coverage-7.13.2-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:9f93959ee0c604bccd8e0697be21de0887b1f73efcc3aa73a3ec0fd13feace92"},
    {file = "coverage-7.13.2-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:13fe81ead04e34e105bf1b3c9f9cdf32ce31736ee5d90a8d2de02b9d3e1bcb82"},
    {file = "coverage-7.13.2-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:d6d16b0f71120e365741bca2cb473ca6fe38930bc5431c5e850ba949f708f892"},
    {file = "coverage-7.13.2-cp314-cp314-win32.whl", hash = "sha256:9b2f4714bb7d99ba3790ee095b3b4ac94767e1347fe424278a0b10acb3ff04fe"},
    {file = "coverage-7.13.2-cp314-cp314-win_amd64.whl", hash = "sha256:e4121a90823a063d717a96e0a0529c727fb31ea889369a0ee3ec00ed99bf6859"},
    {file = "coverage-7.13.2-cp314-cp314-win_arm64.whl", hash = "sha256:6873f0271b4a15a33e7590f338d823f6f66f91ed147a03938d7ce26efd04eee6"},
    {file = "coverage-7.13.2-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:f61d349f5b7cd95c34017f1927ee379bfbe9884300d74e07cf630ccf7a610c1b"},
    {file = "coverage-7.13.2-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:a43d34ce714f4ca674c0d90beb760eb05aad906f2c47580ccee9da8fe8bfb417"},
    {file = "coverage-7.13.2-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:bff1b04cb9d4900ce5c56c4942f047dc7efe57e2608cb7c3c8936e9970ccdbee"},
    {file = "coverage-7.13.2-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:6ae99e4560963ad8e163e819e5d77d413d331fd00566c1e0856aa252303552c1"},
    {file = "coverage-7.13.2-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e79a8c7d461820257d9aa43716c4efc55366d7b292e46b5b37165be1d377405d"},
    {file = "coverage-7.13.2-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:060ee84f6a769d40c492711911a76811b4befb6fba50abb450371abb720f5bd6"},
    {file = "coverage-7.13.2-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:3bca209d001fd03ea2d978f8a4985093240a355c93078aee3f799852c23f561a"},
    {file = "coverage-7.13.2-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:6b8092aa38d72f091db61ef83cb66076f18f02da3e1a75039a4f218629600e04"},
    {file = "coverage-7.13.2-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:4a3158dc2dcce5200d91ec28cd315c999eebff355437d2765840555d765a6e5f"},
    {file = "coverage-7.13.2-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:3973f353b2d70bd9796cc12f532a05945232ccae966456c8ed7034cb96bbfd6f"},
    {file = "coverage-7.13.2-cp314-cp314t-win32.whl", hash = "sha256:79f6506a678a59d4ded048dc72f1859ebede8ec2b9a2d509ebe161f01c2879d3"},
    {file = "coverage-7.13.2-cp314-cp314t-win_amd64.whl", hash = "sha256:196bfeabdccc5a020a57d5a368c681e3a6ceb0447d153aeccc1ab4d70a5032ba"},
    {file = "coverage-7.13.2-cp314-cp314t-win_arm64.whl", hash = "sha256:69269ab58783e090bfbf5b916ab3d188126e22d6070bbfc93098fdd474ef937c"},
    {file = "coverage-7.13.2-py3-none-any.whl", hash = "sha256:40ce1ea1e25125556d8e76bd0b61500839a07944cc287ac21d5626f3e620cad5"},
    {file = "coverage-7.13.2.tar.gz", hash = "sha256:044c6951ec37146b72a50cc81ef02217d27d4c3640efd2640311393cbbf143d3"},
]

[package.dependencies]
tomli = {version = "*", optional = true, markers = "python_full_version <= \"3.11.0a6\" and extra == \"toml\""}

[package.extras]
toml = ["tomli ; python_full_version <= \"3.11.0a6\""]

[[package]]
name = "deprecation"
version = "2.1.0"
description = "A library to handle automated deprecations"
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "deprecation-2.1.0-py2.py3-none-any.whl", hash = "sha256:a10811591210e1fb0e768a8c25517cabeabcba6f0bf96564f8ff45189f90b14a"},
    {file = "deprecation-2.1.0.tar.gz", hash = "sha256:72b3bde64e5d778694b0cf68178aed03d15e15477116add3fb773e581f9518ff"},
]

[package.dependencies]
packaging = "*"

[[package]]
name = "distlib"
version = "0.4.0"
description = "Distribution utilities"
optional = false
python-versions = "*"
groups = ["dev"]
files = [
    {file = "distlib-0.4.0-py2.py3-none-any.whl", hash = "sha256:9659f7d87e46584a30b5780e43ac7a2143098441670ff0a49d5f9034c54a6c16"},
    {file = "distlib-0.4.0.tar.gz", hash = "sha256:feec40075be03a04501a973d81f633735b4b69f98b05450592310c0f401a4e0d"},
]

[[package]]
name = "distro"
version = "1.9.0"
description = "Distro - an OS platform information API"
optional = true
python-versions = ">=3.6"
groups = ["main"]
markers = "sys_platform == \"linux\" and (extra == \"drivers\" or extra == \"nidaqmx\")"
files = [
    {file = "distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2"},
    {file = "distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed"},
]

[[package]]
name = "docutils"
version = "0.21.2"
description = "Docutils -- Python Documentation Utilities"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version == \"3.10\""
files = [
    {file = "docutils-0.21.2-py3-none-any.whl", hash = "sha256:dafca5b9e384f0e419294eb4d2ff9fa826435bf15f15b7bd45723e8ad76811b2"},
    {file = "docutils-0.21.2.tar.gz", hash = "sha256:3a6b18732edf182daa3cd12775bbb338cf5691468f91eeeb109deff6ebfa986f"},
]

[[package]]
name = "docutils"
version = "0.22.4"
description = "Docutils -- Python Documentation Utilities"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version >= \"3.11\""
files = [
    {file = "docutils-0.22.4-py3-none-any.whl", hash = "sha256:d0013f540772d1420576855455d050a2180186c91c15779301ac2ccb3eeb68de"},
    {file = "docutils-0.22.4.tar.gz", hash = "sha256:4db53b1fde9abecbb74d91230d32ab626d94f6badfc575d6db9194a49df29968"},
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
description = "Backport of PEP 654 (exception groups)"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
markers = "python_version == \"3.10\""
files = [
    {file = "exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598"},
    {file = "exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219"},
]

[package.dependencies]
typing-extensions = {version = ">=4.6.0", markers = "python_version < \"3.13\""}

[package.extras]
test = ["pytest (>=6)"]

[[package]]
name = "filelock"
version = "3.29.0"
description = "A platform independent file lock."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "filelock-3.29.0-py3-none-any.whl", hash = "sha256:96f5f6344709aa1572bbf631c640e4ebeeb519e08da902c39a001882f30ac258"},
    {file = "filelock-3.29.0.tar.gz", hash = "sha256:69974355e960702e789734cb4871f884ea6fe50bd8404051a3530bc07809cf90"},
]

[[package]]
name = "flake8"
version = "5.0.4"
description = "the modular source code checker: pep8 pyflakes and co"
optional = false
python-versions = ">=3.6.1"
groups = ["dev"]
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
groups = ["dev"]
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
groups = ["dev"]
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
version = "0.18.2"
description = "Flake8 and pylama plugin that checks the ordering of import statements."
optional = false
python-versions = "*"
groups = ["dev"]
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
groups = ["dev"]
files = [
    {file = "flake8_tidy_imports-4.12.0-py3-none-any.whl", hash = "sha256:ab1e31a5ce07518a31c0a34cd92551f4c27639ae2c35a21364680a0318da312e"},
    {file = "flake8_tidy_imports-4.12.0.tar.gz", hash = "sha256:9254788c3b6862c2fcec0250d2dc9af089afebff9c5b8a8ac8b9525b059b06db"},
]

[package.dependencies]
flake8 = ">=3.8"

[[package]]
name = "grpcio"
version = "1.81.1"
description = "HTTP/2-based RPC framework"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
files = [
    {file = "grpcio-1.81.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:6f9a0c9c1cc15c112d1c053064fd032b64917062292c3d70aea280e02ae10b77"},
    {file = "grpcio-1.81.1-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:69ef28e54fc85397f91b8c19592b8ef3d81952080366914823bd8572a2958120"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:15641444eca4a29358107b3dceb74c1c6305c55c822fd199b458aaea4068a7fb"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:d4b2dddfc219f54f956ccd53cf76a1d338ffe68fc7f2849ec9c7feb9927ff692"},
    {file = "grpcio-1.81.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:ca1cc11d82677b9662082e5478b7528e2b7db7beaa6bdff42bd62789d81be399"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:aa2ba7d2ad6df4d80127cea65e5b8d5e2c3adbf153ff4804452836328aca7c54"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:592b5fee597faa91cce2dd294dd7d9a1c83d76c4dbf877e33ec1adb866b2fbed"},
    {file = "grpcio-1.81.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:62481553b1793a27e9b9c3cf9e5bd483ef045ca72462592074b46d42b0c4d9b9"},
    {file = "grpcio-1.81.1-cp310-cp310-win32.whl", hash = "sha256:bb693b1e3d9a2f3fd228e2110daf4b5aeedb36761ca1e4282f74725f6d89f611"},
    {file = "grpcio-1.81.1-cp310-cp310-win_amd64.whl", hash = "sha256:88268ca418cacea64cecb0d1d600d3c6b3a8038fcba02e1e205178c5b1f47661"},
    {file = "grpcio-1.81.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:d71d30f2d92f67d944631c523713934fee37292469e182ebcd2c1dd8a64ce53f"},
    {file = "grpcio-1.81.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:b137f4bf3ada9dc44d411478decc6ff09a79ed30b306cd2abaa98408c3588137"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:a3acb384427816dd5d470f47e62137b87f74da694faa8a50147012cf40df276a"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:f9a0ebbe45c29b5e5866593c12b78bd9035f0f0f0d4bc8361680cd580d99db49"},
    {file = "grpcio-1.81.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:0a37165cc80b1a368384b383e63a4c38116a10467ae44c904d2d7468c4470ec2"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:6282caffb41ec326d4cb67ca9cf53b739d1b2f975a2acb498c7418e9f7d9a416"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:a35009284d0d3d5c2c9601c164a911b8b4331608d98a9a66d47d97bb2f522b70"},
    {file = "grpcio-1.81.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:1b22c80559854b789a01fd89e8929b3798a156c0829b5282a8939f33ad4115ad"},
    {file = "grpcio-1.81.1-cp311-cp311-win32.whl", hash = "sha256:428bec0161b48d8cf583c068591bc0016d0d9cfff52462b72b3884861ea768c5"},
    {file = "grpcio-1.81.1-cp311-cp311-win_amd64.whl", hash = "sha256:30e825f6848d9f18bba350ed6c75c1b02a0b5184474a31db9a32b1fa66fd8c79"},
    {file = "grpcio-1.81.1-cp312-cp312-linux_armv7l.whl", hash = "sha256:8b39472beafc0bdcafc4c8c73ad082ebfdb449d566897a61e7acb4fa88089115"},
    {file = "grpcio-1.81.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:12b7524c88d4026d3dcb7b0ebe16b6714f3b4af402ddd0f0639ab064a00c87c3"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:1e123f9b37edb8375fd74130d1f69c944bbf0a7b06761ae7211154b8759e94d2"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:2c2e2ae6867c2966b8daccc836d54a13218e0007e9a490aeb81dd05be64d22d7"},
    {file = "grpcio-1.81.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:766bc7c9a9c340342f4c864ccbda8e78111e4751f13b895812b9c148fb79e9d0"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:b259a04a737cb3496be0901328eb8b7552ed8df4865d8c8f1cf1bffcfc0776a3"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:85b10a45b8993d195c4f3ff57025b8d1e11834909ee475c403bfa60cb4caefaf"},
    {file = "grpcio-1.81.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:8ea1936c26b99999b27479853039a7f34713f56c49375ad52b38535ec93a796c"},
    {file = "grpcio-1.81.1-cp312-cp312-win32.whl", hash = "sha256:a185a04039df6cae8648bc8ab6d6fde7bf94f7188ecf7828e76ac52eef1e41d6"},
    {file = "grpcio-1.81.1-cp312-cp312-win_amd64.whl", hash = "sha256:3ad74f8bb1a18963914c5452d289422830b39459e8776ebbcd207be1fbfb1d94"},
    {file = "grpcio-1.81.1-cp313-cp313-linux_armv7l.whl", hash = "sha256:b10e1ff4756ed27d5a29d7fc79cfce7ef1ff56ad20025b89bac7cf79e09abbbe"},
    {file = "grpcio-1.81.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:819edbdcb42ab8598b494bcf0222684bbb7a3c772bd1b1f0be7e029a6063c28e"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:c5bf2dc311127d91230cc79b92188c082634a06cf66c5234db49a43b910183b0"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:e8ca6a1fcdb2943c9cbc1804a1baf3acb6071d72a471591678ded84218006e14"},
    {file = "grpcio-1.81.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:e64dd101d380a115cc5a0c7856788adb535f1a4e21fc543775602f8be95180ae"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:98a07f9bf591e3a8919797bee1c53f026ba4acd587e5a4404c8e57c9ec36b2a5"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:c261d74b1a945cf895a9d6eccd1685a8e837531beaab782da4d630a8d12deffb"},
    {file = "grpcio-1.81.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:58ad1131c300d3c9b933802b3cc4dc69d380822935ba50b28703156ea826fbf7"},
    {file = "grpcio-1.81.1-cp313-cp313-win32.whl", hash = "sha256:78e29211f26da2fdd0e9c6d2b79f489476140cf7029b6a64808ade7ca4156a42"},
    {file = "grpcio-1.81.1-cp313-cp313-win_amd64.whl", hash = "sha256:edb59506291b647a30884b1d51a599d605f40b20af4a7dc3d33786a47a31de60"},
    {file = "grpcio-1.81.1-cp314-cp314-linux_armv7l.whl", hash = "sha256:506f48f2f9c29b143fca3dad7b0d518c188b6c9648c75a2ae6e2d9f2c13a060b"},
    {file = "grpcio-1.81.1-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:d865db4a6318e1c1bea83292e0ed231090538fc4ca45425b0f0480eb338bbc6e"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:e2aa72e3ce1770317ef534f63d397b55e130725f5149bd36077c3b539019db27"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:0490c30c261eded63f3f354979f9dc4502a9fb944cccb60cd9dc85f5a7349854"},
    {file = "grpcio-1.81.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:410482da976329fe5f4067270401b12cf2bd552ff8020f054ecfaddb5475f9d6"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:e3657301562ac3cb8018d30d0d3ebfa39932239f7b5703422057ef14b69949f5"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:24c8e57504c8f45b237e40b99262d181071e5099a07053695b75d97bb53053a0"},
    {file = "grpcio-1.81.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:b427c19380991a4eaab2f6144b64b99b412043314c6bf4ab544f97bb31ee4190"},
    {file = "grpcio-1.81.1-cp314-cp314-win32.whl", hash = "sha256:61233fe8951e5c85dff81c2458b6528624760166946b5b47ea150a589168411f"},
    {file = "grpcio-1.81.1-cp314-cp314-win_amd64.whl", hash = "sha256:3768a5ff1b2125e6f552e561b6b2dca0e64982d8949689b4df145cf8b98d7821"},
    {file = "grpcio-1.81.1.tar.gz", hash = "sha256:6fa10a767143a5e82e8eaab53918af0cd8909a57a27f8cb2288b80a613ac671b"},
]

[package.dependencies]
typing-extensions = ">=4.12,<5.0"

[package.extras]
protobuf = ["grpcio-tools (>=1.81.1)"]

[[package]]
name = "grpcio-tools"
version = "1.49.1"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
markers = "python_version < \"3.12\""
files = [
    {file = "grpcio-tools-1.49.1.tar.gz", hash = "sha256:84cc64e5b46bad43d5d7bd2fd772b656eba0366961187a847e908e2cb735db91"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:2dfb6c7ece84d46bd690b23d3e060d18115c8bc5047d2e8a33e6747ed323a348"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-macosx_10_10_x86_64.whl", hash = "sha256:8f452a107c054a04db2570f7851a07f060313c6e841b0d394ce6030d598290e6"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:6a198871b582287213c4d70792bf275e1d7cf34eed1d019f534ddf4cd15ab039"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:a0cca67a7d0287bdc855d81fdd38dc949c4273273a74f832f9e520abe4f20bc6"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bdaff4c89eecb37c247b93025410db68114d97fa093cbb028e9bd7cda5912473"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:bb8773118ad315db317d7b22b5ff75d649ca20931733281209e7cbd8c0fad53e"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:7cc5534023735b8a8f56760b7c533918f874ce5a9064d7c5456d2709ae2b31f9"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-win32.whl", hash = "sha256:d277642acbe305f5586f9597b78fb9970d6633eb9f89c61e429c92c296c37129"},
    {file = "grpcio_tools-1.49.1-cp310-cp310-win_amd64.whl", hash = "sha256:eed599cf08fc1a06c72492d3c5750c32f58de3750eddd984af1f257c14326701"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:9e5c13809ab2f245398e8446c4c3b399a62d591db651e46806cccf52a700452e"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-macosx_10_10_x86_64.whl", hash = "sha256:ab3d0ee9623720ee585fdf3753b3755d3144a4a8ae35bca8e3655fa2f41056be"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:6ba87e3512bc91d78bf9febcfb522eadda171d2d4ddaf886066b0f01aa4929ad"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:13e13b3643e7577a3ec13b79689eb4d7548890b1e104c04b9ed6557a3c3dd452"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:324f67d9cb4b7058b6ce45352fb64c20cc1fa04c34d97ad44772cfe6a4ae0cf5"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:a64bab81b220c50033f584f57978ebbea575f09c1ccee765cd5c462177988098"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-win32.whl", hash = "sha256:f632d376f92f23e5931697a3acf1b38df7eb719774213d93c52e02acd2d529ac"},
    {file = "grpcio_tools-1.49.1-cp311-cp311-win_amd64.whl", hash = "sha256:28ff2b978d9509474928b9c096a0cce4eaa9c8f7046136aee1545f6211ed8126"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-linux_armv7l.whl", hash = "sha256:46afd3cb7e555187451a5d283f108cdef397952a662cb48680afc615b158864a"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-macosx_10_10_x86_64.whl", hash = "sha256:9284568b728e41fa8f7e9c2e7399545d605f75d8072ef0e9aa2a05655cb679eb"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_aarch64.whl", hash = "sha256:aa34442cf787732cb41f2aa6172007e24f480b8b9d3dc5166de80d63e9072ea4"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3b8c9eb5a4250905414cd53a68caea3eb8f0c515aadb689e6e81b71ebe9ab5c6"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ab15db024051bf21feb21c29cb2c3ea0a2e4f5cf341d46ef76e17fcf6aaef164"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:502084b622f758bef620a9107c2db9fcdf66d26c7e0e481d6bb87db4dc917d70"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:4085890b77c640085f82bf1e90a0ea166ce48000bc2f5180914b974783c9c0a8"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-win32.whl", hash = "sha256:da0edb984699769ce02e18e3392d54b59a7a3f93acd285a68043f5bde4fc028e"},
    {file = "grpcio_tools-1.49.1-cp37-cp37m-win_amd64.whl", hash = "sha256:9887cd622770271101a7dd1832845d64744c3f88fd11ccb2620394079197a42e"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-linux_armv7l.whl", hash = "sha256:8440fe7dae6a40c279e3a24b82793735babd38ecbb0d07bb712ff9c8963185d9"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-macosx_10_10_x86_64.whl", hash = "sha256:b5de2bb7dd6b6231da9b1556ade981513330b740e767f1d902c71ceee0a7d196"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:1e6f06a763aea7836b63d9c117347f2bf7038008ceef72758815c9e09c5fb1fc"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e31562f90120318c5395aabec0f2f69ad8c14b6676996b7730d9d2eaf9415d57"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:49ef9a4e389a618157a9daa9fafdfeeaef1ece9adda7f50f85db928f24d4b3e8"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:b384cb8e8d9bcb55ee8f9b064374561c7a1a05d848249581403d36fc7060032f"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:73732f77943ac3e898879cbb29c27253aa3c47566b8a59780fd24c6a54de1b66"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-win32.whl", hash = "sha256:b594b2745a5ba9e7a76ce561bc5ab40bc65bb44743c505529b1e4f12af29104d"},
    {file = "grpcio_tools-1.49.1-cp38-cp38-win_amd64.whl", hash = "sha256:680fbc88f8709ddcabb88f86749f2d8e429160890cff2c70680880a6970d4eef"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-linux_armv7l.whl", hash = "sha256:e8c3869121860f6767eedb7d24fc54dfd71e737fdfbb26e1334684606f3274fd"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-macosx_10_10_x86_64.whl", hash = "sha256:73e9d7c886ba10e20c97d1dab0ff961ba5800757ae5e31be21b1cda8130c52f8"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:1760de2dd2c4f08de87b039043a4797f3c17193656e7e3eb84e92f0517083c0c"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:cd4b1e216dd04d9245ee8f4e601a1f98c25e6e417ea5cf8d825c50589a8b447e"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c1c28751ab5955cae563d07677e799233f0fe1c0fc49d9cbd61ff1957e83617f"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:c24239c3ee9ed16314c14b4e24437b5079ebc344f343f33629a582f8699f583b"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:892d3dacf1942820f0b7a868a30e6fbcdf5bec08543b682c7274b0101cee632d"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-win32.whl", hash = "sha256:704d21509ec06efc9d034dbe70e7152715aac004941f4f0f553cf3a0aff15bd5"},
    {file = "grpcio_tools-1.49.1-cp39-cp39-win_amd64.whl", hash = "sha256:1efa0c221c719433f441ac0e026fc3c4dbc9a1a08a552ecdc707775e2f2fbbae"},
]

[package.dependencies]
grpcio = ">=1.49.1"
protobuf = ">=4.21.3,<5.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.59.0"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
markers = "python_version == \"3.12\""
files = [
    {file = "grpcio-tools-1.59.0.tar.gz", hash = "sha256:aa4018f2d8662ac4d9830445d3d253a11b3e096e8afe20865547137aa1160e93"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-linux_armv7l.whl", hash = "sha256:882b809b42b5464bee55288f4e60837297f9618e53e69ae3eea6d61b05ce48fa"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-macosx_12_0_universal2.whl", hash = "sha256:4499d4bc5aa9c7b645018d8b0db4bebd663d427aabcd7bee7777046cb1bcbca7"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:f381ae3ad6a5eb27aad8d810438937d8228977067c54e0bd456fce7e11fdbf3d"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f1c684c0d9226d04cadafced620a46ab38c346d0780eaac7448da96bf12066a3"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:40cbf712769242c2ba237745285ef789114d7fcfe8865fc4817d87f20015e99a"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:1df755951f204e65bf9232a9cac5afe7d6b8e4c87ac084d3ecd738fdc7aa4174"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:de156c18b0c638aaee3be6ad650c8ba7dec94ed4bac26403aec3dce95ffe9407"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-win32.whl", hash = "sha256:9af7e138baa9b2895cf1f3eb718ac96fc5ae2f8e31fca405e21e0e5cd1643c52"},
    {file = "grpcio_tools-1.59.0-cp310-cp310-win_amd64.whl", hash = "sha256:f14a6e4f700dfd30ff8f0e6695f944affc16ae5a1e738666b3fae4e44b65637e"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-linux_armv7l.whl", hash = "sha256:db030140d0da2368319e2f23655df3baec278c7e0078ecbe051eaf609a69382c"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-macosx_10_10_universal2.whl", hash = "sha256:eeed386971bb8afc3ec45593df6a1154d680d87be1209ef8e782e44f85f47e64"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_aarch64.whl", hash = "sha256:962d1a3067129152cee3e172213486cb218a6bad703836991f46f216caefcf00"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:26eb2eebf150a33ebf088e67c1acf37eb2ac4133d9bfccbaa011ad2148c08b42"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5b2d6da553980c590487f2e7fd3ec9c1ad8805ff2ec77977b92faa7e3ca14e1f"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:335e2f355a0c544a88854e2c053aff8a3f398b84a263a96fa19d063ca1fe513a"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:204e08f807b1d83f5f0efea30c4e680afe26a43dec8ba614a45fa698a7ef0a19"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-win32.whl", hash = "sha256:05bf7b3ed01c8a562bb7e840f864c58acedbd6924eb616367c0bd0a760bdf483"},
    {file = "grpcio_tools-1.59.0-cp311-cp311-win_amd64.whl", hash = "sha256:df85096fcac7cea8aa5bd84b7a39c4cdbf556b93669bb4772eb96aacd3222a4e"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-linux_armv7l.whl", hash = "sha256:240a7a3c2c54f77f1f66085a635bca72003d02f56a670e7db19aec531eda8f78"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-macosx_10_10_universal2.whl", hash = "sha256:6119f62c462d119c63227b9534210f0f13506a888151b9bf586f71e7edf5088b"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_aarch64.whl", hash = "sha256:387662bee8e4c0b52cc0f61eaaca0ca583f5b227103f685b76083a3590a71a3e"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8f0da5861ee276ca68493b217daef358960e8527cc63c7cb292ca1c9c54939af"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d0f0806de1161c7f248e4c183633ee7a58dfe45c2b77ddf0136e2e7ad0650b1b"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-musllinux_1_1_i686.whl", hash = "sha256:c683be38a9bf4024c223929b4cd2f0a0858c94e9dc8b36d7eaa5a48ce9323a6f"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:f965707da2b48a33128615bcfebedd215a3a30e346447e885bb3da37a143177a"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-win32.whl", hash = "sha256:2ee960904dde12a7fa48e1591a5b3eeae054bdce57bacf9fd26685a98138f5bf"},
    {file = "grpcio_tools-1.59.0-cp312-cp312-win_amd64.whl", hash = "sha256:71cc6db1d66da3bc3730d9937bddc320f7b1f1dfdff6342bcb5741515fe4110b"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-linux_armv7l.whl", hash = "sha256:f6263b85261b62471cb97b7505df72d72b8b62e5e22d8184924871a6155b4dbf"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-macosx_10_10_universal2.whl", hash = "sha256:b8e95d921cc2a1521d4750eedefec9f16031457920a6677edebe9d1b2ad6ae60"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_aarch64.whl", hash = "sha256:cb63055739808144b541986291679d643bae58755d0eb082157c4d4c04443905"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8c4634b3589efa156a8d5860c0a2547315bd5c9e52d14c960d716fe86e0927be"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2d970aa26854f535ffb94ea098aa8b43de020d9a14682e4a15dcdaeac7801b27"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-musllinux_1_1_i686.whl", hash = "sha256:821dba464d84ebbcffd9d420302404db2fa7a40c7ff4c4c4c93726f72bfa2769"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-musllinux_1_1_x86_64.whl", hash = "sha256:0548e901894399886ff4a4cd808cb850b60c021feb4a8977a0751f14dd7e55d9"},
    {file = "grpcio_tools-1.59.0-cp37-cp37m-win_amd64.whl", hash = "sha256:bb87158dbbb9e5a79effe78d54837599caa16df52d8d35366e06a91723b587ae"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-linux_armv7l.whl", hash = "sha256:1d551ff42962c7c333c3da5c70d5e617a87dee581fa2e2c5ae2d5137c8886779"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-macosx_10_10_universal2.whl", hash = "sha256:4ee443abcd241a5befb05629013fbf2eac637faa94aaa3056351aded8a31c1bc"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:520c0c83ea79d14b0679ba43e19c64ca31d30926b26ad2ca7db37cbd89c167e2"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:9fc02a6e517c34dcf885ff3b57260b646551083903e3d2c780b4971ce7d4ab7c"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6aec8a4ed3808b7dfc1276fe51e3e24bec0eeaf610d395bcd42934647cf902a3"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:99b3bde646720bbfb77f263f5ba3e1a0de50632d43c38d405a0ef9c7e94373cd"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:51d9595629998d8b519126c5a610f15deb0327cd6325ed10796b47d1d292e70b"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-win32.whl", hash = "sha256:bfa4b2b7d21c5634b62e5f03462243bd705adc1a21806b5356b8ce06d902e160"},
    {file = "grpcio_tools-1.59.0-cp38-cp38-win_amd64.whl", hash = "sha256:9ed05197c5ab071e91bcef28901e97ca168c4ae94510cb67a14cb4931b94255a"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-linux_armv7l.whl", hash = "sha256:498e7be0b14385980efa681444ba481349c131fc5ec88003819f5d929646947c"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-macosx_10_10_universal2.whl", hash = "sha256:b519f2ecde9a579cad2f4a7057d5bb4e040ad17caab8b5e691ed7a13b9db0be9"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:ef3e8aca2261f7f07436d4e2111556c1fb9bf1f9cfcdf35262743ccdee1b6ce9"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:27a7f226b741b2ebf7e2d0779d2c9b17f446d1b839d59886c1619e62cc2ae472"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:784aa52965916fec5afa1a28eeee6f0073bb43a2a1d7fedf963393898843077a"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:e312ddc2d8bec1a23306a661ad52734f984c9aad5d8f126ebb222a778d95407d"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:868892ad9e00651a38dace3e4924bae82fc4fd4df2c65d37b74381570ee8deb1"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-win32.whl", hash = "sha256:a4f6cae381f21fee1ef0a5cbbbb146680164311157ae618edf3061742d844383"},
    {file = "grpcio_tools-1.59.0-cp39-cp39-win_amd64.whl", hash = "sha256:4a10e59cca462208b489478340b52a96d64e8b8b6f1ac097f3e8cb211d3f66c0"},
]

[package.dependencies]
grpcio = ">=1.59.0"
protobuf = ">=4.21.6,<5.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.67.0"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version == \"3.13\""
files = [
    {file = "grpcio_tools-1.67.0-cp310-cp310-linux_armv7l.whl", hash = "sha256:12aa38af76b5ef00a55808c7c374ed18d5dc7cc8081b717e56da3c50df1776e2"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-macosx_12_0_universal2.whl", hash = "sha256:b0b03d055127bbc7c629454804b53b5cad2cedfcf904576d159a8a04c22b8e66"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_aarch64.whl", hash = "sha256:02b0b50c59a8f7428326197027a2f586d216c46138c547f861533c46bff78bfe"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b2afdfe151ed9edbd4a3fd646716f83b58010769c57f9c0aa1cf4c3bfb1240a8"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc3eeb87575b2b360c5ef5aef22eb76cfdd6a255d2f628a48ab0e5a61a0039fb"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-musllinux_1_1_i686.whl", hash = "sha256:ead78089c4771605a1ff8894e47f2267440693f1beeee06fd5a788aede83370f"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:0671dcdccef09ca4eb415c1d6f470a857c6486733c146676f6810a3ade1d42cb"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-win32.whl", hash = "sha256:a7398d90b8c7da479aec8f853d3664d5a93c209f8ac3bd41cb7ae4e8677a45c6"},
    {file = "grpcio_tools-1.67.0-cp310-cp310-win_amd64.whl", hash = "sha256:f7e7d70a74df7e07be7cceaa694b7e8e5f3bef8e0299906f60885ecf7a40adb4"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-linux_armv7l.whl", hash = "sha256:655716bf931a22a090134d87953710033640996d31e36f5f9b0106ff5f552d8e"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:484ae782f9d3ff58e0bbb2f4cad14d5f5d9132fc701835b1dffd2c2a06f73ba6"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_aarch64.whl", hash = "sha256:f3e34de876efe1273f91e25ef241e449ed7f9411472dd9ff56d2039618017c30"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d8301719edde2c3d388995703cdd962f558b76e9750405f772dce61402e4c3d0"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1629ea246044ccd473d9ac4c9f137a440d830b5e08d35225e1b354dbbb15b75d"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-musllinux_1_1_i686.whl", hash = "sha256:d77a3c5cec0065267ca1a0b2589ececd1277ce25aa67f13ec50c816ee6f26f7f"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9bf992bcc7d9e6eaa20705056e1b955593092a38cec1746fef389d873ab2056"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-win32.whl", hash = "sha256:7e6e3db119c38629e0767cdb2ee18726ecc87e2249117d4c9e7ce06ea8c894ea"},
    {file = "grpcio_tools-1.67.0-cp311-cp311-win_amd64.whl", hash = "sha256:c6c27aec301a0e6cf231f9ee1c467c64002af51170fa7c0f3bb10bbfcd03fee7"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-linux_armv7l.whl", hash = "sha256:dca7f053cbdb26a587d4410ddb893877c585fb60a31f22fdd128e4f7c4dab27c"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-macosx_10_9_universal2.whl", hash = "sha256:de8c4f68ffa690769d84329c17c7fdd5fbe4c61b8f8a0de03f1ad8ef8bb06963"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_aarch64.whl", hash = "sha256:6e4ecb24c27a78f09fead45d4ed873805d6026124ccb6793b6fb93a490b78ddf"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:004d6ef1b5f724480f05c0bdc904bf8c78c43d633c537d99abe51b52ce0cadeb"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9dd257072c86eb9b36791b3674a513a215ba76bbdd38fc228f0e8c6dc5ce3524"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-musllinux_1_1_i686.whl", hash = "sha256:a8cca551317ed26e17d13b6ee27b2bd62f5fe9b3842b4e88389deb984f995848"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:a7ac3b4f837c693142f6688b629d1f6408f6ab250d927159b572555f5339fe25"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-win32.whl", hash = "sha256:95feec33388e2a8f72c360a68efe6f0bfed9c771e94d21b7f2359d0010f60219"},
    {file = "grpcio_tools-1.67.0-cp312-cp312-win_amd64.whl", hash = "sha256:50a31d035193ebe7154181eac84734e25bdcdb36adba849d3b2adf1c3b0c382b"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-linux_armv7l.whl", hash = "sha256:9ecb7c2e5da052a3feaeaa83d8f2a946a8feec8a50751b0e6175da982b49ebb1"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:3c52164f2b9d41c6d75464bb45f45737dcb421e92e98d85d94fda100c67a24d8"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_aarch64.whl", hash = "sha256:471f58b919767290260d427dd9b760796e6208ee5fcda2f76bb8bd585ff842ec"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:72c6bcdf38f672721c093c92b1fb1f9a02a365acc5bd42e1c69fe6e904b26081"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:833b1eb9c03d28a798294523f75294055eff78fa897adf797876337b901afeb9"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-musllinux_1_1_i686.whl", hash = "sha256:1db92ad6ade1946fc5705eb04956fcfdb3a0a4682de8dc3fce31cb97b6e4fcb8"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:38128310ded818e1044c0cd0979d76f7c0d3c3946a526a8aa39cd258624c3bf3"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-win32.whl", hash = "sha256:db57930dc20ab678311727883bdb9f122daf06c14f3fd3067c9ccedb7eb056c3"},
    {file = "grpcio_tools-1.67.0-cp313-cp313-win_amd64.whl", hash = "sha256:7de44d8d3bb920a4973a559f2950d03382fa4aed4880306416ffa73d24838477"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-linux_armv7l.whl", hash = "sha256:793896648734aad3ad8f26795dcdd6040aecd35efef43fcbb67d221373e6379a"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-macosx_10_9_universal2.whl", hash = "sha256:941418cba6a8adfcac3ff7ff3bdef00b55a44d673634c15bddcfa7778e49239e"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_aarch64.whl", hash = "sha256:0d63ff6be6f3d0294249fc7a21f26f06c9cc209130c5328907cd678406d7d232"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:af80ced3ba49377ef7bec93e9ccbfa357875460e9a624ed12d9a7d5348741a76"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e3c3fbb4a6d10764295540579492397bc7a3334e1a92dd17a4bc7b69159cf70a"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-musllinux_1_1_i686.whl", hash = "sha256:a05c10fb783f609d16e1f754ebad9bb432a1adbfc46139d154e8fd6b15f59988"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-musllinux_1_1_x86_64.whl", hash = "sha256:ea8af001f08c678ab59e2bf2614d8b09d62210e540f7af1129c172fe4fd330c7"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-win32.whl", hash = "sha256:004d329aee385fa874979196e5359a967c370d31813f61eba88043ccaa2e06d8"},
    {file = "grpcio_tools-1.67.0-cp38-cp38-win_amd64.whl", hash = "sha256:fc43593bd051abb73a5d130fc041923144089ac459fb01165960106ebb686fd0"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-linux_armv7l.whl", hash = "sha256:d285c036ddfc2618c4db60b584409dd8313d41473bd46177c763ea22ed9aeb1f"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:623fdad489447e1565d0ba5a818d54b4e74cd73800b6a32c4c009601c7f7a36c"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_aarch64.whl", hash = "sha256:24536af8a5f8e532fbd996c1763eff51526d1d1563f9499ff5ffffb9a08811f3"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bd64a9a8eb675dd2aa59cb4b2ab025a3b02ae1bb9e483c7fb518ffa0f0755cda"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f94378bc90fb008b0a56237748aa42c787fd86c392e7df3d65f0fe7fcd93844a"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-musllinux_1_1_i686.whl", hash = "sha256:d0f39a9d860a6768574cd77b5d9ad81513fa1c575d3a050d4e72e6d79dcd62f3"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:c578f1306bfd0dd0668e24f8c04d61529928de2660217022a947a56be177bc2d"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-win32.whl", hash = "sha256:0c2cf8d09bdc05e0550ad413e0bc0d552500bb7f98d36079b7b9d38e064e02f7"},
    {file = "grpcio_tools-1.67.0-cp39-cp39-win_amd64.whl", hash = "sha256:cc570bcd9c9681bb011f746ea90cc50559be629227aaaaae9fde8549525f0287"},
    {file = "grpcio_tools-1.67.0.tar.gz", hash = "sha256:181b3d4e61b83142c182ec366f3079b0023509743986e54c9465ca38cac255f8"},
]

[package.dependencies]
grpcio = ">=1.67.0"
protobuf = ">=5.26.1,<6.0.dev0"
setuptools = "*"

[[package]]
name = "grpcio-tools"
version = "1.75.1"
description = "Protobuf code generator for gRPC"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
markers = "python_version >= \"3.14\""
files = [
    {file = "grpcio_tools-1.75.1-cp310-cp310-linux_armv7l.whl", hash = "sha256:ae0f04d5ec8b8e13476bf516a08fc1de4e58c6bf79f99123a6b964ca7d02c790"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-macosx_11_0_universal2.whl", hash = "sha256:24a881ad7292e904fc256892b647da17d9137ef2e72faf8b7c8e515314ad1377"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:1b5810ace274dba12ecfac69ac32c8047c6ee0200a23274cb4885ed4187271f8"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:ab33993288b97b1180e092fa447a8ce00fbc8c59d67b23553245b88d14fe36bb"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4cac693621043ef11d3ab2318e811d919779f8cd5011ba8e37f44c178c831d94"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:a09cd5d267b296af67116fe098633ad770bc8c19831a5f3c896f65fad90c1064"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:dff4bcb4d16cf9ef745c1984394ed15187e6c23d73d71377377deaf443d11358"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:16d5986b37e2a9203f85e456c7ff8705b932718021d408adfe4a79e0f4d95949"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-win32.whl", hash = "sha256:3fbac14998bfadc6b9140b6339dbc5f673700ebb4d45ba0c4d4fbe0ffb8559a9"},
    {file = "grpcio_tools-1.75.1-cp310-cp310-win_amd64.whl", hash = "sha256:b56e495844eb899de721eb77d9e077192bdeb40842f598481d32a8f6de3db124"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-linux_armv7l.whl", hash = "sha256:f0635231feb70a9d551452829943a1a5fa651283e7a300aadc22df5ea5da696f"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-macosx_11_0_universal2.whl", hash = "sha256:626293296ef7e2d87ab1a80b81a55eef91883c65b59a97576099a28b9535100b"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:071339d90f1faab332ce4919c815a10b9c3ed2c09473f550f686bf9cc148579f"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:44195f58c052fa935b78c7438c85cbcd4b273dd685028e4f6d4d7b30d47daad1"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:860fafdb85726029d646c99859ff7bdca5aae61b5ff038c3bd355fc1ec6b2764"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:4559547a0cb3d3db1b982eea87d4656036339b400f48127fef932210672fb59e"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:9af65a310807d7f36a8f7cddea142fe97d6dffba74444f38870272f2e5a3a06b"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:8c1de31aefc0585d2f915a7cd0994d153547495b8d79c44c58048a3ede0b65be"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-win32.whl", hash = "sha256:efaf95fcaa5d3ac1bcfe44ceed9e2512eb95b5c8c476569bdbbe2bee4b59c8a9"},
    {file = "grpcio_tools-1.75.1-cp311-cp311-win_amd64.whl", hash = "sha256:7cefe76fc35c825f0148d60d2294a527053d0f5dd6a60352419214a8c53223c9"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-linux_armv7l.whl", hash = "sha256:49b68936cf212052eeafa50b824e17731b78d15016b235d36e0d32199000b14c"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-macosx_11_0_universal2.whl", hash = "sha256:08cb6e568e58b76a2178ad3b453845ff057131fff00f634d7e15dcd015cd455b"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:168402ad29a249092673079cf46266936ec2fb18d4f854d96e9c5fa5708efa39"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:bbae11c29fcf450730f021bfc14b12279f2f985e2e493ccc2f133108728261db"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:38c6c7d5d4800f636ee691cd073db1606d1a6a76424ca75c9b709436c9c20439"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:626f6a61a8f141dde9a657775854d1c0d99509f9a2762b82aa401a635f6ec73d"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:f61a8334ae38d4f98c744a732b89527e5af339d17180e25fff0676060f8709b7"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:bd0c3fb40d89a1e24a41974e77c7331e80396ab7cde39bc396a13d6b5e2a750b"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-win32.whl", hash = "sha256:004bc5327593eea48abd03be3188e757c3ca0039079587a6aac24275127cac20"},
    {file = "grpcio_tools-1.75.1-cp312-cp312-win_amd64.whl", hash = "sha256:23952692160b5fe7900653dfdc9858dc78c2c42e15c27e19ee780c8917ba6028"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-linux_armv7l.whl", hash = "sha256:ca9e116aab0ecf4365fc2980f2e8ae1b22273c3847328b9a8e05cbd14345b397"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-macosx_11_0_universal2.whl", hash = "sha256:9fe87a926b65eb7f41f8738b6d03677cc43185ff77a9d9b201bdb2f673f3fa1e"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:45503a6094f91b3fd31c3d9adef26ac514f102086e2a37de797e220a6791ee87"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:b01b60b3de67be531a39fd869d7613fa8f178aff38c05e4d8bc2fc530fa58cb5"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:09e2b9b9488735514777d44c1e4eda813122d2c87aad219f98d5d49b359a8eab"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:55e60300e62b220fabe6f062fe69f143abaeff3335f79b22b56d86254f3c3c80"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:49ce00fcc6facbbf52bf376e55b8e08810cecd03dab0b3a2986d73117c6f6ee4"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:71e95479aea868f8c8014d9dc4267f26ee75388a0d8a552e1648cfa0b53d24b4"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-win32.whl", hash = "sha256:fff9d2297416eae8861e53154ccf70a19994e5935e6c8f58ebf431f81cbd8d12"},
    {file = "grpcio_tools-1.75.1-cp313-cp313-win_amd64.whl", hash = "sha256:1849ddd508143eb48791e81d42ddc924c554d1b4900e06775a927573a8d4267f"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-linux_armv7l.whl", hash = "sha256:f281b594489184b1f9a337cdfed1fc1ddb8428f41c4b4023de81527e90b38e1e"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-macosx_11_0_universal2.whl", hash = "sha256:becf8332f391abc62bf4eea488b63be063d76a7cf2ef00b2e36c617d9ee9216b"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:a08330f24e5cd7b39541882a95a8ba04ffb4df79e2984aa0cd01ed26dcdccf49"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:6bf3742bd8f102630072ed317d1496f31c454cd85ad19d37a68bd85bf9d5f8b9"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:f26028949474feb380460ce52d9d090d00023940c65236294a66c42ac5850e8b"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:1bd68fb98bf08f11b6c3210834a14eefe585bad959bdba38e78b4ae3b04ba5bd"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:f1496e21586193da62c3a73cd16f9c63c5b3efd68ff06dab96dbdfefa90d40bf"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:14a78b1e36310cdb3516cdf9ee2726107875e0b247e2439d62fc8dc38cf793c1"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-win32.whl", hash = "sha256:0e6f916daf222002fb98f9a6f22de0751959e7e76a24941985cc8e43cea77b50"},
    {file = "grpcio_tools-1.75.1-cp314-cp314-win_amd64.whl", hash = "sha256:878c3b362264588c45eba57ce088755f8b2b54893d41cc4a68cdeea62996da5c"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-linux_armv7l.whl", hash = "sha256:eca28a90020fc1596f48cf51b02e56bc3d285f7f9ebaf0493144160d69c2cae7"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-macosx_11_0_universal2.whl", hash = "sha256:6744a14983f82e04cfd799ed779d06ee92035bb497f2d0fa84e81921a6c9c985"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:2a59120f17d36de6e16a058d88f2fcd255bafaccb487fea0613860a5287f77c6"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_i686.manylinux_2_17_i686.whl", hash = "sha256:02b0c237882e45247570afdc34717ce80831184882186ef47afca9f8cac2f71c"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4999ada9721ce2a0eae66bf7f2793bc6fe7a473eef4e38bb542d1e5c6d9f7d91"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:dd13f0d87605eb34f8b8868e3ad9202b90e9e58417276db79c3298538d0d60e3"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:9555db0d2eb22850b7e9a27c0476627d483c114fcdf40d29b03aef446f5e4c43"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:a35800ce3ecea4aaad511bc18daccd37b1560132694f30b606f2044f1242c9a0"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-win32.whl", hash = "sha256:8e7f2c1a37a5c8db92c5cba4034c370598f7458b275606f7a2a114f8c25c0326"},
    {file = "grpcio_tools-1.75.1-cp39-cp39-win_amd64.whl", hash = "sha256:0de3a82ee33d960f117ab66da51254cccd8bda9118d11ec3379f954cfbf6bc39"},
    {file = "grpcio_tools-1.75.1.tar.gz", hash = "sha256:bb78960cf3d58941e1fec70cbdaccf255918beed13c34112a6915a6d8facebd1"},
]

[package.dependencies]
grpcio = ">=1.75.1"
protobuf = ">=6.31.1,<7.0.0"
setuptools = "*"

[[package]]
name = "hightime"
version = "1.0.0"
description = "Hightime Python API"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main"]
files = [
    {file = "hightime-1.0.0-py3-none-any.whl", hash = "sha256:ba86d42976c36451b14e11c736e61f296f9f00dbb79c8488e18d70c6b2dbb395"},
    {file = "hightime-1.0.0.tar.gz", hash = "sha256:480d2a03e2c3ed44916d2406d40ab6d10a276ed7f101619fc3fcc1e00c46aacf"},
]

[[package]]
name = "idna"
version = "3.11"
description = "Internationalized Domain Names in Applications (IDNA)"
optional = false
python-versions = ">=3.8"
groups = ["main", "docs"]
files = [
    {file = "idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea"},
    {file = "idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902"},
]
markers = {main = "extra == \"drivers\" or extra == \"nidaqmx\""}

[package.extras]
all = ["flake8 (>=7.1.1)", "mypy (>=1.11.2)", "pytest (>=8.3.2)", "ruff (>=0.6.2)"]

[[package]]
name = "imagesize"
version = "1.4.1"
description = "Getting image size from png/jpeg/jpeg2000/gif file"
optional = false
python-versions = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*"
groups = ["docs"]
files = [
    {file = "imagesize-1.4.1-py2.py3-none-any.whl", hash = "sha256:0d8d18d08f840c19d0ee7ca1fd82490fdc3729b7ac93f49870406ddde8ef8d8b"},
    {file = "imagesize-1.4.1.tar.gz", hash = "sha256:69150444affb9cb0d5cc5a92b3676f0b2fb7cd9ae39e947a5e11a36b4497cd4a"},
]

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
name = "isort"
version = "7.0.0"
description = "A Python utility / library to sort Python imports."
optional = false
python-versions = ">=3.10.0"
groups = ["dev"]
files = [
    {file = "isort-7.0.0-py3-none-any.whl", hash = "sha256:1bcabac8bc3c36c7fb7b98a76c8abb18e0f841a3ba81decac7691008592499c1"},
    {file = "isort-7.0.0.tar.gz", hash = "sha256:5513527951aadb3ac4292a41a16cbc50dd1642432f5e8c20057d414bdafb4187"},
]

[package.extras]
colors = ["colorama"]
plugins = ["setuptools"]

[[package]]
name = "jinja2"
version = "3.1.6"
description = "A very fast and expressive template engine."
optional = false
python-versions = ">=3.7"
groups = ["docs"]
files = [
    {file = "jinja2-3.1.6-py3-none-any.whl", hash = "sha256:85ece4451f492d0c13c5dd7c13a64681a86afae63a5f347908daf103ce6d2f67"},
    {file = "jinja2-3.1.6.tar.gz", hash = "sha256:0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d"},
]

[package.dependencies]
MarkupSafe = ">=2.0"

[package.extras]
i18n = ["Babel (>=2.7)"]

[[package]]
name = "librt"
version = "0.9.0"
description = "Mypyc runtime library"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
markers = "platform_python_implementation != \"PyPy\""
files = [
    {file = "librt-0.9.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2f8e12706dcb8ff6b3ed57514a19e45c49ad00bcd423e87b2b2e4b5f64578443"},
    {file = "librt-0.9.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:4e3dda8345307fd7306db0ed0cb109a63a2c85ba780eb9dc2d09b2049a931f9c"},
    {file = "librt-0.9.0-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:de7dac64e3eb832ffc7b840eb8f52f76420cde1b845be51b2a0f6b870890645e"},
    {file = "librt-0.9.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:22a904cbdb678f7cb348c90d543d3c52f581663d687992fee47fd566dcbf5285"},
    {file = "librt-0.9.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:224b9727eb8bc188bc3bcf29d969dba0cd61b01d9bac80c41575520cc4baabb2"},
    {file = "librt-0.9.0-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e94cbc6ad9a6aeea46d775cbb11f361022f778a9cc8cc90af653d3a594b057ce"},
    {file = "librt-0.9.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:7bc30ad339f4e1a01d4917d645e522a0bc0030644d8973f6346397c93ba1503f"},
    {file = "librt-0.9.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:56d65b583cf43b8cf4c8fbe1e1da20fa3076cc32a1149a141507af1062718236"},
    {file = "librt-0.9.0-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:0a1be03168b2691ba61927e299b352a6315189199ca18a57b733f86cb3cc8d38"},
    {file = "librt-0.9.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:63c12efcd160e1d14da11af0c46c0217473e1e0d2ae1acbccc83f561ea4c2a7b"},
    {file = "librt-0.9.0-cp310-cp310-win32.whl", hash = "sha256:e9002e98dcb1c0a66723592520decd86238ddcef168b37ff6cfb559200b4b774"},
    {file = "librt-0.9.0-cp310-cp310-win_amd64.whl", hash = "sha256:9fcb461fbf70654a52a7cc670e606f04449e2374c199b1825f754e16dacfedd8"},
    {file = "librt-0.9.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:90904fac73c478f4b83f4ed96c99c8208b75e6f9a8a1910548f69a00f1eaa671"},
    {file = "librt-0.9.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:789fff71757facc0738e8d89e3b84e4f0251c1c975e85e81b152cdaca927cc2d"},
    {file = "librt-0.9.0-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:1bf465d1e5b0a27713862441f6467b5ab76385f4ecf8f1f3a44f8aa3c695b4b6"},
    {file = "librt-0.9.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f819e0c6413e259a17a7c0d49f97f405abadd3c2a316a3b46c6440b7dbbedbb1"},
    {file = "librt-0.9.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e0785c2fb4a81e1aece366aa3e2e039f4a4d7d21aaaded5227d7f3c703427882"},
    {file = "librt-0.9.0-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:80b25c7b570a86c03b5da69e665809deb39265476e8e21d96a9328f9762f9990"},
    {file = "librt-0.9.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d4d16b608a1c43d7e33142099a75cd93af482dadce0bf82421e91cad077157f4"},
    {file = "librt-0.9.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:194fc1a32e1e21fe809d38b5faea66cc65eaa00217c8901fbdb99866938adbdb"},
    {file = "librt-0.9.0-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:8c6bc1384d9738781cfd41d09ad7f6e8af13cfea2c75ece6bd6d2566cdea2076"},
    {file = "librt-0.9.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:15cb151e52a044f06e54ac7f7b47adbfc89b5c8e2b63e1175a9d587c43e8942a"},
    {file = "librt-0.9.0-cp311-cp311-win32.whl", hash = "sha256:f100bfe2acf8a3689af9d0cc660d89f17286c9c795f9f18f7b62dd1a6b247ae6"},
    {file = "librt-0.9.0-cp311-cp311-win_amd64.whl", hash = "sha256:0b73e4266307e51c95e09c0750b7ec383c561d2e97d58e473f6f6a209952fbb8"},
    {file = "librt-0.9.0-cp311-cp311-win_arm64.whl", hash = "sha256:bc5518873822d2faa8ebdd2c1a4d7c8ef47b01a058495ab7924cb65bdbf5fc9a"},
    {file = "librt-0.9.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:9b3e3bc363f71bda1639a4ee593cb78f7fbfeacc73411ec0d4c92f00730010a4"},
    {file = "librt-0.9.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:0a09c2f5869649101738653a9b7ab70cf045a1105ac66cbb8f4055e61df78f2d"},
    {file = "librt-0.9.0-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:5ca8e133d799c948db2ab1afc081c333a825b5540475164726dcbf73537e5c2f"},
    {file = "librt-0.9.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:603138ee838ee1583f1b960b62d5d0007845c5c423feb68e44648b1359014e27"},
    {file = "librt-0.9.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f4003f70c56a5addd6aa0897f200dd59afd3bf7bcd5b3cce46dd21f925743bc2"},
    {file = "librt-0.9.0-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:78042f6facfd98ecb25e9829c7e37cce23363d9d7c83bc5f72702c5059eb082b"},
    {file = "librt-0.9.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:a361c9434a64d70a7dbb771d1de302c0cc9f13c0bffe1cf7e642152814b35265"},
    {file = "librt-0.9.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:dd2c7e082b0b92e1baa4da28163a808672485617bc855cc22a2fd06978fa9084"},
    {file = "librt-0.9.0-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:7e6274fd33fc5b2a14d41c9119629d3ff395849d8bcbc80cf637d9e8d2034da8"},
    {file = "librt-0.9.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5093043afb226ecfa1400120d1ebd4442b4f99977783e4f4f7248879009b227f"},
    {file = "librt-0.9.0-cp312-cp312-win32.whl", hash = "sha256:9edcc35d1cae9fd5320171b1a838c7da8a5c968af31e82ecc3dff30b4be0957f"},
    {file = "librt-0.9.0-cp312-cp312-win_amd64.whl", hash = "sha256:3cc2917258e131ae5f958a4d872e07555b51cb7466a43433218061c74ef33745"},
    {file = "librt-0.9.0-cp312-cp312-win_arm64.whl", hash = "sha256:90e6d5420fc8a300518d4d2288154ff45005e920425c22cbbfe8330f3f754bd9"},
    {file = "librt-0.9.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:f29b68cd9714531672db62cc54f6e8ff981900f824d13fa0e00749189e13778e"},
    {file = "librt-0.9.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:7d5c8a5929ac325729f6119802070b561f4db793dffc45e9ac750992a4ed4d22"},
    {file = "librt-0.9.0-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:756775d25ec8345b837ab52effee3ad2f3b2dfd6bbee3e3f029c517bd5d8f05a"},
    {file = "librt-0.9.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2b8f5d00b49818f4e2b1667db994488b045835e0ac16fe2f924f3871bd2b8ac5"},
    {file = "librt-0.9.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c81aef782380f0f13ead670aae01825eb653b44b046aa0e5ebbb79f76ed4aa11"},
    {file = "librt-0.9.0-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:66b58fed90a545328e80d575467244de3741e088c1af928f0b489ebec3ef3858"},
    {file = "librt-0.9.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e78fb7419e07d98c2af4b8567b72b3eaf8cb05caad642e9963465569c8b2d87e"},
    {file = "librt-0.9.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:2c3786f0f4490a5cd87f1ed6cefae833ad6b1060d52044ce0434a2e85893afd0"},
    {file = "librt-0.9.0-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:8494cfc61e03542f2d381e71804990b3931175a29b9278fdb4a5459948778dc2"},
    {file = "librt-0.9.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:07cf11f769831186eeac424376e6189f20ace4f7263e2134bdb9757340d84d4d"},
    {file = "librt-0.9.0-cp313-cp313-win32.whl", hash = "sha256:850d6d03177e52700af605fd60db7f37dcb89782049a149674d1a9649c2138fd"},
    {file = "librt-0.9.0-cp313-cp313-win_amd64.whl", hash = "sha256:a5af136bfba820d592f86c67affcef9b3ff4d4360ac3255e341e964489b48519"},
    {file = "librt-0.9.0-cp313-cp313-win_arm64.whl", hash = "sha256:4c4d0440a3a8e31d962340c3e1cc3fc9ee7febd34c8d8f770d06adb947779ea5"},
    {file = "librt-0.9.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:3f05d145df35dca5056a8bc3838e940efebd893a54b3e19b2dda39ceaa299bcb"},
    {file = "librt-0.9.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1c587494461ebd42229d0f1739f3aa34237dd9980623ecf1be8d3bcba79f4499"},
    {file = "librt-0.9.0-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:b0a2040f801406b93657a70b72fa12311063a319fee72ce98e1524da7200171f"},
    {file = "librt-0.9.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f38bc489037eca88d6ebefc9c4d41a4e07c8e8b4de5188a9e6d290273ad7ebb1"},
    {file = "librt-0.9.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f3fd278f5e6bf7c75ccd6d12344eb686cc020712683363b66f46ac79d37c799f"},
    {file = "librt-0.9.0-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:fcbdf2a9ca24e87bbebb47f1fe34e531ef06f104f98c9ccfc953a3f3344c567a"},
    {file = "librt-0.9.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:e306d956cfa027fe041585f02a1602c32bfa6bb8ebea4899d373383295a6c62f"},
    {file = "librt-0.9.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:465814ab157986acb9dfa5ccd7df944be5eefc0d08d31ec6e8d88bc71251d845"},
    {file = "librt-0.9.0-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:703f4ae36d6240bfe24f542bac784c7e4194ec49c3ba5a994d02891649e2d85b"},
    {file = "librt-0.9.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:3be322a15ee5e70b93b7a59cfd074614f22cc8c9ff18bd27f474e79137ea8d3b"},
    {file = "librt-0.9.0-cp314-cp314-win32.whl", hash = "sha256:b8da9f8035bb417770b1e1610526d87ad4fc58a2804dc4d79c53f6d2cf5a6eb9"},
    {file = "librt-0.9.0-cp314-cp314-win_amd64.whl", hash = "sha256:b8bd70d5d816566a580d193326912f4a76ec2d28a97dc4cd4cc831c0af8e330e"},
    {file = "librt-0.9.0-cp314-cp314-win_arm64.whl", hash = "sha256:fc5758e2b7a56532dc33e3c544d78cbaa9ecf0a0f2a2da2df882c1d6b99a317f"},
    {file = "librt-0.9.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:f24b90b0e0c8cc9491fb1693ae91fe17cb7963153a1946395acdbdd5818429a4"},
    {file = "librt-0.9.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:3fe56e80badb66fdcde06bef81bbaa5bfcf6fbd7aefb86222d9e369c38c6b228"},
    {file = "librt-0.9.0-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:527b5b820b47a09e09829051452bb0d1dd2122261254e2a6f674d12f1d793d54"},
    {file = "librt-0.9.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7d429bdd4ac0ab17c8e4a8af0ed2a7440b16eba474909ab357131018fe8c7e71"},
    {file = "librt-0.9.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7202bdcac47d3a708271c4304a474a8605a4a9a4a709e954bf2d3241140aa938"},
    {file = "librt-0.9.0-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c0d620e74897f8c2613b3c4e2e9c1e422eb46d2ddd07df540784d44117836af3"},
    {file = "librt-0.9.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:d69fc39e627908f4c03297d5a88d9284b73f4d90b424461e32e8c2485e21c283"},
    {file = "librt-0.9.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:c2640e23d2b7c98796f123ffd95cf2022c7777aa8a4a3b98b36c570d37e85eee"},
    {file = "librt-0.9.0-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:451daa98463b7695b0a30aa56bf637831ea559e7b8101ac2ef6382e8eb15e29c"},
    {file = "librt-0.9.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:928bd06eca2c2bbf4349e5b817f837509b0604342e65a502de1d50a7570afd15"},
    {file = "librt-0.9.0-cp314-cp314t-win32.whl", hash = "sha256:a9c63e04d003bc0fb6a03b348018b9a3002f98268200e22cc80f146beac5dc40"},
    {file = "librt-0.9.0-cp314-cp314t-win_amd64.whl", hash = "sha256:f162af66a2ed3f7d1d161a82ca584efd15acd9c1cff190a373458c32f7d42118"},
    {file = "librt-0.9.0-cp314-cp314t-win_arm64.whl", hash = "sha256:a4b25c6c25cac5d0d9d6d6da855195b254e0021e513e0249f0e3b444dc6e0e61"},
    {file = "librt-0.9.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:5112c2fb7c2eefefaeaf5c97fec81343ef44ee86a30dcfaa8223822fba6467b4"},
    {file = "librt-0.9.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:a81eea9b999b985e4bacc650c4312805ea7008fd5e45e1bf221310176a7bcb3a"},
    {file = "librt-0.9.0-cp39-cp39-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:eea1b54943475f51698f85fa230c65ccac769f1e603b981be060ac5763d90927"},
    {file = "librt-0.9.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:81107843ed1836874b46b310f9b1816abcb89912af627868522461c3b7333c0f"},
    {file = "librt-0.9.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:aa95738a68cedd3a6f5492feddc513e2e166b50602958139e47bbdd82da0f5a7"},
    {file = "librt-0.9.0-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:6788207daa0c19955d2b668f3294a368d19f67d9b5f274553fd073c1260cbb9f"},
    {file = "librt-0.9.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:f48c963a76d71b9d7927eb817b543d0dccd52ab6648b99d37bd54f4cd475d856"},
    {file = "librt-0.9.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:42ff8a962554c350d4a83cf47d9b7b78b0e6ff7943e87df7cdfc97c07f3c016f"},
    {file = "librt-0.9.0-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:657f8ba7b9eaaa82759a104137aed2a3ef7bc46ccfd43e0d89b04005b3e0a4cc"},
    {file = "librt-0.9.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:2d03fa4fd277a7974c1978c92c374c57f44edeee163d147b477b143446ad1bf6"},
    {file = "librt-0.9.0-cp39-cp39-win32.whl", hash = "sha256:d9da80e5b04acce03ced8ba6479a71c2a2edf535c2acc0d09c80d2f80f3bad15"},
    {file = "librt-0.9.0-cp39-cp39-win_amd64.whl", hash = "sha256:54d412e47c21b85865676ed0724e37a89e9593c2eee1e7367adf85bfad56ffb1"},
    {file = "librt-0.9.0.tar.gz", hash = "sha256:a0951822531e7aee6e0dfb556b30d5ee36bbe234faf60c20a16c01be3530869d"},
]

[[package]]
name = "m2r2"
version = "0.3.4"
description = "Markdown and reStructuredText in a single file."
optional = false
python-versions = ">=3.7"
groups = ["docs"]
files = [
    {file = "m2r2-0.3.4-py3-none-any.whl", hash = "sha256:1a445514af8a229496bfb1380c52da8dd38313e48600359ee92b2c9d2e4df34a"},
    {file = "m2r2-0.3.4.tar.gz", hash = "sha256:e278f5f337e9aa7b2080fcc3e94b051bda9615b02e36c6fb3f23ff019872f043"},
]

[package.dependencies]
docutils = ">=0.19"
mistune = "0.8.4"

[[package]]
name = "markdown-it-py"
version = "4.0.0"
description = "Python port of markdown-it. Markdown parsing, done right!"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147"},
    {file = "markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3"},
]

[package.dependencies]
mdurl = ">=0.1,<1.0"

[package.extras]
benchmarking = ["psutil", "pytest", "pytest-benchmark"]
compare = ["commonmark (>=0.9,<1.0)", "markdown (>=3.4,<4.0)", "markdown-it-pyrs", "mistletoe (>=1.0,<2.0)", "mistune (>=3.0,<4.0)", "panflute (>=2.3,<3.0)"]
linkify = ["linkify-it-py (>=1,<3)"]
plugins = ["mdit-py-plugins (>=0.5.0)"]
profiling = ["gprof2dot"]
rtd = ["ipykernel", "jupyter_sphinx", "mdit-py-plugins (>=0.5.0)", "myst-parser", "pyyaml", "sphinx", "sphinx-book-theme (>=1.0,<2.0)", "sphinx-copybutton", "sphinx-design"]
testing = ["coverage", "pytest", "pytest-cov", "pytest-regressions", "requests"]

[[package]]
name = "markupsafe"
version = "3.0.3"
description = "Safely add untrusted strings to HTML/XML markup."
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "markupsafe-3.0.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2f981d352f04553a7171b8e44369f2af4055f888dfb147d55e42d29e29e74559"},
    {file = "markupsafe-3.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:e1c1493fb6e50ab01d20a22826e57520f1284df32f2d8601fdd90b6304601419"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1ba88449deb3de88bd40044603fafffb7bc2b055d626a330323a9ed736661695"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f42d0984e947b8adf7dd6dde396e720934d12c506ce84eea8476409563607591"},
    {file = "markupsafe-3.0.3-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c0c0b3ade1c0b13b936d7970b1d37a57acde9199dc2aecc4c336773e1d86049c"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:0303439a41979d9e74d18ff5e2dd8c43ed6c6001fd40e5bf2e43f7bd9bbc523f"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:d2ee202e79d8ed691ceebae8e0486bd9a2cd4794cec4824e1c99b6f5009502f6"},
    {file = "markupsafe-3.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:177b5253b2834fe3678cb4a5f0059808258584c559193998be2601324fdeafb1"},
    {file = "markupsafe-3.0.3-cp310-cp310-win32.whl", hash = "sha256:2a15a08b17dd94c53a1da0438822d70ebcd13f8c3a95abe3a9ef9f11a94830aa"},
    {file = "markupsafe-3.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:c4ffb7ebf07cfe8931028e3e4c85f0357459a3f9f9490886198848f4fa002ec8"},
    {file = "markupsafe-3.0.3-cp310-cp310-win_arm64.whl", hash = "sha256:e2103a929dfa2fcaf9bb4e7c091983a49c9ac3b19c9061b6d5427dd7d14d81a1"},
    {file = "markupsafe-3.0.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:1cc7ea17a6824959616c525620e387f6dd30fec8cb44f649e31712db02123dad"},
    {file = "markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4bd4cd07944443f5a265608cc6aab442e4f74dff8088b0dfc8238647b8f6ae9a"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6b5420a1d9450023228968e7e6a9ce57f65d148ab56d2313fcd589eee96a7a50"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0bf2a864d67e76e5c9a34dc26ec616a66b9888e25e7b9460e1c76d3293bd9dbf"},
    {file = "markupsafe-3.0.3-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc51efed119bc9cfdf792cdeaa4d67e8f6fcccab66ed4bfdd6bde3e59bfcbb2f"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:068f375c472b3e7acbe2d5318dea141359e6900156b5b2ba06a30b169086b91a"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:7be7b61bb172e1ed687f1754f8e7484f1c8019780f6f6b0786e76bb01c2ae115"},
    {file = "markupsafe-3.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f9e130248f4462aaa8e2552d547f36ddadbeaa573879158d721bbd33dfe4743a"},
    {file = "markupsafe-3.0.3-cp311-cp311-win32.whl", hash = "sha256:0db14f5dafddbb6d9208827849fad01f1a2609380add406671a26386cdf15a19"},
    {file = "markupsafe-3.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:de8a88e63464af587c950061a5e6a67d3632e36df62b986892331d4620a35c01"},
    {file = "markupsafe-3.0.3-cp311-cp311-win_arm64.whl", hash = "sha256:3b562dd9e9ea93f13d53989d23a7e775fdfd1066c33494ff43f5418bc8c58a5c"},
    {file = "markupsafe-3.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d53197da72cc091b024dd97249dfc7794d6a56530370992a5e1a08983ad9230e"},
    {file = "markupsafe-3.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:1872df69a4de6aead3491198eaf13810b565bdbeec3ae2dc8780f14458ec73ce"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3a7e8ae81ae39e62a41ec302f972ba6ae23a5c5396c8e60113e9066ef893da0d"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d6dd0be5b5b189d31db7cda48b91d7e0a9795f31430b7f271219ab30f1d3ac9d"},
    {file = "markupsafe-3.0.3-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:94c6f0bb423f739146aec64595853541634bde58b2135f27f61c1ffd1cd4d16a"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:be8813b57049a7dc738189df53d69395eba14fb99345e0a5994914a3864c8a4b"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:83891d0e9fb81a825d9a6d61e3f07550ca70a076484292a70fde82c4b807286f"},
    {file = "markupsafe-3.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:77f0643abe7495da77fb436f50f8dab76dbc6e5fd25d39589a0f1fe6548bfa2b"},
    {file = "markupsafe-3.0.3-cp312-cp312-win32.whl", hash = "sha256:d88b440e37a16e651bda4c7c2b930eb586fd15ca7406cb39e211fcff3bf3017d"},
    {file = "markupsafe-3.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:26a5784ded40c9e318cfc2bdb30fe164bdb8665ded9cd64d500a34fb42067b1c"},
    {file = "markupsafe-3.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:35add3b638a5d900e807944a078b51922212fb3dedb01633a8defc4b01a3c85f"},
    {file = "markupsafe-3.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e1cf1972137e83c5d4c136c43ced9ac51d0e124706ee1c8aa8532c1287fa8795"},
    {file = "markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:116bb52f642a37c115f517494ea5feb03889e04df47eeff5b130b1808ce7c219"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:133a43e73a802c5562be9bbcd03d090aa5a1fe899db609c29e8c8d815c5f6de6"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ccfcd093f13f0f0b7fdd0f198b90053bf7b2f02a3927a30e63f3ccc9df56b676"},
    {file = "markupsafe-3.0.3-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:509fa21c6deb7a7a273d629cf5ec029bc209d1a51178615ddf718f5918992ab9"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:a4afe79fb3de0b7097d81da19090f4df4f8d3a2b3adaa8764138aac2e44f3af1"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:795e7751525cae078558e679d646ae45574b47ed6e7771863fcc079a6171a0fc"},
    {file = "markupsafe-3.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:8485f406a96febb5140bfeca44a73e3ce5116b2501ac54fe953e488fb1d03b12"},
    {file = "markupsafe-3.0.3-cp313-cp313-win32.whl", hash = "sha256:bdd37121970bfd8be76c5fb069c7751683bdf373db1ed6c010162b2a130248ed"},
    {file = "markupsafe-3.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:9a1abfdc021a164803f4d485104931fb8f8c1efd55bc6b748d2f5774e78b62c5"},
    {file = "markupsafe-3.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:7e68f88e5b8799aa49c85cd116c932a1ac15caaa3f5db09087854d218359e485"},
    {file = "markupsafe-3.0.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:218551f6df4868a8d527e3062d0fb968682fe92054e89978594c28e642c43a73"},
    {file = "markupsafe-3.0.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:3524b778fe5cfb3452a09d31e7b5adefeea8c5be1d43c4f810ba09f2ceb29d37"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4e885a3d1efa2eadc93c894a21770e4bc67899e3543680313b09f139e149ab19"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8709b08f4a89aa7586de0aadc8da56180242ee0ada3999749b183aa23df95025"},
    {file = "markupsafe-3.0.3-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:b8512a91625c9b3da6f127803b166b629725e68af71f8184ae7e7d54686a56d6"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:9b79b7a16f7fedff2495d684f2b59b0457c3b493778c9eed31111be64d58279f"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:12c63dfb4a98206f045aa9563db46507995f7ef6d83b2f68eda65c307c6829eb"},
    {file = "markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8f71bc33915be5186016f675cd83a1e08523649b0e33efdb898db577ef5bb009"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win32.whl", hash = "sha256:69c0b73548bc525c8cb9a251cddf1931d1db4d2258e9599c28c07ef3580ef354"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win_amd64.whl", hash = "sha256:1b4b79e8ebf6b55351f0d91fe80f893b4743f104bff22e90697db1590e47a218"},
    {file = "markupsafe-3.0.3-cp313-cp313t-win_arm64.whl", hash = "sha256:ad2cf8aa28b8c020ab2fc8287b0f823d0a7d8630784c31e9ee5edea20f406287"},
    {file = "markupsafe-3.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:eaa9599de571d72e2daf60164784109f19978b327a3910d3e9de8c97b5b70cfe"},
    {file = "markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c47a551199eb8eb2121d4f0f15ae0f923d31350ab9280078d1e5f12b249e0026"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f34c41761022dd093b4b6896d4810782ffbabe30f2d443ff5f083e0cbbb8c737"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:457a69a9577064c05a97c41f4e65148652db078a3a509039e64d3467b9e7ef97"},
    {file = "markupsafe-3.0.3-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e8afc3f2ccfa24215f8cb28dcf43f0113ac3c37c2f0f0806d8c70e4228c5cf4d"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:ec15a59cf5af7be74194f7ab02d0f59a62bdcf1a537677ce67a2537c9b87fcda"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:0eb9ff8191e8498cca014656ae6b8d61f39da5f95b488805da4bb029cccbfbaf"},
    {file = "markupsafe-3.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2713baf880df847f2bece4230d4d094280f4e67b1e813eec43b4c0e144a34ffe"},
    {file = "markupsafe-3.0.3-cp314-cp314-win32.whl", hash = "sha256:729586769a26dbceff69f7a7dbbf59ab6572b99d94576a5592625d5b411576b9"},
    {file = "markupsafe-3.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:bdc919ead48f234740ad807933cdf545180bfbe9342c2bb451556db2ed958581"},
    {file = "markupsafe-3.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:5a7d5dc5140555cf21a6fefbdbf8723f06fcd2f63ef108f2854de715e4422cb4"},
    {file = "markupsafe-3.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:1353ef0c1b138e1907ae78e2f6c63ff67501122006b0f9abad68fda5f4ffc6ab"},
    {file = "markupsafe-3.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:1085e7fbddd3be5f89cc898938f42c0b3c711fdcb37d75221de2666af647c175"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1b52b4fb9df4eb9ae465f8d0c228a00624de2334f216f178a995ccdcf82c4634"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:fed51ac40f757d41b7c48425901843666a6677e3e8eb0abcff09e4ba6e664f50"},
    {file = "markupsafe-3.0.3-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:f190daf01f13c72eac4efd5c430a8de82489d9cff23c364c3ea822545032993e"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:e56b7d45a839a697b5eb268c82a71bd8c7f6c94d6fd50c3d577fa39a9f1409f5"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:f3e98bb3798ead92273dc0e5fd0f31ade220f59a266ffd8a4f6065e0a3ce0523"},
    {file = "markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:5678211cb9333a6468fb8d8be0305520aa073f50d17f089b5b4b477ea6e67fdc"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win32.whl", hash = "sha256:915c04ba3851909ce68ccc2b8e2cd691618c4dc4c4232fb7982bca3f41fd8c3d"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4faffd047e07c38848ce017e8725090413cd80cbc23d86e55c587bf979e579c9"},
    {file = "markupsafe-3.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:32001d6a8fc98c8cb5c947787c5d08b0a50663d139f1305bac5885d98d9b40fa"},
    {file = "markupsafe-3.0.3-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:15d939a21d546304880945ca1ecb8a039db6b4dc49b2c5a400387cdae6a62e26"},
    {file = "markupsafe-3.0.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:f71a396b3bf33ecaa1626c255855702aca4d3d9fea5e051b41ac59a9c1c41edc"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f4b68347f8c5eab4a13419215bdfd7f8c9b19f2b25520968adfad23eb0ce60c"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e8fc20152abba6b83724d7ff268c249fa196d8259ff481f3b1476383f8f24e42"},
    {file = "markupsafe-3.0.3-cp39-cp39-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:949b8d66bc381ee8b007cd945914c721d9aba8e27f71959d750a46f7c282b20b"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:3537e01efc9d4dccdf77221fb1cb3b8e1a38d5428920e0657ce299b20324d758"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_riscv64.whl", hash = "sha256:591ae9f2a647529ca990bc681daebdd52c8791ff06c2bfa05b65163e28102ef2"},
    {file = "markupsafe-3.0.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:a320721ab5a1aba0a233739394eb907f8c8da5c98c9181d1161e77a0c8e36f2d"},
    {file = "markupsafe-3.0.3-cp39-cp39-win32.whl", hash = "sha256:df2449253ef108a379b8b5d6b43f4b1a8e81a061d6537becd5582fba5f9196d7"},
    {file = "markupsafe-3.0.3-cp39-cp39-win_amd64.whl", hash = "sha256:7c3fb7d25180895632e5d3148dbdc29ea38ccb7fd210aa27acbd1201a1902c6e"},
    {file = "markupsafe-3.0.3-cp39-cp39-win_arm64.whl", hash = "sha256:38664109c14ffc9e7437e86b4dceb442b0096dfe3541d7864d9cbe1da4cf36c8"},
    {file = "markupsafe-3.0.3.tar.gz", hash = "sha256:722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698"},
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
name = "mdurl"
version = "0.1.2"
description = "Markdown URL utilities"
optional = false
python-versions = ">=3.7"
groups = ["dev"]
files = [
    {file = "mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8"},
    {file = "mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba"},
]

[[package]]
name = "mistune"
version = "0.8.4"
description = "The fastest markdown parser in pure Python"
optional = false
python-versions = "*"
groups = ["docs"]
files = [
    {file = "mistune-0.8.4-py2.py3-none-any.whl", hash = "sha256:88a1051873018da288eee8538d476dffe1262495144b33ecb586c4ab266bb8d4"},
    {file = "mistune-0.8.4.tar.gz", hash = "sha256:59a3429db53c50b5c6bcc8a07f8848cb00d7dc8bdb431a4ab41920d201d4756e"},
]

[[package]]
name = "mypy"
version = "1.20.2"
description = "Optional static typing for Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "mypy-1.20.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:cf5a4db6dca263010e2c7bff081c89383c72d187ba2cf4c44759aac970e2f0c4"},
    {file = "mypy-1.20.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:7b0e817b518bff7facd7f85ea05b643ad8bdcce684cf29784987b0a7c8e1f997"},
    {file = "mypy-1.20.2-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:97d7b9a485b40f8ca425460e89bf1da2814625b2da627c0dcc6aa46c92631d14"},
    {file = "mypy-1.20.2-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1e1c12f6d2db3d78b909b5f77513c11eb7f2dd2782b96a3ab6dffc7d44575c99"},
    {file = "mypy-1.20.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:89dce27e142d25ffbc154c1819383b69f2e9234dc4ed4766f42e0e8cb264ab5c"},
    {file = "mypy-1.20.2-cp310-cp310-win_amd64.whl", hash = "sha256:f376e37f9bf2a946872fc5fd1199c99310748e3c26c7a26683f13f8bdb756cbd"},
    {file = "mypy-1.20.2-cp310-cp310-win_arm64.whl", hash = "sha256:6e2b469efd811707bc530fd1effef0f5d6eebcb7fe376affae69025da4b979a2"},
    {file = "mypy-1.20.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:4077797a273e56e8843d001e9dfe4ba10e33323d6ade647ff260e5cd97d9758c"},
    {file = "mypy-1.20.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:cdecf62abcc4292500d7858aeae87a1f8f1150f4c4dd08fb0b336ee79b2a6df3"},
    {file = "mypy-1.20.2-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c566c3a88b6ece59b3d70f65bedef17304f48eb52ff040a6a18214e1917b3254"},
    {file = "mypy-1.20.2-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0deb80d062b2479f2c87ae568f89845afc71d11bc41b04179e58165fd9f31e98"},
    {file = "mypy-1.20.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:bba9ad231e92a3e424b3e56b65aa17704993425bba97e302c832f9466bb85bac"},
    {file = "mypy-1.20.2-cp311-cp311-win_amd64.whl", hash = "sha256:baf593f2765fa3a6b1ef95807dbaa3d25b594f6a52adcc506a6b9cb115e1be67"},
    {file = "mypy-1.20.2-cp311-cp311-win_arm64.whl", hash = "sha256:20175a1c0f49863946ec20b7f63255768058ac4f07d2b9ded6a6b46cfb5a9100"},
    {file = "mypy-1.20.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:4dbfcf869f6b0517f70cf0030ba6ea1d6645e132337a7d5204a18d8d5636c02b"},
    {file = "mypy-1.20.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4b6481b228d072315b053210b01ac320e1be243dc17f9e5887ef167f23f5fae4"},
    {file = "mypy-1.20.2-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:34397cdced6b90b836e38182076049fdb41424322e0b0728c946b0939ebdf9f6"},
    {file = "mypy-1.20.2-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a5da6976f20cae27059ea8d0c86e7cef3de720e04c4bb9ee18e3690fdb792066"},
    {file = "mypy-1.20.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:56908d7e08318d39f85b1f0c6cfd47b0cac1a130da677630dac0de3e0623e102"},
    {file = "mypy-1.20.2-cp312-cp312-win_amd64.whl", hash = "sha256:d52ad8d78522da1d308789df651ee5379088e77c76cb1994858d40a426b343b9"},
    {file = "mypy-1.20.2-cp312-cp312-win_arm64.whl", hash = "sha256:785b08db19c9f214dc37d65f7c165d19a30fcecb48abfa30f31b01b5acaabb58"},
    {file = "mypy-1.20.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:edfbfca868cdd6bd8d974a60f8a3682f5565d3f5c99b327640cedd24c4264026"},
    {file = "mypy-1.20.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:e2877a02380adfcdbc69071a0f74d6e9dbbf593c0dc9d174e1f223ffd5281943"},
    {file = "mypy-1.20.2-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7488448de6007cd5177c6cea0517ac33b4c0f5ee9b5e9f2be51ce75511a85517"},
    {file = "mypy-1.20.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:bb9c2fa06887e21d6a3a868762acb82aec34e2c6fd0174064f27c93ede68ad15"},
    {file = "mypy-1.20.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:9d56a78b646f2e3daa865bc70cd5ec5a46c50045801ca8ff17a0c43abc97e3ee"},
    {file = "mypy-1.20.2-cp313-cp313-win_amd64.whl", hash = "sha256:2a4102b03bb7481d9a91a6da8d174740c9c8c4401024684b9ca3b7cc5e49852f"},
    {file = "mypy-1.20.2-cp313-cp313-win_arm64.whl", hash = "sha256:a95a9248b0c6fd933a442c03c3b113c3b61320086b88e2c444676d3fd1ca3330"},
    {file = "mypy-1.20.2-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:419413398fe250aae057fd2fe50166b61077083c9b82754c341cf4fd73038f30"},
    {file = "mypy-1.20.2-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:e73c07f23009962885c197ccb9b41356a30cc0e5a1d0c2ea8fd8fb1362d7f924"},
    {file = "mypy-1.20.2-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0c64e5973df366b747646fc98da921f9d6eba9716d57d1db94a83c026a08e0fb"},
    {file = "mypy-1.20.2-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5a65aa591af023864fd08a97da9974e919452cfe19cb146c8a5dc692626445dc"},
    {file = "mypy-1.20.2-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:4fef51b01e638974a6e69885687e9bd40c8d1e09a6cd291cca0619625cf1f558"},
    {file = "mypy-1.20.2-cp314-cp314-win_amd64.whl", hash = "sha256:913485a03f1bcf5d279409a9d2b9ed565c151f61c09f29991e5faa14033da4c8"},
    {file = "mypy-1.20.2-cp314-cp314-win_arm64.whl", hash = "sha256:c3bae4f855d965b5453784300c12ffc63a548304ac7f99e55d4dc7c898673aa3"},
    {file = "mypy-1.20.2-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:2de3dcea53babc1c3237a19002bc3d228ce1833278f093b8d619e06e7cc79609"},
    {file = "mypy-1.20.2-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:52b176444e2e5054dfcbcb8c75b0b719865c96247b37407184bbfca5c353f2c2"},
    {file = "mypy-1.20.2-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:688c3312e5dadb573a2c69c82af3a298d43ecf9e6d264e0f95df960b5f6ac19c"},
    {file = "mypy-1.20.2-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:29752dbbf8cc53f89f6ac096d363314333045c257c9c75cbd189ca2de0455744"},
    {file = "mypy-1.20.2-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:803203d2b6ea644982c644895c2f78b28d0e208bba7b27d9b921e0ec5eb207c6"},
    {file = "mypy-1.20.2-cp314-cp314t-win_amd64.whl", hash = "sha256:9bcb8aa397ff0093c824182fd76a935a9ba7ad097fcbef80ae89bf6c1731d8ec"},
    {file = "mypy-1.20.2-cp314-cp314t-win_arm64.whl", hash = "sha256:e061b58443f1736f8a37c48978d7ab581636d6ab03e3d4f99e3fa90463bb9382"},
    {file = "mypy-1.20.2-py3-none-any.whl", hash = "sha256:a94c5a76ab46c5e6257c7972b6c8cff0574201ca7dc05647e33e795d78680563"},
    {file = "mypy-1.20.2.tar.gz", hash = "sha256:e8222c26daaafd9e8626dec58ae36029f82585890589576f769a650dd20fd665"},
]

[package.dependencies]
librt = {version = ">=0.8.0", markers = "platform_python_implementation != \"PyPy\""}
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
native-parser = ["ast-serialize (>=0.1.1,<1.0.0)"]
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
name = "mypy-protobuf"
version = "3.6.0"
description = "Generate mypy stub files from protobuf specs"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version < \"3.14\""
files = [
    {file = "mypy-protobuf-3.6.0.tar.gz", hash = "sha256:02f242eb3409f66889f2b1a3aa58356ec4d909cdd0f93115622e9e70366eca3c"},
    {file = "mypy_protobuf-3.6.0-py3-none-any.whl", hash = "sha256:56176e4d569070e7350ea620262478b49b7efceba4103d468448f1d21492fd6c"},
]

[package.dependencies]
protobuf = ">=4.25.3"
types-protobuf = ">=4.24"

[[package]]
name = "mypy-protobuf"
version = "5.0.0"
description = "Generate mypy stub files from protobuf specs"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
markers = "python_version >= \"3.14\""
files = [
    {file = "mypy_protobuf-5.0.0-py3-none-any.whl", hash = "sha256:3a7dd753ef3e3b8783a824eb51f07983f62812f9ec066e4fbb1b22d6c5dc36d0"},
    {file = "mypy_protobuf-5.0.0.tar.gz", hash = "sha256:6fdd1cfdbb4419c713291d800a332d4bba6510dbd1341ed95e0bcc82fcadb6b5"},
]

[package.dependencies]
protobuf = ">=4.25.3"
types-protobuf = ">=4.24"

[[package]]
name = "ni-grpc-extensions"
version = "1.1.0"
description = "gRPC Extensions"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_grpc_extensions-1.1.0-py3-none-any.whl", hash = "sha256:db0357acd244854f4acccf202c89fe6462b4283d264ed639f4e248e6cc86bc9b"},
    {file = "ni_grpc_extensions-1.1.0.tar.gz", hash = "sha256:028ea33e5c5234bc050bf5dc99f5b61611531de8f012293e9d4c6985b7b37afb"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-grpcdevice-v1-proto"
version = "1.1.0"
description = "Protobuf generated code for the nidevice_grpc gRPC API"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_grpcdevice_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:2784c4b3e64a9c1e6b743d26847b7a44bf781ab46a9e19b02b379c1e0bc6dcfb"},
    {file = "ni_grpcdevice_v1_proto-1.1.0.tar.gz", hash = "sha256:ad14ab44e456a67d50a8fc38329e01dccae1732eab22a529c96eb3d5cb46370c"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-discovery-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Discovery Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_discovery_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:366dcc3b93627ed1ede488955637e0768b29cb7a375e59ac1020f4c53892d00c"},
    {file = "ni_measurementlink_discovery_v1_client-1.1.0.tar.gz", hash = "sha256:831b6145cf8def0021cb00579b08a2ad1da5a19fdeedea4522a3cb4a30978c48"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-proto = ">=1.1.0"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}

[[package]]
name = "ni-measurementlink-discovery-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI discovery gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:6a3061ca858d3ee887987dc5130074fc439ce6c2b26fe6b3f9401da023461d43"},
    {file = "ni_measurementlink_discovery_v1_proto-1.1.0.tar.gz", hash = "sha256:f9a9b4572ac5d169fad21ab56e2639abdb77979cf0dc3a88cdb71b2c783d009c"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-measurement-v1-proto"
version = "1.1.1"
description = "Protobuf data types for NI measurement gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_measurement_v1_proto-1.1.1-py3-none-any.whl", hash = "sha256:cb0e1e26f8d08829de46f5707061aacbbb6e42248811bac7eababbdd524f0196"},
    {file = "ni_measurementlink_measurement_v1_proto-1.1.1.tar.gz", hash = "sha256:81b1d321d78b2f15e2cbd41316314f39a9446866928f29a69ed501bd911be6f7"},
]

[package.dependencies]
ni-measurementlink-proto = ">=1.1.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-measurement-v2-proto"
version = "1.1.1"
description = "Protobuf data types for NI measurement gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_measurement_v2_proto-1.1.1-py3-none-any.whl", hash = "sha256:2776adb4402f58ad6fc23436349989eb92b74a718dcbb084aab65fcce3b43b51"},
    {file = "ni_measurementlink_measurement_v2_proto-1.1.1.tar.gz", hash = "sha256:de236b4b02a03730be6d94b362edba01c1b11fb803436bd2a65fdb7bc95bf605"},
]

[package.dependencies]
ni-measurementlink-proto = ">=1.0.0"
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-pinmap-v1-client"
version = "1.1.0"
description = "gRPC Client for NI Pin Map Service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_pinmap_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:2d758aa15addd78fde63e57a69e4c4cbb25e1689c4ce2e5d7b456c22c1b3607e"},
    {file = "ni_measurementlink_pinmap_v1_client-1.1.0.tar.gz", hash = "sha256:ae5b406781544071ea46a5afb862daeb29e989ce67beb80972f88fb80135bc4f"},
]

[package.dependencies]
grpcio = ">=1.49.0,<2.0"
ni-grpc-extensions = ">=1.1.0"
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurementlink-measurement-v1-proto = ">=1.1.1"
ni-measurementlink-measurement-v2-proto = ">=1.1.1"
ni-measurementlink-pinmap-v1-proto = ">=1.1.0"
ni-measurementlink-sessionmanagement-v1-client = ">=1.1.0"

[[package]]
name = "ni-measurementlink-pinmap-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI pinmap gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_pinmap_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:c2334d2ffe4e11f776b0087ad25184b504faa63fa57ec3c7eb87e1a3234dd686"},
    {file = "ni_measurementlink_pinmap_v1_proto-1.1.0.tar.gz", hash = "sha256:db6cef7969c6423349e6560850983008a269a3de0ca7dd623795d7153ede64c1"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-proto"
version = "1.1.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_proto-1.1.0-py3-none-any.whl", hash = "sha256:b7fb6c7b6c36a80d0a1e67fd47d2fa6cccfed993dd5047aa720b04f07c5a546e"},
    {file = "ni_measurementlink_proto-1.1.0.tar.gz", hash = "sha256:4fca44af39715f8501d711944f4d6bae11f1b9ffa059a6995eb69770872c3fa5"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-measurementlink-sessionmanagement-v1-client"
version = "1.1.0"
description = "Client gRPC APIs for the session management service"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_sessionmanagement_v1_client-1.1.0-py3-none-any.whl", hash = "sha256:90ddf2561f82c8b32d9e86908326c8e50c388f6e74c1ea2bac758f4e10553a3f"},
    {file = "ni_measurementlink_sessionmanagement_v1_client-1.1.0.tar.gz", hash = "sha256:53348004828452fe0de3cae89e0aed4952a120254beb346b8764428373116038"},
]

[package.dependencies]
deprecation = ">=2.1"
ni-grpc-extensions = ">=1.1.0"
ni-grpcdevice-v1-proto = ">=1.1.0"
ni-measurementlink-discovery-v1-client = ">=1.1.0"
ni-measurementlink-pinmap-v1-proto = ">=1.1.0"
ni-measurementlink-proto = ">=1.1.0"
ni-measurementlink-sessionmanagement-v1-proto = ">=1.1.0"
protobuf = ">=4.21"
python-decouple = ">=3.8"
pywin32 = {version = ">=303", markers = "sys_platform == \"win32\""}
traceloggingdynamic = {version = ">=1.0", markers = "sys_platform == \"win32\""}

[package.extras]
drivers = ["nidaqmx[grpc] (>=0.8.0)", "nidcpower[grpc] (>=1.4.4)", "nidigital[grpc] (>=1.4.4)", "nidmm[grpc] (>=1.4.4)", "nifgen[grpc] (>=1.4.4)", "niscope[grpc] (>=1.4.4)", "niswitch[grpc] (>=1.4.4)"]
nidaqmx = ["nidaqmx[grpc] (>=0.8.0)"]
nidcpower = ["nidcpower[grpc] (>=1.4.4)"]
nidigital = ["nidigital[grpc] (>=1.4.4)"]
nidmm = ["nidmm[grpc] (>=1.4.4)"]
nifgen = ["nifgen[grpc] (>=1.4.4)"]
niscope = ["niscope[grpc] (>=1.4.4)"]
niswitch = ["niswitch[grpc] (>=1.4.4)"]

[[package]]
name = "ni-measurementlink-sessionmanagement-v1-proto"
version = "1.1.0"
description = "Protobuf data types for NI session management gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_measurementlink_sessionmanagement_v1_proto-1.1.0-py3-none-any.whl", hash = "sha256:e88d8beaf141e85f83daba1858a8b372df9d2c2671b3c4b0bb3b50e745e14585"},
    {file = "ni_measurementlink_sessionmanagement_v1_proto-1.1.0.tar.gz", hash = "sha256:cedc461b7990bc496ac87a932ca32f7b9f6f1c73c8eb5bda71f5e60709ef76e1"},
]

[package.dependencies]
protobuf = ">=4.21"

[[package]]
name = "ni-protobuf-types"
version = "1.2.0"
description = "Protobuf data types for NI gRPC APIs"
optional = false
python-versions = "<4.0,>=3.10"
groups = ["main"]
files = [
    {file = "ni_protobuf_types-1.2.0-py3-none-any.whl", hash = "sha256:461c4825571d0054fd5427664403c3d69fcd180c9c00868ac1911693dd9bf901"},
    {file = "ni_protobuf_types-1.2.0.tar.gz", hash = "sha256:e8226f8ef44b104ffb1b1f6e416511c416be4d91bf5c2633db7ab58294e037bb"},
]

[package.dependencies]
nitypes = ">=1.1.0"
protobuf = ">=4.21"

[[package]]
name = "ni-python-styleguide"
version = "0.5.0"
description = "NI's internal and external Python linter rules and plugins"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["dev"]
files = [
    {file = "ni_python_styleguide-0.5.0-py3-none-any.whl", hash = "sha256:66784d97bc2898552386ca8e0667a11fa5f712820130585df7709d08836f6bc0"},
    {file = "ni_python_styleguide-0.5.0.tar.gz", hash = "sha256:66bd05f7d9fc98a87e5e85319faa752efd54549c979938ed1bb64e2d1f412630"},
]

[package.dependencies]
better-diff = ">=0.1.3,<0.2.0"
black = ">=23.1,<26.0"
click = ">=7.1.2"
flake8 = [
    {version = ">=6.1,<7.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=5.0,<6.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
flake8-black = ">=0.2.1"
flake8-docstrings = ">=1.5.0"
flake8-import-order = ">=0.18.1,<0.19.0"
flake8-tidy-imports = ">=4.11.0"
isort = ">=5.10"
pathspec = ">=0.11.1"
pep8-naming = ">=0.11.1"
pycodestyle = [
    {version = ">=2.11,<3.0", markers = "python_version >= \"3.12\" and python_version < \"4.0\""},
    {version = ">=2.9,<3.0", markers = "python_version >= \"3.8\" and python_version < \"3.12\""},
]
setuptools = "<82"
toml = ">=0.10.1"

[[package]]
name = "nidaqmx"
version = "1.5.0"
description = "NI-DAQmx Python API"
optional = true
python-versions = "<4.0,>=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"nidaqmx\""
files = [
    {file = "nidaqmx-1.5.0-py3-none-any.whl", hash = "sha256:ab2e6668027cc4f9fe0e4fdd7f5d77c6005f0587a849094b66bfde5bef533e7f"},
    {file = "nidaqmx-1.5.0.tar.gz", hash = "sha256:4e7e20b2a898b550f4d8563a9298d51193f9c9073d9b79f39bff073822fcac51"},
]

[package.dependencies]
click = ">=8.0.0"
deprecation = ">=2.1"
distro = {version = ">=1.9.0", markers = "sys_platform == \"linux\""}
grpcio = {version = ">=1.49.0,<2.0", optional = true, markers = "extra == \"grpc\""}
hightime = ">=0.2.2"
ni-grpcdevice-v1-proto = {version = ">=1.0.0", optional = true, markers = "extra == \"grpc\""}
ni-protobuf-types = {version = ">=1.0.0", optional = true, markers = "extra == \"grpc\""}
nitypes = ">=1.0.1"
numpy = [
    {version = ">=2.1", markers = "python_version >= \"3.13\" and python_version < \"4.0\""},
    {version = ">=1.22", markers = "python_version >= \"3.9\" and python_version < \"3.13\""},
]
protobuf = {version = ">=4.21", optional = true, markers = "extra == \"grpc\""}
python-decouple = ">=3.8"
requests = ">=2.25.0"
typing_extensions = ">=4.0.0"
tzlocal = ">=5.0,<6.0"

[package.extras]
grpc = ["grpcio (>=1.49.0,<2.0)", "ni-grpcdevice-v1-proto (>=1.0.0)", "ni-protobuf-types (>=1.0.0)", "protobuf (>=4.21)"]

[[package]]
name = "nidcpower"
version = "1.5.0"
description = "NI-DCPower Python API"
optional = true
python-versions = ">=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"nidcpower\""
files = [
    {file = "nidcpower-1.5.0-py3-none-any.whl", hash = "sha256:04e42b5af98dd5df1eccd4859a039cfaa541719b5532d395e922cf60833b8c53"},
    {file = "nidcpower-1.5.0.tar.gz", hash = "sha256:fd09a3fa118ea44dfc0e6f91995fc0ab0a24d724b5e93ddb93d723a248d62246"},
]

[package.dependencies]
grpcio = {version = ">=1.59.0,<2.0", optional = true, markers = "extra == \"grpc\""}
hightime = ">=0.2.0"
protobuf = {version = ">=4.21.6", optional = true, markers = "extra == \"grpc\""}

[package.extras]
grpc = ["grpcio (>=1.59.0,<2.0)", "protobuf (>=4.21.6)"]

[[package]]
name = "nidigital"
version = "1.4.9"
description = "NI-Digital Pattern Driver Python API"
optional = true
python-versions = ">=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"nidigital\""
files = [
    {file = "nidigital-1.4.9-py3-none-any.whl", hash = "sha256:589316e3a48672e2fdd7cd3b47b86f879191f7ab5790b9577a688eef7ce6a495"},
    {file = "nidigital-1.4.9.tar.gz", hash = "sha256:5eac70ecc97c6f15d59097092ff82e79cfe8cfc4f903ae15886dbbaa9d18ffbf"},
]

[package.dependencies]
grpcio = {version = ">=1.59.0,<2.0", optional = true, markers = "extra == \"grpc\""}
hightime = ">=0.2.0"
nitclk = "*"
protobuf = {version = ">=4.21.6", optional = true, markers = "extra == \"grpc\""}

[package.extras]
grpc = ["grpcio (>=1.59.0,<2.0)", "protobuf (>=4.21.6)"]

[[package]]
name = "nidmm"
version = "1.4.9"
description = "NI-DMM Python API"
optional = true
python-versions = ">=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"nidmm\""
files = [
    {file = "nidmm-1.4.9-py3-none-any.whl", hash = "sha256:108180f5a3ca3f2d1c8ac3cda66692a2a58c869dab12456e02ff56042ed79aee"},
    {file = "nidmm-1.4.9.tar.gz", hash = "sha256:7eaf388e35deb4c5c118e2d8bfd05647e5c93d63fb9d92059806a0ccd3e0780c"},
]

[package.dependencies]
grpcio = {version = ">=1.59.0,<2.0", optional = true, markers = "extra == \"grpc\""}
hightime = ">=0.2.0"
protobuf = {version = ">=4.21.6", optional = true, markers = "extra == \"grpc\""}

[package.extras]
grpc = ["grpcio (>=1.59.0,<2.0)", "protobuf (>=4.21.6)"]

[[package]]
name = "nifgen"
version = "1.4.9"
description = "NI-FGEN Python API"
optional = true
python-versions = ">=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"nifgen\""
files = [
    {file = "nifgen-1.4.9-py3-none-any.whl", hash = "sha256:8d3617aae6ba5f0635eed17d14b2615e01166f62271a6a8124441ee500aee33d"},
    {file = "nifgen-1.4.9.tar.gz", hash = "sha256:900f1ba20d2db643dd7c5ae04bbdff921d84e5fdf9baed0bbe4931e0cce1487d"},
]

[package.dependencies]
grpcio = {version = ">=1.59.0,<2.0", optional = true, markers = "extra == \"grpc\""}
hightime = ">=0.2.0"
nitclk = "*"
protobuf = {version = ">=4.21.6", optional = true, markers = "extra == \"grpc\""}

[package.extras]
grpc = ["grpcio (>=1.59.0,<2.0)", "protobuf (>=4.21.6)"]

[[package]]
name = "niscope"
version = "1.4.9"
description = "NI-SCOPE Python API"
optional = true
python-versions = ">=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"niscope\""
files = [
    {file = "niscope-1.4.9-py3-none-any.whl", hash = "sha256:0b03f1e665ef22ba614defc476149500bc6ddf20e64534476d7496b4f58b30c0"},
    {file = "niscope-1.4.9.tar.gz", hash = "sha256:e85493c9d3f707fac1b280352ea2c1cacd71fd733d6faf9a22a05853492fe87a"},
]

[package.dependencies]
grpcio = {version = ">=1.59.0,<2.0", optional = true, markers = "extra == \"grpc\""}
hightime = ">=0.2.0"
nitclk = "*"
protobuf = {version = ">=4.21.6", optional = true, markers = "extra == \"grpc\""}

[package.extras]
grpc = ["grpcio (>=1.59.0,<2.0)", "protobuf (>=4.21.6)"]

[[package]]
name = "niswitch"
version = "1.4.9"
description = "NI-SWITCH Python API"
optional = true
python-versions = ">=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"niswitch\""
files = [
    {file = "niswitch-1.4.9-py3-none-any.whl", hash = "sha256:416c5ececcaa47cfc68ffbc26ba5eaee5369ac68a06afd28c29fc04a75518edf"},
    {file = "niswitch-1.4.9.tar.gz", hash = "sha256:0347702d2f4c83a428b149adef3baf782d53a367b1134aacd75424f17cc4742a"},
]

[package.dependencies]
grpcio = {version = ">=1.59.0,<2.0", optional = true, markers = "extra == \"grpc\""}
hightime = ">=0.2.0"
protobuf = {version = ">=4.21.6", optional = true, markers = "extra == \"grpc\""}

[package.extras]
grpc = ["grpcio (>=1.59.0,<2.0)", "protobuf (>=4.21.6)"]

[[package]]
name = "nitclk"
version = "1.4.9"
description = "NI-TClk Python API"
optional = true
python-versions = ">=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"nidigital\" or extra == \"nifgen\" or extra == \"niscope\""
files = [
    {file = "nitclk-1.4.9-py3-none-any.whl", hash = "sha256:fa62a03fd8a820246f0adebb59f95249ad086dd407dab9102204338343833b45"},
    {file = "nitclk-1.4.9.tar.gz", hash = "sha256:86835d4c8f08411433bd7c6dce26a346eef5120e476510bebdbaeb2700582cf5"},
]

[package.dependencies]
hightime = ">=0.2.0"

[[package]]
name = "nitypes"
version = "1.1.0"
description = "Data types for NI Python APIs"
optional = false
python-versions = "<4.0,>=3.9"
groups = ["main"]
files = [
    {file = "nitypes-1.1.0-py3-none-any.whl", hash = "sha256:b43ac7027e1cceeca7ceffa58f31ffadd03feeb1788ca5cb8f9d105e73893b14"},
    {file = "nitypes-1.1.0.tar.gz", hash = "sha256:f273b5131ef0d5b848c37a0a63452626caf5c2938f7744c324f7991b76fa0b60"},
]

[package.dependencies]
hightime = ">=0.2.2"
numpy = [
    {version = ">=2.1", markers = "python_version >= \"3.13\" and python_version < \"4.0\""},
    {version = ">=1.22", markers = "python_version >= \"3.9\" and python_version < \"3.13\""},
]
typing-extensions = ">=4.13.2"

[[package]]
name = "numpy"
version = "2.2.6"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.10"
groups = ["main", "dev"]
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
version = "2.4.1"
description = "Fundamental package for array computing in Python"
optional = false
python-versions = ">=3.11"
groups = ["main", "dev"]
markers = "python_version >= \"3.11\""
files = [
    {file = "numpy-2.4.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:0cce2a669e3c8ba02ee563c7835f92c153cf02edff1ae05e1823f1dde21b16a5"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:899d2c18024984814ac7e83f8f49d8e8180e2fbe1b2e252f2e7f1d06bea92425"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:09aa8a87e45b55a1c2c205d42e2808849ece5c484b2aab11fecabec3841cafba"},
    {file = "numpy-2.4.1-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:edee228f76ee2dab4579fad6f51f6a305de09d444280109e0f75df247ff21501"},
    {file = "numpy-2.4.1-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a92f227dbcdc9e4c3e193add1a189a9909947d4f8504c576f4a732fd0b54240a"},
    {file = "numpy-2.4.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:538bf4ec353709c765ff75ae616c34d3c3dca1a68312727e8f2676ea644f8509"},
    {file = "numpy-2.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:ac08c63cb7779b85e9d5318e6c3518b424bc1f364ac4cb2c6136f12e5ff2dccc"},
    {file = "numpy-2.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:4f9c360ecef085e5841c539a9a12b883dff005fbd7ce46722f5e9cef52634d82"},
    {file = "numpy-2.4.1-cp311-cp311-win32.whl", hash = "sha256:0f118ce6b972080ba0758c6087c3617b5ba243d806268623dc34216d69099ba0"},
    {file = "numpy-2.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:18e14c4d09d55eef39a6ab5b08406e84bc6869c1e34eef45564804f90b7e0574"},
    {file = "numpy-2.4.1-cp311-cp311-win_arm64.whl", hash = "sha256:6461de5113088b399d655d45c3897fa188766415d0f568f175ab071c8873bd73"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d3703409aac693fa82c0aee023a1ae06a6e9d065dba10f5e8e80f642f1e9d0a2"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7211b95ca365519d3596a1d8688a95874cc94219d417504d9ecb2df99fa7bfa8"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:5adf01965456a664fc727ed69cc71848f28d063217c63e1a0e200a118d5eec9a"},
    {file = "numpy-2.4.1-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:26f0bcd9c79a00e339565b303badc74d3ea2bd6d52191eeca5f95936cad107d0"},
    {file = "numpy-2.4.1-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0093e85df2960d7e4049664b26afc58b03236e967fb942354deef3208857a04c"},
    {file = "numpy-2.4.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7ad270f438cbdd402c364980317fb6b117d9ec5e226fff5b4148dd9aa9fc6e02"},
    {file = "numpy-2.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:297c72b1b98100c2e8f873d5d35fb551fce7040ade83d67dd51d38c8d42a2162"},
    {file = "numpy-2.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:cf6470d91d34bf669f61d515499859fa7a4c2f7c36434afb70e82df7217933f9"},
    {file = "numpy-2.4.1-cp312-cp312-win32.whl", hash = "sha256:b6bcf39112e956594b3331316d90c90c90fb961e39696bda97b89462f5f3943f"},
    {file = "numpy-2.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:e1a27bb1b2dee45a2a53f5ca6ff2d1a7f135287883a1689e930d44d1ff296c87"},
    {file = "numpy-2.4.1-cp312-cp312-win_arm64.whl", hash = "sha256:0e6e8f9d9ecf95399982019c01223dc130542960a12edfa8edd1122dfa66a8a8"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:d797454e37570cfd61143b73b8debd623c3c0952959adb817dd310a483d58a1b"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:82c55962006156aeef1629b953fd359064aa47e4d82cfc8e67f0918f7da3344f"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:71abbea030f2cfc3092a0ff9f8c8fdefdc5e0bf7d9d9c99663538bb0ecdac0b9"},
    {file = "numpy-2.4.1-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:5b55aa56165b17aaf15520beb9cbd33c9039810e0d9643dd4379e44294c7303e"},
    {file = "numpy-2.4.1-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c0faba4a331195bfa96f93dd9dfaa10b2c7aa8cda3a02b7fd635e588fe821bf5"},
    {file = "numpy-2.4.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d3e3087f53e2b4428766b54932644d148613c5a595150533ae7f00dab2f319a8"},
    {file = "numpy-2.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:49e792ec351315e16da54b543db06ca8a86985ab682602d90c60ef4ff4db2a9c"},
    {file = "numpy-2.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:79e9e06c4c2379db47f3f6fc7a8652e7498251789bf8ff5bd43bf478ef314ca2"},
    {file = "numpy-2.4.1-cp313-cp313-win32.whl", hash = "sha256:3d1a100e48cb266090a031397863ff8a30050ceefd798f686ff92c67a486753d"},
    {file = "numpy-2.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:92a0e65272fd60bfa0d9278e0484c2f52fe03b97aedc02b357f33fe752c52ffb"},
    {file = "numpy-2.4.1-cp313-cp313-win_arm64.whl", hash = "sha256:20d4649c773f66cc2fc36f663e091f57c3b7655f936a4c681b4250855d1da8f5"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:f93bc6892fe7b0663e5ffa83b61aab510aacffd58c16e012bb9352d489d90cb7"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:178de8f87948163d98a4c9ab5bee4ce6519ca918926ec8df195af582de28544d"},
    {file = "numpy-2.4.1-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:98b35775e03ab7f868908b524fc0a84d38932d8daf7b7e1c3c3a1b6c7a2c9f15"},
    {file = "numpy-2.4.1-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:941c2a93313d030f219f3a71fd3d91a728b82979a5e8034eb2e60d394a2b83f9"},
    {file = "numpy-2.4.1-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:529050522e983e00a6c1c6b67411083630de8b57f65e853d7b03d9281b8694d2"},
    {file = "numpy-2.4.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:2302dc0224c1cbc49bb94f7064f3f923a971bfae45c33870dcbff63a2a550505"},
    {file = "numpy-2.4.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:9171a42fcad32dcf3fa86f0a4faa5e9f8facefdb276f54b8b390d90447cff4e2"},
    {file = "numpy-2.4.1-cp313-cp313t-win32.whl", hash = "sha256:382ad67d99ef49024f11d1ce5dcb5ad8432446e4246a4b014418ba3a1175a1f4"},
    {file = "numpy-2.4.1-cp313-cp313t-win_amd64.whl", hash = "sha256:62fea415f83ad8fdb6c20840578e5fbaf5ddd65e0ec6c3c47eda0f69da172510"},
    {file = "numpy-2.4.1-cp313-cp313t-win_arm64.whl", hash = "sha256:a7870e8c5fc11aef57d6fea4b4085e537a3a60ad2cdd14322ed531fdca68d261"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:3869ea1ee1a1edc16c29bbe3a2f2a4e515cc3a44d43903ad41e0cacdbaf733dc"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:e867df947d427cdd7a60e3e271729090b0f0df80f5f10ab7dd436f40811699c3"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:e3bd2cb07841166420d2fa7146c96ce00cb3410664cbc1a6be028e456c4ee220"},
    {file = "numpy-2.4.1-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:f0a90aba7d521e6954670550e561a4cb925713bd944445dbe9e729b71f6cabee"},
    {file = "numpy-2.4.1-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5d558123217a83b2d1ba316b986e9248a1ed1971ad495963d555ccd75dcb1556"},
    {file = "numpy-2.4.1-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:2f44de05659b67d20499cbc96d49f2650769afcb398b79b324bb6e297bfe3844"},
    {file = "numpy-2.4.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:69e7419c9012c4aaf695109564e3387f1259f001b4326dfa55907b098af082d3"},
    {file = "numpy-2.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2ffd257026eb1b34352e749d7cc1678b5eeec3e329ad8c9965a797e08ccba205"},
    {file = "numpy-2.4.1-cp314-cp314-win32.whl", hash = "sha256:727c6c3275ddefa0dc078524a85e064c057b4f4e71ca5ca29a19163c607be745"},
    {file = "numpy-2.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:7d5d7999df434a038d75a748275cd6c0094b0ecdb0837342b332a82defc4dc4d"},
    {file = "numpy-2.4.1-cp314-cp314-win_arm64.whl", hash = "sha256:ce9ce141a505053b3c7bce3216071f3bf5c182b8b28930f14cd24d43932cd2df"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:4e53170557d37ae404bf8d542ca5b7c629d6efa1117dac6a83e394142ea0a43f"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:a73044b752f5d34d4232f25f18160a1cc418ea4507f5f11e299d8ac36875f8a0"},
    {file = "numpy-2.4.1-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:fb1461c99de4d040666ca0444057b06541e5642f800b71c56e6ea92d6a853a0c"},
    {file = "numpy-2.4.1-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:423797bdab2eeefbe608d7c1ec7b2b4fd3c58d51460f1ee26c7500a1d9c9ee93"},
    {file = "numpy-2.4.1-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:52b5f61bdb323b566b528899cc7db2ba5d1015bda7ea811a8bcf3c89c331fa42"},
    {file = "numpy-2.4.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:42d7dd5fa36d16d52a84f821eb96031836fd405ee6955dd732f2023724d0aa01"},
    {file = "numpy-2.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:e7b6b5e28bbd47b7532698e5db2fe1db693d84b58c254e4389d99a27bb9b8f6b"},
    {file = "numpy-2.4.1-cp314-cp314t-win32.whl", hash = "sha256:5de60946f14ebe15e713a6f22850c2372fa72f4ff9a432ab44aa90edcadaa65a"},
    {file = "numpy-2.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:8f085da926c0d491ffff3096f91078cc97ea67e7e6b65e490bc8dcda65663be2"},
    {file = "numpy-2.4.1-cp314-cp314t-win_arm64.whl", hash = "sha256:6436cffb4f2bf26c974344439439c95e152c9a527013f26b3577be6c2ca64295"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_10_15_x86_64.whl", hash = "sha256:8ad35f20be147a204e28b6a0575fbf3540c5e5f802634d4258d55b1ff5facce1"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:8097529164c0f3e32bb89412a0905d9100bf434d9692d9fc275e18dcf53c9344"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_14_0_arm64.whl", hash = "sha256:ea66d2b41ca4a1630aae5507ee0a71647d3124d1741980138aa8f28f44dac36e"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-macosx_14_0_x86_64.whl", hash = "sha256:d3f8f0df9f4b8be57b3bf74a1d087fec68f927a2fab68231fdb442bf2c12e426"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2023ef86243690c2791fd6353e5b4848eedaa88ca8a2d129f462049f6d484696"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8361ea4220d763e54cff2fbe7d8c93526b744f7cd9ddab47afeff7e14e8503be"},
    {file = "numpy-2.4.1-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:4f1b68ff47680c2925f8063402a693ede215f0257f02596b1318ecdfb1d79e33"},
    {file = "numpy-2.4.1.tar.gz", hash = "sha256:a1ceafc5042451a858231588a104093474c6a5c57dcc724841f5c888d237d690"},
]

[[package]]
name = "packaging"
version = "26.0"
description = "Core utilities for Python packages"
optional = false
python-versions = ">=3.8"
groups = ["main", "dev", "docs"]
files = [
    {file = "packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529"},
    {file = "packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4"},
]

[[package]]
name = "pathspec"
version = "1.0.3"
description = "Utility library for gitignore style pattern matching of file paths."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
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
groups = ["dev"]
files = [
    {file = "pep8_naming-0.15.1-py3-none-any.whl", hash = "sha256:eb63925e7fd9e028c7f7ee7b1e413ec03d1ee5de0e627012102ee0222c273c86"},
    {file = "pep8_naming-0.15.1.tar.gz", hash = "sha256:f6f4a499aba2deeda93c1f26ccc02f3da32b035c8b2db9696b730ef2c9639d29"},
]

[package.dependencies]
flake8 = ">=5.0.0"

[[package]]
name = "platformdirs"
version = "4.9.6"
description = "A small Python package for determining appropriate platform-specific dirs, e.g. a `user data dir`."
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "platformdirs-4.9.6-py3-none-any.whl", hash = "sha256:e61adb1d5e5cb3441b4b7710bea7e4c12250ca49439228cc1021c00dcfac0917"},
    {file = "platformdirs-4.9.6.tar.gz", hash = "sha256:3bfa75b0ad0db84096ae777218481852c0ebc6c727b3168c1b9e0118e458cf0a"},
]

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
name = "protobuf"
version = "4.25.9"
description = ""
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
markers = "python_version <= \"3.12\""
files = [
    {file = "protobuf-4.25.9-cp310-abi3-win32.whl", hash = "sha256:bde396f568b0b46fc8fbfe9f02facf25b6755b2578a3b8ac61e74b9d69499e03"},
    {file = "protobuf-4.25.9-cp310-abi3-win_amd64.whl", hash = "sha256:3683c05154252206f7cb2d371626514b3708199d9bcf683b503dabf3a2e38e06"},
    {file = "protobuf-4.25.9-cp37-abi3-macosx_10_9_universal2.whl", hash = "sha256:9560813560e6ee72c11ca8873878bdb7ee003c96a57ebb013245fe84e2540904"},
    {file = "protobuf-4.25.9-cp37-abi3-manylinux2014_aarch64.whl", hash = "sha256:999146ef02e7fa6a692477badd1528bcd7268df211852a3df2d834ba2b480791"},
    {file = "protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl", hash = "sha256:438c636de8fb706a0de94a12a268ef1ae8f5ba5ae655a7671fcda5968ba3c9be"},
    {file = "protobuf-4.25.9-cp38-cp38-win32.whl", hash = "sha256:7f7c1abcea3fc215918fba67a2d2a80fbcccc0f84159610eb187e9bbe6f939ee"},
    {file = "protobuf-4.25.9-cp38-cp38-win_amd64.whl", hash = "sha256:79faf4e5a80b231d94dcf3a0a2917ccbacf0f586f12c9b9c91794b41b913a853"},
    {file = "protobuf-4.25.9-cp39-cp39-win32.whl", hash = "sha256:9481e80e8cffb1c492c68e7c4e6726f4ad02eebc4fa97ead7beebeaa3639511d"},
    {file = "protobuf-4.25.9-cp39-cp39-win_amd64.whl", hash = "sha256:b1d467352de666dc1b6d5740b6319d9c08cab7b21b452501e4ee5b0ac5156780"},
    {file = "protobuf-4.25.9-py3-none-any.whl", hash = "sha256:d49b615e7c935194ac161f0965699ac84df6112c378e05ec53da65d2e4cbb6d4"},
    {file = "protobuf-4.25.9.tar.gz", hash = "sha256:b0dc7e7c68de8b1ce831dacb12fb407e838edbb8b6cc0dc3a2a6b4cbf6de9cff"},
]

[[package]]
name = "protobuf"
version = "5.29.6"
description = ""
optional = false
python-versions = ">=3.8"
groups = ["main", "dev"]
markers = "python_version == \"3.13\""
files = [
    {file = "protobuf-5.29.6-cp310-abi3-win32.whl", hash = "sha256:62e8a3114992c7c647bce37dcc93647575fc52d50e48de30c6fcb28a6a291eb1"},
    {file = "protobuf-5.29.6-cp310-abi3-win_amd64.whl", hash = "sha256:7e6ad413275be172f67fdee0f43484b6de5a904cc1c3ea9804cb6fe2ff366eda"},
    {file = "protobuf-5.29.6-cp38-abi3-macosx_10_9_universal2.whl", hash = "sha256:b5a169e664b4057183a34bdc424540e86eea47560f3c123a0d64de4e137f9269"},
    {file = "protobuf-5.29.6-cp38-abi3-manylinux2014_aarch64.whl", hash = "sha256:a8866b2cff111f0f863c1b3b9e7572dc7eaea23a7fae27f6fc613304046483e6"},
    {file = "protobuf-5.29.6-cp38-abi3-manylinux2014_x86_64.whl", hash = "sha256:e3387f44798ac1106af0233c04fb8abf543772ff241169946f698b3a9a3d3ab9"},
    {file = "protobuf-5.29.6-cp38-cp38-win32.whl", hash = "sha256:36ade6ff88212e91aef4e687a971a11d7d24d6948a66751abc1b3238648f5d05"},
    {file = "protobuf-5.29.6-cp38-cp38-win_amd64.whl", hash = "sha256:831e2da16b6cc9d8f1654c041dd594eda43391affd3c03a91bea7f7f6da106d6"},
    {file = "protobuf-5.29.6-cp39-cp39-win32.whl", hash = "sha256:cb4c86de9cd8a7f3a256b9744220d87b847371c6b2f10bde87768918ef33ba49"},
    {file = "protobuf-5.29.6-cp39-cp39-win_amd64.whl", hash = "sha256:76e07e6567f8baf827137e8d5b8204b6c7b6488bbbff1bf0a72b383f77999c18"},
    {file = "protobuf-5.29.6-py3-none-any.whl", hash = "sha256:6b9edb641441b2da9fa8f428760fc136a49cf97a52076010cf22a2ff73438a86"},
    {file = "protobuf-5.29.6.tar.gz", hash = "sha256:da9ee6a5424b6b30fd5e45c5ea663aef540ca95f9ad99d1e887e819cdf9b8723"},
]

[[package]]
name = "protobuf"
version = "6.33.6"
description = ""
optional = false
python-versions = ">=3.9"
groups = ["main", "dev"]
markers = "python_version >= \"3.14\""
files = [
    {file = "protobuf-6.33.6-cp310-abi3-win32.whl", hash = "sha256:7d29d9b65f8afef196f8334e80d6bc1d5d4adedb449971fefd3723824e6e77d3"},
    {file = "protobuf-6.33.6-cp310-abi3-win_amd64.whl", hash = "sha256:0cd27b587afca21b7cfa59a74dcbd48a50f0a6400cfb59391340ad729d91d326"},
    {file = "protobuf-6.33.6-cp39-abi3-macosx_10_9_universal2.whl", hash = "sha256:9720e6961b251bde64edfdab7d500725a2af5280f3f4c87e57c0208376aa8c3a"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_aarch64.whl", hash = "sha256:e2afbae9b8e1825e3529f88d514754e094278bb95eadc0e199751cdd9a2e82a2"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_s390x.whl", hash = "sha256:c96c37eec15086b79762ed265d59ab204dabc53056e3443e702d2681f4b39ce3"},
    {file = "protobuf-6.33.6-cp39-abi3-manylinux2014_x86_64.whl", hash = "sha256:e9db7e292e0ab79dd108d7f1a94fe31601ce1ee3f7b79e0692043423020b0593"},
    {file = "protobuf-6.33.6-cp39-cp39-win32.whl", hash = "sha256:bd56799fb262994b2c2faa1799693c95cc2e22c62f56fb43af311cae45d26f0e"},
    {file = "protobuf-6.33.6-cp39-cp39-win_amd64.whl", hash = "sha256:f443a394af5ed23672bc6c486be138628fbe5c651ccbc536873d7da23d1868cf"},
    {file = "protobuf-6.33.6-py3-none-any.whl", hash = "sha256:77179e006c476e69bf8e8ce866640091ec42e1beb80b213c3900006ecfba6901"},
    {file = "protobuf-6.33.6.tar.gz", hash = "sha256:a6768d25248312c297558af96a9f9c929e8c4cee0659cb07e780731095f38135"},
]

[[package]]
name = "psutil"
version = "7.2.2"
description = "Cross-platform lib for process and system monitoring."
optional = false
python-versions = ">=3.6"
groups = ["dev"]
files = [
    {file = "psutil-7.2.2-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:2edccc433cbfa046b980b0df0171cd25bcaeb3a68fe9022db0979e7aa74a826b"},
    {file = "psutil-7.2.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:e78c8603dcd9a04c7364f1a3e670cea95d51ee865e4efb3556a3a63adef958ea"},
    {file = "psutil-7.2.2-cp313-cp313t-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1a571f2330c966c62aeda00dd24620425d4b0cc86881c89861fbc04549e5dc63"},
    {file = "psutil-7.2.2-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:917e891983ca3c1887b4ef36447b1e0873e70c933afc831c6b6da078ba474312"},
    {file = "psutil-7.2.2-cp313-cp313t-win_amd64.whl", hash = "sha256:ab486563df44c17f5173621c7b198955bd6b613fb87c71c161f827d3fb149a9b"},
    {file = "psutil-7.2.2-cp313-cp313t-win_arm64.whl", hash = "sha256:ae0aefdd8796a7737eccea863f80f81e468a1e4cf14d926bd9b6f5f2d5f90ca9"},
    {file = "psutil-7.2.2-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:eed63d3b4d62449571547b60578c5b2c4bcccc5387148db46e0c2313dad0ee00"},
    {file = "psutil-7.2.2-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7b6d09433a10592ce39b13d7be5a54fbac1d1228ed29abc880fb23df7cb694c9"},
    {file = "psutil-7.2.2-cp314-cp314t-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1fa4ecf83bcdf6e6c8f4449aff98eefb5d0604bf88cb883d7da3d8d2d909546a"},
    {file = "psutil-7.2.2-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e452c464a02e7dc7822a05d25db4cde564444a67e58539a00f929c51eddda0cf"},
    {file = "psutil-7.2.2-cp314-cp314t-win_amd64.whl", hash = "sha256:c7663d4e37f13e884d13994247449e9f8f574bc4655d509c3b95e9ec9e2b9dc1"},
    {file = "psutil-7.2.2-cp314-cp314t-win_arm64.whl", hash = "sha256:11fe5a4f613759764e79c65cf11ebdf26e33d6dd34336f8a337aa2996d71c841"},
    {file = "psutil-7.2.2-cp36-abi3-macosx_10_9_x86_64.whl", hash = "sha256:ed0cace939114f62738d808fdcecd4c869222507e266e574799e9c0faa17d486"},
    {file = "psutil-7.2.2-cp36-abi3-macosx_11_0_arm64.whl", hash = "sha256:1a7b04c10f32cc88ab39cbf606e117fd74721c831c98a27dc04578deb0c16979"},
    {file = "psutil-7.2.2-cp36-abi3-manylinux2010_x86_64.manylinux_2_12_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:076a2d2f923fd4821644f5ba89f059523da90dc9014e85f8e45a5774ca5bc6f9"},
    {file = "psutil-7.2.2-cp36-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b0726cecd84f9474419d67252add4ac0cd9811b04d61123054b9fb6f57df6e9e"},
    {file = "psutil-7.2.2-cp36-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:fd04ef36b4a6d599bbdb225dd1d3f51e00105f6d48a28f006da7f9822f2606d8"},
    {file = "psutil-7.2.2-cp36-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:b58fabe35e80b264a4e3bb23e6b96f9e45a3df7fb7eed419ac0e5947c61e47cc"},
    {file = "psutil-7.2.2-cp37-abi3-win_amd64.whl", hash = "sha256:eb7e81434c8d223ec4a219b5fc1c47d0417b12be7ea866e24fb5ad6e84b3d988"},
    {file = "psutil-7.2.2-cp37-abi3-win_arm64.whl", hash = "sha256:8c233660f575a5a89e6d4cb65d9f938126312bca76d8fe087b947b3a1aaac9ee"},
    {file = "psutil-7.2.2.tar.gz", hash = "sha256:0746f5f8d406af344fd547f1c8daa5f5c33dbc293bb8d6a16d80b4bb88f59372"},
]

[package.extras]
dev = ["abi3audit", "black", "check-manifest", "colorama ; os_name == \"nt\"", "coverage", "packaging", "psleak", "pylint", "pyperf", "pypinfo", "pyreadline3 ; os_name == \"nt\"", "pytest", "pytest-cov", "pytest-instafail", "pytest-xdist", "pywin32 ; os_name == \"nt\" and implementation_name != \"pypy\"", "requests", "rstcheck", "ruff", "setuptools", "sphinx", "sphinx_rtd_theme", "toml-sort", "twine", "validate-pyproject[all]", "virtualenv", "vulture", "wheel", "wheel ; os_name == \"nt\" and implementation_name != \"pypy\"", "wmi ; os_name == \"nt\" and implementation_name != \"pypy\""]
test = ["psleak", "pytest", "pytest-instafail", "pytest-xdist", "pywin32 ; os_name == \"nt\" and implementation_name != \"pypy\"", "setuptools", "wheel ; os_name == \"nt\" and implementation_name != \"pypy\"", "wmi ; os_name == \"nt\" and implementation_name != \"pypy\""]

[[package]]
name = "pycodestyle"
version = "2.9.1"
description = "Python style guide checker"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
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
groups = ["dev"]
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
version = "2.5.0"
description = "passive checker of Python programs"
optional = false
python-versions = ">=3.6"
groups = ["dev"]
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
groups = ["dev"]
markers = "python_version >= \"3.12\""
files = [
    {file = "pyflakes-3.1.0-py2.py3-none-any.whl", hash = "sha256:4132f6d49cb4dae6819e5379898f2b8cce3c5f23994194c24b77d5da2e36f774"},
    {file = "pyflakes-3.1.0.tar.gz", hash = "sha256:a0aae034c444db0071aa077972ba4768d40c830d9539fd45bf4cd3f8f6992efc"},
]

[[package]]
name = "pygments"
version = "2.19.2"
description = "Pygments is a syntax highlighting package written in Python."
optional = false
python-versions = ">=3.8"
groups = ["dev", "docs"]
files = [
    {file = "pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b"},
    {file = "pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887"},
]

[package.extras]
windows-terminal = ["colorama (>=0.4.6)"]

[[package]]
name = "pyproject-api"
version = "1.10.0"
description = "API to interact with the python pyproject.toml based projects"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "pyproject_api-1.10.0-py3-none-any.whl", hash = "sha256:8757c41a79c0f4ab71b99abed52b97ecf66bd20b04fa59da43b5840bac105a09"},
    {file = "pyproject_api-1.10.0.tar.gz", hash = "sha256:40c6f2d82eebdc4afee61c773ed208c04c19db4c4a60d97f8d7be3ebc0bbb330"},
]

[package.dependencies]
packaging = ">=25"
tomli = {version = ">=2.3", markers = "python_version < \"3.11\""}

[package.extras]
docs = ["furo (>=2025.9.25)", "sphinx-autodoc-typehints (>=3.5.1)"]
testing = ["covdefaults (>=2.3)", "pytest (>=8.4.2)", "pytest-cov (>=7)", "pytest-mock (>=3.15.1)", "setuptools (>=80.9)"]

[[package]]
name = "pytest"
version = "9.1.1"
description = "pytest: simple powerful testing with Python"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "pytest-9.1.1-py3-none-any.whl", hash = "sha256:37a86b45efb9a47a61a36449063e8e18d0cab3161329fc099eb21783169c4f0c"},
    {file = "pytest-9.1.1.tar.gz", hash = "sha256:1088fbde8f2b49d95a549a195707afa7a76a3ce9bcadc26b6d71f0ffda5fe313"},
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
name = "pytest-cov"
version = "7.1.0"
description = "Pytest plugin for measuring coverage."
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pytest_cov-7.1.0-py3-none-any.whl", hash = "sha256:a0461110b7865f9a271aa1b51e516c9a95de9d696734a2f71e3e78f46e1d4678"},
    {file = "pytest_cov-7.1.0.tar.gz", hash = "sha256:30674f2b5f6351aa09702a9c8c364f6a01c27aae0c1366ae8016160d1efc56b2"},
]

[package.dependencies]
coverage = {version = ">=7.10.6", extras = ["toml"]}
pluggy = ">=1.2"
pytest = ">=7"

[package.extras]
testing = ["process-tests", "pytest-xdist", "virtualenv"]

[[package]]
name = "pytest-mock"
version = "3.15.1"
description = "Thin-wrapper around the mock package for easier use with pytest"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "pytest_mock-3.15.1-py3-none-any.whl", hash = "sha256:0a25e2eb88fe5168d535041d09a4529a188176ae608a6d249ee65abc0949630d"},
    {file = "pytest_mock-3.15.1.tar.gz", hash = "sha256:1849a238f6f396da19762269de72cb1814ab44416fa73a8686deac10b0d87a0f"},
]

[package.dependencies]
pytest = ">=6.2.5"

[package.extras]
dev = ["pre-commit", "pytest-asyncio", "tox"]

[[package]]
name = "python-decouple"
version = "3.8"
description = "Strict separation of settings from code."
optional = false
python-versions = "*"
groups = ["main"]
files = [
    {file = "python-decouple-3.8.tar.gz", hash = "sha256:ba6e2657d4f376ecc46f77a3a615e058d93ba5e465c01bbe57289bfb7cce680f"},
    {file = "python_decouple-3.8-py3-none-any.whl", hash = "sha256:d0d45340815b25f4de59c974b855bb38d03151d81b037d9e3f463b0c9f8cbd66"},
]

[[package]]
name = "python-discovery"
version = "1.2.2"
description = "Python interpreter discovery"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "python_discovery-1.2.2-py3-none-any.whl", hash = "sha256:e1ae95d9af875e78f15e19aed0c6137ab1bb49c200f21f5061786490c9585c7a"},
    {file = "python_discovery-1.2.2.tar.gz", hash = "sha256:876e9c57139eb757cb5878cbdd9ae5379e5d96266c99ef731119e04fffe533bb"},
]

[package.dependencies]
filelock = ">=3.15.4"
platformdirs = ">=4.3.6,<5"

[package.extras]
docs = ["furo (>=2025.12.19)", "sphinx (>=9.1)", "sphinx-autodoc-typehints (>=3.6.3)", "sphinxcontrib-mermaid (>=2)"]
testing = ["covdefaults (>=2.3)", "coverage (>=7.5.4)", "pytest (>=8.3.5)", "pytest-mock (>=3.14)", "setuptools (>=75.1)"]

[[package]]
name = "pytokens"
version = "0.4.0"
description = "A Fast, spec compliant Python 3.14+ tokenizer that runs on older Pythons."
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "pytokens-0.4.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:af0c3166aea367a9e755a283171befb92dd3043858b94ae9b3b7efbe9def26a3"},
    {file = "pytokens-0.4.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:daae524ed14ca459932cbf51d74325bea643701ba8a8b0cc2d10f7cd4b3e2b63"},
    {file = "pytokens-0.4.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e95cb158c44d642ed62f555bf8136bbe780dbd64d2fb0b9169e11ffb944664c3"},
    {file = "pytokens-0.4.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:df58d44630eaf25f587540e94bdf1fc50b4e6d5f212c786de0fb024bfcb8753a"},
    {file = "pytokens-0.4.0-cp310-cp310-win_amd64.whl", hash = "sha256:55efcc36f9a2e0e930cfba0ce7f83445306b02f8326745585ed5551864eba73a"},
    {file = "pytokens-0.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:92eb3ef88f27c22dc9dbab966ace4d61f6826e02ba04dac8e2d65ea31df56c8e"},
    {file = "pytokens-0.4.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f4b77858a680635ee9904306f54b0ee4781effb89e211ba0a773d76539537165"},
    {file = "pytokens-0.4.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:25cacc20c2ad90acb56f3739d87905473c54ca1fa5967ffcd675463fe965865e"},
    {file = "pytokens-0.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:628fab535ebc9079e4db35cd63cb401901c7ce8720a9834f9ad44b9eb4e0f1d4"},
    {file = "pytokens-0.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:4d0f568d7e82b7e96be56d03b5081de40e43c904eb6492bf09aaca47cd55f35b"},
    {file = "pytokens-0.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:cd8da894e5a29ba6b6da8be06a4f7589d7220c099b5e363cb0643234b9b38c2a"},
    {file = "pytokens-0.4.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:237ba7cfb677dbd3b01b09860810aceb448871150566b93cd24501d5734a04b1"},
    {file = "pytokens-0.4.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01d1a61e36812e4e971cfe2c0e4c1f2d66d8311031dac8bf168af8a249fa04dd"},
    {file = "pytokens-0.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:e47e2ef3ec6ee86909e520d79f965f9b23389fda47460303cf715d510a6fe544"},
    {file = "pytokens-0.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:3d36954aba4557fd5a418a03cf595ecbb1cdcce119f91a49b19ef09d691a22ae"},
    {file = "pytokens-0.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:73eff3bdd8ad08da679867992782568db0529b887bed4c85694f84cdf35eafc6"},
    {file = "pytokens-0.4.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d97cc1f91b1a8e8ebccf31c367f28225699bea26592df27141deade771ed0afb"},
    {file = "pytokens-0.4.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a2c8952c537cb73a1a74369501a83b7f9d208c3cf92c41dd88a17814e68d48ce"},
    {file = "pytokens-0.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5dbf56f3c748aed9310b310d5b8b14e2c96d3ad682ad5a943f381bdbbdddf753"},
    {file = "pytokens-0.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:e131804513597f2dff2b18f9911d9b6276e21ef3699abeffc1c087c65a3d975e"},
    {file = "pytokens-0.4.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:0d7374c917197106d3c4761374718bc55ea2e9ac0fb94171588ef5840ee1f016"},
    {file = "pytokens-0.4.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0cd3fa1caf9e47a72ee134a29ca6b5bea84712724bba165d6628baa190c6ea5b"},
    {file = "pytokens-0.4.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9c6986576b7b07fe9791854caa5347923005a80b079d45b63b0be70d50cce5f1"},
    {file = "pytokens-0.4.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:9940f7c2e2f54fb1cb5fe17d0803c54da7a2bf62222704eb4217433664a186a7"},
    {file = "pytokens-0.4.0-cp314-cp314-win_amd64.whl", hash = "sha256:54691cf8f299e7efabcc25adb4ce715d3cef1491e1c930eaf555182f898ef66a"},
    {file = "pytokens-0.4.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:94ff5db97a0d3cd7248a5b07ba2167bd3edc1db92f76c6db00137bbaf068ddf8"},
    {file = "pytokens-0.4.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d0dd6261cd9cc95fae1227b1b6ebee023a5fd4a4b6330b071c73a516f5f59b63"},
    {file = "pytokens-0.4.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0cdca8159df407dbd669145af4171a0d967006e0be25f3b520896bc7068f02c4"},
    {file = "pytokens-0.4.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:4b5770abeb2a24347380a1164a558f0ebe06e98aedbd54c45f7929527a5fb26e"},
    {file = "pytokens-0.4.0-cp314-cp314t-win_amd64.whl", hash = "sha256:74500d72c561dad14c037a9e86a657afd63e277dd5a3bb7570932ab7a3b12551"},
    {file = "pytokens-0.4.0-cp38-cp38-macosx_11_0_arm64.whl", hash = "sha256:e368e0749e4e9d86a6e08763310dc92bc69ad73d9b6db5243b30174c71a8a534"},
    {file = "pytokens-0.4.0-cp38-cp38-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:865cc65c75c8f2e9e0d8330338f649b12bfd9442561900ebaf58c596a72107d2"},
    {file = "pytokens-0.4.0-cp38-cp38-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:dbb9338663b3538f31c4ca7afe4f38d9b9b3a16a8be18a273a5704a1bc7a2367"},
    {file = "pytokens-0.4.0-cp38-cp38-musllinux_1_2_x86_64.whl", hash = "sha256:658f870523ac1a5f4733d7db61ce9af61a0c23b2aeea3d03d1800c93f760e15f"},
    {file = "pytokens-0.4.0-cp38-cp38-win_amd64.whl", hash = "sha256:d69a2491190a74e4b6f87f3b9dfce7a6873de3f3bf330d20083d374380becac0"},
    {file = "pytokens-0.4.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:8cd795191c4127fcb3d7b76d84006a07748c390226f47657869235092eedbc05"},
    {file = "pytokens-0.4.0-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ef2bcbddb73ac18599a86c8c549d5145130f2cd9d83dc2b5482fd8322b7806cd"},
    {file = "pytokens-0.4.0-cp39-cp39-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:06ac081c1187389762b58823d90d6339e6880ce0df912f71fb9022d81d7fd429"},
    {file = "pytokens-0.4.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:278129d54573efdc79e75c6082e73ebd19858e22a2e848359f93629323186ca6"},
    {file = "pytokens-0.4.0-cp39-cp39-win_amd64.whl", hash = "sha256:9380fb6d96fa5ab83ed606ebad27b6171930cc14a8a8d215f6adb187ba428690"},
    {file = "pytokens-0.4.0-py3-none-any.whl", hash = "sha256:0508d11b4de157ee12063901603be87fb0253e8f4cb9305eb168b1202ab92068"},
    {file = "pytokens-0.4.0.tar.gz", hash = "sha256:6b0b03e6ea7c9f9d47c5c61164b69ad30f4f0d70a5d9fe7eac4d19f24f77af2d"},
]

[package.extras]
dev = ["black", "build", "mypy", "pytest", "pytest-cov", "setuptools", "tox", "twine", "wheel"]

[[package]]
name = "pywin32"
version = "311"
description = "Python for Window Extensions"
optional = false
python-versions = "*"
groups = ["main"]
markers = "sys_platform == \"win32\""
files = [
    {file = "pywin32-311-cp310-cp310-win32.whl", hash = "sha256:d03ff496d2a0cd4a5893504789d4a15399133fe82517455e78bad62efbb7f0a3"},
    {file = "pywin32-311-cp310-cp310-win_amd64.whl", hash = "sha256:797c2772017851984b97180b0bebe4b620bb86328e8a884bb626156295a63b3b"},
    {file = "pywin32-311-cp310-cp310-win_arm64.whl", hash = "sha256:0502d1facf1fed4839a9a51ccbcc63d952cf318f78ffc00a7e78528ac27d7a2b"},
    {file = "pywin32-311-cp311-cp311-win32.whl", hash = "sha256:184eb5e436dea364dcd3d2316d577d625c0351bf237c4e9a5fabbcfa5a58b151"},
    {file = "pywin32-311-cp311-cp311-win_amd64.whl", hash = "sha256:3ce80b34b22b17ccbd937a6e78e7225d80c52f5ab9940fe0506a1a16f3dab503"},
    {file = "pywin32-311-cp311-cp311-win_arm64.whl", hash = "sha256:a733f1388e1a842abb67ffa8e7aad0e70ac519e09b0f6a784e65a136ec7cefd2"},
    {file = "pywin32-311-cp312-cp312-win32.whl", hash = "sha256:750ec6e621af2b948540032557b10a2d43b0cee2ae9758c54154d711cc852d31"},
    {file = "pywin32-311-cp312-cp312-win_amd64.whl", hash = "sha256:b8c095edad5c211ff31c05223658e71bf7116daa0ecf3ad85f3201ea3190d067"},
    {file = "pywin32-311-cp312-cp312-win_arm64.whl", hash = "sha256:e286f46a9a39c4a18b319c28f59b61de793654af2f395c102b4f819e584b5852"},
    {file = "pywin32-311-cp313-cp313-win32.whl", hash = "sha256:f95ba5a847cba10dd8c4d8fefa9f2a6cf283b8b88ed6178fa8a6c1ab16054d0d"},
    {file = "pywin32-311-cp313-cp313-win_amd64.whl", hash = "sha256:718a38f7e5b058e76aee1c56ddd06908116d35147e133427e59a3983f703a20d"},
    {file = "pywin32-311-cp313-cp313-win_arm64.whl", hash = "sha256:7b4075d959648406202d92a2310cb990fea19b535c7f4a78d3f5e10b926eeb8a"},
    {file = "pywin32-311-cp314-cp314-win32.whl", hash = "sha256:b7a2c10b93f8986666d0c803ee19b5990885872a7de910fc460f9b0c2fbf92ee"},
    {file = "pywin32-311-cp314-cp314-win_amd64.whl", hash = "sha256:3aca44c046bd2ed8c90de9cb8427f581c479e594e99b5c0bb19b29c10fd6cb87"},
    {file = "pywin32-311-cp314-cp314-win_arm64.whl", hash = "sha256:a508e2d9025764a8270f93111a970e1d0fbfc33f4153b388bb649b7eec4f9b42"},
    {file = "pywin32-311-cp38-cp38-win32.whl", hash = "sha256:6c6f2969607b5023b0d9ce2541f8d2cbb01c4f46bc87456017cf63b73f1e2d8c"},
    {file = "pywin32-311-cp38-cp38-win_amd64.whl", hash = "sha256:c8015b09fb9a5e188f83b7b04de91ddca4658cee2ae6f3bc483f0b21a77ef6cd"},
    {file = "pywin32-311-cp39-cp39-win32.whl", hash = "sha256:aba8f82d551a942cb20d4a83413ccbac30790b50efb89a75e4f586ac0bb8056b"},
    {file = "pywin32-311-cp39-cp39-win_amd64.whl", hash = "sha256:e0c4cfb0621281fe40387df582097fd796e80430597cb9944f0ae70447bacd91"},
    {file = "pywin32-311-cp39-cp39-win_arm64.whl", hash = "sha256:62ea666235135fee79bb154e695f3ff67370afefd71bd7fea7512fc70ef31e3d"},
]

[[package]]
name = "pyyaml"
version = "6.0.3"
description = "YAML parser and emitter for Python"
optional = false
python-versions = ">=3.8"
groups = ["dev", "docs"]
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
version = "2.32.5"
description = "Python HTTP for Humans."
optional = false
python-versions = ">=3.9"
groups = ["main", "docs"]
files = [
    {file = "requests-2.32.5-py3-none-any.whl", hash = "sha256:2462f94637a34fd532264295e186976db0f5d453d1cdd31473c85a6a161affb6"},
    {file = "requests-2.32.5.tar.gz", hash = "sha256:dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf"},
]
markers = {main = "extra == \"drivers\" or extra == \"nidaqmx\""}

[package.dependencies]
certifi = ">=2017.4.17"
charset_normalizer = ">=2,<4"
idna = ">=2.5,<4"
urllib3 = ">=1.21.1,<3"

[package.extras]
socks = ["PySocks (>=1.5.6,!=1.5.7)"]
use-chardet-on-py3 = ["chardet (>=3.0.2,<6)"]

[[package]]
name = "rich"
version = "14.3.1"
description = "Render rich text, tables, progress bars, syntax highlighting, markdown and more to the terminal"
optional = false
python-versions = ">=3.8.0"
groups = ["dev"]
files = [
    {file = "rich-14.3.1-py3-none-any.whl", hash = "sha256:da750b1aebbff0b372557426fb3f35ba56de8ef954b3190315eb64076d6fb54e"},
    {file = "rich-14.3.1.tar.gz", hash = "sha256:b8c5f568a3a749f9290ec6bddedf835cec33696bfc1e48bcfecb276c7386e4b8"},
]

[package.dependencies]
markdown-it-py = ">=2.2.0"
pygments = ">=2.13.0,<3.0.0"

[package.extras]
jupyter = ["ipywidgets (>=7.5.1,<9)"]

[[package]]
name = "roman-numerals"
version = "4.1.0"
description = "Manipulate well-formed Roman numerals"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
markers = "python_version >= \"3.11\""
files = [
    {file = "roman_numerals-4.1.0-py3-none-any.whl", hash = "sha256:647ba99caddc2cc1e55a51e4360689115551bf4476d90e8162cf8c345fe233c7"},
    {file = "roman_numerals-4.1.0.tar.gz", hash = "sha256:1af8b147eb1405d5839e78aeb93131690495fe9da5c91856cb33ad55a7f1e5b2"},
]

[[package]]
name = "setuptools"
version = "80.10.1"
description = "Easily download, build, install, upgrade, and uninstall Python packages"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "setuptools-80.10.1-py3-none-any.whl", hash = "sha256:fc30c51cbcb8199a219c12cc9c281b5925a4978d212f84229c909636d9f6984e"},
    {file = "setuptools-80.10.1.tar.gz", hash = "sha256:bf2e513eb8144c3298a3bd28ab1a5edb739131ec5c22e045ff93cd7f5319703a"},
]

[package.extras]
check = ["pytest-checkdocs (>=2.4)", "pytest-ruff (>=0.2.1) ; sys_platform != \"cygwin\"", "ruff (>=0.8.0) ; sys_platform != \"cygwin\""]
core = ["importlib_metadata (>=6) ; python_version < \"3.10\"", "jaraco.functools (>=4)", "jaraco.text (>=3.7)", "more_itertools", "more_itertools (>=8.8)", "packaging (>=24.2)", "platformdirs (>=4.2.2)", "tomli (>=2.0.1) ; python_version < \"3.11\"", "wheel (>=0.43.0)"]
cover = ["pytest-cov"]
doc = ["furo", "jaraco.packaging (>=9.3)", "jaraco.tidelift (>=1.4)", "pygments-github-lexers (==0.0.5)", "pyproject-hooks (!=1.1)", "rst.linker (>=1.9)", "sphinx (>=3.5)", "sphinx-favicon", "sphinx-inline-tabs", "sphinx-lint", "sphinx-notfound-page (>=1,<2)", "sphinx-reredirects", "sphinxcontrib-towncrier", "towncrier (<24.7)"]
enabler = ["pytest-enabler (>=2.2)"]
test = ["build[virtualenv] (>=1.0.3)", "filelock (>=3.4.0)", "ini2toml[lite] (>=0.14)", "jaraco.develop (>=7.21) ; python_version >= \"3.9\" and sys_platform != \"cygwin\"", "jaraco.envs (>=2.2)", "jaraco.path (>=3.7.2)", "jaraco.test (>=5.5)", "packaging (>=24.2)", "pip (>=19.1)", "pyobjc (<12) ; sys_platform == \"darwin\" and python_version <= \"3.9\"", "pyproject-hooks (!=1.1)", "pytest (>=6,!=8.1.*)", "pytest-home (>=0.5)", "pytest-perf ; sys_platform != \"cygwin\"", "pytest-subprocess", "pytest-timeout", "pytest-xdist (>=3)", "tomli-w (>=1.0.0)", "virtualenv (>=13.0.0)", "wheel (>=0.44.0)"]
type = ["importlib_metadata (>=7.0.2) ; python_version < \"3.10\"", "jaraco.develop (>=7.21) ; sys_platform != \"cygwin\"", "mypy (==1.14.*)", "pytest-mypy"]

[[package]]
name = "snowballstemmer"
version = "3.0.1"
description = "This package provides 32 stemmers for 30 languages generated from Snowball algorithms."
optional = false
python-versions = "!=3.0.*,!=3.1.*,!=3.2.*"
groups = ["dev", "docs"]
files = [
    {file = "snowballstemmer-3.0.1-py3-none-any.whl", hash = "sha256:6cd7b3897da8d6c9ffb968a6781fa6532dce9c3618a4b127d920dab764a19064"},
    {file = "snowballstemmer-3.0.1.tar.gz", hash = "sha256:6d5eeeec8e9f84d4d56b847692bacf79bc2c8e90c7f80ca4444ff8b6f2e52895"},
]

[[package]]
name = "sphinx"
version = "7.4.7"
description = "Python documentation generator"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
markers = "python_version == \"3.10\""
files = [
    {file = "sphinx-7.4.7-py3-none-any.whl", hash = "sha256:c2419e2135d11f1951cd994d6eb18a1835bd8fdd8429f9ca375dc1f3281bd239"},
    {file = "sphinx-7.4.7.tar.gz", hash = "sha256:242f92a7ea7e6c5b406fdc2615413890ba9f699114a9c09192d7dfead2ee9cfe"},
]

[package.dependencies]
alabaster = ">=0.7.14,<0.8.0"
babel = ">=2.13"
colorama = {version = ">=0.4.6", markers = "sys_platform == \"win32\""}
docutils = ">=0.20,<0.22"
imagesize = ">=1.3"
Jinja2 = ">=3.1"
packaging = ">=23.0"
Pygments = ">=2.17"
requests = ">=2.30.0"
snowballstemmer = ">=2.2"
sphinxcontrib-applehelp = "*"
sphinxcontrib-devhelp = "*"
sphinxcontrib-htmlhelp = ">=2.0.0"
sphinxcontrib-jsmath = "*"
sphinxcontrib-qthelp = "*"
sphinxcontrib-serializinghtml = ">=1.1.9"
tomli = {version = ">=2", markers = "python_version < \"3.11\""}

[package.extras]
docs = ["sphinxcontrib-websupport"]
lint = ["flake8 (>=6.0)", "importlib-metadata (>=6.0)", "mypy (==1.10.1)", "pytest (>=6.0)", "ruff (==0.5.2)", "sphinx-lint (>=0.9)", "tomli (>=2)", "types-docutils (==0.21.0.20240711)", "types-requests (>=2.30.0)"]
test = ["cython (>=3.0)", "defusedxml (>=0.7.1)", "pytest (>=8.0)", "setuptools (>=70.0)", "typing_extensions (>=4.9)"]

[[package]]
name = "sphinx"
version = "9.0.4"
description = "Python documentation generator"
optional = false
python-versions = ">=3.11"
groups = ["docs"]
markers = "python_version == \"3.11\""
files = [
    {file = "sphinx-9.0.4-py3-none-any.whl", hash = "sha256:5bebc595a5e943ea248b99c13814c1c5e10b3ece718976824ffa7959ff95fffb"},
    {file = "sphinx-9.0.4.tar.gz", hash = "sha256:594ef59d042972abbc581d8baa577404abe4e6c3b04ef61bd7fc2acbd51f3fa3"},
]

[package.dependencies]
alabaster = ">=0.7.14"
babel = ">=2.13"
colorama = {version = ">=0.4.6", markers = "sys_platform == \"win32\""}
docutils = ">=0.20,<0.23"
imagesize = ">=1.3"
Jinja2 = ">=3.1"
packaging = ">=23.0"
Pygments = ">=2.17"
requests = ">=2.30.0"
roman-numerals = ">=1.0.0"
snowballstemmer = ">=2.2"
sphinxcontrib-applehelp = ">=1.0.7"
sphinxcontrib-devhelp = ">=1.0.6"
sphinxcontrib-htmlhelp = ">=2.0.6"
sphinxcontrib-jsmath = ">=1.0.1"
sphinxcontrib-qthelp = ">=1.0.6"
sphinxcontrib-serializinghtml = ">=1.1.9"

[[package]]
name = "sphinx"
version = "9.1.0"
description = "Python documentation generator"
optional = false
python-versions = ">=3.12"
groups = ["docs"]
markers = "python_version >= \"3.12\""
files = [
    {file = "sphinx-9.1.0-py3-none-any.whl", hash = "sha256:c84fdd4e782504495fe4f2c0b3413d6c2bf388589bb352d439b2a3bb99991978"},
    {file = "sphinx-9.1.0.tar.gz", hash = "sha256:7741722357dd75f8190766926071fed3bdc211c74dd2d7d4df5404da95930ddb"},
]

[package.dependencies]
alabaster = ">=0.7.14"
babel = ">=2.13"
colorama = {version = ">=0.4.6", markers = "sys_platform == \"win32\""}
docutils = ">=0.21,<0.23"
imagesize = ">=1.3"
Jinja2 = ">=3.1"
packaging = ">=23.0"
Pygments = ">=2.17"
requests = ">=2.30.0"
roman-numerals = ">=1.0.0"
snowballstemmer = ">=2.2"
sphinxcontrib-applehelp = ">=1.0.7"
sphinxcontrib-devhelp = ">=1.0.6"
sphinxcontrib-htmlhelp = ">=2.0.6"
sphinxcontrib-jsmath = ">=1.0.1"
sphinxcontrib-qthelp = ">=1.0.6"
sphinxcontrib-serializinghtml = ">=1.1.9"

[[package]]
name = "sphinx-autoapi"
version = "3.8.0"
description = "Sphinx API documentation generator"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
files = [
    {file = "sphinx_autoapi-3.8.0-py3-none-any.whl", hash = "sha256:245aefdeab85609ae4aa3576b0d99f69676aa6333dda438761bd125755b3c42d"},
    {file = "sphinx_autoapi-3.8.0.tar.gz", hash = "sha256:9f8ac7d43baf28a0831ac0e392fab6a095b875af07e52d135a5f716cc3cf1142"},
]

[package.dependencies]
astroid = ">=3.0"
Jinja2 = "*"
PyYAML = "*"
sphinx = ">=7.4.0"

[[package]]
name = "sphinx-click"
version = "6.2.0"
description = "Sphinx extension that automatically documents click applications"
optional = false
python-versions = ">=3.10"
groups = ["docs"]
files = [
    {file = "sphinx_click-6.2.0-py3-none-any.whl", hash = "sha256:1fb1851cb4f2c286d43cbcd57f55db6ef5a8d208bfc3370f19adde232e5803d7"},
    {file = "sphinx_click-6.2.0.tar.gz", hash = "sha256:fc78b4154a4e5159462e36de55b8643747da6cda86b3b52a8bb62289e603776c"},
]

[package.dependencies]
click = ">=8.0"
docutils = "*"
sphinx = ">=4.0"

[package.extras]
docs = ["reno"]
test = ["pytest", "pytest-cov"]

[[package]]
name = "sphinx-rtd-theme"
version = "3.1.0"
description = "Read the Docs theme for Sphinx"
optional = false
python-versions = ">=3.8"
groups = ["docs"]
files = [
    {file = "sphinx_rtd_theme-3.1.0-py2.py3-none-any.whl", hash = "sha256:1785824ae8e6632060490f67cf3a72d404a85d2d9fc26bce3619944de5682b89"},
    {file = "sphinx_rtd_theme-3.1.0.tar.gz", hash = "sha256:b44276f2c276e909239a4f6c955aa667aaafeb78597923b1c60babc76db78e4c"},
]

[package.dependencies]
docutils = ">0.18,<0.23"
sphinx = ">=6,<10"
sphinxcontrib-jquery = ">=4,<5"

[package.extras]
dev = ["bump2version", "transifex-client", "twine", "wheel"]

[[package]]
name = "sphinxcontrib-applehelp"
version = "2.0.0"
description = "sphinxcontrib-applehelp is a Sphinx extension which outputs Apple help books"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_applehelp-2.0.0-py3-none-any.whl", hash = "sha256:4cd3f0ec4ac5dd9c17ec65e9ab272c9b867ea77425228e68ecf08d6b28ddbdb5"},
    {file = "sphinxcontrib_applehelp-2.0.0.tar.gz", hash = "sha256:2f29ef331735ce958efa4734873f084941970894c6090408b079c61b2e1c06d1"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["pytest"]

[[package]]
name = "sphinxcontrib-devhelp"
version = "2.0.0"
description = "sphinxcontrib-devhelp is a sphinx extension which outputs Devhelp documents"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_devhelp-2.0.0-py3-none-any.whl", hash = "sha256:aefb8b83854e4b0998877524d1029fd3e6879210422ee3780459e28a1f03a8a2"},
    {file = "sphinxcontrib_devhelp-2.0.0.tar.gz", hash = "sha256:411f5d96d445d1d73bb5d52133377b4248ec79db5c793ce7dbe59e074b4dd1ad"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["pytest"]

[[package]]
name = "sphinxcontrib-htmlhelp"
version = "2.1.0"
description = "sphinxcontrib-htmlhelp is a sphinx extension which renders HTML help files"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_htmlhelp-2.1.0-py3-none-any.whl", hash = "sha256:166759820b47002d22914d64a075ce08f4c46818e17cfc9470a9786b759b19f8"},
    {file = "sphinxcontrib_htmlhelp-2.1.0.tar.gz", hash = "sha256:c9e2916ace8aad64cc13a0d233ee22317f2b9025b9cf3295249fa985cc7082e9"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["html5lib", "pytest"]

[[package]]
name = "sphinxcontrib-jquery"
version = "4.1"
description = "Extension to include jQuery on newer Sphinx releases"
optional = false
python-versions = ">=2.7"
groups = ["docs"]
files = [
    {file = "sphinxcontrib-jquery-4.1.tar.gz", hash = "sha256:1620739f04e36a2c779f1a131a2dfd49b2fd07351bf1968ced074365933abc7a"},
    {file = "sphinxcontrib_jquery-4.1-py2.py3-none-any.whl", hash = "sha256:f936030d7d0147dd026a4f2b5a57343d233f1fc7b363f68b3d4f1cb0993878ae"},
]

[package.dependencies]
Sphinx = ">=1.8"

[[package]]
name = "sphinxcontrib-jsmath"
version = "1.0.1"
description = "A sphinx extension which renders display math in HTML via JavaScript"
optional = false
python-versions = ">=3.5"
groups = ["docs"]
files = [
    {file = "sphinxcontrib-jsmath-1.0.1.tar.gz", hash = "sha256:a9925e4a4587247ed2191a22df5f6970656cb8ca2bd6284309578f2153e0c4b8"},
    {file = "sphinxcontrib_jsmath-1.0.1-py2.py3-none-any.whl", hash = "sha256:2ec2eaebfb78f3f2078e73666b1415417a116cc848b72e5172e596c871103178"},
]

[package.extras]
test = ["flake8", "mypy", "pytest"]

[[package]]
name = "sphinxcontrib-qthelp"
version = "2.0.0"
description = "sphinxcontrib-qthelp is a sphinx extension which outputs QtHelp documents"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_qthelp-2.0.0-py3-none-any.whl", hash = "sha256:b18a828cdba941ccd6ee8445dbe72ffa3ef8cbe7505d8cd1fa0d42d3f2d5f3eb"},
    {file = "sphinxcontrib_qthelp-2.0.0.tar.gz", hash = "sha256:4fe7d0ac8fc171045be623aba3e2a8f613f8682731f9153bb2e40ece16b9bbab"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["defusedxml (>=0.7.1)", "pytest"]

[[package]]
name = "sphinxcontrib-serializinghtml"
version = "2.0.0"
description = "sphinxcontrib-serializinghtml is a sphinx extension which outputs \"serialized\" HTML files (json and pickle)"
optional = false
python-versions = ">=3.9"
groups = ["docs"]
files = [
    {file = "sphinxcontrib_serializinghtml-2.0.0-py3-none-any.whl", hash = "sha256:6e2cb0eef194e10c27ec0023bfeb25badbbb5868244cf5bc5bdc04e4464bf331"},
    {file = "sphinxcontrib_serializinghtml-2.0.0.tar.gz", hash = "sha256:e9d912827f872c029017a53f0ef2180b327c3f7fd23c87229f7a8e8b70031d4d"},
]

[package.extras]
lint = ["mypy", "ruff (==0.5.5)", "types-docutils"]
standalone = ["Sphinx (>=5)"]
test = ["pytest"]

[[package]]
name = "stevedore"
version = "5.6.0"
description = "Manage dynamic plugins for Python applications"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "stevedore-5.6.0-py3-none-any.whl", hash = "sha256:4a36dccefd7aeea0c70135526cecb7766c4c84c473b1af68db23d541b6dc1820"},
    {file = "stevedore-5.6.0.tar.gz", hash = "sha256:f22d15c6ead40c5bbfa9ca54aa7e7b4a07d59b36ae03ed12ced1a54cf0b51945"},
]

[[package]]
name = "toml"
version = "0.10.2"
description = "Python Library for Tom's Obvious, Minimal Language"
optional = false
python-versions = ">=2.6, !=3.0.*, !=3.1.*, !=3.2.*"
groups = ["dev", "docs"]
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
groups = ["dev", "docs"]
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
name = "tomli-w"
version = "1.2.0"
description = "A lil' TOML writer"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "tomli_w-1.2.0-py3-none-any.whl", hash = "sha256:188306098d013b691fcadc011abd66727d3c414c571bb01b1a174ba8c983cf90"},
    {file = "tomli_w-1.2.0.tar.gz", hash = "sha256:2dd14fac5a47c27be9cd4c976af5a12d87fb1f0b4512f81d69cce3b35ae25021"},
]

[[package]]
name = "tox"
version = "4.56.1"
description = "tox is a generic virtualenv management and test command line tool"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "tox-4.56.1-py3-none-any.whl", hash = "sha256:4d06b925c4dd67872099b39c5a46fba79a2169c5f6e32060f95a8b1181f0ef55"},
    {file = "tox-4.56.1.tar.gz", hash = "sha256:db1c2610802553189cf40de251661d066a635ee0ed9bf2a60093b5f1a7f36ef8"},
]

[package.dependencies]
cachetools = ">=7.0.3"
colorama = ">=0.4.6"
filelock = ">=3.25"
packaging = ">=26"
platformdirs = ">=4.9.4"
pluggy = ">=1.6"
pyproject-api = ">=1.10"
python-discovery = ">=1.2.2"
tomli = {version = ">=2.4", markers = "python_version < \"3.11\""}
tomli-w = ">=1.2"
typing-extensions = {version = ">=4.15", markers = "python_version < \"3.11\""}
virtualenv = ">=21.1"

[package.extras]
completion = ["argcomplete (>=3.6.3)"]
testing = ["devpi-process (>=1.1.1)", "pytest (>=9.0.2)", "pytest-mock (>=3.15.1)"]

[[package]]
name = "traceloggingdynamic"
version = "1.0.1"
description = "Generates Event Tracing for Windows events using TraceLogging"
optional = false
python-versions = ">=3.6"
groups = ["main"]
markers = "sys_platform == \"win32\""
files = [
    {file = "traceloggingdynamic-1.0.1-py3-none-any.whl", hash = "sha256:0e19da491a8960725b3622366487ae35f49d8f595bb2e4e5ce1795eb5928db7c"},
    {file = "traceloggingdynamic-1.0.1.tar.gz", hash = "sha256:d9dd4b291dd04c15e34181eed06f73fdf4ffa7b1f895b78217163def48ab1a52"},
]

[[package]]
name = "types-grpcio"
version = "1.0.0.20260614"
description = "Typing stubs for grpcio"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_grpcio-1.0.0.20260614-py3-none-any.whl", hash = "sha256:050472cb4ef329ae8fe20278c62bc0da5b961aad3dd889cc35f6e0c70d368dae"},
    {file = "types_grpcio-1.0.0.20260614.tar.gz", hash = "sha256:e86d1aabb7e7eedae487c3ac10e010a13d5db1fd350e766562053af557366aab"},
]

[[package]]
name = "types-protobuf"
version = "7.34.1.20260518"
description = "Typing stubs for protobuf"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_protobuf-7.34.1.20260518-py3-none-any.whl", hash = "sha256:a0a5337413347166439c0e07cbc26c6164d091401c6f01b1dfd8cdb966c4dd8f"},
    {file = "types_protobuf-7.34.1.20260518.tar.gz", hash = "sha256:28cfaded25889cb83ebfb63cfb0a43628f0b6f3785767bec17287dc6468795f2"},
]

[[package]]
name = "types-psutil"
version = "7.2.2.20260518"
description = "Typing stubs for psutil"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_psutil-7.2.2.20260518-py3-none-any.whl", hash = "sha256:6a3d697665754a60d7b5a41d5a2cff12b53f5e0676d77810cd28ba5e14cb4049"},
    {file = "types_psutil-7.2.2.20260518.tar.gz", hash = "sha256:9f825f631463a5b4d26f19f63aebc9ec25f01140d655026f3ad8a67841f9b331"},
]

[[package]]
name = "types-pywin32"
version = "311.0.0.20260521"
description = "Typing stubs for pywin32"
optional = false
python-versions = ">=3.10"
groups = ["dev"]
files = [
    {file = "types_pywin32-311.0.0.20260521-py3-none-any.whl", hash = "sha256:0a5d6e96983eb38da7d7fd5712e15d3066a02d64a09c234bad9c655539bed8a9"},
    {file = "types_pywin32-311.0.0.20260521.tar.gz", hash = "sha256:e3fb48ef40a83b9798402312c02f96e30cf97d79584a83c36b0a32ce8d93c5ff"},
]

[[package]]
name = "types-setuptools"
version = "80.10.0.20260124"
description = "Typing stubs for setuptools"
optional = false
python-versions = ">=3.9"
groups = ["dev"]
files = [
    {file = "types_setuptools-80.10.0.20260124-py3-none-any.whl", hash = "sha256:efed7e044f01adb9c2806c7a8e1b6aa3656b8e382379b53d5f26ee3db24d4c01"},
    {file = "types_setuptools-80.10.0.20260124.tar.gz", hash = "sha256:1b86d9f0368858663276a0cbe5fe5a9722caf94b5acde8aba0399a6e90680f20"},
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
description = "Backported and Experimental Type Hints for Python 3.9+"
optional = false
python-versions = ">=3.9"
groups = ["main", "dev", "docs"]
files = [
    {file = "typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548"},
    {file = "typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466"},
]
markers = {docs = "python_version == \"3.10\""}

[[package]]
name = "tzdata"
version = "2025.3"
description = "Provider of IANA time zone data"
optional = true
python-versions = ">=2"
groups = ["main"]
markers = "platform_system == \"Windows\" and (extra == \"drivers\" or extra == \"nidaqmx\")"
files = [
    {file = "tzdata-2025.3-py2.py3-none-any.whl", hash = "sha256:06a47e5700f3081aab02b2e513160914ff0694bce9947d6b76ebd6bf57cfc5d1"},
    {file = "tzdata-2025.3.tar.gz", hash = "sha256:de39c2ca5dc7b0344f2eba86f49d614019d29f060fc4ebc8a417896a620b56a7"},
]

[[package]]
name = "tzlocal"
version = "5.3.1"
description = "tzinfo object for the local timezone"
optional = true
python-versions = ">=3.9"
groups = ["main"]
markers = "extra == \"drivers\" or extra == \"nidaqmx\""
files = [
    {file = "tzlocal-5.3.1-py3-none-any.whl", hash = "sha256:eb1a66c3ef5847adf7a834f1be0800581b683b5608e74f86ecbcef8ab91bb85d"},
    {file = "tzlocal-5.3.1.tar.gz", hash = "sha256:cceffc7edecefea1f595541dbd6e990cb1ea3d19bf01b2809f362a03dd7921fd"},
]

[package.dependencies]
tzdata = {version = "*", markers = "platform_system == \"Windows\""}

[package.extras]
devenv = ["check-manifest", "pytest (>=4.3)", "pytest-cov", "pytest-mock (>=3.3)", "zest.releaser"]

[[package]]
name = "urllib3"
version = "2.6.3"
description = "HTTP library with thread-safe connection pooling, file post, and more."
optional = false
python-versions = ">=3.9"
groups = ["main", "docs"]
files = [
    {file = "urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4"},
    {file = "urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed"},
]
markers = {main = "extra == \"drivers\" or extra == \"nidaqmx\""}

[package.extras]
brotli = ["brotli (>=1.2.0) ; platform_python_implementation == \"CPython\"", "brotlicffi (>=1.2.0.0) ; platform_python_implementation != \"CPython\""]
h2 = ["h2 (>=4,<5)"]
socks = ["pysocks (>=1.5.6,!=1.5.7,<2.0)"]
zstd = ["backports-zstd (>=1.0.0) ; python_version < \"3.14\""]

[[package]]
name = "virtualenv"
version = "21.3.0"
description = "Virtual Python Environment builder"
optional = false
python-versions = ">=3.8"
groups = ["dev"]
files = [
    {file = "virtualenv-21.3.0-py3-none-any.whl", hash = "sha256:4d28ee41f6d9ec8f1f00cd472b9ffbcedda1b3d3b9a575b5c94a2d004fd51bd7"},
    {file = "virtualenv-21.3.0.tar.gz", hash = "sha256:733750db978ec95c2d8eb4feadaa57091002bce404cb39ba69899cf7bd28944e"},
]

[package.dependencies]
distlib = ">=0.3.7,<1"
filelock = {version = ">=3.24.2,<4", markers = "python_version >= \"3.10\""}
platformdirs = ">=3.9.1,<5"
python-discovery = ">=1.2.2"
typing-extensions = {version = ">=4.13.2", markers = "python_version < \"3.11\""}

[extras]
drivers = ["nidaqmx", "nidcpower", "nidigital", "nidmm", "nifgen", "niscope", "niswitch"]
nidaqmx = ["nidaqmx"]
nidcpower = ["nidcpower"]
nidigital = ["nidigital"]
nidmm = ["nidmm"]
nifgen = ["nifgen"]
niscope = ["niscope"]
niswitch = ["niswitch"]

[metadata]
lock-version = "2.1"
python-versions = "^3.10"
content-hash = "569000f4897cad2fc5cdbfc5129405ca1917678f8b3d9cb2bc1dffa24f9c75c0"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/poetry.toml sha256=68e4888bac696abc8ade5a5f29a3f2554c73dde0f6c1e1a4c4f6470bc2af504c bytes=755 -->
## FILE: packages/service/poetry.toml

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/poetry.toml`
- sha256: `68e4888bac696abc8ade5a5f29a3f2554c73dde0f6c1e1a4c4f6470bc2af504c`
- bytes: 755

````toml
[virtualenvs]
in-project = true

[solver]
# Set min-release-age to 2 weeks, same as in https://github.com/ni/python-renovate-config
min-release-age = 14
min-release-age-exclude = [
    "hightime",
    "ni-grpc-extensions",
    "ni-grpcdevice-v1-proto",
    "ni-measurementlink-discovery-v1-client",
    "ni-measurementlink-discovery-v1-proto",
    "ni-measurementlink-measurement-v1-proto",
    "ni-measurementlink-measurement-v2-proto",
    "ni-measurementlink-pinmap-v1-client",
    "ni-measurementlink-pinmap-v1-proto",
    "ni-measurementlink-proto",
    "ni-measurementlink-sessionmanagement-v1-client",
    "ni-measurementlink-sessionmanagement-v1-proto",
    "ni-protobuf-types",
    "ni-python-styleguide",
    "nitypes",
]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/pyproject.toml sha256=4c75cc03d6309da1792ce3280b90f51bd4a93c36324acdc1bbe14b35fe042f3f bytes=6647 -->
## FILE: packages/service/pyproject.toml

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/pyproject.toml`
- sha256: `4c75cc03d6309da1792ce3280b90f51bd4a93c36324acdc1bbe14b35fe042f3f`
- bytes: 6647

````toml
[tool.black]
extend_exclude = '\.tox/|_pb2(_grpc)?\.(py|pyi)$|ni_measurement_plugin_sdk_generator/|examples/|third_party/'
line-length = 100

[tool.ni-python-styleguide]
extend_exclude = '.tox/,*_pb2_grpc.py,*_pb2_grpc.pyi,*_pb2.py,*_pb2.pyi,ni_measurement_plugin_sdk_generator/,examples/,third_party/'

[tool.poetry]
name = "ni_measurement_plugin_sdk_service"
version = "3.2.0.dev0"
description = "Measurement Plug-In Support for Python"
authors = ["NI <opensource@ni.com>"]
readme = "README.md" # apply the repo readme to the package as well
repository = "https://github.com/ni/measurement-plugin-python/"
license = "MIT"
classifiers = [
  "Development Status :: 5 - Production/Stable",
  "Intended Audience :: Developers",
  "Intended Audience :: Manufacturing",
  "Intended Audience :: Science/Research",
  "Operating System :: Microsoft :: Windows",
  # Poetry automatically adds classifiers for the license and the supported Python versions.
  "Programming Language :: Python :: Implementation :: CPython",
  "Topic :: Scientific/Engineering",
  "Topic :: System :: Hardware",
]

[tool.poetry.dependencies]
python = "^3.10"
# This package includes gRPC stubs that were generated with the version of grpcio-tools specified
# below. Please keep the minimum grpcio version in sync with the grpcio-tools version. Otherwise,
# the generated gRPC stubs may not work with the minimum grpcio version.
grpcio = "^1.49.1"
protobuf = ">=4.21"
pywin32 = { version = ">=303", platform = "win32" }
deprecation = ">=2.1"
python-decouple = ">=3.8"
nidaqmx = { version = ">=0.8.0", extras = ["grpc"], optional = true }
nidcpower = { version = ">=1.4.4", extras = ["grpc"], optional = true }
nidigital = { version = ">=1.4.4", extras = ["grpc"], optional = true }
nidmm = { version = ">=1.4.4", extras = ["grpc"], optional = true }
nifgen = { version = ">=1.4.4", extras = ["grpc"], optional = true }
niscope = { version = ">=1.4.4", extras = ["grpc"], optional = true }
niswitch = { version = ">=1.4.4", extras = ["grpc"], optional = true }
ni-grpc-extensions =  { version = "^1.0.0" }
ni-measurementlink-discovery-v1-client = { version = "^1.0.0" }
ni-measurementlink-measurement-v1-proto = { version = "^1.0.0" }
ni-measurementlink-measurement-v2-proto = { version = "^1.0.0" }
ni-measurementlink-pinmap-v1-client = { version = "^1.0.0" }
ni-measurementlink-sessionmanagement-v1-client = { version = "^1.0.0" }
ni-protobuf-types = { version = "^1.0.0" }


[tool.poetry.extras]
drivers = [
  "nidaqmx",
  "nidcpower",
  "nidigital",
  "nidmm",
  "nifgen",
  "niscope",
  "niswitch",
]
nidaqmx = ["nidaqmx"]
nidcpower = ["nidcpower"]
nidigital = ["nidigital"]
nidmm = ["nidmm"]
nifgen = ["nifgen"]
niscope = ["niscope"]
niswitch = ["niswitch"]

[tool.poetry.group.dev.dependencies]
pytest = ">=7.2.0"
ni-python-styleguide = ">=0.4.1"
# When you update the grpcio-tools version, you should update the minimum grpcio version
# and regenerate gRPC stubs.
grpcio-tools = [
  # requires protobuf v4 or later
  { version = "1.49.1", python = ">=3.10,<3.12" },
  { version = "1.59.0", python = ">=3.12,<3.13" },
  # requires protobuf v5 or later
  { version = "1.67.0", python = ">=3.13,<3.14" },
  # requires protobuf v6 or later
  { version = "1.75.1", python = "^3.14" },
]
pytest-cov = ">=3.0.0"
pytest-mock = ">=3.0"
tox = ">=4.0"
mypy = ">=1.0"
# mypy-protobuf 3.6 is the last version that supports protobuf v4.
mypy-protobuf = [
  # requires protobuf v4 or later
  {version = ">=3.4,<3.7", python = ">=3.10,<3.14"},
  # requires protobuf v6 or later
  {version = ">=3.4", python = "^3.14"}
]
types-protobuf = ">=4.21"
types-setuptools = "*"
types-pywin32 = ">=304"
types-grpcio = ">=1.0"
psutil = ">=6.0"
types-psutil = ">=6.0"
# NumPy dropped support for Python 3.8 before adding support for Python 3.12, so
# we need to include multiple NumPy versions in poetry.lock.
numpy = [
  { version = ">=1.22", python = ">=3.10,<3.12"},
  { version = ">=1.26", python = ">=3.12,<3.13"},
  { version = ">=2.1", python = "^3.13"},
]
bandit = { version = ">=1.7", extras = ["toml"] }

[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
# The latest Sphinx requires a recent Python version.
Sphinx = [
  { version = "<8.0", python = ">=3.10,<3.11" },
  { version = ">=8.2", python = ">=3.11,<3.13" },
]
sphinx-rtd-theme = ">=1.0.0"
sphinx-autoapi = ">=1.8.4"
m2r2 = ">=0.3.2"
toml = ">=0.10.2"
sphinx-click = ">=4.1.0"
# Workaround to docutils error with 0.21.post1 release
docutils = ">=0.16, !=0.21.post1"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.pytest.ini_options]
addopts = "--doctest-modules --strict-markers"
filterwarnings = ["always::ImportWarning", "always::ResourceWarning"]
testpaths = ["tests"]
markers = [
  "disable_feature_toggle: specifies a feature toggle to disable for the test function/module.",
  "enable_feature_toggle: specifies a feature toggle to enable for the test function/module.",
  "service_class: specifies which test service to use.",
  "use_code_readiness: specifies a code readiness level to use for the test function/module.",
]

[tool.mypy]
files = "ni_measurement_plugin_sdk_service/,tests/"
exclude = "^tests/assets/"
disallow_untyped_defs = true
namespace_packages = true
warn_redundant_casts = true
warn_unused_configs = true
warn_unused_ignores = true

[[tool.mypy.overrides]]
module = [
  # https://github.com/HBNetwork/python-decouple/issues/122 - Add support for type stubs
  "decouple.*",
  # https://github.com/briancurtin/deprecation/issues/56 - Add type information (PEP 561)
  "deprecation.*",
  "grpc.framework.foundation.*",
  # https://github.com/ni/hightime/issues/4 - Add type annotations
  "hightime.*",
  # https://github.com/ni/nidaqmx-python/issues/209 - Support type annotations
  "nidaqmx",
  # https://github.com/ni/nimi-python/issues/1887 - Support type annotations
  "nidcpower",
  "nidigital",
  "nidmm",
  "nifgen",
  "niscope",
  "niswitch",
]
ignore_missing_imports = true

[[tool.mypy.overrides]]
# mypy-protobuf codegen has some unused ignores.
module = [
  "ni_measurement_plugin_sdk_service._internal.stubs.*",
  "tests.utilities.stubs.*",
]
warn_unused_ignores = false

[[tool.mypy.overrides]]
# The tests are not yet ready for --disallow-untyped-defs (or even --disallow-incomplete-defs)
module = ["tests.*"]
check_untyped_defs = true
disallow_untyped_defs = false

[tool.bandit]
skips = [
  "B101", # assert_used
]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/README.md sha256=d57353421721d110a681ea4fcc6101806eb4bbfd99a27bbe03ea3dc8e84d17d3 bytes=16550 -->
## FILE: packages/service/README.md

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/README.md`
- sha256: `d57353421721d110a681ea4fcc6101806eb4bbfd99a27bbe03ea3dc8e84d17d3`
- bytes: 16550

````markdown
# Measurement Plug-In SDK Service for Python

- [Measurement Plug-In Service for Python](#measurement-plug-in-sdk-service-for-python)
  - [Introduction](#introduction)
  - [Dependencies](#dependencies)
  - [Documentation](#documentation)
  - [System Configuration](#system-configuration)
    - [Enable Win32 Long Paths](#enable-win32-long-paths)
  - [Examples](#examples)
  - [Developing Measurements: Quick Start](#developing-measurements-quick-start)
    - [Installation](#installation)
    - [Developing a minimal Python measurement](#developing-a-minimal-python-measurement)
  - [Steps to run/debug the measurement service](#steps-to-rundebug-the-measurement-service)
  - [Static Registration of Python Measurements](#static-registration-of-python-measurements)
    - [Create a batch file that runs a Python measurement](#create-a-batch-file-that-runs-a-python-measurement)
    - [Create Executable for Python Scripts](#create-executable-for-python-scripts)
  - [Troubleshooting](#troubleshooting)
    - ["File not found" or "No such file or directory" errors when copying or running a measurement service](#file-not-found-or-no-such-file-or-directory-errors-when-copying-or-running-a-measurement-service)
  - [Appendix: Managing Measurement with Python](#appendix-managing-measurement-with-python)
    - [Create and Manage Python Measurement using Poetry](#create-and-manage-python-measurement-using-poetry)
    - [Create and Manage Python Measurement using `venv`](#create-and-manage-python-measurement-using-venv)
    - [Create and Manage Python Measurement by directly installing `ni-measurement-plugin-sdk` as a system-level package](#create-and-manage-python-measurement-by-directly-installing-ni-measurement-plugin-sdk-as-a-system-level-package)

---

## Introduction

Measurement Plug-In SDK Service for Python (`ni-measurement-plugin-sdk-service`) is a Python
framework that helps you create reusable measurement plug-ins using gRPC
services. Deploy your measurement plug-ins to perform interactive validation in
InstrumentStudio and automated testing in TestStand.

---

## Dependencies

- [Python >= 3.10](https://www.python.org/downloads/release/python-3100/)
- [grpcio >= 1.49.1, < 2.x](https://pypi.org/project/grpcio/1.49.1/)
- [protobuf >= 4.21](https://pypi.org/project/protobuf/4.21.0/)
- [pywin32 >= 303 (Only for Windows)](https://pypi.org/project/pywin32/303/)

---

## Documentation

- [Measurement Plug-In SDK Manual](https://www.ni.com/docs/en-US/bundle/measurementplugins/)
- [API Reference](https://ni.github.io/measurement-plugin-python/)

---

## System Configuration

### Enable Win32 Long Paths

By default, Windows has a path length limit of 260 characters. NI recommends enabling support for long paths when developing and deploying Python measurement services.

There are three ways to do this:
- When installing Python using the Python for Windows installer, click `Disable path length limit` at the end of the installation.
- Set the `Enable Win32 long paths` group policy:
  - Run `gpedit.msc`.
  - Expand `Computer Configuration` » `Administrative Templates` » `All Settings`.
  - Find `Enable Win32 long paths` in the list, double-click it, and set it to `Enabled`.
- In the Windows registry, set `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\FileSystem\LongPathsEnabled` (type: `REG_DWORD`) to 1. For more details, see [Maximum Path Length Limitation](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation).

---

## Examples

The `examples` directory contains example measurements for use with InstrumentStudio 2024 Q3 or later.

For more information on setting up and running the example measurements, see the included `README.md` file.

For best results, use the example measurements corresponding to the version of InstrumentStudio
that you are using. Newer examples may demonstrate features that are not available in older
versions of InstrumentStudio.

---

## Developing Measurements: Quick Start

This section provides instructions to develop custom measurement services in Python using Measurement Plug-In SDK for Python.

### Installation

Make sure the system has the recommended Python version installed. Install Measurement Plug-In SDK for Python using [pip](https://pip.pypa.io/).

``` cmd
REM Activate the required virtual environment if any.
pip install ni-measurement-plugin-sdk
```

Check if you have installed the expected version of Measurement Plug-In SDK for Python installed by running the below command:

```cmd
pip show ni-measurement-plugin-sdk
```

### Developing a minimal Python measurement

1. Run the `ni-measurement-plugin-generator` tool. Use command line arguments to specify the `display-name` and optionally the `version`, `measurement-type`, and `product-type`.

    1. Running `ni-measurement-plugin-generator` without optional arguments:

    `ni-measurement-plugin-generator SampleMeasurement`

    'SampleMeasurement' is the display name of your measurement service. Without the optional arguments,
    the other arguments are generated for you based on the display name.

    2. Running `ni-measurement-plugin-generator` with optional arguments for `measurement-version`, `ui-file`,
    `service-class`, and `description-url`:

    `ni-measurement-plugin-generator SampleMeasurement --measurement-version 0.1.0.0 --ui-file MeasurementUI.measui --service-class SampleMeasurement_Python --description-url https://www.example.com/SampleMeasurement.html`

    3. Running `ni-measurement-plugin-generator` with optional argument for `directory-out`

    `ni-measurement-plugin-generator SampleMeasurement --directory-out <new_path_for_created_files>`

    If no output directory is specified, the files will
    be placed in a new folder under the current directory
    named after the display name without spaces.

2. To customize the created measurement, provide metadata of the measurement's configuration (input parameters) and outputs (output parameters) in `measurement.py`.
    1. Use the `configuration()` decorator to provide metadata about the configurations.**The order of the configuration decorator must match with the order of the parameters defined in the function signature.**

        ``` python
        @foo_measurement_service.register_measurement
        #Display Names can not contains backslash or front slash.
        @foo_measurement_service.configuration("DisplayNameForInput1", DataType.String, "DefaultValueForInput1")
        @foo_measurement_service.configuration("DisplayNameForInput2", DataType.String, "DefaultValueForInput2")
        def measure(input_1, input_2):
            ''' A simple Measurement method'''
            return ["foo", "bar"]
        ```

    2. Use the `output()` decorator to provide metadata about the output.**The order of the output decorators from top to bottom must match the order of the values of the list returned by the function.**

        ``` python
        @foo_measurement_service.register_measurement
        @foo_measurement_service.configuration("DisplayNameForInput1", nims.DataType.String, "DefaultValueForInput1")
        @foo_measurement_service.configuration("DisplayNameForInput2", nims.DataType.String, "DefaultValueForInput2")
        @foo_measurement_service.output("DisplayNameForOutput1", nims.DataType.String)
        @foo_measurement_service.output("DisplayNameForOutput2", nims.DataType.String)
        def measure(input_1, input_2):
            return ["foo", "bar"]
        ```

3. Run/Debug the created measurement by following the steps discussed in the section ["Steps to run/debug the measurement service".](#steps-to-rundebug-the-measurement-service)

---

## Steps to run/debug the measurement service

1. Start the discovery service if not already started.

2. (Optional) Activate related virtual environments. Measurement developers can skip this step if they are not using any [virtual environments](#create-and-manage-python-measurement-using-venv) or [poetry-based projects.](#create-and-manage-python-measurement-using-poetry)

    ```cmd
    .venv\scripts\activate
    ```

    - After successful activation, you can see the name of the environment, `(.venv)` is added to the command prompt.
    - If you face an access issue when trying to activate, retry after allowing scripts to run as Administrator by executing the below command in Windows PowerShell:

        ```cmd
        Set-ExecutionPolicy RemoteSigned
        ```

3. [Run](https://code.visualstudio.com/docs/python/python-tutorial#_run-hello-world)/[Debug](https://code.visualstudio.com/docs/python/debugging#_basic-debugging) the measurement Python file.

4. To stop the running measurement service, press `Enter` in the terminal to properly close the service.

5. (Optional) After the usage of measurement, deactivate the virtual environment. Measurement developers can skip this step if they are not using any [virtual environments](#create-and-manage-python-measurement-using-venv) or [poetry-based projects.](#create-and-manage-python-measurement-using-poetry)

    ```cmd
    deactivate
    ```

---

## Static Registration of Python Measurements

The NI Discovery Service provides a registry of other services, and can discover and activate other services on the system. These features allow the discovery service to distinguish, manage, and describe measurement services on the system.

To statically register a measurement service with the NI Discovery Service, do the following:

1. Create a [startup batch file](#create-a-batch-file-that-runs-a-python-measurement) or [executable](#create-executable-for-python-scripts) for the measurement service.

2. Edit the measurement service's `.serviceconfig` file and set the `path` value to the filename of the startup batch file or executable.

3. Copy the measurement service's directory (including the `.serviceconfig` file and startup batch file) to a subdirectory of `C:\ProgramData\National Instruments\Plug-Ins\Measurements`.
> **Note**
> If you are using a virtual environment, do not copy the `.venv` subdirectory&mdash;the virtual environment must be re-created in the new location.

Once your measurement service is statically registered, the NI Discovery Service makes it visible in supported NI applications.

### Create a batch file that runs a Python measurement

The batch file used for static registration is responsible for starting the Python Scripts.

Typical Batch File:

``` cmd
"<path_to_python_exe>" "<path_to_measurement_file>"
```

Examples to start the fictitious file named `foo_measurement.py`:

1. Using the Python system distribution

    ```cmd
    python foo_measurement.py
    ```

2. Using the virtual environment

    ```cmd
    REM Windows
    .\.venv\Scripts\python.exe foo_measurement.py

    REM Linux
    .venv/bin/python foo_measurement.py
    ```

### Create Executable for Python Scripts

To create an executable from a measurement, you can use the [pyinstaller](https://www.pyinstaller.org/) tooling. If you are using a Poetry project, add `pyinstaller` to its `dev-dependencies`. When statically registering the service, install the EXE into a unique directory along with its .serviceconfig and UI files.

Typical PyInstaller command to build executable:

```cmd
pyinstaller --onefile --console --paths .venv\Lib\site-packages measurement.py
```

## Troubleshooting

### "File not found" or "No such file or directory" errors when copying or running a measurement service

If copying or running a measurement service produces "File not found" or "No such file or directory" errors, make sure to [enable Win32 long paths](#enable-win32-long-paths). If you are unable to enable Win32 long paths, consider deploying the measurement service to a directory with a shorter path.

## Appendix: Managing Measurement with Python

A measurement and its related files can be maintained in different ways in Python. The basic components of any Python measurement are:

1. Measurement Python module (`.py` file)
    - This file contains all the details related to the measurement and also contains the logic for the measurement execution.
    - This file is run to start the measurement as a service.

2. UI File
    - UI file for the measurement. Types of supported UI files are:
        - Measurement UI (`.measui`): created using the **Measurement Plug-In UI Editor** application.
        - LabVIEW UI (`.vi`)
    - The path of this file is configured by `ui_file_path` in `measurement_info` variable definition in measurement Python module (`.py`).

Python communities have different ways of managing Python projects and their dependencies. It is up to the measurement developer to decide how to maintain the project and dependencies. Measurement developers can choose from a few common approaches discussed below based on their requirements.

### Create and Manage Python Measurement using Poetry

1. Install `poetry` (one-time setup)

    1. Make sure the system has the recommended Python version installed.

    2. Install `poetry` using the installation steps given in <https://python-poetry.org/docs/#installation>.

2. Create a new Python project and add `ni-measurement-plugin-sdk` as a dependency to the project.

    1. Open a command prompt, and change the working directory to the directory of your choice where you want to create the project.

        ``` cmd
        cd <path_of_directory_of_your_choice>
        ```

    2. Create a Poetry project using the `poetry new` command. Poetry will create boilerplate files and folders that are commonly needed for a Python project.

        ``` cmd
        poetry new <name_of_the_project>
        ```

    3. Add the `ni-measurement-plugin-sdk` package as a dependency using the [`poetry add`](https://python-poetry.org/docs/cli/#add) command.

        ``` cmd
        cd <name_of_the_project>
        poetry add ni-measurement-plugin-sdk
        ```

    4. The virtual environment will be auto-created by poetry.

    5. Create measurement modules as described in ["Developing a minimal Python measurement"](#developing-a-minimal-python-measurement)
        - Any additional dependencies required by measurement can be added using [add command](https://python-poetry.org/docs/cli/#add).

            ``` cmd
            poetry add <dependency_package_name>
            ```

For detailed info on managing projects using poetry [refer to the official documentation](https://python-poetry.org/docs/cli/).

### Create and Manage Python Measurement using `venv`

1. Make sure the system has the recommended Python version installed.

2. Open a command prompt, and change the working directory to the directory of your choice where you want to create a project.

    ``` cmd
    cd <path_of_directory_of_your_choice>
    ```

3. Create a virtual environment.

    ``` cmd
    REM This creates a virtual environment named .venv
    python -m venv .venv
    ```

4. Activate the virtual environment. After successful activation

    ``` cmd
    .venv\scripts\activate
    REM Optionally upgrade the pip within the venv by executing the command
    python -m pip install -U pip
    ```

5. Install the `ni-measurement-plugin-sdk` package into the virtual environment.

    ``` cmd
    pip install ni-measurement-plugin-sdk
    ```

6. Create measurement modules as described in ["Developing a minimal Python measurement"](#developing-a-minimal-python-measurement)
    - Any additional dependencies required by measurement can be added pip install.

        ``` cmd
        pip install <dependency_package_name>
        ```

For detailed info on managing projects with a virtual environment, refer to the [official documentation](https://docs.python.org/3/tutorial/venv.html).

### Create and Manage Python Measurement by directly installing `ni-measurement-plugin-sdk` as a system-level package

Measurement developers can also install `ni-measurement-plugin-sdk` as a system package if necessary.

1. Install the `ni-measurement-plugin-sdk` package from the command prompt

    ``` cmd
    pip install ni-measurement-plugin-sdk
    ```

2. Create measurement modules as described in ["Developing a minimal Python measurement"](#developing-a-minimal-python-measurement)

---
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/scripts/generate_grpc_stubs.py sha256=7a278bf762c9d26fb0ff2348810fda78fa1f1a7f474ec0695cc3a74bf58dfd29 bytes=1774 -->
## FILE: packages/service/scripts/generate_grpc_stubs.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/scripts/generate_grpc_stubs.py`
- sha256: `7a278bf762c9d26fb0ff2348810fda78fa1f1a7f474ec0695cc3a74bf58dfd29`
- bytes: 1774

````python
#!/usr/bin/env python3
"""Generates gRPC Python stubs from proto files."""

import pathlib
from collections.abc import Sequence

import grpc_tools.protoc
import pkg_resources

PROTO_PATH = pathlib.Path(__file__).parent.parent.parent.parent / "third_party" / "ni-apis"
TEST_STUBS_PATH = pathlib.Path(__file__).parent.parent / "tests" / "utilities" / "stubs"
TEST_PROTO_PATH = TEST_STUBS_PATH
TEST_PROTO_FILES = list(TEST_PROTO_PATH.rglob("*.proto"))


def main():
    """Generate test gRPC Python stubs."""
    generate_python_files(TEST_STUBS_PATH, TEST_PROTO_PATH, TEST_PROTO_FILES, PROTO_PATH)


def is_relative_to(path: pathlib.PurePath, other: pathlib.PurePath) -> bool:
    """Return whether or not this path is relative to the other path."""
    try:
        path.relative_to(other)
        return True
    except ValueError:
        return False


def generate_python_files(
    stubs_path: pathlib.Path,
    proto_path: pathlib.Path,
    proto_files: Sequence[pathlib.Path],
    alternate_proto_path: pathlib.Path = "",
):
    """Generate python files from .proto files with protoc."""
    arguments = [
        "protoc",
        f"--proto_path={str(proto_path)}",
        f"--proto_path={pkg_resources.resource_filename('grpc_tools', '_proto')}",
        f"--python_out={str(stubs_path)}",
        f"--mypy_out={str(stubs_path)}",
        f"--grpc_python_out={str(stubs_path)}",
        f"--mypy_grpc_out={str(stubs_path)}",
    ]
    if alternate_proto_path != "":
        arguments += (f"--proto_path={str(alternate_proto_path)}",)

    arguments += [str(path.relative_to(proto_path)).replace("\\", "/") for path in proto_files]

    grpc_tools.protoc.main(arguments)


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/scripts/install_examples.py sha256=f22b7133b15e12096acfd17eaeaf55534ac32bea5d92d28b9a460dbb35655136 bytes=2714 -->
## FILE: packages/service/scripts/install_examples.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/scripts/install_examples.py`
- sha256: `f22b7133b15e12096acfd17eaeaf55534ac32bea5d92d28b9a460dbb35655136`
- bytes: 2714

````python
#!/usr/bin/env python3
"""Install all example services."""

import os
import pathlib
import re
import shutil
import subprocess

ROOT_DIR = pathlib.Path(__file__).parent.parent.parent.parent
EXAMPLES_PATH = ROOT_DIR / "examples"
SERVICES_PATH = (
    pathlib.Path(os.environ["ProgramData"]) / "National Instruments" / "Plug-Ins" / "Measurements"
)


def main():
    """Install all example services."""
    clean_env = _get_clean_env()
    for example_path in EXAMPLES_PATH.iterdir():
        if not (example_path / "pyproject.toml").exists():
            continue

        print(f"{example_path.name}:")

        install_path = SERVICES_PATH / example_path.name
        if install_path.is_dir():
            print(f"Deleting example from {install_path}")
            shutil.rmtree(install_path)

        print(f"Installing example into {install_path}")
        shutil.copytree(example_path, install_path, ignore=shutil.ignore_patterns(".venv"))

        poetry_lock = install_path / "poetry.lock"
        if poetry_lock.exists():
            print(f"Deleting lock file {poetry_lock}")
            poetry_lock.unlink()

        venv_dir = install_path / ".venv"
        if venv_dir.is_dir():
            print(f"Deleting virtualenv {venv_dir}")
            shutil.rmtree(venv_dir)

        pyproject_path = install_path / "pyproject.toml"
        pyproject_data = pyproject_path.read_text()
        new_pyproject_data = re.sub(
            r'^ni-measurement-plugin-sdk-service\s*=\s*\{\s*path\s*=\s*"\.\./\.\."',
            lambda m: m.group(0).replace("../..", ROOT_DIR.absolute().as_posix()),
            pyproject_data,
            flags=re.MULTILINE,
        )
        if new_pyproject_data != pyproject_data:
            print(f"Patching pyproject.toml to use absolute path")
            pyproject_path.write_text(new_pyproject_data)

        print(f"Installing dependencies")
        subprocess.run(
            ["poetry", "-v", "install", "--only", "main"],
            check=True,
            cwd=install_path,
            env=clean_env,
        )

        print("")


def _get_clean_env():
    """Get a clean environment with no venv activated.

    This is a workaround for https://github.com/python-poetry/poetry/issues/4055
    Option to force Poetry to create a virtual environment, even if a virtual env is active

    """
    env = os.environ.copy()
    if env.pop("VIRTUAL_ENV", None) is not None:
        for var in os.environ.keys():
            value = env.pop(f"_OLD_VIRTUAL_{var}", None)
            if value is not None:
                env[var] = value
    return env


if __name__ == "__main__":
    main()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/__init__.py sha256=14a272de191ef5de47d1830c42c5fc79bdb7eaeab8b953e425ddf03e5d7c269a bytes=14 -->
## FILE: packages/service/tests/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/__init__.py`
- sha256: `14a272de191ef5de47d1830c42c5fc79bdb7eaeab8b953e425ddf03e5d7c269a`
- bytes: 14

````python
"""Tests."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/__init__.py sha256=1b68459d29337bc998c2ecca65616a941c1fe12792763af0be0f92414361088a bytes=25 -->
## FILE: packages/service/tests/acceptance/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/__init__.py`
- sha256: `1b68459d29337bc998c2ecca65616a941c1fe12792763af0be0f92414361088a`
- bytes: 25

````python
"""Acceptance tests."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/conftest.py sha256=9fa5b6746b94fb3e7d4bb4af34f534dcc0a1e9c067a4eaf124f5ec9ca7c27ff7 bytes=766 -->
## FILE: packages/service/tests/acceptance/conftest.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/conftest.py`
- sha256: `9fa5b6746b94fb3e7d4bb4af34f534dcc0a1e9c067a4eaf124f5ec9ca7c27ff7`
- bytes: 766

````python
"""Pytest configuration file for acceptance tests."""

import pathlib
import warnings
from collections.abc import Generator

import pytest

from ni_measurement_plugin_sdk_service.measurement import WrongMessageTypeWarning


@pytest.fixture(scope="module")
def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path:
    """Test fixture that returns the pin map directory."""
    return test_assets_directory / "acceptance" / "session_management"


@pytest.fixture
def filter_wrong_configurations_message_type_warnings() -> Generator:
    """Test fixture to filter out WrongMessageTypeWarning warnings for Configurations messages."""
    warnings.filterwarnings("ignore", ".*Configurations.*", WrongMessageTypeWarning)
    yield
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_logging.py sha256=59b5edb41ddac49dfbd8f382fd3eaf5e2cda738d429b5e331a5365edc0e06117 bytes=7253 -->
## FILE: packages/service/tests/acceptance/test_logging.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_logging.py`
- sha256: `59b5edb41ddac49dfbd8f382fd3eaf5e2cda738d429b5e331a5365edc0e06117`
- bytes: 7253

````python
import logging
import pathlib
import re
from collections.abc import Generator

import pytest
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    GRPC_SERVICE_CLASS,
    GRPC_SERVICE_INTERFACE_NAME,
    SessionManagementClient,
)
from pytest import FixtureRequest, LogCaptureFixture

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.acceptance.test_streaming_data_measurement import (
    _get_configuration_parameters as get_streaming_data_configuration_parameters,
)
from tests.utilities.discovery_service_process import DiscoveryServiceProcess
from tests.utilities.measurements import (
    loopback_measurement,
    streaming_data_measurement,
)


def test___discovery_client___call___client_call_logged(
    caplog: LogCaptureFixture, discovery_client: DiscoveryClient
) -> None:
    with caplog.at_level(logging.DEBUG):
        _ = discovery_client.resolve_service(GRPC_SERVICE_INTERFACE_NAME, GRPC_SERVICE_CLASS)

    method_name = "/ni.measurementlink.discovery.v1.DiscoveryService/ResolveService"
    debug_messages = [r.message for r in caplog.records if r.levelno == logging.DEBUG]
    assert f"gRPC client call starting: {method_name}" in debug_messages
    assert f"gRPC client call complete: {method_name}" in debug_messages


def test___pin_map_client___call___client_call_logged(
    caplog: LogCaptureFixture,
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
) -> None:
    with caplog.at_level(logging.DEBUG):
        pin_map_path = pin_map_directory / "1Smu1ChannelGroup2Pin2Site.pinmap"
        _ = pin_map_client.update_pin_map(pin_map_path)

    method_name = "/ni.measurementlink.pinmap.v1.PinMapService/UpdatePinMapFromXml"
    debug_messages = [r.message for r in caplog.records if r.levelno == logging.DEBUG]
    assert f"gRPC client call starting: {method_name}" in debug_messages
    assert f"gRPC client call complete: {method_name}" in debug_messages


def test___session_management_client___call___client_call_logged(
    caplog: LogCaptureFixture, request: FixtureRequest
) -> None:
    with caplog.at_level(logging.DEBUG):
        # HACK: set log level before constructing client
        session_management_client: SessionManagementClient = request.getfixturevalue(
            "session_management_client"
        )

        session_management_client.unregister_sessions(session_info=[])

    method_name = (
        "/ni.measurementlink.sessionmanagement.v1.SessionManagementService/UnregisterSessions"
    )
    debug_messages = [r.message for r in caplog.records if r.levelno == logging.DEBUG]
    assert f"gRPC client call starting: {method_name}" in debug_messages
    assert f"gRPC client call complete: {method_name}" in debug_messages


@pytest.mark.service_class("ni.tests.LoopbackMeasurement_Python")
def test___loopback_measurement___get_metadata___server_call_logged(
    caplog: LogCaptureFixture, request: FixtureRequest
) -> None:
    with caplog.at_level(logging.DEBUG):
        # HACK: set log level before constructing server
        stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub = request.getfixturevalue(
            "stub_v2"
        )

        _ = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

    method_name = "/ni.measurementlink.measurement.v2.MeasurementService/GetMetadata"
    debug_messages = [r.message for r in caplog.records if r.levelno == logging.DEBUG]
    assert f"gRPC server call starting: {method_name}" in debug_messages
    assert f"gRPC server call complete: {method_name}" in debug_messages
    info_messages = [r.message for r in caplog.records if r.levelno == logging.INFO]
    info_regex = re.compile(rf"gRPC server call {method_name} responded OK in [\d.]+ ms")
    assert len(list(filter(info_regex.match, info_messages))) == 1


@pytest.mark.service_class("ni.tests.StreamingDataMeasurement_Python")
def test___streaming_data_measurement___measure___server_call_logged(
    caplog: LogCaptureFixture, request: FixtureRequest
) -> None:
    with caplog.at_level(logging.DEBUG):
        # HACK: set log level before constructing server
        stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub = request.getfixturevalue(
            "stub_v2"
        )
        num_responses = 10
        metadata = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

        measure_request = v2_measurement_service_pb2.MeasureRequest(
            configuration_parameters=get_streaming_data_configuration_parameters(
                message_type=metadata.measurement_signature.configuration_parameters_message_type,
                num_responses=num_responses,
            )
        )
        response_iterator = stub_v2.Measure(measure_request)
        for response in response_iterator:
            pass

    method_name = "/ni.measurementlink.measurement.v2.MeasurementService/Measure"
    debug_messages = [r.message for r in caplog.records if r.levelno == logging.DEBUG]
    assert f"gRPC server call starting: {method_name}" in debug_messages
    assert f"gRPC server call complete: {method_name}" in debug_messages
    debug_response_regex = re.compile(rf"gRPC server call streaming response: {method_name}")
    assert len(list(filter(debug_response_regex.match, debug_messages))) == num_responses
    info_messages = [r.message for r in caplog.records if r.levelno == logging.INFO]
    info_regex = re.compile(rf"gRPC server call {method_name} responded OK in [\d.]+ ms")
    assert len(list(filter(info_regex.match, info_messages))) == 1


@pytest.fixture
def measurement_service(request: FixtureRequest) -> MeasurementService:
    service_class_marker = request.node.get_closest_marker("service_class")
    service_class = service_class_marker.args[0]
    if service_class == "ni.tests.LoopbackMeasurement_Python":
        return request.getfixturevalue("loopback_measurement_service")
    elif service_class == "ni.tests.StreamingDataMeasurement_Python":
        return request.getfixturevalue("streaming_data_measurement_service")
    else:
        raise ValueError(f"Unsupported service class: {service_class}")


@pytest.fixture
def loopback_measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates a loopback measurement."""
    with loopback_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def streaming_data_measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates a loopback measurement."""
    with streaming_data_measurement.measurement_service.host_service() as service:
        yield service
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_measurement_service.py sha256=9480298c5e97f7fb635623ece4af182c9ebc02a44e43437541382c369a9b7d42 bytes=10582 -->
## FILE: packages/service/tests/acceptance/test_measurement_service.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_measurement_service.py`
- sha256: `9480298c5e97f7fb635623ece4af182c9ebc02a44e43437541382c369a9b7d42`
- bytes: 10582

````python
"""Tests to validate measurement service. Uses the Sample Measurement Example."""

from __future__ import annotations

import random
import sys
import urllib.parse
import urllib.request
from collections.abc import Generator
from enum import Enum
from os import path

import pytest
from google.protobuf import any_pb2
from ni.measurementlink.measurement.v1 import (
    measurement_service_pb2 as v1_measurement_service_pb2,
    measurement_service_pb2_grpc as v1_measurement_service_pb2_grpc,
)
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import loopback_measurement
from tests.utilities.stubs.loopback.types_pb2 import Parameters, ProtobufColor

EXPECTED_PARAMETER_COUNT = 7
EXPECTED_UI_FILE_COUNT = 1


class Color(Enum):
    """Primary colors used for example enum-typed config and output."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


def test___measurement_service_v1___get_metadata___returns_metadata(
    stub_v1: v1_measurement_service_pb2_grpc.MeasurementServiceStub,
):
    response = stub_v1.GetMetadata(v1_measurement_service_pb2.GetMetadataRequest())

    _validate_get_metadata_response(response)


def test___measurement_service_v2___get_metadata___returns_metadata(
    stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub,
):
    response = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

    _validate_get_metadata_response(response)


@pytest.mark.parametrize(
    "float_in,double_array_in,bool_in,string_in,enum_in,protobuf_enum_in,string_array_in",
    [
        (
            0.9,
            [1.0, 23.56],
            True,
            "InputString",
            Color.BLUE,
            ProtobufColor.WHITE,
            ["", "TestString1", "#$%!@<*(&^~`"],
        )
    ],
)
def test___measurement_service_v1___measure___returns_output(
    float_in: float,
    double_array_in: list[float],
    bool_in: bool,
    string_in: str,
    enum_in: Enum,
    protobuf_enum_in: ProtobufColor.ValueType,
    string_array_in: list[str],
    stub_v1: v1_measurement_service_pb2_grpc.MeasurementServiceStub,
):
    metadata = stub_v1.GetMetadata(v1_measurement_service_pb2.GetMetadataRequest())

    request = v1_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            float_in,
            double_array_in,
            bool_in,
            string_in,
            enum_in,
            protobuf_enum_in,
            string_array_in,
            message_type=metadata.measurement_signature.configuration_parameters_message_type,
        )
    )
    response = stub_v1.Measure(request)

    serialized_parameter = _get_serialized_measurement_signature(
        float_in, double_array_in, bool_in, string_in, enum_in, protobuf_enum_in, string_array_in
    )
    assert response.outputs.value == serialized_parameter


@pytest.mark.parametrize(
    "float_in,double_array_in,bool_in,string_in,enum_in,protobuf_enum_in,string_array_in",
    [
        (
            0.9,
            [1.0, 23.56],
            True,
            "InputString",
            Color.BLUE,
            ProtobufColor.WHITE,
            ["", "TestString1", "#$%!@<*(&^~`"],
        )
    ],
)
def test___measurement_service_v2___measure___returns_output(
    float_in: float,
    double_array_in: list[float],
    bool_in: bool,
    string_in: str,
    enum_in: Enum,
    protobuf_enum_in: ProtobufColor.ValueType,
    string_array_in: list[str],
    stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub,
):
    metadata = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

    request = v2_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            float_in,
            double_array_in,
            bool_in,
            string_in,
            enum_in,
            protobuf_enum_in,
            string_array_in,
            message_type=metadata.measurement_signature.configuration_parameters_message_type,
        )
    )
    response_iterator = stub_v2.Measure(request)
    responses = [response for response in response_iterator]

    serialized_parameter = _get_serialized_measurement_signature(
        float_in, double_array_in, bool_in, string_in, enum_in, protobuf_enum_in, string_array_in
    )
    assert len(responses) == 1
    assert responses[0].outputs.value == serialized_parameter


@pytest.mark.parametrize("double_array_len", [10000, 100000, 1000000, 10000000])  # up to 80 MB
def test___measurement_service_v1___measure_with_large_array___returns_output(
    double_array_len: int, stub_v1: v1_measurement_service_pb2_grpc.MeasurementServiceStub
):
    if sys.platform == "win32" and sys.maxsize < 2**32 and double_array_len > 1000000:
        pytest.skip("TODO: 32-bit Python tests fail with out-of-memory errors #818")
    float_in = 1.23
    double_array_in = [random.random() for i in range(double_array_len)]
    bool_in = False
    string_in = "InputString"
    enum_in = Color.BLUE
    protobuf_enum_in = ProtobufColor.WHITE
    string_array_in = ["", "TestString1", "#$%!@<*(&^~`"]
    metadata = stub_v1.GetMetadata(v1_measurement_service_pb2.GetMetadataRequest())

    request = v1_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            float_in,
            double_array_in,
            bool_in,
            string_in,
            enum_in,
            protobuf_enum_in,
            string_array_in,
            message_type=metadata.measurement_signature.configuration_parameters_message_type,
        )
    )
    response = stub_v1.Measure(request)

    serialized_parameter = _get_serialized_measurement_signature(
        float_in, double_array_in, bool_in, string_in, enum_in, protobuf_enum_in, string_array_in
    )
    assert response.outputs.value == serialized_parameter


@pytest.mark.parametrize("double_array_len", [10000, 100000, 1000000, 10000000])  # up to 80 MB
def test___measurement_service_v2___measure_with_large_array___returns_output(
    double_array_len: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub
):
    if sys.platform == "win32" and sys.maxsize < 2**32 and double_array_len > 1000000:
        pytest.skip("TODO: 32-bit Python tests fail with out-of-memory errors #818")
    float_in = 1.23
    double_array_in = [random.random() for i in range(double_array_len)]
    bool_in = False
    enum_in = Color.BLUE
    protobuf_enum_in = ProtobufColor.WHITE
    string_in = "InputString"
    string_array_in = ["", "TestString1", "#$%!@<*(&^~`"]
    metadata = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

    request = v2_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            float_in,
            double_array_in,
            bool_in,
            string_in,
            enum_in,
            protobuf_enum_in,
            string_array_in,
            message_type=metadata.measurement_signature.configuration_parameters_message_type,
        )
    )
    response_iterator = stub_v2.Measure(request)
    responses = [response for response in response_iterator]

    serialized_parameter = _get_serialized_measurement_signature(
        float_in, double_array_in, bool_in, string_in, enum_in, protobuf_enum_in, string_array_in
    )
    assert len(responses) == 1
    assert responses[0].outputs.value == serialized_parameter


@pytest.fixture(scope="module")
def measurement_service(discovery_service_process) -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with loopback_measurement.measurement_service.host_service() as service:
        yield service


def _get_configuration_parameters(*args, message_type: str = "", **kwargs) -> any_pb2.Any:
    serialized_parameter = _get_serialized_measurement_signature(*args, **kwargs)
    config_params_any = any_pb2.Any()
    config_params_any.type_url = "type.googleapis.com/" + message_type
    config_params_any.value = serialized_parameter
    return config_params_any


def _get_serialized_measurement_signature(
    float_in: float,
    double_array_in: list[float],
    bool_in: bool,
    string_in: str,
    enum_in: Enum,
    protobuf_enum_in: ProtobufColor.ValueType,
    string_array_in: list[str],
) -> bytes:
    config_params = Parameters()
    config_params.float_in = float_in
    config_params.double_array_in.extend(double_array_in)
    config_params.bool_in = bool_in
    config_params.string_in = string_in
    config_params.enum_in = enum_in.value
    config_params.protobuf_enum_in = protobuf_enum_in
    config_params.string_array_in.extend(string_array_in)

    temp_any = any_pb2.Any()
    temp_any.Pack(config_params)
    grpc_serialized_data = temp_any.value
    return grpc_serialized_data


def _validate_get_metadata_response(
    get_metadata_response: (
        v1_measurement_service_pb2.GetMetadataResponse
        | v2_measurement_service_pb2.GetMetadataResponse
    ),
):
    assert get_metadata_response.measurement_details.display_name == "Loopback Measurement (Py)"
    assert get_metadata_response.measurement_details.version == "1.2.3.4"

    assert (
        get_metadata_response.measurement_signature.configuration_parameters_message_type
        == "ni.tests.LoopbackMeasurement_Python.Configurations"
    )
    assert (
        get_metadata_response.measurement_signature.outputs_message_type
        == "ni.tests.LoopbackMeasurement_Python.Outputs"
    )
    assert (
        len(get_metadata_response.measurement_signature.configuration_parameters)
        == EXPECTED_PARAMETER_COUNT
    )
    assert len(get_metadata_response.measurement_signature.outputs) == EXPECTED_PARAMETER_COUNT

    assert len(get_metadata_response.user_interface_details) == EXPECTED_UI_FILE_COUNT
    for details in get_metadata_response.user_interface_details:
        url = urllib.parse.urlparse(details.file_url)
        localpath = urllib.request.url2pathname(url.path)
        assert path.exists(localpath)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nidaqmx_measurement.py sha256=a4c3d51ff991bb93a56243715638c56f7cda0a89fe3fb44c99f146f9245b3e7b bytes=3847 -->
## FILE: packages/service/tests/acceptance/test_nidaqmx_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_nidaqmx_measurement.py`
- sha256: `a4c3d51ff991bb93a56243715638c56f7cda0a89fe3fb44c99f146f9245b3e7b`
- bytes: 3847

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import nidaqmx_measurement
from tests.utilities.stubs.nidaqmx.types_pb2 import Configurations, Outputs

_SITE = 0


pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___single_session___measure___returns_measured_values(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_names = ["Pin1"]
    min_value = -10.5
    max_value = 10.5
    configurations = Configurations(pin_names=pin_names, multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert min_value <= outputs.voltage_values[0] <= max_value


def test___single_session___measure___creates_single_session(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_names = ["Pin1"]
    configurations = Configurations(pin_names=pin_names, multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert _get_output(outputs) == [_MeasurementOutput("Dev1", "Dev1", "Dev1/ai0", "Dev1/ai0")]


def test___multiple_sessions___measure___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    configurations = Configurations(pin_names=pin_names, multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert _get_output(outputs) == [
        _MeasurementOutput("Dev1", "Dev1", "Dev1/ai0", "Dev1/ai0"),
        _MeasurementOutput("Dev2", "Dev2", "Dev2/ai0", "Dev2/ai0"),
    ]


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service() -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with nidaqmx_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Mio2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])


class _MeasurementOutput(NamedTuple):
    session_name: str
    resource_name: str
    channel_list: str
    connected_channels: str


def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]:
    return [
        _MeasurementOutput(session_name, resource_name, channel_list, connected_channels)
        for session_name, resource_name, channel_list, connected_channels in zip(
            outputs.session_names,
            outputs.resource_names,
            outputs.channel_lists,
            outputs.connected_channels,
        )
    ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nidcpower_measurement.py sha256=85180d23f9cb44980347e4d34d0f40ada0cd345f72283ea2f8d9af037245517b bytes=4128 -->
## FILE: packages/service/tests/acceptance/test_nidcpower_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_nidcpower_measurement.py`
- sha256: `85180d23f9cb44980347e4d34d0f40ada0cd345f72283ea2f8d9af037245517b`
- bytes: 4128

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import nidcpower_measurement
from tests.utilities.stubs.nidcpower.types_pb2 import Configurations, Outputs

_SITE = 0


pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___single_session___measure___returns_measured_values(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["Pin1"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert outputs.voltage_measurements == [5]
    assert outputs.current_measurements == [0.0001]


def test___single_session___measure___creates_single_session(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["Pin1"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert _get_output(outputs) == [
        _MeasurementOutput("DCPower1/0", "DCPower1/0", "DCPower1/0", "DCPower1/0")
    ]


def test___multiple_sessions___measure___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["Pin1", "Pin2"], multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    actual = _get_output(outputs)
    expected1 = [
        _MeasurementOutput("DCPower1/0", "DCPower1/0", "DCPower1/0", "DCPower1/0"),
        _MeasurementOutput("DCPower1/2", "DCPower1/2", "DCPower1/2", "DCPower1/2"),
    ]
    expected2 = [
        _MeasurementOutput("niDCPower-DCPower1/0", "DCPower1/0", "DCPower1/0", "DCPower1/0"),
        _MeasurementOutput("niDCPower-DCPower1/2", "DCPower1/2", "DCPower1/2", "DCPower1/2"),
    ]
    assert actual == expected1 or actual == expected2


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service() -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with nidcpower_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "1Smu2ChannelGroup2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])


class _MeasurementOutput(NamedTuple):
    session_name: str
    resource_name: str
    channel_list: str
    connected_channels: str


def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]:
    return [
        _MeasurementOutput(session_name, resource_name, channel_list, connected_channels)
        for session_name, resource_name, channel_list, connected_channels in zip(
            outputs.session_names,
            outputs.resource_names,
            outputs.channel_lists,
            outputs.connected_channels,
        )
    ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nidigital_measurement.py sha256=9bb5071bf5062f4598bc6c364b8e0a8a60ba0c3646aa4a6df98d73fa63d63ea8 bytes=5224 -->
## FILE: packages/service/tests/acceptance/test_nidigital_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_nidigital_measurement.py`
- sha256: `9bb5071bf5062f4598bc6c364b8e0a8a60ba0c3646aa4a6df98d73fa63d63ea8`
- bytes: 5224

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import nidigital_measurement
from tests.utilities.stubs.nidigital.types_pb2 import Configurations, Outputs

pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___single_session___measure___returns_measured_values(
    pin_map_id: str,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
    configurations = Configurations(pin_names=["CS", "SCLK", "MOSI", "MISO"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert outputs.passing_sites == [0]
    assert outputs.failing_sites == []


def test___single_session___measure___creates_single_session(
    pin_map_id: str,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
    configurations = Configurations(pin_names=["CS", "SCLK", "MOSI", "MISO"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    actual = _get_output(outputs)
    expected1 = [
        _MeasurementOutput(
            "DigitalPattern1",
            "DigitalPattern1",
            "site0/CS, site0/SCLK, site0/MOSI, site0/MISO",
            "site0/CS",
        )
    ]
    expected2 = [
        _MeasurementOutput(
            "niDigitalPattern-DigitalPattern1",
            "DigitalPattern1",
            "site0/CS, site0/SCLK, site0/MOSI, site0/MISO",
            "site0/CS",
        )
    ]
    assert actual == expected1 or actual == expected2


def test___multiple_sessions___measure___creates_multiple_sessions(
    pin_map_id: str,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
    configurations = Configurations(pin_names=["CS", "SCLK", "MOSI", "MISO"], multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    actual = _get_output(outputs)
    expected1 = [
        _MeasurementOutput(
            "DigitalPattern1",
            "DigitalPattern1",
            "site0/CS, site0/SCLK, site0/MOSI, site0/MISO",
            "site0/CS, site0/SCLK, site0/MOSI, site0/MISO",
        ),
        _MeasurementOutput(
            "DigitalPattern2",
            "DigitalPattern2",
            "site1/CS, site1/SCLK, site1/MOSI, site1/MISO",
            "site1/CS, site1/SCLK, site1/MOSI, site1/MISO",
        ),
    ]
    expected2 = [
        _MeasurementOutput(
            "niDigitalPattern-DigitalPattern1",
            "DigitalPattern1",
            "site0/CS, site0/SCLK, site0/MOSI, site0/MISO",
            "site0/CS, site0/SCLK, site0/MOSI, site0/MISO",
        ),
        _MeasurementOutput(
            "niDigitalPattern-DigitalPattern2",
            "DigitalPattern2",
            "site1/CS, site1/SCLK, site1/MOSI, site1/MISO",
            "site1/CS, site1/SCLK, site1/MOSI, site1/MISO",
        ),
    ]
    assert actual == expected1 or actual == expected2


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service() -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with nidigital_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def pin_map_id(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> str:
    pin_map_name = "2Digital2Group4Pin1Site.pinmap"
    return pin_map_client.update_pin_map(pin_map_directory / pin_map_name)


class _MeasurementOutput(NamedTuple):
    session_name: str
    resource_name: str
    channel_list: str
    connected_channels: str


def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]:
    return [
        _MeasurementOutput(session_name, resource_name, channel_list, connected_channels)
        for session_name, resource_name, channel_list, connected_channels in zip(
            outputs.session_names,
            outputs.resource_names,
            outputs.channel_lists,
            outputs.connected_channels,
        )
    ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nidmm_measurement.py sha256=2b42c4f5d79b749d727c929c1454dc54d54af3d6fbe79c95d42b4bec361e65d5 bytes=4030 -->
## FILE: packages/service/tests/acceptance/test_nidmm_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_nidmm_measurement.py`
- sha256: `2b42c4f5d79b749d727c929c1454dc54d54af3d6fbe79c95d42b4bec361e65d5`
- bytes: 4030

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import nidmm_measurement
from tests.utilities.stubs.nidmm.types_pb2 import Configurations, Outputs

_SITE = 0


pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___single_session___measure___returns_measured_values(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_names = ["Pin1"]
    configurations = Configurations(pin_names=pin_names, multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert outputs.signals_out_of_range == [False]
    assert outputs.absolute_resolutions == pytest.approx([5.0e-05])


def test___single_session___measure___creates_single_session(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_names = ["Pin1"]
    configurations = Configurations(pin_names=pin_names, multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert _get_output(outputs) == [_MeasurementOutput("DMM1", "DMM1", "0", "0")]


def test___multiple_sessions___measure___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    configurations = Configurations(pin_names=pin_names, multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    actual = _get_output(outputs)
    expected1 = [
        _MeasurementOutput("DMM1", "DMM1", "0", "0"),
        _MeasurementOutput("DMM2", "DMM2", "0", "0"),
    ]
    expected2 = [
        _MeasurementOutput("niDMM-DMM1", "DMM1", "0", "0"),
        _MeasurementOutput("niDMM-DMM2", "DMM2", "0", "0"),
    ]
    assert actual == expected1 or actual == expected2


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service() -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with nidmm_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Dmm2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])


class _MeasurementOutput(NamedTuple):
    session_name: str
    resource_name: str
    channel_list: str
    connected_channels: str


def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]:
    return [
        _MeasurementOutput(session_name, resource_name, channel_list, connected_channels)
        for session_name, resource_name, channel_list, connected_channels in zip(
            outputs.session_names,
            outputs.resource_names,
            outputs.channel_lists,
            outputs.connected_channels,
        )
    ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_nifgen_measurement.py sha256=bf5ae1eb5f6e5e44557ddcc784aad4f269c38ccbe12bf590677c3b640cd8a7b7 bytes=3541 -->
## FILE: packages/service/tests/acceptance/test_nifgen_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_nifgen_measurement.py`
- sha256: `bf5ae1eb5f6e5e44557ddcc784aad4f269c38ccbe12bf590677c3b640cd8a7b7`
- bytes: 3541

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import nifgen_measurement
from tests.utilities.stubs.nifgen.types_pb2 import Configurations, Outputs

_SITE = 0


pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___single_session___measure___creates_single_session(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["Pin1"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert _get_output(outputs) == [_MeasurementOutput("FGEN1", "FGEN1", "0", "0")]


def test___multiple_sessions___measure___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["Pin1", "Pin2"], multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    actual = _get_output(outputs)
    expected1 = [
        _MeasurementOutput("FGEN1", "FGEN1", "0", "0"),
        _MeasurementOutput("FGEN2", "FGEN2", "0", "0"),
    ]
    expected2 = [
        _MeasurementOutput("niFGen-FGEN1", "FGEN1", "0", "0"),
        _MeasurementOutput("niFGen-FGEN2", "FGEN2", "0", "0"),
    ]
    assert actual == expected1 or actual == expected2


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service() -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with nifgen_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Fgen2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])


class _MeasurementOutput(NamedTuple):
    session_name: str
    resource_name: str
    channel_list: str
    connected_channels: str


def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]:
    return [
        _MeasurementOutput(session_name, resource_name, channel_list, connected_channels)
        for session_name, resource_name, channel_list, connected_channels in zip(
            outputs.session_names,
            outputs.resource_names,
            outputs.channel_lists,
            outputs.connected_channels,
        )
    ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_niscope_measurement.py sha256=c192ae4a8626519e2733e90e67b05dd970b732a40c3bace260c6ce78001a2364 bytes=3936 -->
## FILE: packages/service/tests/acceptance/test_niscope_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_niscope_measurement.py`
- sha256: `c192ae4a8626519e2733e90e67b05dd970b732a40c3bace260c6ce78001a2364`
- bytes: 3936

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import niscope_measurement
from tests.utilities.stubs.niscope.types_pb2 import Configurations, Outputs

_SITE = 0


pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___single_session___measure___returns_measured_values(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["Pin1"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert all([-2.5 < sample < 2.5 for sample in outputs.waveform])


def test___single_session___measure___creates_single_session(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["Pin1"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert _get_output(outputs) == [_MeasurementOutput("SCOPE1", "SCOPE1", "0", "0")]


def test___multiple_sessions___measure___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["Pin1", "Pin2"], multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    actual = _get_output(outputs)
    expected1 = [
        _MeasurementOutput("SCOPE1", "SCOPE1", "0", "0"),
        _MeasurementOutput("SCOPE2", "SCOPE2", "0", "0"),
    ]
    expected2 = [
        _MeasurementOutput("niScope-SCOPE1", "SCOPE1", "0", "0"),
        _MeasurementOutput("niScope-SCOPE2", "SCOPE2", "0", "0"),
    ]
    assert actual == expected1 or actual == expected2


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service() -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with niscope_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Scope2Pin2Group1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])


class _MeasurementOutput(NamedTuple):
    session_name: str
    resource_name: str
    channel_list: str
    connected_channels: str


def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]:
    return [
        _MeasurementOutput(session_name, resource_name, channel_list, connected_channels)
        for session_name, resource_name, channel_list, connected_channels in zip(
            outputs.session_names,
            outputs.resource_names,
            outputs.channel_lists,
            outputs.connected_channels,
        )
    ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_niswitch_measurement.py sha256=4a0638fd55ecf0493940c91cb1ddc5c91ce4662a37bb00c1953e4eb01b7ba8dd bytes=3832 -->
## FILE: packages/service/tests/acceptance/test_niswitch_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_niswitch_measurement.py`
- sha256: `4a0638fd55ecf0493940c91cb1ddc5c91ce4662a37bb00c1953e4eb01b7ba8dd`
- bytes: 3832

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import niswitch_measurement
from tests.utilities.stubs.niswitch.types_pb2 import Configurations, Outputs

_SITE = 0


pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___single_session___measure___creates_single_session(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(relay_names=["SiteRelay1"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    actual = _get_output(outputs)
    expected1 = [_MeasurementOutput("RelayDriver1", "RelayDriver1", "K0", "K0")]
    expected2 = [_MeasurementOutput("niRelayDriver-RelayDriver1", "RelayDriver1", "K0", "K0")]
    assert actual == expected1 or actual == expected2


def test___multiple_sessions___measure___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(relay_names=["SiteRelay1", "SiteRelay2"], multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)
    actual = _get_output(outputs)
    expected1 = [
        _MeasurementOutput("RelayDriver1", "RelayDriver1", "K0", "K0"),
        _MeasurementOutput("RelayDriver2", "RelayDriver2", "K1", "K1"),
    ]
    expected2 = [
        _MeasurementOutput("niRelayDriver-RelayDriver1", "RelayDriver1", "K0", "K0"),
        _MeasurementOutput("niRelayDriver-RelayDriver2", "RelayDriver2", "K1", "K1"),
    ]
    assert actual == expected1 or actual == expected2


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service() -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with niswitch_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Switch2Relay1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])


class _MeasurementOutput(NamedTuple):
    session_name: str
    resource_name: str
    channel_list: str
    connected_channels: str


def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]:
    return [
        _MeasurementOutput(session_name, resource_name, channel_list, connected_channels)
        for session_name, resource_name, channel_list, connected_channels in zip(
            outputs.session_names,
            outputs.resource_names,
            outputs.channel_lists,
            outputs.connected_channels,
        )
    ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_niswitch_multiplexer_measurement.py sha256=a3ca26a6498d68620368c61239ee429a5a8008dbd6df554b7410f4addaa95dd6 bytes=3542 -->
## FILE: packages/service/tests/acceptance/test_niswitch_multiplexer_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_niswitch_multiplexer_measurement.py`
- sha256: `a3ca26a6498d68620368c61239ee429a5a8008dbd6df554b7410f4addaa95dd6`
- bytes: 3542

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import niswitch_multiplexer_measurement
from tests.utilities.stubs.niswitchmultiplexer.types_pb2 import Configurations, Outputs

_SITE = 0


pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___single_session___measure___creates_single_session(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["A"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert _get_output(outputs) == [
        _MeasurementOutput("Multiplexer1", "Multiplexer1", "b0c1->b0r0", "DCPower1/0")
    ]


def test___multiple_sessions___measure___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    stub_v2: MeasurementServiceStub,
) -> None:
    configurations = Configurations(pin_names=["A", "B"], multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert _get_output(outputs) == [
        _MeasurementOutput("Multiplexer1", "Multiplexer1", "b0c1->b0r0", "DCPower1/0"),
        _MeasurementOutput("Multiplexer2", "Multiplexer2", "b0c3->b0r0", "DCPower1/2"),
    ]


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service() -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with niswitch_multiplexer_measurement.measurement_service.host_service() as service:
        yield service


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2SwitchMultiplexer1Smu2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])


class _MeasurementOutput(NamedTuple):
    multiplexer_session_name: str
    multiplexer_resource_name: str
    multiplexer_route: str
    connected_channel: str


def _get_output(outputs: Outputs) -> Iterable[_MeasurementOutput]:
    return [
        _MeasurementOutput(session_name, resource_name, multiplexer_route, connected_channel)
        for session_name, resource_name, multiplexer_route, connected_channel in zip(
            outputs.multiplexer_session_names,
            outputs.multiplexer_resource_names,
            outputs.multiplexer_routes,
            outputs.connected_channels,
        )
    ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_security.py sha256=e79477e0ec718a0ca3c743aa4b0b5a31be1f5b233bff19efb3c7d4c17e7f2502 bytes=1241 -->
## FILE: packages/service/tests/acceptance/test_security.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_security.py`
- sha256: `e79477e0ec718a0ca3c743aa4b0b5a31be1f5b233bff19efb3c7d4c17e7f2502`
- bytes: 1241

````python
from collections.abc import Generator
from ipaddress import ip_address

import psutil
import pytest

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.discovery_service_process import DiscoveryServiceProcess
from tests.utilities.measurements import loopback_measurement


def test___loopback_measurement___listening_on_loopback_interface(
    measurement_service: MeasurementService,
):
    insecure_port = int(measurement_service.service_location.insecure_port)

    listener_ips = [
        ip_address(conn.laddr.ip)
        for conn in psutil.Process().net_connections()
        if conn.laddr.port == insecure_port and conn.status == psutil.CONN_LISTEN
    ]
    assert len(listener_ips) >= 1 and all([ip.is_loopback for ip in listener_ips])
    assert measurement_service.service_location.ssl_authenticated_port == ""


@pytest.fixture(scope="module")
def measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates and hosts a measurement service."""
    with loopback_measurement.measurement_service.host_service() as service:
        yield service
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_session_management.py sha256=124e59e4f1ba1a33a8a2e54119a0010c59b053424cfe7c5f3f6cbaebd7c8583b bytes=11296 -->
## FILE: packages/service/tests/acceptance/test_session_management.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_session_management.py`
- sha256: `124e59e4f1ba1a33a8a2e54119a0010c59b053424cfe7c5f3f6cbaebd7c8583b`
- bytes: 11296

````python
from __future__ import annotations

import pathlib
from collections.abc import Generator, Iterable
from typing import NamedTuple

import grpc
import pytest
from ni.measurementlink.measurement.v2.measurement_service_pb2 import (
    MeasureRequest,
)
from ni.measurementlink.measurement.v2.measurement_service_pb2_grpc import (
    MeasurementServiceStub,
)
from ni.measurementlink.pin_map_context_pb2 import (
    PinMapContext,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.discovery_service_process import DiscoveryServiceProcess
from tests.utilities.measurements import pin_aware_measurement
from tests.utilities.stubs.pinaware.types_pb2 import Configurations, Outputs

pytestmark = pytest.mark.usefixtures("filter_wrong_configurations_message_type_warnings")


def test___pin_map_context___measure___sends_pin_map_id_and_sites(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_map_path = pin_map_directory / "1Smu1ChannelGroup2Pin2Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_path)
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
    configurations = Configurations(pin_names=["Pin1", "Pin2"], multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert outputs.pin_map_id == pin_map_id
    assert outputs.sites == pin_map_context.sites


class Configuration(NamedTuple):
    """A group of shared test parameters."""

    pin_map_name: str
    pin_names: Iterable[str]
    sites: Iterable[int]
    expected_session_names: Iterable[str]
    expected_resource_names: Iterable[str]
    expected_channel_lists: Iterable[str]
    expected_session_names2: Iterable[str]


_FGEN_SINGLE_SESSION_CONFIGURATIONS = [
    Configuration(
        "1Fgen1Pin1Site.pinmap",
        ["Pin1"],
        [0],
        ["FGEN1"],
        ["FGEN1"],
        ["0"],
        expected_session_names2=["niFGen-FGEN1"],
    ),
    Configuration(
        "2Fgen2Pin2Site.pinmap",
        ["Pin1"],
        [0],
        ["FGEN1"],
        ["FGEN1"],
        ["0"],
        expected_session_names2=["niFGen-FGEN1"],
    ),
    Configuration(
        "2Fgen2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [0],
        ["FGEN1"],
        ["FGEN1"],
        ["0, 1"],
        expected_session_names2=["niFGen-FGEN1"],
    ),
    Configuration(
        "2Fgen2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [1],
        ["FGEN2"],
        ["FGEN2"],
        ["0, 1"],
        expected_session_names2=["niFGen-FGEN2"],
    ),
]

_FGEN_MULTI_SESSION_CONFIGURATIONS = [
    Configuration(
        "2Fgen2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [0, 1],
        ["FGEN1", "FGEN2"],
        ["FGEN1", "FGEN2"],
        ["0, 1", "0, 1"],
        expected_session_names2=["niFGen-FGEN1", "niFGen-FGEN2"],
    ),
]

_SMU_SINGLE_SESSION_CONFIGURATIONS = [
    Configuration(
        "1Smu1ChannelGroup1Pin1Site.pinmap",
        ["Pin1"],
        [0],
        ["DCPower1/0"],
        ["DCPower1/0"],
        ["DCPower1/0"],
        expected_session_names2=["niDCPower-DCPower1/0"],
    ),
    Configuration(
        "1Smu1ChannelGroup2Pin2Site.pinmap",
        ["Pin1"],
        [0],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        ["DCPower1/0"],
        expected_session_names2=["niDCPower-DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
    ),
    Configuration(
        "1Smu1ChannelGroup2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [0],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/1"],
        expected_session_names2=["niDCPower-DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
    ),
    Configuration(
        "1Smu1ChannelGroup2Pin2Site.pinmap",
        ["Pin1"],
        [0, 1],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/2"],
        expected_session_names2=["niDCPower-DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
    ),
    Configuration(
        "1Smu1ChannelGroup2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [0, 1],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
        expected_session_names2=["niDCPower-DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3"],
    ),
    Configuration(
        "1Smu2ChannelGroup2Pin2Site.pinmap",
        ["Pin1"],
        [0],
        ["DCPower1/0, DCPower1/1"],
        ["DCPower1/0, DCPower1/1"],
        ["DCPower1/0"],
        expected_session_names2=["niDCPower-DCPower1/0, DCPower1/1"],
    ),
    Configuration(
        "1Smu2ChannelGroup2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [0],
        ["DCPower1/0, DCPower1/1"],
        ["DCPower1/0, DCPower1/1"],
        ["DCPower1/0, DCPower1/1"],
        expected_session_names2=["niDCPower-DCPower1/0, DCPower1/1"],
    ),
    Configuration(
        "1Smu2ChannelGroup2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [1],
        ["DCPower1/2, DCPower1/3"],
        ["DCPower1/2, DCPower1/3"],
        ["DCPower1/2, DCPower1/3"],
        expected_session_names2=["niDCPower-DCPower1/2, DCPower1/3"],
    ),
    Configuration(
        "2Smu2ChannelGroup2Pin2Site.pinmap",
        ["Pin1"],
        [0],
        ["DCPower1/0, DCPower1/1"],
        ["DCPower1/0, DCPower1/1"],
        ["DCPower1/0"],
        expected_session_names2=["niDCPower-DCPower1/0, DCPower1/1"],
    ),
    Configuration(
        "2Smu2ChannelGroup2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [0],
        ["DCPower1/0, DCPower1/1"],
        ["DCPower1/0, DCPower1/1"],
        ["DCPower1/0, DCPower1/1"],
        expected_session_names2=["niDCPower-DCPower1/0, DCPower1/1"],
    ),
    Configuration(
        "2Smu2ChannelGroup2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [1],
        ["DCPower2/0, DCPower2/1"],
        ["DCPower2/0, DCPower2/1"],
        ["DCPower2/0, DCPower2/1"],
        expected_session_names2=["niDCPower-DCPower2/0, DCPower2/1"],
    ),
]

_SMU_MULTI_SESSION_CONFIGURATIONS = [
    Configuration(
        "1Smu2ChannelGroup2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [0, 1],
        ["DCPower1/0, DCPower1/1", "DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/1", "DCPower1/2, DCPower1/3"],
        ["DCPower1/0, DCPower1/1", "DCPower1/2, DCPower1/3"],
        expected_session_names2=[
            "niDCPower-DCPower1/0, DCPower1/1",
            "niDCPower-DCPower1/2, DCPower1/3",
        ],
    ),
    Configuration(
        "2Smu2ChannelGroup2Pin2Site.pinmap",
        ["Pin1", "Pin2"],
        [0, 1],
        ["DCPower1/0, DCPower1/1", "DCPower2/0, DCPower2/1"],
        ["DCPower1/0, DCPower1/1", "DCPower2/0, DCPower2/1"],
        ["DCPower1/0, DCPower1/1", "DCPower2/0, DCPower2/1"],
        expected_session_names2=[
            "niDCPower-DCPower1/0, DCPower1/1",
            "niDCPower-DCPower2/0, DCPower2/1",
        ],
    ),
]


@pytest.mark.parametrize(
    "configuration", _FGEN_SINGLE_SESSION_CONFIGURATIONS + _SMU_SINGLE_SESSION_CONFIGURATIONS
)
def test___single_session___measure___reserves_single_session(
    configuration: Configuration,
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / configuration.pin_map_name)
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=configuration.sites)
    configurations = Configurations(pin_names=configuration.pin_names, multi_session=False)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert outputs.session_names == configuration.expected_session_names
    assert outputs.resource_names == configuration.expected_resource_names
    assert outputs.channel_lists == configuration.expected_channel_lists


@pytest.mark.parametrize(
    "configuration",
    _FGEN_SINGLE_SESSION_CONFIGURATIONS
    + _FGEN_MULTI_SESSION_CONFIGURATIONS
    + _SMU_SINGLE_SESSION_CONFIGURATIONS
    + _SMU_MULTI_SESSION_CONFIGURATIONS,
)
def test___multi_session___measure___reserves_multiple_sessions(
    configuration: Configuration,
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / configuration.pin_map_name)
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=configuration.sites)
    configurations = Configurations(pin_names=configuration.pin_names, multi_session=True)

    outputs = _measure(stub_v2, pin_map_context, configurations)

    assert (
        outputs.session_names == configuration.expected_session_names
        or outputs.session_names == configuration.expected_session_names2
    )
    assert outputs.resource_names == configuration.expected_resource_names
    assert outputs.channel_lists == configuration.expected_channel_lists


@pytest.mark.parametrize(
    "configuration", _FGEN_MULTI_SESSION_CONFIGURATIONS + _SMU_MULTI_SESSION_CONFIGURATIONS
)
def test___multi_session_but_expecting_single_session___measure___raises_too_many_sessions_error(
    configuration: Configuration,
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    stub_v2: MeasurementServiceStub,
) -> None:
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / configuration.pin_map_name)
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=configuration.sites)
    configurations = Configurations(pin_names=configuration.pin_names, multi_session=False)

    with pytest.raises(grpc.RpcError) as exc_info:
        _ = _measure(stub_v2, pin_map_context, configurations)

    assert exc_info.value.code() == grpc.StatusCode.UNKNOWN
    assert "Too many sessions reserved." in (exc_info.value.details() or "")


def _measure(
    stub_v2: MeasurementServiceStub,
    pin_map_context: PinMapContext,
    configurations: Configurations,
) -> Outputs:
    request = MeasureRequest(pin_map_context=pin_map_context)
    request.configuration_parameters.Pack(configurations)
    response_iterator = stub_v2.Measure(request)
    responses = list(response_iterator)
    assert len(responses) == 1
    outputs = Outputs.FromString(responses[0].outputs.value)
    return outputs


@pytest.fixture(scope="module")
def measurement_service(
    discovery_service_process: DiscoveryServiceProcess,
) -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with pin_aware_measurement.measurement_service.host_service() as service:
        yield service
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_streaming_data_measurement.py sha256=4936eedb39b6452be54814dd10dfa4f01f88c664888a0097b3f9a0877246b470 bytes=6183 -->
## FILE: packages/service/tests/acceptance/test_streaming_data_measurement.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_streaming_data_measurement.py`
- sha256: `4936eedb39b6452be54814dd10dfa4f01f88c664888a0097b3f9a0877246b470`
- bytes: 6183

````python
"""Tests to validate a v2 measurement service that streams data."""

from __future__ import annotations

from collections.abc import Generator

import grpc
import pytest
from google.protobuf import any_pb2
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import streaming_data_measurement
from tests.utilities.stubs.streamingdata.types_pb2 import Configurations, Outputs


@pytest.mark.parametrize("num_responses", [1, 10, 100])
def test___streaming_measurement_service___request_number_of_responses___receives_responses(
    num_responses: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub
):
    metadata = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

    request = v2_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            message_type=metadata.measurement_signature.configuration_parameters_message_type,
            num_responses=num_responses,
        )
    )

    response_iterator = stub_v2.Measure(request)

    responses = [response for response in response_iterator]
    assert len(responses) == num_responses


@pytest.mark.parametrize("data_size", [1, 10, 100])
def test___streaming_measurement_service___request_data_cumulatively___receives_expected_amount_of_data(
    data_size: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub
):
    metadata = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

    name = "testing-cumulative"
    request = v2_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            message_type=metadata.measurement_signature.configuration_parameters_message_type,
            name=name,
            data_size=data_size,
            cumulative_data=True,
        )
    )

    response_iterator = stub_v2.Measure(request)

    expected_data: list[int] = []
    index = 0
    for response in response_iterator:
        expected_data.extend(index for i in range(data_size))
        expected = _get_serialized_measurement_outputs(name, index, expected_data)
        assert expected == response.outputs.value
        index += 1


@pytest.mark.parametrize("data_size", [1, 10, 100])
def test___streaming_measurement_service___specify_data_size___receives_expected_amount_of_data(
    data_size: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub
):
    metadata = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

    name = "testing-not-cumulative"
    request = v2_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            message_type=metadata.measurement_signature.configuration_parameters_message_type,
            name=name,
            data_size=data_size,
            cumulative_data=False,
        )
    )

    response_iterator = stub_v2.Measure(request)

    index = 0
    for response in response_iterator:
        expected_data = [index for i in range(data_size)]
        expected = _get_serialized_measurement_outputs(name, index, expected_data)
        assert expected == response.outputs.value
        index += 1


@pytest.mark.parametrize("error_on_index", [1, 5, 9])
def test___streaming_measurement_service___specify_error_index___errors_at_expected_response(
    error_on_index: int, stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub
):
    metadata = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())

    request = v2_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            message_type=metadata.measurement_signature.configuration_parameters_message_type,
            error_on_index=error_on_index,
        )
    )

    response_iterator = stub_v2.Measure(request)

    with pytest.raises(grpc.RpcError, match=f"Errored at index {error_on_index}"):
        for index, response in enumerate(response_iterator):
            pass
    assert (index + 1) == error_on_index


def _get_configuration_parameters(*args, message_type: str = "", **kwargs) -> any_pb2.Any:
    serialized_parameter = _get_serialized_measurement_configuration_parameters(*args, **kwargs)
    config_params_any = any_pb2.Any()
    config_params_any.type_url = "type.googleapis.com/" + message_type
    config_params_any.value = serialized_parameter
    return config_params_any


def _get_serialized_measurement_configuration_parameters(
    name: str = "test",
    num_responses: int = 10,
    data_size: int = 1,
    cumulative_data: bool = True,
    response_interval_in_ms: int = 1,
    error_on_index: int = -1,
) -> bytes:
    config_params = Configurations()
    config_params.name = name
    config_params.num_responses = num_responses
    config_params.data_size = data_size
    config_params.cumulative_data = cumulative_data
    config_params.response_interval_in_ms = response_interval_in_ms
    config_params.error_on_index = error_on_index

    temp_any = any_pb2.Any()
    temp_any.Pack(config_params)
    grpc_serialized_data = temp_any.value
    return grpc_serialized_data


def _get_serialized_measurement_outputs(
    name: str,
    index: int,
    data: list[int],
) -> bytes:
    config_params = Outputs()
    config_params.name = name
    config_params.index = index
    config_params.data.extend(data)

    temp_any = any_pb2.Any()
    temp_any.Pack(config_params)
    grpc_serialized_data = temp_any.value
    return grpc_serialized_data


@pytest.fixture(scope="module")
def measurement_service(discovery_service_process) -> Generator[MeasurementService]:
    """Test fixture that creates and hosts a measurement service."""
    with streaming_data_measurement.measurement_service.host_service() as service:
        yield service
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/acceptance/test_yield_vs_return.py sha256=d01ff86058c122e11df6b970f048073a21ee3d68c4a5ba5401badaa1d00073f6 bytes=2572 -->
## FILE: packages/service/tests/acceptance/test_yield_vs_return.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/acceptance/test_yield_vs_return.py`
- sha256: `d01ff86058c122e11df6b970f048073a21ee3d68c4a5ba5401badaa1d00073f6`
- bytes: 2572

````python
"""Tests to validate that yield and return are both supported in v2 measurements."""

from collections.abc import Generator

import pytest
from google.protobuf import any_pb2
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2 as v2_measurement_service_pb2,
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService
from tests.utilities.measurements import yield_vs_return_measurement
from tests.utilities.stubs.yieldvsreturn.types_pb2 import Configurations, Outputs


def test___measurement_utilizing_yield_and_return___call_measurement___receives_responses_from_yield_and_return(
    stub_v2: v2_measurement_service_pb2_grpc.MeasurementServiceStub,
):
    metadata = stub_v2.GetMetadata(v2_measurement_service_pb2.GetMetadataRequest())
    request = v2_measurement_service_pb2.MeasureRequest(
        configuration_parameters=_get_configuration_parameters(
            message_type=metadata.measurement_signature.configuration_parameters_message_type
        )
    )

    response_iterator = stub_v2.Measure(request)
    responses = [response for response in response_iterator]

    for index, response in enumerate(responses):
        output = Outputs()
        output.ParseFromString(response.outputs.value)
        if index + 1 == len(responses):
            assert output.status == f"Total updates: {index + 1}"
        else:
            assert output.status == f"Update: {index + 1}"


def _get_configuration_parameters(*args, message_type: str = "", **kwargs) -> any_pb2.Any:
    serialized_parameter = _get_serialized_measurement_configuration_parameters(*args, **kwargs)
    config_params_any = any_pb2.Any()
    config_params_any.type_url = "type.googleapis.com/" + message_type
    config_params_any.value = serialized_parameter
    return config_params_any


def _get_serialized_measurement_configuration_parameters(
    time_in_seconds: float = 1.0,
) -> bytes:
    config_params = Configurations(time_in_seconds=time_in_seconds)

    temp_any = any_pb2.Any()
    temp_any.Pack(config_params)
    grpc_serialized_data = temp_any.value
    return grpc_serialized_data


@pytest.fixture(scope="module")
def measurement_service(discovery_service_process) -> Generator[MeasurementService, None, None]:
    """Test fixture that creates and hosts a measurement service."""
    with yield_vs_return_measurement.measurement_service.host_service() as service:
        yield service
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/__init__.py sha256=1a0661d88fec598d742c3bb1937962a67a2223b74bc90c105f525a91e277310a bytes=29 -->
## FILE: packages/service/tests/assets/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/__init__.py`
- sha256: `1a0661d88fec598d742c3bb1937962a67a2223b74bc90c105f525a91e277310a`
- bytes: 29

````python
"""Contains test assets."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/1Fgen1Pin1Site.pinmap sha256=364bfd912753d983db78483c6d0bc4dfacf003d152a4b3348b8a27e844447010 bytes=521 -->
## FILE: packages/service/tests/assets/acceptance/session_management/1Fgen1Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/1Fgen1Pin1Site.pinmap`
- sha256: `364bfd912753d983db78483c6d0bc4dfacf003d152a4b3348b8a27e844447010`
- bytes: 521

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIFGenInstrument name="FGEN1" numberOfChannels="1" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="FGEN1" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/1Smu1ChannelGroup1Pin1Site.pinmap sha256=3bfd0e7dbb4bec1f88d9bf3bfd1c11b655c2850a7a73e0259cdc99d9b17646e3 bytes=605 -->
## FILE: packages/service/tests/assets/acceptance/session_management/1Smu1ChannelGroup1Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/1Smu1ChannelGroup1Pin1Site.pinmap`
- sha256: `3bfd0e7dbb4bec1f88d9bf3bfd1c11b655c2850a7a73e0259cdc99d9b17646e3`
- bytes: 605

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/1Smu1ChannelGroup2Pin2Site.pinmap sha256=af0472e6543663b5894964008c800014a544f43ef88531aca5f91226189b18da bytes=892 -->
## FILE: packages/service/tests/assets/acceptance/session_management/1Smu1ChannelGroup2Pin2Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/1Smu1ChannelGroup2Pin2Site.pinmap`
- sha256: `af0472e6543663b5894964008c800014a544f43ef88531aca5f91226189b18da`
- bytes: 892

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="DCPower1" channel="1" />
		<Connection pin="Pin1" siteNumber="1" instrument="DCPower1" channel="2" />
		<Connection pin="Pin2" siteNumber="1" instrument="DCPower1" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/1Smu2ChannelGroup2Pin1Site.pinmap sha256=e314f603433cb2312df69b0849f6a623f6eef70b82a0df47cb0d424514f0af62 bytes=783 -->
## FILE: packages/service/tests/assets/acceptance/session_management/1Smu2ChannelGroup2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/1Smu2ChannelGroup2Pin1Site.pinmap`
- sha256: `e314f603433cb2312df69b0849f6a623f6eef70b82a0df47cb0d424514f0af62`
- bytes: 783

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="DCPowerChannelGroup0" channels="0,1" />
			<ChannelGroup name="DCPowerChannelGroup1" channels="2,3" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="DCPower1" channel="2" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/1Smu2ChannelGroup2Pin2Site.pinmap sha256=6c7d11dfdbdf990d189fd0f200f2312417457464f744d8b6a64c1bcecb870c3a bytes=966 -->
## FILE: packages/service/tests/assets/acceptance/session_management/1Smu2ChannelGroup2Pin2Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/1Smu2ChannelGroup2Pin2Site.pinmap`
- sha256: `6c7d11dfdbdf990d189fd0f200f2312417457464f744d8b6a64c1bcecb870c3a`
- bytes: 966

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="DCPowerChannelGroup0" channels="0,1" />
			<ChannelGroup name="DCPowerChannelGroup1" channels="2,3" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="DCPower1" channel="1" />
		<Connection pin="Pin1" siteNumber="1" instrument="DCPower1" channel="2" />
		<Connection pin="Pin2" siteNumber="1" instrument="DCPower1" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2Digital2Group4Pin1Site.pinmap sha256=015f715462dee410ce7342d0159544efd6db2dc98e8f36bcc6af91b106bff7e8 bytes=1359 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2Digital2Group4Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2Digital2Group4Pin1Site.pinmap`
- sha256: `015f715462dee410ce7342d0159544efd6db2dc98e8f36bcc6af91b106bff7e8`
- bytes: 1359

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Digital0" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" group="Digital1" />
	</Instruments>
	<Pins>
		<DUTPin name="CS" />
		<DUTPin name="SCLK" />
		<DUTPin name="MOSI" />
		<DUTPin name="MISO" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="CS" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="SCLK" siteNumber="0" instrument="DigitalPattern1" channel="1" />
		<Connection pin="MOSI" siteNumber="0" instrument="DigitalPattern1" channel="2" />
		<Connection pin="MISO" siteNumber="0" instrument="DigitalPattern1" channel="3" />
		<Connection pin="CS" siteNumber="1" instrument="DigitalPattern2" channel="0" />
		<Connection pin="SCLK" siteNumber="1" instrument="DigitalPattern2" channel="1" />
		<Connection pin="MOSI" siteNumber="1" instrument="DigitalPattern2" channel="2" />
		<Connection pin="MISO" siteNumber="1" instrument="DigitalPattern2" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2Dmm2Pin1Site.pinmap sha256=34f755eb73267093d8672b313353c2b80723c290fae84a167140d91eb9721902 bytes=629 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2Dmm2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2Dmm2Pin1Site.pinmap`
- sha256: `34f755eb73267093d8672b313353c2b80723c290fae84a167140d91eb9721902`
- bytes: 629

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDmmInstrument name="DMM1" />
		<NIDmmInstrument name="DMM2" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DMM1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="DMM2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2Fgen2Pin1Site.pinmap sha256=33d0c97df0a80551e2f58bb358183549f517fa280fd39313f5d899da8e4d046f bytes=680 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2Fgen2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2Fgen2Pin1Site.pinmap`
- sha256: `33d0c97df0a80551e2f58bb358183549f517fa280fd39313f5d899da8e4d046f`
- bytes: 680

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIFGenInstrument name="FGEN1" numberOfChannels="1" />
		<NIFGenInstrument name="FGEN2" numberOfChannels="1" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="FGEN1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="FGEN2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2Fgen2Pin2Site.pinmap sha256=d1cd9f639e1f6c3c108e11aaf65eea3b079d6f9440dd8bace73ef5051ce5acbf bytes=857 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2Fgen2Pin2Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2Fgen2Pin2Site.pinmap`
- sha256: `d1cd9f639e1f6c3c108e11aaf65eea3b079d6f9440dd8bace73ef5051ce5acbf`
- bytes: 857

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIFGenInstrument name="FGEN1" numberOfChannels="2" />
		<NIFGenInstrument name="FGEN2" numberOfChannels="2" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="FGEN1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="FGEN1" channel="1" />
		<Connection pin="Pin1" siteNumber="1" instrument="FGEN2" channel="0" />
		<Connection pin="Pin2" siteNumber="1" instrument="FGEN2" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2Mio2Pin1Site.pinmap sha256=325420713db6f7095342aebbbc35bd9af2f31ed45c70a475a9d8f1855c3ff3dd bytes=730 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2Mio2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2Mio2Pin1Site.pinmap`
- sha256: `325420713db6f7095342aebbbc35bd9af2f31ed45c70a475a9d8f1855c3ff3dd`
- bytes: 730

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIDAQmxTask name="Dev1" taskType="AnalogInput" channelList="Dev1/ai0" />
		<NIDAQmxTask name="Dev2" taskType="AnalogInput" channelList="Dev2/ai0" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="Dev1" channel="Dev1/ai0" />
		<Connection pin="Pin2" siteNumber="0" instrument="Dev2" channel="Dev2/ai0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2Scope2Pin2Group1Site.pinmap sha256=b021f1a86165851effd9e717861f551c90f21d55469b74e2c92f060069115963 bytes=716 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2Scope2Pin2Group1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2Scope2Pin2Group1Site.pinmap`
- sha256: `b021f1a86165851effd9e717861f551c90f21d55469b74e2c92f060069115963`
- bytes: 716

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIScopeInstrument name="SCOPE1" numberOfChannels="4" group="Scope0" />
		<NIScopeInstrument name="SCOPE2" numberOfChannels="4" group="Scope1" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="SCOPE1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="SCOPE2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2Smu2ChannelGroup2Pin2Site.pinmap sha256=6425a239e206b3e9c779582fa14f6c2d11083e9113cf758617a5cf102a6633cc bytes=1024 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2Smu2ChannelGroup2Pin2Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2Smu2ChannelGroup2Pin2Site.pinmap`
- sha256: `6425a239e206b3e9c779582fa14f6c2d11083e9113cf758617a5cf102a6633cc`
- bytes: 1024

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="DCPowerChannelGroup0" />
		</NIDCPowerInstrument>
		<NIDCPowerInstrument name="DCPower2" numberOfChannels="4">
			<ChannelGroup name="DCPowerChannelGroup1" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="DCPower1" channel="1" />
		<Connection pin="Pin1" siteNumber="1" instrument="DCPower2" channel="0" />
		<Connection pin="Pin2" siteNumber="1" instrument="DCPower2" channel="1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2Switch2Relay1Site.pinmap sha256=ac41fc05a84733a0adcfb0c82d583800b796534cdbee9ca617fed3dae596d5c2 bytes=842 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2Switch2Relay1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2Switch2Relay1Site.pinmap`
- sha256: `ac41fc05a84733a0adcfb0c82d583800b796534cdbee9ca617fed3dae596d5c2`
- bytes: 842

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.4">
	<Instruments>
		<NIRelayDriverModule name="RelayDriver1" numberOfControlLines="64" />
		<NIRelayDriverModule name="RelayDriver2" numberOfControlLines="64" />
	</Instruments>
	<Pins></Pins>
	<PinGroups></PinGroups>
	<Relays>
		<SiteRelay name="SiteRelay1" />
		<SiteRelay name="SiteRelay2" />
	</Relays>
	<RelayGroups></RelayGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<RelayConnection relay="SiteRelay1" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K0" />
		<RelayConnection relay="SiteRelay2" siteNumber="0" relayDriverModule="RelayDriver2" controlLine="K1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/acceptance/session_management/2SwitchMultiplexer1Smu2Pin1Site.pinmap sha256=6ca585a9c35f3e976d7a4533238c5ff8907a814b2201c6c7bcc389ab7731cfee bytes=1096 -->
## FILE: packages/service/tests/assets/acceptance/session_management/2SwitchMultiplexer1Smu2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/acceptance/session_management/2SwitchMultiplexer1Smu2Pin1Site.pinmap`
- sha256: `6ca585a9c35f3e976d7a4533238c5ff8907a814b2201c6c7bcc389ab7731cfee`
- bytes: 1096

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.6" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<Multiplexer name="Multiplexer1" multiplexerTypeId="MyMultiplexerType" />
		<Multiplexer name="Multiplexer2" multiplexerTypeId="MyMultiplexerType" />
	</Instruments>
	<Pins>
		<DUTPin name="A" />
		<DUTPin name="B" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<MultiplexedConnection instrument="DCPower1" channel="0">
			<MultiplexedDUTPinRoute pin="A" siteNumber="0" multiplexer="Multiplexer1" routeName="b0c1-&gt;b0r0" />
		</MultiplexedConnection>
		<MultiplexedConnection instrument="DCPower1" channel="2">
			<MultiplexedDUTPinRoute pin="B" siteNumber="0" multiplexer="Multiplexer2" routeName="b0c3-&gt;b0r0" />
		</MultiplexedConnection>
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.AllAnnotations.serviceconfig sha256=b0757a1113a5b4778c7d0d3b5a58f8e25e1e20e4973d14c714ebedd026010597 bytes=683 -->
## FILE: packages/service/tests/assets/example.AllAnnotations.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.AllAnnotations.serviceconfig`
- sha256: `b0757a1113a5b4778c7d0d3b5a58f8e25e1e20e4973d14c714ebedd026010597`
- bytes: 683

````json
{
  "services": [
    {
      "displayName": "SampleMeasurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "version": "1.0.6",
      "annotations": {
        "ni/service.description": "Testing extra Client info",
        "client/extra.NumberID" : 500,
        "client/extra.Parts" : [ "A25898", "A25412" ],
        "client/extra.GroupName" : {
            "SpeakerType": "true",
            "PhoneType": "false"
        }
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.CustomAnnotations.serviceconfig sha256=f8c8164a51c506cf54c753b74623c5587b4ecd5614647a9f6c9d151f10984115 bytes=853 -->
## FILE: packages/service/tests/assets/example.CustomAnnotations.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.CustomAnnotations.serviceconfig`
- sha256: `f8c8164a51c506cf54c753b74623c5587b4ecd5614647a9f6c9d151f10984115`
- bytes: 853

````json
{
  "services": [
    {
      "displayName": "SampleMeasurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService"
      ],
      "path": "NoFile.exe",
      "version": "1.0.7",
      "annotations": {
        "description": "An annotated test measurement service.",
        "collection": "Tests.Measurements",
        "tags": [
          "test",
          "measurement"
        ],
        "custom": {
          "foo": "bar",
          "baz": [ "qux", "quux", "quuux" ],
          "snork": {
            "blarg": "flarp",
            "oogle": [ "foogle", "boogle" ],
            "ork": [ "zork", "gork", "bork" ]
          }
        }
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.localized.serviceconfig sha256=1984d3a6a647065b3be4a3743c979d0fdac5ff0c20189c867ed424909175d991 bytes=366 -->
## FILE: packages/service/tests/assets/example.localized.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.localized.serviceconfig`
- sha256: `1984d3a6a647065b3be4a3743c979d0fdac5ff0c20189c867ed424909175d991`
- bytes: 366

````json
{
  "services": [
    {
      "displayName": "示例测量",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "version": "1.0.8"
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.NoVersion.serviceconfig sha256=19d218077bb63ee74bd954e0b7ff0180e029cf5093ad085be3ad71c2f52abcad bytes=681 -->
## FILE: packages/service/tests/assets/example.NoVersion.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.NoVersion.serviceconfig`
- sha256: `19d218077bb63ee74bd954e0b7ff0180e029cf5093ad085be3ad71c2f52abcad`
- bytes: 681

````json
{
  "services": [
    {
      "displayName": "SampleMeasurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "annotations": {
        "ni/service.description": "Measure inrush current with a shorted load and validate results against configured limits.",
        "ni/service.collection": "CurrentTests.Inrush",
        "ni/service.tags": [ "powerup", "current" ]
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.OnlyCollection.serviceconfig sha256=e54f19dafb8b86c4d37c394541358afbfbda9d1968670a39bc517ae843fc7879 bytes=525 -->
## FILE: packages/service/tests/assets/example.OnlyCollection.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.OnlyCollection.serviceconfig`
- sha256: `e54f19dafb8b86c4d37c394541358afbfbda9d1968670a39bc517ae843fc7879`
- bytes: 525

````json
{
  "services": [
    {
      "displayName": "SampleMeasurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "version": "1.0.4",
      "annotations": {
        "ni/service.collection": "CurrentTests.Inrush"
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.OnlyTags.serviceconfig sha256=3878a40493cc9879edf9003451eea0846e7c469e6313a66a104a335e1b5172aa bytes=468 -->
## FILE: packages/service/tests/assets/example.OnlyTags.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.OnlyTags.serviceconfig`
- sha256: `3878a40493cc9879edf9003451eea0846e7c469e6313a66a104a335e1b5172aa`
- bytes: 468

````json
{
  "services": [
    {
      "displayName": "SampleMeasurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "version": "1.0.5",
      "annotations": {
        "ni/service.tags": [ "powerup", "current", "voltage" ]
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.serviceconfig sha256=a03ed2c11dfbf3898184c2c5ebf0954fd03e212e1a171726c4a6a7602d67405d bytes=708 -->
## FILE: packages/service/tests/assets/example.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.serviceconfig`
- sha256: `a03ed2c11dfbf3898184c2c5ebf0954fd03e212e1a171726c4a6a7602d67405d`
- bytes: 708

````json
{
  "services": [
    {
      "displayName": "SampleMeasurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService",
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "version": "1.0.1",
      "annotations": {
        "ni/service.description": "Measure inrush current with a shorted load and validate results against configured limits.",
        "ni/service.collection": "CurrentTests.Inrush",
        "ni/service.tags": [ "powerup", "current" ]
      }
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.v1.serviceconfig sha256=2be81f753e870ca724008245bafe2d32b387fea5da20e3d121f20f6089babede bytes=368 -->
## FILE: packages/service/tests/assets/example.v1.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.v1.serviceconfig`
- sha256: `2be81f753e870ca724008245bafe2d32b387fea5da20e3d121f20f6089babede`
- bytes: 368

````json
{
  "services": [
    {
      "displayName": "SampleMeasurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v1.MeasurementService"
      ],
      "version": "1.0.1",
      "path": "start.bat"
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/example.v2.serviceconfig sha256=71194affa72749c2a3e0104dfef59576dcbb91341e6d82f72dcf338ad38be3e8 bytes=370 -->
## FILE: packages/service/tests/assets/example.v2.serviceconfig

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/example.v2.serviceconfig`
- sha256: `71194affa72749c2a3e0104dfef59576dcbb91341e6d82f72dcf338ad38be3e8`
- bytes: 370

````json
{
  "services": [
    {
      "displayName": "SampleMeasurement",
      "serviceClass": "SampleMeasurement_Python",
      "descriptionUrl": "https://www.example.com/SampleMeasurement.html",
      "providedInterfaces": [
        "ni.measurementlink.measurement.v2.MeasurementService"
      ],
      "path": "start.bat",
      "version": "1.0.3"
    }
  ]
}
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/1Smu2ChannelGroup2Pin1Site.pinmap sha256=e314f603433cb2312df69b0849f6a623f6eef70b82a0df47cb0d424514f0af62 bytes=783 -->
## FILE: packages/service/tests/assets/integration/session_management/1Smu2ChannelGroup2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/1Smu2ChannelGroup2Pin1Site.pinmap`
- sha256: `e314f603433cb2312df69b0849f6a623f6eef70b82a0df47cb0d424514f0af62`
- bytes: 783

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="DCPowerChannelGroup0" channels="0,1" />
			<ChannelGroup name="DCPowerChannelGroup1" channels="2,3" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="DCPower1" channel="2" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/1Smu2Multiplexer2Pin1Site.pinmap sha256=097cdb3360307253f795cdd5fa7728cf4447f16d7f59c49649fef700dd9e9344 bytes=1088 -->
## FILE: packages/service/tests/assets/integration/session_management/1Smu2Multiplexer2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/1Smu2Multiplexer2Pin1Site.pinmap`
- sha256: `097cdb3360307253f795cdd5fa7728cf4447f16d7f59c49649fef700dd9e9344`
- bytes: 1088

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<Multiplexer name="Multiplexer1" multiplexerTypeId="" />
		<Multiplexer name="Multiplexer2" multiplexerTypeId="" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<MultiplexedConnection instrument="DCPower1" channel="0">
			<MultiplexedDUTPinRoute pin="Pin1" siteNumber="0" multiplexer="Multiplexer2" routeName="C1-&gt;r2, C2-&gt;r2" />
		</MultiplexedConnection>
		<MultiplexedConnection instrument="DCPower1" channel="1">
			<MultiplexedDUTPinRoute pin="Pin2" siteNumber="0" multiplexer="Multiplexer1" routeName="C3-&gt;r1, C4-&gt;r1" />
		</MultiplexedConnection>
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/2Digital2Group4Pin1Site.pinmap sha256=015f715462dee410ce7342d0159544efd6db2dc98e8f36bcc6af91b106bff7e8 bytes=1359 -->
## FILE: packages/service/tests/assets/integration/session_management/2Digital2Group4Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/2Digital2Group4Pin1Site.pinmap`
- sha256: `015f715462dee410ce7342d0159544efd6db2dc98e8f36bcc6af91b106bff7e8`
- bytes: 1359

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.5" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDigitalPatternInstrument name="DigitalPattern1" numberOfChannels="32" group="Digital0" />
		<NIDigitalPatternInstrument name="DigitalPattern2" numberOfChannels="32" group="Digital1" />
	</Instruments>
	<Pins>
		<DUTPin name="CS" />
		<DUTPin name="SCLK" />
		<DUTPin name="MOSI" />
		<DUTPin name="MISO" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="CS" siteNumber="0" instrument="DigitalPattern1" channel="0" />
		<Connection pin="SCLK" siteNumber="0" instrument="DigitalPattern1" channel="1" />
		<Connection pin="MOSI" siteNumber="0" instrument="DigitalPattern1" channel="2" />
		<Connection pin="MISO" siteNumber="0" instrument="DigitalPattern1" channel="3" />
		<Connection pin="CS" siteNumber="1" instrument="DigitalPattern2" channel="0" />
		<Connection pin="SCLK" siteNumber="1" instrument="DigitalPattern2" channel="1" />
		<Connection pin="MOSI" siteNumber="1" instrument="DigitalPattern2" channel="2" />
		<Connection pin="MISO" siteNumber="1" instrument="DigitalPattern2" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/2Dmm2Pin1Site.pinmap sha256=34f755eb73267093d8672b313353c2b80723c290fae84a167140d91eb9721902 bytes=629 -->
## FILE: packages/service/tests/assets/integration/session_management/2Dmm2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/2Dmm2Pin1Site.pinmap`
- sha256: `34f755eb73267093d8672b313353c2b80723c290fae84a167140d91eb9721902`
- bytes: 629

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDmmInstrument name="DMM1" />
		<NIDmmInstrument name="DMM2" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DMM1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="DMM2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/2Fgen2Pin1Site.pinmap sha256=33d0c97df0a80551e2f58bb358183549f517fa280fd39313f5d899da8e4d046f bytes=680 -->
## FILE: packages/service/tests/assets/integration/session_management/2Fgen2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/2Fgen2Pin1Site.pinmap`
- sha256: `33d0c97df0a80551e2f58bb358183549f517fa280fd39313f5d899da8e4d046f`
- bytes: 680

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIFGenInstrument name="FGEN1" numberOfChannels="1" />
		<NIFGenInstrument name="FGEN2" numberOfChannels="1" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="FGEN1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="FGEN2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/2Mio2Pin1Site.pinmap sha256=325420713db6f7095342aebbbc35bd9af2f31ed45c70a475a9d8f1855c3ff3dd bytes=730 -->
## FILE: packages/service/tests/assets/integration/session_management/2Mio2Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/2Mio2Pin1Site.pinmap`
- sha256: `325420713db6f7095342aebbbc35bd9af2f31ed45c70a475a9d8f1855c3ff3dd`
- bytes: 730

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.1">
	<Instruments>
		<NIDAQmxTask name="Dev1" taskType="AnalogInput" channelList="Dev1/ai0" />
		<NIDAQmxTask name="Dev2" taskType="AnalogInput" channelList="Dev2/ai0" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="Dev1" channel="Dev1/ai0" />
		<Connection pin="Pin2" siteNumber="0" instrument="Dev2" channel="Dev2/ai0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/2Scope2Pin2Group1Site.pinmap sha256=b021f1a86165851effd9e717861f551c90f21d55469b74e2c92f060069115963 bytes=716 -->
## FILE: packages/service/tests/assets/integration/session_management/2Scope2Pin2Group1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/2Scope2Pin2Group1Site.pinmap`
- sha256: `b021f1a86165851effd9e717861f551c90f21d55469b74e2c92f060069115963`
- bytes: 716

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.5">
	<Instruments>
		<NIScopeInstrument name="SCOPE1" numberOfChannels="4" group="Scope0" />
		<NIScopeInstrument name="SCOPE2" numberOfChannels="4" group="Scope1" />
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
		<DUTPin name="Pin2" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="SCOPE1" channel="0" />
		<Connection pin="Pin2" siteNumber="0" instrument="SCOPE2" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/2Switch2Relay1Site.pinmap sha256=ac41fc05a84733a0adcfb0c82d583800b796534cdbee9ca617fed3dae596d5c2 bytes=842 -->
## FILE: packages/service/tests/assets/integration/session_management/2Switch2Relay1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/2Switch2Relay1Site.pinmap`
- sha256: `ac41fc05a84733a0adcfb0c82d583800b796534cdbee9ca617fed3dae596d5c2`
- bytes: 842

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.4">
	<Instruments>
		<NIRelayDriverModule name="RelayDriver1" numberOfControlLines="64" />
		<NIRelayDriverModule name="RelayDriver2" numberOfControlLines="64" />
	</Instruments>
	<Pins></Pins>
	<PinGroups></PinGroups>
	<Relays>
		<SiteRelay name="SiteRelay1" />
		<SiteRelay name="SiteRelay2" />
	</Relays>
	<RelayGroups></RelayGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<RelayConnection relay="SiteRelay1" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K0" />
		<RelayConnection relay="SiteRelay2" siteNumber="0" relayDriverModule="RelayDriver2" controlLine="K1" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/PinMapA_3Instruments_3DutPins_2SystemPins_2Sites.pinmap sha256=cb8a0c8ce2ec9868046430b4f15713130bbb89e3fcbda469046358f1aebd3fd8 bytes=1445 -->
## FILE: packages/service/tests/assets/integration/session_management/PinMapA_3Instruments_3DutPins_2SystemPins_2Sites.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/PinMapA_3Instruments_3DutPins_2SystemPins_2Sites.pinmap`
- sha256: `cb8a0c8ce2ec9868046430b4f15713130bbb89e3fcbda469046358f1aebd3fd8`
- bytes: 1445

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.6" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<NIScopeInstrument name="SCOPE1" numberOfChannels="4" group="Scope" />
		<NIDCPowerInstrument name="DCPower2" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="A" />
		<DUTPin name="B" />
		<SystemPin name="S1" />
		<SystemPin name="S2" />
		<DUTPin name="C" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="A" siteNumber="0" instrument="DCPower1" channel="0" />
		<Connection pin="A" siteNumber="1" instrument="DCPower1" channel="1" />
		<Connection pin="B" siteNumber="0" instrument="DCPower1" channel="2" />
		<Connection pin="B" siteNumber="1" instrument="DCPower2" channel="1" />
		<Connection pin="C" siteNumber="0" instrument="SCOPE1" channel="0" />
		<Connection pin="C" siteNumber="1" instrument="SCOPE1" channel="1" />
		<SystemConnection pin="S1" instrument="DCPower1" channel="3" />
		<SystemConnection pin="S2" instrument="SCOPE1" channel="3" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/PinMapB_3Instruments_3DutPins_2SystemPins_2Sites_SharedPins.pinmap sha256=2a3a302353fc8f6a7b041878392927b5251eaa251ae10b7bd5bd77150e3cf0c9 bytes=1375 -->
## FILE: packages/service/tests/assets/integration/session_management/PinMapB_3Instruments_3DutPins_2SystemPins_2Sites_SharedPins.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/PinMapB_3Instruments_3DutPins_2SystemPins_2Sites_SharedPins.pinmap`
- sha256: `2a3a302353fc8f6a7b041878392927b5251eaa251ae10b7bd5bd77150e3cf0c9`
- bytes: 1375

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.4" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <Instruments>
        <NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
            <ChannelGroup name="CommonDCPowerChannelGroup" />
        </NIDCPowerInstrument>
        <NIScopeInstrument name="SCOPE1" numberOfChannels="4" group="Scope" />
        <NIDCPowerInstrument name="DCPower2" numberOfChannels="4">
            <ChannelGroup name="CommonDCPowerChannelGroup" />
        </NIDCPowerInstrument>
    </Instruments>
    <Pins>
        <DUTPin name="A" />
        <DUTPin name="B" />
        <SystemPin name="S1" />
        <SystemPin name="S2" />
        <DUTPin name="C" />
    </Pins>
    <PinGroups></PinGroups>
    <Sites>
        <Site siteNumber="0" />
        <Site siteNumber="1" />
    </Sites>
    <Connections>
        <Connection pin="A" siteNumber="0,1" instrument="DCPower1" channel="0" />
        <Connection pin="B" siteNumber="0,1" instrument="DCPower2" channel="1" />
        <Connection pin="C" siteNumber="0,1" instrument="SCOPE1" channel="2" />
        <SystemConnection pin="S1" instrument="SCOPE1" channel="1" />
        <SystemConnection pin="S2" instrument="DCPower1" channel="2" />
    </Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/PinMapC_MultipleInstrumentsPinsRelaysAndSites.pinmap sha256=ce3770d10be50b52b178a38d1f2d45d75553a613cd34b5cbc8420eec6d4b62d4 bytes=2669 -->
## FILE: packages/service/tests/assets/integration/session_management/PinMapC_MultipleInstrumentsPinsRelaysAndSites.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/PinMapC_MultipleInstrumentsPinsRelaysAndSites.pinmap`
- sha256: `ce3770d10be50b52b178a38d1f2d45d75553a613cd34b5cbc8420eec6d4b62d4`
- bytes: 2669

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.6" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<NIScopeInstrument name="SCOPE1" numberOfChannels="4" group="Scope" />
		<NIDCPowerInstrument name="DCPower2" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<NIRelayDriverModule name="RelayDriver1" numberOfControlLines="64" />
		<NIRelayDriverModule name="RelayDriver2" numberOfControlLines="64" />
	</Instruments>
	<Pins>
		<DUTPin name="A" />
		<DUTPin name="B" />
		<SystemPin name="S1" />
		<SystemPin name="S2" />
		<DUTPin name="C" />
	</Pins>
	<PinGroups>
		<PinGroup name="PinGroup1">
			<PinReference pin="A" />
			<PinReference pin="S1" />
		</PinGroup>
		<PinGroup name="PinGroup2">
			<PinReference pin="C" />
			<PinReference pin="PinGroup1" />
		</PinGroup>
	</PinGroups>
	<Relays>
		<SiteRelay name="RelayUsingSameDriver" />
		<SiteRelay name="RelayUsingDifferentDrivers" />
		<SystemRelay name="SystemRelay" />
	</Relays>
	<RelayGroups>
		<RelayGroup name="RelayGroup1">
			<RelayReference relay="RelayUsingSameDriver" />
			<RelayReference relay="SystemRelay" />
		</RelayGroup>
		<RelayGroup name="RelayGroup2">
			<RelayReference relay="RelayGroup1" />
			<RelayReference relay="RelayUsingDifferentDrivers" />
		</RelayGroup>
	</RelayGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="A" siteNumber="0,1" instrument="DCPower1" channel="0" />
		<Connection pin="B" siteNumber="0,1" instrument="DCPower2" channel="1" />
		<Connection pin="C" siteNumber="0,1" instrument="SCOPE1" channel="2" />
		<SystemConnection pin="S1" instrument="SCOPE1" channel="1" />
		<SystemConnection pin="S2" instrument="DCPower1" channel="2" />
		<RelayConnection relay="RelayUsingDifferentDrivers" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K10" />
		<RelayConnection relay="RelayUsingDifferentDrivers" siteNumber="1" relayDriverModule="RelayDriver2" controlLine="K10" />
		<RelayConnection relay="RelayUsingSameDriver" siteNumber="0" relayDriverModule="RelayDriver1" controlLine="K0" />
		<RelayConnection relay="RelayUsingSameDriver" siteNumber="1" relayDriverModule="RelayDriver1" controlLine="K1" />
		<SystemRelayConnection relay="SystemRelay" relayDriverModule="RelayDriver1" controlLine="K60" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/integration/session_management/PinMapD_3Instruments_4DutPins_2Sites_2Multiplexers.pinmap sha256=2083a078bed68afd5aff24c9f85ea44557ca7ab8582b22490a37f657bfaaad91 bytes=1919 -->
## FILE: packages/service/tests/assets/integration/session_management/PinMapD_3Instruments_4DutPins_2Sites_2Multiplexers.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/integration/session_management/PinMapD_3Instruments_4DutPins_2Sites_2Multiplexers.pinmap`
- sha256: `2083a078bed68afd5aff24c9f85ea44557ca7ab8582b22490a37f657bfaaad91`
- bytes: 1919

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap schemaVersion="1.6" xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<NIDCPowerInstrument name="DCPower2" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
		<NIScopeInstrument name="SCOPE1" numberOfChannels="4" group="Scope" />
		<Multiplexer name="Multiplexer1" multiplexerTypeId="MyMultiplexerType" />
		<Multiplexer name="Multiplexer2" multiplexerTypeId="MyMultiplexerType" />
	</Instruments>
	<Pins>
		<DUTPin name="A" />
		<DUTPin name="B" />
		<DUTPin name="C" />
		<DUTPin name="D" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
		<Site siteNumber="1" />
	</Sites>
	<Connections>
		<Connection pin="A" siteNumber="1" instrument="DCPower1" channel="1" />
		<Connection pin="C" siteNumber="0" instrument="SCOPE1" channel="0" />
		<Connection pin="C" siteNumber="1" instrument="SCOPE1" channel="1" />
		<Connection pin="D" siteNumber="1" instrument="DCPower1" channel="3" />
		<MultiplexedConnection instrument="DCPower1" channel="0">
			<MultiplexedDUTPinRoute pin="A" siteNumber="0" multiplexer="Multiplexer1" routeName="C1-&gt;r0,C2-&gt;r0" />
			<MultiplexedDUTPinRoute pin="B" siteNumber="0" multiplexer="Multiplexer1" routeName="C3-&gt;r0,C4-&gt;r0" />
		</MultiplexedConnection>
		<MultiplexedConnection instrument="DCPower2" channel="2">
			<MultiplexedDUTPinRoute pin="B" siteNumber="1" multiplexer="Multiplexer2" routeName="C1-&gt;r2,C2-&gt;r2" />
			<MultiplexedDUTPinRoute pin="D" siteNumber="0" multiplexer="Multiplexer2" routeName="C3-&gt;r2,C4-&gt;r2" />
		</MultiplexedConnection>
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/assets/unit/pin_map/1Smu1ChannelGroup1Pin1Site.pinmap sha256=3bfd0e7dbb4bec1f88d9bf3bfd1c11b655c2850a7a73e0259cdc99d9b17646e3 bytes=605 -->
## FILE: packages/service/tests/assets/unit/pin_map/1Smu1ChannelGroup1Pin1Site.pinmap

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/assets/unit/pin_map/1Smu1ChannelGroup1Pin1Site.pinmap`
- sha256: `3bfd0e7dbb4bec1f88d9bf3bfd1c11b655c2850a7a73e0259cdc99d9b17646e3`
- bytes: 605

````text
<?xml version="1.0" encoding="utf-8"?>
<PinMap xmlns="http://www.ni.com/TestStand/SemiconductorModule/PinMap.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" schemaVersion="1.6">
	<Instruments>
		<NIDCPowerInstrument name="DCPower1" numberOfChannels="4">
			<ChannelGroup name="CommonDCPowerChannelGroup" />
		</NIDCPowerInstrument>
	</Instruments>
	<Pins>
		<DUTPin name="Pin1" />
	</Pins>
	<PinGroups></PinGroups>
	<Sites>
		<Site siteNumber="0" />
	</Sites>
	<Connections>
		<Connection pin="Pin1" siteNumber="0" instrument="DCPower1" channel="0" />
	</Connections>
</PinMap>
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/conftest.py sha256=095c0dbd182f5088020bc42a81d7c6f263c2cd991f2a1890ff7e5053e8a8b8ae bytes=5535 -->
## FILE: packages/service/tests/conftest.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/conftest.py`
- sha256: `095c0dbd182f5088020bc42a81d7c6f263c2cd991f2a1890ff7e5053e8a8b8ae`
- bytes: 5535

````python
"""Pytest configuration file."""

from __future__ import annotations

import pathlib
import sys
from collections.abc import Generator

import grpc
import pytest
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.discovery.v1.client._support import (
    _get_registration_json_file_path,
)
from ni.measurementlink.measurement.v1 import (
    measurement_service_pb2_grpc as v1_measurement_service_pb2_grpc,
)
from ni.measurementlink.measurement.v2 import (
    measurement_service_pb2_grpc as v2_measurement_service_pb2_grpc,
)
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import SessionManagementClient

from ni_measurement_plugin_sdk_service import _featuretoggles
from ni_measurement_plugin_sdk_service._featuretoggles import (
    CodeReadiness,
    FeatureToggle,
)
from ni_measurement_plugin_sdk_service.measurement.service import (
    GrpcChannelPool,
    MeasurementService,
)
from tests.utilities.discovery_service_process import DiscoveryServiceProcess


@pytest.fixture(scope="module")
def test_assets_directory() -> pathlib.Path:
    """Gets path to test_assets directory."""
    return pathlib.Path(__file__).parent / "assets"


@pytest.fixture
def grpc_channel(measurement_service: MeasurementService) -> Generator[grpc.Channel]:
    """Test fixture that creates a gRPC channel."""
    target = measurement_service.service_location.insecure_address
    options = [
        ("grpc.max_receive_message_length", -1),
        ("grpc.max_send_message_length", -1),
    ]
    with grpc.insecure_channel(target, options) as channel:
        yield channel


@pytest.fixture
def stub_v1(grpc_channel: grpc.Channel) -> v1_measurement_service_pb2_grpc.MeasurementServiceStub:
    """Test fixture that creates a MeasurementService v1 stub."""
    return v1_measurement_service_pb2_grpc.MeasurementServiceStub(grpc_channel)


@pytest.fixture
def stub_v2(grpc_channel: grpc.Channel) -> v2_measurement_service_pb2_grpc.MeasurementServiceStub:
    """Test fixture that creates a MeasurementService v2 stub."""
    return v2_measurement_service_pb2_grpc.MeasurementServiceStub(grpc_channel)


@pytest.fixture(scope="session")
def discovery_service_process() -> Generator[DiscoveryServiceProcess]:
    """Test fixture that creates discovery service process."""
    if sys.platform != "win32":
        pytest.skip(f"Platform {sys.platform} is not supported for discovery service tests.")

    try:
        registration_json_file_exists = _get_registration_json_file_path().exists()
    except FileNotFoundError:  # registry key not found
        registration_json_file_exists = False
    if not registration_json_file_exists:
        pytest.skip("Registration file not found. Ensure the Measurement Plug-In SDK is installed.")

    with DiscoveryServiceProcess() as proc:
        yield proc


@pytest.fixture(scope="session")
def grpc_channel_pool() -> Generator[GrpcChannelPool]:
    """Test fixture that creates a gRPC channel pool."""
    with GrpcChannelPool() as grpc_channel_pool:
        yield grpc_channel_pool


@pytest.fixture
def discovery_client(
    discovery_service_process: DiscoveryServiceProcess, grpc_channel_pool: GrpcChannelPool
) -> DiscoveryClient:
    """Test fixture that creates a discovery client."""
    return DiscoveryClient(grpc_channel_pool=grpc_channel_pool)


@pytest.fixture
def pin_map_client(
    discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool
) -> PinMapClient:
    """Test fixture that creates a pin map client."""
    return PinMapClient(discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool)


@pytest.fixture
def session_management_client(
    discovery_client: DiscoveryClient, grpc_channel_pool: GrpcChannelPool
) -> SessionManagementClient:
    """Test fixture that creates a session management client."""
    return SessionManagementClient(
        discovery_client=discovery_client, grpc_channel_pool=grpc_channel_pool
    )


@pytest.fixture
def feature_toggles(monkeypatch: pytest.MonkeyPatch, request: pytest.FixtureRequest) -> None:
    """Test fixture that disables or enables feature toggles."""
    for mark in request.node.iter_markers():
        if mark.name in ["disable_feature_toggle", "enable_feature_toggle"]:
            feature_toggle = mark.args[0]
            assert isinstance(feature_toggle, FeatureToggle)
            monkeypatch.setattr(
                feature_toggle, "_is_enabled_override", mark.name == "enable_feature_toggle"
            )
        elif mark.name == "use_code_readiness":
            code_readiness = mark.args[0]
            assert isinstance(code_readiness, CodeReadiness)
            monkeypatch.setattr(_featuretoggles, "_CODE_READINESS_LEVEL", code_readiness)


def pytest_collection_modifyitems(items: list[pytest.Item]) -> None:
    """Hook to inject fixtures based on marks."""
    # By default, all features are enabled when running tests.
    _featuretoggles._CODE_READINESS_LEVEL = CodeReadiness.PROTOTYPE

    for item in items:
        if (
            item.get_closest_marker("disable_feature_toggle")
            or item.get_closest_marker("enable_feature_toggle")
            or item.get_closest_marker("use_code_readiness")
        ):
            assert hasattr(item, "fixturenames")
            item.fixturenames.append("feature_toggles")
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/__init__.py sha256=f7781a708413193ce45865c8a3bd2ceb0a295820657d4101ff01f1c6fc1df78e bytes=26 -->
## FILE: packages/service/tests/integration/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/__init__.py`
- sha256: `f7781a708413193ce45865c8a3bd2ceb0a295820657d4101ff01f1c6fc1df78e`
- bytes: 26

````python
"""Integration tests."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/__init__.py sha256=1526557f927451500bfa34842a5631f1605cfe6887266607009c1ec9b216bc0d bytes=70 -->
## FILE: packages/service/tests/integration/session_management/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/__init__.py`
- sha256: `1526557f927451500bfa34842a5631f1605cfe6887266607009c1ec9b216bc0d`
- bytes: 70

````python
"""Integration tests for driver-specific session management APIs."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/conftest.py sha256=8b8076423703afc4722c94e554fa66d253a31c1f4cd541a0de2a9bdc6fdf0864 bytes=338 -->
## FILE: packages/service/tests/integration/session_management/conftest.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/conftest.py`
- sha256: `8b8076423703afc4722c94e554fa66d253a31c1f4cd541a0de2a9bdc6fdf0864`
- bytes: 338

````python
"""Pytest configuration file for integration tests."""

import pathlib

import pytest


@pytest.fixture(scope="module")
def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path:
    """Test fixture that returns the pin map directory."""
    return test_assets_directory / "integration" / "session_management"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nidaqmx_reservation.py sha256=1f988d3a5dc3167395dd70651ca81eef9256d4c65b434b5c5477603c97609747 bytes=3464 -->
## FILE: packages/service/tests/integration/session_management/test_nidaqmx_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_nidaqmx_reservation.py`
- sha256: `1f988d3a5dc3167395dd70651ca81eef9256d4c65b434b5c5477603c97609747`
- bytes: 3464

````python
import pathlib
from contextlib import ExitStack

import pytest
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import ConnectionSubset, get_connection_subset

_SITE = 0


def test___single_session_reserved___create_nidaqmx_task___creates_task(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )

        session_info = stack.enter_context(reservation.create_nidaqmx_task())

        assert session_info.session is not None
        assert session_info.session_name == "Dev1"


def test___multiple_sessions_reserved___create_nidaqmx_tasks___creates_tasks(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    nidaqmx_resource = ["Dev1", "Dev2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )

        session_infos = stack.enter_context(reservation.create_nidaqmx_tasks())

        assert all([session_info.session is not None for session_info in session_infos])
        assert all(
            [
                session_info.session_name == expected_resource
                for session_info, expected_resource in zip(session_infos, nidaqmx_resource)
            ]
        )


def test___task_created___get_nidaqmx_connection___returns_connection(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_name = "Pin1"
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_name)
        )
        stack.enter_context(reservation.create_nidaqmx_task())

        connection = reservation.get_nidaqmx_connection(pin_name)

        assert get_connection_subset(connection) == ConnectionSubset(
            pin_name, _SITE, "Dev1", "Dev1/ai0"
        )


def test___tasks_created___get_nidaqmx_connections___returns_connections(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.create_nidaqmx_tasks())

        connections = reservation.get_nidaqmx_connections(pin_names)

        assert [get_connection_subset(connection) for connection in connections] == [
            ConnectionSubset(pin_names[0], _SITE, "Dev1", "Dev1/ai0"),
            ConnectionSubset(pin_names[1], _SITE, "Dev2", "Dev2/ai0"),
        ]


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Mio2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nidcpower_reservation.py sha256=cdc5527e174314deb1e50bad9edde4c999078cfcd61dc3fc8275e868626b7a50 bytes=4066 -->
## FILE: packages/service/tests/integration/session_management/test_nidcpower_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_nidcpower_reservation.py`
- sha256: `cdc5527e174314deb1e50bad9edde4c999078cfcd61dc3fc8275e868626b7a50`
- bytes: 4066

````python
import pathlib
from contextlib import ExitStack

import pytest
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import ConnectionSubset, get_connection_subset

_SITE = 0


def test___single_session_reserved___initialize_nidcpower_session___creates_single_session(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )

        session_info = stack.enter_context(reservation.initialize_nidcpower_session())

        assert session_info.session is not None
        assert (
            session_info.session_name == "DCPower1/0"
            or session_info.session_name == "niDCPower-DCPower1/0"
        )


def test___multiple_sessions_reserved___initialize_nidcpower_sessions___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    nidcpower_resources = ["DCPower1/0", "DCPower1/2"]
    nidcpower_resources2 = ["niDCPower-DCPower1/0", "niDCPower-DCPower1/2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )

        session_infos = stack.enter_context(reservation.initialize_nidcpower_sessions())

        assert all([session_info.session is not None for session_info in session_infos])
        matches1 = all(
            [
                session_info.session_name == expected_resource
                for session_info, expected_resource in zip(session_infos, nidcpower_resources)
            ]
        )
        matches2 = all(
            [
                session_info.session_name == expected_resource
                for session_info, expected_resource in zip(session_infos, nidcpower_resources2)
            ]
        )
        assert matches1 or matches2


def test___session_created___get_nidcpower_connection___returns_connection(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nidcpower_session())

        connection = reservation.get_nidcpower_connection(pin_names[0])

        assert get_connection_subset(connection) == ConnectionSubset(
            pin_names[0], _SITE, "DCPower1/0", "DCPower1/0"
        )


def test___sessions_created___get_nidcpower_connections___returns_connections(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nidcpower_sessions())

        connections = reservation.get_nidcpower_connections(pin_names)

        assert [get_connection_subset(connection) for connection in connections] == [
            ConnectionSubset(pin_names[0], _SITE, "DCPower1/0", "DCPower1/0"),
            ConnectionSubset(pin_names[1], _SITE, "DCPower1/2", "DCPower1/2"),
        ]


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "1Smu2ChannelGroup2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nidigital_reservation.py sha256=cb7d3227cf53aa79d7e7f42e854de9727ec1d9dd8fb45ea15d29ba7776fe8937 bytes=3815 -->
## FILE: packages/service/tests/integration/session_management/test_nidigital_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_nidigital_reservation.py`
- sha256: `cb7d3227cf53aa79d7e7f42e854de9727ec1d9dd8fb45ea15d29ba7776fe8937`
- bytes: 3815

````python
import pathlib
from contextlib import ExitStack

import pytest
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import ConnectionSubset, get_connection_subset


def test___single_session_reserved___initialize_nidigital_session___creates_single_session(
    pin_map_id: str,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["CS"]
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )

        session_info = stack.enter_context(reservation.initialize_nidigital_session())

        assert session_info.session is not None
        assert (
            session_info.session_name == "DigitalPattern1"
            or session_info.session_name == "niDigitalPattern-DigitalPattern1"
        )


def test___multiple_sessions_reserved___initialize_nidigital_sessions___creates_multiple_sessions(
    pin_map_id: str,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["CS", "SCLK"]
    nidigital_resource = ["DigitalPattern1", "DigitalPattern2"]
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )

        session_infos = stack.enter_context(reservation.initialize_nidigital_sessions())

        assert all([session_info.session is not None for session_info in session_infos])
        assert [
            session_info.session_name == expected_resouce
            for session_info, expected_resouce in zip(session_infos, nidigital_resource)
        ]


def test___session_created___get_nidigital_connection___returns_connection(
    pin_map_id: str,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["CS"]
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nidigital_session())

        connection = reservation.get_nidigital_connection(pin_names[0])

        assert get_connection_subset(connection) == ConnectionSubset(
            pin_names[0], 0, "DigitalPattern1", "site0/CS"
        )


def test___session_created___get_nidigital_connections___returns_connections(
    pin_map_id: str,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["CS", "SCLK"]
    pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nidigital_session())

        connections = reservation.get_nidigital_connections(pin_names)

        assert [get_connection_subset(connection) for connection in connections] == [
            ConnectionSubset(pin_names[0], 0, "DigitalPattern1", "site0/CS"),
            ConnectionSubset(pin_names[1], 0, "DigitalPattern1", "site0/SCLK"),
        ]


@pytest.fixture
def pin_map_id(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> str:
    pin_map_name = "2Digital2Group4Pin1Site.pinmap"
    return pin_map_client.update_pin_map(pin_map_directory / pin_map_name)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nidmm_reservation.py sha256=04ddca356b080195cac99e9c7ba2d8ece880f4f4977d87a87a8f5dcfd0000cc6 bytes=3825 -->
## FILE: packages/service/tests/integration/session_management/test_nidmm_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_nidmm_reservation.py`
- sha256: `04ddca356b080195cac99e9c7ba2d8ece880f4f4977d87a87a8f5dcfd0000cc6`
- bytes: 3825

````python
import pathlib
from contextlib import ExitStack

import pytest
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import ConnectionSubset, get_connection_subset

_SITE = 0


def test___single_session_reserved___initialize_nidmm_session___creates_single_session(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )

        session_info = stack.enter_context(reservation.initialize_nidmm_session())

        assert session_info.session is not None
        assert session_info.session_name == "DMM1" or session_info.session_name == "niDMM-DMM1"


def test___multiple_sessions_reserved___initialize_nidmm_sessions___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    nidmm_resource = ["DMM1", "DMM2"]
    nidmm_resource2 = ["niDMM-DMM1", "niDMM-DMM2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )

        session_infos = stack.enter_context(reservation.initialize_nidmm_sessions())

        assert all([session_info.session is not None for session_info in session_infos])
        matches1 = all(
            [
                session_info.session_name == expected_resource
                for session_info, expected_resource in zip(session_infos, nidmm_resource)
            ]
        )
        matches2 = all(
            [
                session_info.session_name == expected_resource
                for session_info, expected_resource in zip(session_infos, nidmm_resource2)
            ]
        )
        assert matches1 or matches2


def test___session_created___get_nidmm_connection___returns_connection(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_name = "Pin1"
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_name)
        )
        stack.enter_context(reservation.initialize_nidmm_session())

        connection = reservation.get_nidmm_connection(pin_name)

        assert get_connection_subset(connection) == ConnectionSubset(pin_name, _SITE, "DMM1", "0")


def test___sessions_created___get_nidmm_connections___returns_connections(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nidmm_sessions())

        connections = reservation.get_nidmm_connections(pin_names)

        assert [get_connection_subset(connection) for connection in connections] == [
            ConnectionSubset(pin_names[0], _SITE, "DMM1", "0"),
            ConnectionSubset(pin_names[1], _SITE, "DMM2", "0"),
        ]


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Dmm2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_nifgen_reservation.py sha256=21d71d08123eac38756211fcedc4285c2e8895d6e4483f5fba8c1812dc43a0ef bytes=3601 -->
## FILE: packages/service/tests/integration/session_management/test_nifgen_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_nifgen_reservation.py`
- sha256: `21d71d08123eac38756211fcedc4285c2e8895d6e4483f5fba8c1812dc43a0ef`
- bytes: 3601

````python
import pathlib
from contextlib import ExitStack

import pytest
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import ConnectionSubset, get_connection_subset

_SITE = 0


def test___single_session_reserved___initialize_nifgen_session___creates_single_session(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )

        session_info = stack.enter_context(reservation.initialize_nifgen_session())

        assert session_info.session is not None
        assert session_info.session_name == "FGEN1" or session_info.session_name == "niFGen-FGEN1"


def test___multiple_sessions_reserved___initialize_nifgen_sessions___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )

        session_infos = stack.enter_context(reservation.initialize_nifgen_sessions())

        assert all([session_info.session is not None for session_info in session_infos])
        assert (
            session_infos[0].session_name == "FGEN1"
            or session_infos[0].session_name == "niFGen-FGEN1"
        )
        assert (
            session_infos[1].session_name == "FGEN2"
            or session_infos[1].session_name == "niFGen-FGEN2"
        )


def test___session_created___get_nifgen_connection___returns_connection(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nifgen_session())

        connection = reservation.get_nifgen_connection(pin_names[0])

        assert get_connection_subset(connection) == ConnectionSubset(
            pin_names[0], _SITE, "FGEN1", "0"
        )


def test___sessions_created___get_nifgen_connections___returns_connections(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nifgen_sessions())

        connections = reservation.get_nifgen_connections(pin_names)

        assert [get_connection_subset(connection) for connection in connections] == [
            ConnectionSubset(pin_names[0], _SITE, "FGEN1", "0"),
            ConnectionSubset(pin_names[1], _SITE, "FGEN2", "0"),
        ]


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Fgen2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_niscope_reservation.py sha256=38fd5f4c27e6672390d7668640845827b24b93ce171c4587e7438171be8a880b bytes=3656 -->
## FILE: packages/service/tests/integration/session_management/test_niscope_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_niscope_reservation.py`
- sha256: `38fd5f4c27e6672390d7668640845827b24b93ce171c4587e7438171be8a880b`
- bytes: 3656

````python
import pathlib
from contextlib import ExitStack

import pytest
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import ConnectionSubset, get_connection_subset

_SITE = 0


def test___single_session_reserved___initialize_niscope_session___creates_single_session(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )

        session_info = stack.enter_context(reservation.initialize_niscope_session())

        assert session_info.session is not None
        assert (
            session_info.session_name == "SCOPE1" or session_info.session_name == "niScope-SCOPE1"
        )


def test___multiple_sessions_reserved___initialize_niscope_sessions___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )

        session_infos = stack.enter_context(reservation.initialize_niscope_sessions())

        assert all([session_info.session is not None for session_info in session_infos])
        assert (
            session_infos[0].session_name == "SCOPE1"
            or session_infos[0].session_name == "niScope-SCOPE1"
        )
        assert (
            session_infos[1].session_name == "SCOPE2"
            or session_infos[1].session_name == "niScope-SCOPE2"
        )


def test___session_created___get_niscope_connection___returns_connection(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_niscope_session())

        connection = reservation.get_niscope_connection(pin_names[0])

        assert get_connection_subset(connection) == ConnectionSubset(
            pin_names[0], _SITE, "SCOPE1", "0"
        )


def test___sessions_created___get_niscope_connections___returns_connections(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_niscope_sessions())

        connections = reservation.get_niscope_connections(pin_names)

        assert [get_connection_subset(connection) for connection in connections] == [
            ConnectionSubset(pin_names[0], _SITE, "SCOPE1", "0"),
            ConnectionSubset(pin_names[1], _SITE, "SCOPE2", "0"),
        ]


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Scope2Pin2Group1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_niswitch_multiplexer_reservation.py sha256=9fe5bf06c070d65f925b22ab4bd5a89a7129b6ae8f2574c9c636b7673611e7c8 bytes=4953 -->
## FILE: packages/service/tests/integration/session_management/test_niswitch_multiplexer_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_niswitch_multiplexer_reservation.py`
- sha256: `9fe5bf06c070d65f925b22ab4bd5a89a7129b6ae8f2574c9c636b7673611e7c8`
- bytes: 4953

````python
import pathlib
from contextlib import ExitStack

import niswitch
import pytest
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import (
    ConnectionSubset,
    get_connection_subset_with_multiplexer,
)

_SITE = 0


def test___reserved_single_session_with_single_multiplexer___initialize_niswitch_multiplexer_session___creates_single_multiplexer_session(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )

        multiplexer_session_info = stack.enter_context(
            reservation.initialize_niswitch_multiplexer_session()
        )

        assert multiplexer_session_info.session is not None
        assert multiplexer_session_info.session_name == "Multiplexer2"


def test___reserved_sessions_with_multiple_multiplexer___initialize_niswitch_multiplexer_sessions___creates_multiple_multiplexer_sessions(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    niswitch_multiplexer_resources = ["Multiplexer1", "Multiplexer2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )

        multiplexer_session_infos = stack.enter_context(
            reservation.initialize_niswitch_multiplexer_sessions()
        )

        assert all([session_info.session is not None for session_info in multiplexer_session_infos])
        assert [
            session_info.session_name == expected_resource
            for session_info, expected_resource in zip(
                multiplexer_session_infos, niswitch_multiplexer_resources
            )
        ]


def test___created_single_session___get_nidcpower_connection_with_multiplexer___returns_connection_with_multiplexer_session(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nidcpower_session())
        stack.enter_context(reservation.initialize_niswitch_multiplexer_session())

        connection = reservation.get_nidcpower_connection_with_multiplexer(
            niswitch.Session, pin_names[0]
        )

        assert connection.multiplexer_session is not None
        assert get_connection_subset_with_multiplexer(connection) == ConnectionSubset(
            pin_names[0],
            _SITE,
            "DCPower1/0, DCPower1/1",
            "DCPower1/0",
            "Multiplexer2",
            "C1->r2, C2->r2",
        )


def test___created_multiple_sessions___get_nidcpower_connections_with_multiplexer___returns_connections_with_multiplexer_sessions(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    pin_names = ["Pin1", "Pin2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_names)
        )
        stack.enter_context(reservation.initialize_nidcpower_sessions())
        stack.enter_context(reservation.initialize_niswitch_multiplexer_sessions())

        connections = reservation.get_nidcpower_connections_with_multiplexer(
            niswitch.Session, pin_names
        )

        assert all([conn.multiplexer_session is not None for conn in connections])
        assert [
            get_connection_subset_with_multiplexer(connection) for connection in connections
        ] == [
            ConnectionSubset(
                pin_names[0],
                _SITE,
                "DCPower1/0, DCPower1/1",
                "DCPower1/0",
                "Multiplexer2",
                "C1->r2, C2->r2",
            ),
            ConnectionSubset(
                pin_names[1],
                _SITE,
                "DCPower1/0, DCPower1/1",
                "DCPower1/1",
                "Multiplexer1",
                "C3->r1, C4->r1",
            ),
        ]


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "1Smu2Multiplexer2Pin1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_niswitch_reservation.py sha256=a77dd38ba5a6bc3d4c2be9bc08f9a40d9a9a09b25b829aa53bf06248edf59d6a bytes=3714 -->
## FILE: packages/service/tests/integration/session_management/test_niswitch_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_niswitch_reservation.py`
- sha256: `a77dd38ba5a6bc3d4c2be9bc08f9a40d9a9a09b25b829aa53bf06248edf59d6a`
- bytes: 3714

````python
import pathlib
from contextlib import ExitStack

import pytest
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import ConnectionSubset, get_connection_subset

_SITE = 0


def test___single_session_reserved___initialize_niswitch_session___creates_single_session(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    relay_names = ["SiteRelay1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, relay_names)
        )

        session_info = stack.enter_context(reservation.initialize_niswitch_session())

        assert session_info.session is not None
        assert (
            session_info.session_name == "RelayDriver1"
            or session_info.session_name == "niRelayDriver-RelayDriver1"
        )


def test___multiple_sessions_reserved___initialize_niswitch_sessions___creates_multiple_sessions(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    relay_names = ["SiteRelay1", "SiteRelay2"]
    niswitch_resource = ["RelayDriver1", "RelayDriver2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, relay_names)
        )

        session_infos = stack.enter_context(reservation.initialize_niswitch_sessions())

        assert all([session_info.session is not None for session_info in session_infos])
        assert [
            session_info.session_name == expected_resource
            for session_info, expected_resource in zip(session_infos, niswitch_resource)
        ]


def test___session_created___get_niswitch_connection___returns_connection(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    relay_names = ["SiteRelay1"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_session(pin_map_context, relay_names)
        )
        stack.enter_context(reservation.initialize_niswitch_session())

        connection = reservation.get_niswitch_connection(relay_names[0])

        assert get_connection_subset(connection) == ConnectionSubset(
            relay_names[0], _SITE, "RelayDriver1", "K0"
        )


def test___sessions_created___get_niswitch_connections___returns_connections(
    pin_map_context: PinMapContext,
    session_management_client: SessionManagementClient,
) -> None:
    relay_names = ["SiteRelay1", "SiteRelay2"]
    with ExitStack() as stack:
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, relay_names)
        )
        stack.enter_context(reservation.initialize_niswitch_sessions())

        connections = reservation.get_niswitch_connections(relay_names)

        assert [get_connection_subset(connection) for connection in connections] == [
            ConnectionSubset(relay_names[0], _SITE, "RelayDriver1", "K0"),
            ConnectionSubset(relay_names[1], _SITE, "RelayDriver2", "K1"),
        ]


@pytest.fixture
def pin_map_context(pin_map_client: PinMapClient, pin_map_directory: pathlib.Path) -> PinMapContext:
    pin_map_name = "2Switch2Relay1Site.pinmap"
    pin_map_id = pin_map_client.update_pin_map(pin_map_directory / pin_map_name)

    return PinMapContext(pin_map_id=pin_map_id, sites=[_SITE])
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/session_management/test_reservation.py sha256=08c06ba37e2ce94d80fd7a9d5d71c7816000976fac2de0e8b3bc67f9af9076f7 bytes=29677 -->
## FILE: packages/service/tests/integration/session_management/test_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/session_management/test_reservation.py`
- sha256: `08c06ba37e2ce94d80fd7a9d5d71c7816000976fac2de0e8b3bc67f9af9076f7`
- bytes: 29677

````python
from __future__ import annotations

import pathlib
from contextlib import ExitStack

from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.sessionmanagement.v1.client import (
    INSTRUMENT_TYPE_NI_DCPOWER,
    INSTRUMENT_TYPE_NI_RELAY_DRIVER,
    INSTRUMENT_TYPE_NI_SCOPE,
    PinMapContext,
    SessionManagementClient,
)

from tests.utilities.connection_subset import (
    ConnectionSubset,
    get_connection_subset,
    get_connection_subset_with_multiplexer,
)

_PIN_MAP_A = "PinMapA_3Instruments_3DutPins_2SystemPins_2Sites.pinmap"
_PIN_MAP_A_PIN_NAMES = ["A", "B", "C", "S1", "S2"]

_PIN_MAP_B = "PinMapB_3Instruments_3DutPins_2SystemPins_2Sites_SharedPins.pinmap"
_PIN_MAP_B_PIN_NAMES = ["A", "B", "C", "S1", "S2"]

_PIN_MAP_C = "PinMapC_MultipleInstrumentsPinsRelaysAndSites.pinmap"
_PIN_MAP_C_PIN_NAMES = ["A", "B", "C", "S1", "S2"]
_PIN_MAP_C_RELAY_NAMES = ["RelayUsingDifferentDrivers", "RelayUsingSameDriver", "SystemRelay"]
_PIN_MAP_C_PIN_OR_RELAY_NAMES = _PIN_MAP_C_PIN_NAMES + _PIN_MAP_C_RELAY_NAMES

_PIN_MAP_D = "PinMapD_3Instruments_4DutPins_2Sites_2Multiplexers.pinmap"
_PIN_MAP_D_PIN_NAMES = ["A", "B", "C", "D"]


def test___sessions_reserved___get_connections___connections_returned(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_A)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_A_PIN_NAMES)
        )

        connections = reservation.get_connections(object)

        nidcpower_resource = "DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3, DCPower2/1"
        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("A", 0, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("B", 0, nidcpower_resource, "DCPower1/2"),
            ConnectionSubset("C", 0, "SCOPE1", "0"),
            ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/1"),
            ConnectionSubset("B", 1, nidcpower_resource, "DCPower2/1"),
            ConnectionSubset("C", 1, "SCOPE1", "1"),
            ConnectionSubset("S1", -1, nidcpower_resource, "DCPower1/3"),
            ConnectionSubset("S2", -1, "SCOPE1", "3"),
        ]


def test___sessions_reserved___get_connections_by_pin___connections_returned(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_A)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_A_PIN_NAMES)
        )

        connections = [
            reservation.get_connections(object, pin_name) for pin_name in _PIN_MAP_A_PIN_NAMES
        ]

        nidcpower_resource = "DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3, DCPower2/1"
        assert [[get_connection_subset(conn) for conn in group] for group in connections] == [
            [
                ConnectionSubset("A", 0, nidcpower_resource, "DCPower1/0"),
                ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/1"),
            ],
            [
                ConnectionSubset("B", 0, nidcpower_resource, "DCPower1/2"),
                ConnectionSubset("B", 1, nidcpower_resource, "DCPower2/1"),
            ],
            [
                ConnectionSubset("C", 0, "SCOPE1", "0"),
                ConnectionSubset("C", 1, "SCOPE1", "1"),
            ],
            [
                ConnectionSubset("S1", -1, nidcpower_resource, "DCPower1/3"),
            ],
            [
                ConnectionSubset("S2", -1, "SCOPE1", "3"),
            ],
        ]


def test___sessions_reserved___get_connections_by_site___connections_returned(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_A)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_A_PIN_NAMES)
        )

        connections = [reservation.get_connections(object, sites=site) for site in [0, 1]]

        nidcpower_resource = "DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3, DCPower2/1"
        assert [[get_connection_subset(conn) for conn in group] for group in connections] == [
            [
                ConnectionSubset("A", 0, nidcpower_resource, "DCPower1/0"),
                ConnectionSubset("B", 0, nidcpower_resource, "DCPower1/2"),
                ConnectionSubset("C", 0, "SCOPE1", "0"),
                ConnectionSubset("S1", -1, nidcpower_resource, "DCPower1/3"),
                ConnectionSubset("S2", -1, "SCOPE1", "3"),
            ],
            [
                ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/1"),
                ConnectionSubset("B", 1, nidcpower_resource, "DCPower2/1"),
                ConnectionSubset("C", 1, "SCOPE1", "1"),
                ConnectionSubset("S1", -1, nidcpower_resource, "DCPower1/3"),
                ConnectionSubset("S2", -1, "SCOPE1", "3"),
            ],
        ]


def test___sessions_reserved___get_connections_by_instrument_type___connections_returned(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_A)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_A_PIN_NAMES)
        )

        connections = [
            reservation.get_connections(object, instrument_type_id=instrument_type_id)
            for instrument_type_id in [INSTRUMENT_TYPE_NI_DCPOWER, INSTRUMENT_TYPE_NI_SCOPE]
        ]

        nidcpower_resource = "DCPower1/0, DCPower1/1, DCPower1/2, DCPower1/3, DCPower2/1"
        assert [[get_connection_subset(conn) for conn in group] for group in connections] == [
            [
                ConnectionSubset("A", 0, nidcpower_resource, "DCPower1/0"),
                ConnectionSubset("B", 0, nidcpower_resource, "DCPower1/2"),
                ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/1"),
                ConnectionSubset("B", 1, nidcpower_resource, "DCPower2/1"),
                ConnectionSubset("S1", -1, nidcpower_resource, "DCPower1/3"),
            ],
            [
                ConnectionSubset("C", 0, "SCOPE1", "0"),
                ConnectionSubset("C", 1, "SCOPE1", "1"),
                ConnectionSubset("S2", -1, "SCOPE1", "3"),
            ],
        ]


def test___sessions_reserved_using_pin_group___get_connections_by_pins___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, "PinGroup1")
        )

        connections = reservation.get_connections(object, pin_or_relay_names=["A", "S1"])

        nidcpower_resource = "DCPower1/0, DCPower1/2, DCPower2/1"
        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("A", 0, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("S1", -1, "SCOPE1", "1"),
        ]


def test___sessions_reserved_using_nested_pin_group___get_connections_by_pins___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, "PinGroup2")
        )

        connections = reservation.get_connections(object, pin_or_relay_names=["A", "C", "S1"])

        nidcpower_resource = "DCPower1/0, DCPower1/2, DCPower2/1"
        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("A", 0, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("C", 0, "SCOPE1", "2"),
            ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("C", 1, "SCOPE1", "2"),
            ConnectionSubset("S1", -1, "SCOPE1", "1"),
        ]


def test___sessions_reserved_using_relay_group___get_connections_by_relays___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, ["RelayGroup1"])
        )

        connections = reservation.get_connections(
            object, pin_or_relay_names=["RelayUsingSameDriver", "SystemRelay"]
        )

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("RelayUsingSameDriver", 0, "RelayDriver1", "K0"),
            ConnectionSubset("SystemRelay", -1, "RelayDriver1", "K60"),
        ]


def test___sessions_reserved_using_nested_relay_group___get_connections_by_relays___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, ["RelayGroup2"])
        )

        connections = reservation.get_connections(object, pin_or_relay_names=_PIN_MAP_C_RELAY_NAMES)

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("RelayUsingDifferentDrivers", 0, "RelayDriver1", "K10"),
            ConnectionSubset("RelayUsingSameDriver", 0, "RelayDriver1", "K0"),
            ConnectionSubset("SystemRelay", -1, "RelayDriver1", "K60"),
        ]


def test___sessions_reserved___get_connections_by_pin_group___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
        pin_group = ["PinGroup1"]
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_group)
        )

        connections = reservation.get_connections(object, pin_or_relay_names=pin_group)

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("A", 0, "DCPower1/0, DCPower1/2, DCPower2/1", "DCPower1/0"),
            ConnectionSubset("S1", -1, "SCOPE1", "1"),
        ]


def test___sessions_reserved___get_connections_by_nested_pin_group___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
        pin_groups = ["PinGroup1", "PinGroup2"]
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, pin_groups)
        )

        connections = reservation.get_connections(object, pin_or_relay_names=pin_groups)

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("A", 0, "DCPower1/0, DCPower1/2, DCPower2/1", "DCPower1/0"),
            ConnectionSubset("C", 0, "SCOPE1", "2"),
            ConnectionSubset("S1", -1, "SCOPE1", "1"),
        ]


def test___sessions_reserved___get_connections_by_relay_group___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
        relay_group = ["RelayGroup1"]
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, relay_group)
        )

        connections = reservation.get_connections(object, pin_or_relay_names=relay_group)

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("RelayUsingSameDriver", 0, "RelayDriver1", "K0"),
            ConnectionSubset("SystemRelay", -1, "RelayDriver1", "K60"),
        ]


def test___sessions_reserved___get_connections_by_nested_relay_groups___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
        relay_groups = ["RelayGroup1", "RelayGroup2"]
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, relay_groups)
        )

        connections = reservation.get_connections(object, pin_or_relay_names=relay_groups)

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("RelayUsingSameDriver", 0, "RelayDriver1", "K0"),
            ConnectionSubset("RelayUsingDifferentDrivers", 0, "RelayDriver1", "K10"),
            ConnectionSubset("SystemRelay", -1, "RelayDriver1", "K60"),
        ]


def test___reserve_sessions_with_multiplexer___get_connections_with_multiplexer___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_D)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_D_PIN_NAMES)
        )

        connections = reservation.get_connections_with_multiplexer(object, object)

        nidcpower_resource = "DCPower1/0, DCPower1/1, DCPower1/3, DCPower2/2"
        assert [get_connection_subset_with_multiplexer(conn) for conn in connections] == [
            ConnectionSubset(
                "A", 0, nidcpower_resource, "DCPower1/0", "Multiplexer1", "C1->r0,C2->r0"
            ),
            ConnectionSubset(
                "B", 0, nidcpower_resource, "DCPower1/0", "Multiplexer1", "C3->r0,C4->r0"
            ),
            ConnectionSubset("C", 0, "SCOPE1", "0", "", ""),
            ConnectionSubset(
                "D", 0, nidcpower_resource, "DCPower2/2", "Multiplexer2", "C3->r2,C4->r2"
            ),
            ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/1", "", ""),
            ConnectionSubset(
                "B", 1, nidcpower_resource, "DCPower2/2", "Multiplexer2", "C1->r2,C2->r2"
            ),
            ConnectionSubset("C", 1, "SCOPE1", "1", "", ""),
            ConnectionSubset("D", 1, nidcpower_resource, "DCPower1/3", "", ""),
        ]


def test___reserve_sessions_with_multiplexer___get_connections_with_multiplexer_by_pin___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_D)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_D_PIN_NAMES)
        )

        connections = [
            reservation.get_connections_with_multiplexer(object, object, pin_name)
            for pin_name in _PIN_MAP_D_PIN_NAMES
        ]

        nidcpower_resource = "DCPower1/0, DCPower1/1, DCPower1/3, DCPower2/2"
        assert [
            [get_connection_subset_with_multiplexer(conn) for conn in group]
            for group in connections
        ] == [
            [
                ConnectionSubset(
                    "A", 0, nidcpower_resource, "DCPower1/0", "Multiplexer1", "C1->r0,C2->r0"
                ),
                ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/1", "", ""),
            ],
            [
                ConnectionSubset(
                    "B", 0, nidcpower_resource, "DCPower1/0", "Multiplexer1", "C3->r0,C4->r0"
                ),
                ConnectionSubset(
                    "B", 1, nidcpower_resource, "DCPower2/2", "Multiplexer2", "C1->r2,C2->r2"
                ),
            ],
            [
                ConnectionSubset("C", 0, "SCOPE1", "0", "", ""),
                ConnectionSubset("C", 1, "SCOPE1", "1", "", ""),
            ],
            [
                ConnectionSubset(
                    "D", 0, nidcpower_resource, "DCPower2/2", "Multiplexer2", "C3->r2,C4->r2"
                ),
                ConnectionSubset("D", 1, nidcpower_resource, "DCPower1/3", "", ""),
            ],
        ]


def test___reserve_sessions_with_multiplexer___get_connections_with_multiplexer_by_site___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_D)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_D_PIN_NAMES)
        )

        connections = [
            reservation.get_connections_with_multiplexer(object, object, sites=site)
            for site in [0, 1]
        ]

        nidcpower_resource = "DCPower1/0, DCPower1/1, DCPower1/3, DCPower2/2"
        assert [
            [get_connection_subset_with_multiplexer(conn) for conn in group]
            for group in connections
        ] == [
            [
                ConnectionSubset(
                    "A", 0, nidcpower_resource, "DCPower1/0", "Multiplexer1", "C1->r0,C2->r0"
                ),
                ConnectionSubset(
                    "B", 0, nidcpower_resource, "DCPower1/0", "Multiplexer1", "C3->r0,C4->r0"
                ),
                ConnectionSubset("C", 0, "SCOPE1", "0", "", ""),
                ConnectionSubset(
                    "D", 0, nidcpower_resource, "DCPower2/2", "Multiplexer2", "C3->r2,C4->r2"
                ),
            ],
            [
                ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/1", "", ""),
                ConnectionSubset(
                    "B", 1, nidcpower_resource, "DCPower2/2", "Multiplexer2", "C1->r2,C2->r2"
                ),
                ConnectionSubset("C", 1, "SCOPE1", "1", "", ""),
                ConnectionSubset("D", 1, nidcpower_resource, "DCPower1/3", "", ""),
            ],
        ]


def test___reserve_session_with_multiplexer___get_connections_with_multiplexer_by_instrument_type___returns_connections(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_D)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_D_PIN_NAMES)
        )

        connections = [
            reservation.get_connections_with_multiplexer(
                object, object, instrument_type_id=instrument_type_id
            )
            for instrument_type_id in [INSTRUMENT_TYPE_NI_DCPOWER, INSTRUMENT_TYPE_NI_SCOPE]
        ]

        nidcpower_resource = "DCPower1/0, DCPower1/1, DCPower1/3, DCPower2/2"
        assert [
            [get_connection_subset_with_multiplexer(conn) for conn in group]
            for group in connections
        ] == [
            [
                ConnectionSubset(
                    "A", 0, nidcpower_resource, "DCPower1/0", "Multiplexer1", "C1->r0,C2->r0"
                ),
                ConnectionSubset(
                    "B", 0, nidcpower_resource, "DCPower1/0", "Multiplexer1", "C3->r0,C4->r0"
                ),
                ConnectionSubset(
                    "D", 0, nidcpower_resource, "DCPower2/2", "Multiplexer2", "C3->r2,C4->r2"
                ),
                ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/1", "", ""),
                ConnectionSubset(
                    "B", 1, nidcpower_resource, "DCPower2/2", "Multiplexer2", "C1->r2,C2->r2"
                ),
                ConnectionSubset("D", 1, nidcpower_resource, "DCPower1/3", "", ""),
            ],
            [
                ConnectionSubset("C", 0, "SCOPE1", "0", "", ""),
                ConnectionSubset("C", 1, "SCOPE1", "1", "", ""),
            ],
        ]


def test___sessions_reserved_with_shared_pins_all_sites___get_connections___returns_connections_for_all_sites(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_B)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_B_PIN_NAMES)
        )

        connections = reservation.get_connections(object)

        nidcpower_resource = "DCPower1/0, DCPower1/2, DCPower2/1"
        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("A", 0, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("B", 0, nidcpower_resource, "DCPower2/1"),
            ConnectionSubset("C", 0, "SCOPE1", "2"),
            ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("B", 1, nidcpower_resource, "DCPower2/1"),
            ConnectionSubset("C", 1, "SCOPE1", "2"),
            ConnectionSubset("S1", -1, "SCOPE1", "1"),
            ConnectionSubset("S2", -1, nidcpower_resource, "DCPower1/2"),
        ]


def test___sessions_reserved_with_shared_pins_site0___get_connections___connections_returned(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_B)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_B_PIN_NAMES)
        )

        connections = reservation.get_connections(object)

        nidcpower_resource = "DCPower1/0, DCPower1/2, DCPower2/1"
        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("A", 0, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("B", 0, nidcpower_resource, "DCPower2/1"),
            ConnectionSubset("C", 0, "SCOPE1", "2"),
            ConnectionSubset("S1", -1, "SCOPE1", "1"),
            ConnectionSubset("S2", -1, nidcpower_resource, "DCPower1/2"),
        ]


def test___sessions_reserved_with_shared_pins_site1___get_connections___connections_returned(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_B)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(pin_map_context, _PIN_MAP_B_PIN_NAMES)
        )

        connections = reservation.get_connections(object)

        nidcpower_resource = "DCPower1/0, DCPower1/2, DCPower2/1"
        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("A", 1, nidcpower_resource, "DCPower1/0"),
            ConnectionSubset("B", 1, nidcpower_resource, "DCPower2/1"),
            ConnectionSubset("C", 1, "SCOPE1", "2"),
            ConnectionSubset("S1", -1, "SCOPE1", "1"),
            ConnectionSubset("S2", -1, nidcpower_resource, "DCPower1/2"),
        ]


def test___sessions_reserved_with_relays___get_connections_for_relay_driver___connections_returned(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(
                pin_map_context, _PIN_MAP_C_PIN_OR_RELAY_NAMES
            )
        )

        connections = reservation.get_connections(
            object, instrument_type_id=INSTRUMENT_TYPE_NI_RELAY_DRIVER
        )

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("RelayUsingDifferentDrivers", 0, "RelayDriver1", "K10"),
            ConnectionSubset("RelayUsingSameDriver", 0, "RelayDriver1", "K0"),
            ConnectionSubset("RelayUsingDifferentDrivers", 1, "RelayDriver2", "K10"),
            ConnectionSubset("RelayUsingSameDriver", 1, "RelayDriver1", "K1"),
            ConnectionSubset("SystemRelay", -1, "RelayDriver1", "K60"),
        ]


def test___sessions_reserved_with_relays___get_connections_for_relay_driver_by_site___connections_returned(
    pin_map_client: PinMapClient,
    pin_map_directory: pathlib.Path,
    session_management_client: SessionManagementClient,
) -> None:
    with ExitStack() as stack:
        pin_map_id = pin_map_client.update_pin_map(pin_map_directory / _PIN_MAP_C)
        pin_map_context = PinMapContext(pin_map_id=pin_map_id, sites=[0, 1])
        reservation = stack.enter_context(
            session_management_client.reserve_sessions(
                pin_map_context, _PIN_MAP_C_PIN_OR_RELAY_NAMES
            )
        )

        connections = [
            reservation.get_connections(
                object, sites=site, instrument_type_id=INSTRUMENT_TYPE_NI_RELAY_DRIVER
            )
            for site in [0, 1]
        ]

        assert [[get_connection_subset(conn) for conn in group] for group in connections] == [
            [
                ConnectionSubset("RelayUsingDifferentDrivers", 0, "RelayDriver1", "K10"),
                ConnectionSubset("RelayUsingSameDriver", 0, "RelayDriver1", "K0"),
                ConnectionSubset("SystemRelay", -1, "RelayDriver1", "K60"),
            ],
            [
                ConnectionSubset("RelayUsingDifferentDrivers", 1, "RelayDriver2", "K10"),
                ConnectionSubset("RelayUsingSameDriver", 1, "RelayDriver1", "K1"),
                ConnectionSubset("SystemRelay", -1, "RelayDriver1", "K60"),
            ],
        ]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/integration/test_service_manager.py sha256=fd857a23b932802b0741dd0e016af9974eea2e84f547780b73e8e767aa6e27ae bytes=6492 -->
## FILE: packages/service/tests/integration/test_service_manager.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/integration/test_service_manager.py`
- sha256: `fd857a23b932802b0741dd0e016af9974eea2e84f547780b73e8e767aa6e27ae`
- bytes: 6492

````python
"""Contains test to validate service_manager.py."""

from __future__ import annotations

from typing import cast

import grpc
import pytest
from grpc import RpcError
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.discovery.v1.discovery_service_pb2_grpc import (
    DiscoveryServiceStub,
)
from ni.measurementlink.measurement.v1 import (
    measurement_service_pb2,
    measurement_service_pb2_grpc,
)

from ni_measurement_plugin_sdk_service._internal.service_manager import GrpcService
from tests.utilities.fake_discovery_service import (
    FakeDiscoveryServiceError,
    FakeDiscoveryServiceStub,
    FakeDiscoveryServiceStubError,
)
from tests.utilities.measurements import (
    loopback_measurement,
    unknown_interface_measurement,
    v1_only_measurement,
    v2_only_measurement,
)


def test___grpc_service___start_service___service_hosted(grpc_service: GrpcService):
    port_number = grpc_service.start(
        loopback_measurement.measurement_service.measurement_info,
        loopback_measurement.measurement_service.service_info,
        loopback_measurement.measurement_service._configuration_parameter_list,
        loopback_measurement.measurement_service._output_parameter_list,
        loopback_measurement.measurement_service._measure_function,
    )

    _validate_if_service_running_by_making_rpc(port_number)


def test___grpc_service_without_discovery_service___start_service___service_hosted(
    grpc_service: GrpcService,
):
    port_number = grpc_service.start(
        loopback_measurement.measurement_service.measurement_info,
        loopback_measurement.measurement_service.service_info,
        loopback_measurement.measurement_service._configuration_parameter_list,
        loopback_measurement.measurement_service._output_parameter_list,
        loopback_measurement.measurement_service._measure_function,
    )

    _validate_if_service_running_by_making_rpc(port_number)


@pytest.mark.parametrize("expect_discovery_service_error_stub", [True])
def test___grpc_service___start_service_error_registering_measurement___raises_error(
    grpc_service: GrpcService,
):
    with pytest.raises(FakeDiscoveryServiceError):
        grpc_service.start(
            loopback_measurement.measurement_service.measurement_info,
            loopback_measurement.measurement_service.service_info,
            loopback_measurement.measurement_service._configuration_parameter_list,
            loopback_measurement.measurement_service._output_parameter_list,
            loopback_measurement.measurement_service._measure_function,
        )


def test___grpc_service_started___stop_service___service_stopped(grpc_service: GrpcService):
    port_number = grpc_service.start(
        loopback_measurement.measurement_service.measurement_info,
        loopback_measurement.measurement_service.service_info,
        loopback_measurement.measurement_service._configuration_parameter_list,
        loopback_measurement.measurement_service._output_parameter_list,
        loopback_measurement.measurement_service._measure_function,
    )

    grpc_service.stop()

    with pytest.raises(RpcError):
        _validate_if_service_running_by_making_rpc(port_number)


def test___grpc_service_v2_only___start_service_and_check_v1___raises_error(
    grpc_service: GrpcService,
):
    port_number = grpc_service.start(
        v2_only_measurement.measurement_service.measurement_info,
        v2_only_measurement.measurement_service.service_info,
        v2_only_measurement.measurement_service._configuration_parameter_list,
        v2_only_measurement.measurement_service._output_parameter_list,
        v2_only_measurement.measurement_service._measure_function,
    )

    with pytest.raises(RpcError):
        _validate_if_service_running_by_making_rpc(port_number)


def test___grpc_service_v1_only___start_service_and_check_v1___service_hosted(
    grpc_service: GrpcService,
):
    port_number = grpc_service.start(
        v1_only_measurement.measurement_service.measurement_info,
        v1_only_measurement.measurement_service.service_info,
        v1_only_measurement.measurement_service._configuration_parameter_list,
        v1_only_measurement.measurement_service._output_parameter_list,
        v1_only_measurement.measurement_service._measure_function,
    )

    _validate_if_service_running_by_making_rpc(port_number)


def test___grpc_service_unknown_interface___start_service_and_check_v1___raises_error(
    grpc_service: GrpcService,
):
    with pytest.raises(ValueError):
        grpc_service.start(
            unknown_interface_measurement.measurement_service.measurement_info,
            unknown_interface_measurement.measurement_service.service_info,
            unknown_interface_measurement.measurement_service._configuration_parameter_list,
            unknown_interface_measurement.measurement_service._output_parameter_list,
            unknown_interface_measurement.measurement_service._measure_function,
        )


@pytest.fixture
def grpc_service(discovery_client: DiscoveryClient) -> GrpcService:
    """Create a GrpcService."""
    return GrpcService(discovery_client)


@pytest.fixture
def discovery_client(discovery_service_stub: FakeDiscoveryServiceStub) -> DiscoveryClient:
    """Create a DiscoveryClient."""
    return DiscoveryClient(cast(DiscoveryServiceStub, discovery_service_stub))


@pytest.fixture
def discovery_service_stub(expect_discovery_service_error_stub: bool) -> FakeDiscoveryServiceStub:
    """Create a valid/error stub based on expect_discovery_service_error_stub value."""
    return (
        FakeDiscoveryServiceStubError()
        if expect_discovery_service_error_stub
        else FakeDiscoveryServiceStub()
    )


@pytest.fixture
def expect_discovery_service_error_stub() -> bool:
    """Boolean to choose between FakeDiscoveryServiceStub and FakeDiscoveryServiceStubError."""
    return False


def _validate_if_service_running_by_making_rpc(port_number):
    """Implicit validation of running service.

    Throws exception during RPC if service not hosted.
    """
    with grpc.insecure_channel("localhost:" + port_number) as channel:
        stub = measurement_service_pb2_grpc.MeasurementServiceStub(channel)
        stub.GetMetadata(measurement_service_pb2.GetMetadataRequest())  # RPC call
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/__init__.py sha256=405938c7e4abf5f5e55e0656625f84385eb85e6453100fada3a3b3f369c284ba bytes=19 -->
## FILE: packages/service/tests/unit/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/__init__.py`
- sha256: `405938c7e4abf5f5e55e0656625f84385eb85e6453100fada3a3b3f369c284ba`
- bytes: 19

````python
"""Unit tests."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/__init__.py sha256=20f37b9160a4c6b924acf962fecf1d0c50d8bbb980ee30679872f55f3805229f bytes=66 -->
## FILE: packages/service/tests/unit/_drivers/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/__init__.py`
- sha256: `20f37b9160a4c6b924acf962fecf1d0c50d8bbb980ee30679872f55f3805229f`
- bytes: 66

````python
"""Unit tests for ni_measurement_plugin_sdk_service._drivers."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/_driver_utils.py sha256=4d6cff03ae2ce5190dc42184fc2678952f99da1c442df435fe39105f3e184505 bytes=1178 -->
## FILE: packages/service/tests/unit/_drivers/_driver_utils.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/_driver_utils.py`
- sha256: `4d6cff03ae2ce5190dc42184fc2678952f99da1c442df435fe39105f3e184505`
- bytes: 1178

````python
"""Driver-related unit test utilities."""

from __future__ import annotations

from typing import TypeVar
from unittest.mock import Mock, create_autospec

from pytest_mock import MockerFixture

from ni_measurement_plugin_sdk_service._configuration import MIDriverOptions

TSession = TypeVar("TSession")


def create_mock_session(session_type: type[TSession]) -> Mock:
    """Create a single mock session object."""
    mock = create_autospec(session_type)
    mock.__enter__.return_value = mock
    mock.__exit__.return_value = None
    return mock


def create_mock_sessions(session_type: type[TSession], count: int) -> list[Mock]:
    """Create multiple mock session objects."""
    return [create_mock_session(session_type) for _ in range(count)]


def set_simulation_options(
    driver_name: str, mocker: MockerFixture, simulate: bool, board_type: str, model: str
) -> None:
    """Set simulation options for the specified driver."""
    mocker.patch(
        f"ni.measurementlink.sessionmanagement.v1.client._drivers._{driver_name}.{driver_name.upper()}_OPTIONS",
        MIDriverOptions(driver_name, simulate, board_type, model),
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_grpcdevice.py sha256=5cecc4f1055a4061d00217fae5783bb55627e04e48b0643c55083a66c6598c8f bytes=6499 -->
## FILE: packages/service/tests/unit/_drivers/test_grpcdevice.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/test_grpcdevice.py`
- sha256: `5cecc4f1055a4061d00217fae5783bb55627e04e48b0643c55083a66c6598c8f`
- bytes: 6499

````python
from unittest.mock import Mock

import pytest
from ni.measurementlink.discovery.v1.client import ServiceLocation
from ni.measurementlink.sessionmanagement.v1.client._drivers._grpcdevice import (
    SERVICE_CLASS,
    get_grpc_device_server_location,
    get_insecure_grpc_device_server_channel,
)
from pytest_mock import MockerFixture

from tests.utilities import fake_driver


def test___default_configuration___get_grpc_device_server_location___resolves_service_and_returns_discovered_location(
    discovery_client: Mock,
) -> None:
    discovery_client.resolve_service.return_value = ServiceLocation("localhost", "1234", "")

    service_location = get_grpc_device_server_location(
        discovery_client, fake_driver.GRPC_SERVICE_INTERFACE_NAME
    )

    discovery_client.resolve_service.assert_called_with(
        provided_interface=fake_driver.GRPC_SERVICE_INTERFACE_NAME,
        deployment_target="",
        service_class=SERVICE_CLASS,
    )
    assert service_location == ServiceLocation("localhost", "1234", "")


def test___use_grpc_device_server_false___get_grpc_device_server_location___returns_empty_string(
    discovery_client: Mock,
    mocker: MockerFixture,
) -> None:
    mocker.patch(
        "ni.measurementlink.sessionmanagement.v1.client._drivers._grpcdevice.USE_GRPC_DEVICE_SERVER",
        False,
    )

    service_location = get_grpc_device_server_location(
        discovery_client, fake_driver.GRPC_SERVICE_INTERFACE_NAME
    )

    assert service_location is None


@pytest.mark.parametrize(
    "grpc_device_server_address,expected_location",
    [
        ("http://[::1]:31763", ServiceLocation("[::1]", "31763", "")),
        ("http://localhost:1234", ServiceLocation("localhost", "1234", "")),
        ("http://somehost:31763/", ServiceLocation("somehost", "31763", "")),
        ("https://somehost:31763/", ServiceLocation("somehost", "", "31763")),
    ],
)
def test___grpc_device_server_address_set___get_grpc_device_server_location___returns_configured_address(
    discovery_client: Mock,
    mocker: MockerFixture,
    grpc_device_server_address: str,
    expected_location: ServiceLocation,
) -> None:
    mocker.patch(
        "ni.measurementlink.sessionmanagement.v1.client._drivers._grpcdevice.GRPC_DEVICE_SERVER_ADDRESS",
        grpc_device_server_address,
    )

    service_location = get_grpc_device_server_location(
        discovery_client, fake_driver.GRPC_SERVICE_INTERFACE_NAME
    )

    assert service_location == expected_location


@pytest.mark.parametrize(
    "grpc_device_server_address,expected_message",
    [
        (
            "file:///c:/windows/system.ini",
            "Unsupported URL scheme 'file' in 'file:///c:/windows/system.ini'",
        ),
        (
            "http://localhost:1234/index.html",
            "Unsupported path '/index.html' in 'http://localhost:1234/index.html'",
        ),
        (
            "http://localhost:1234/;param=123",
            "Unsupported path '/;param=123' in 'http://localhost:1234/;param=123'",
        ),
        (
            "http://localhost:1234?query=123",
            "Unsupported query '?query=123' in 'http://localhost:1234?query=123'",
        ),
        (
            "http://localhost:1234#fragment",
            "Unsupported fragment '#fragment' in 'http://localhost:1234#fragment'",
        ),
        (
            "http://:1234",
            "No host specified in 'http://:1234'",
        ),
        (
            "http://localhost",
            "No port number specified in 'http://localhost'",
        ),
    ],
)
def test___grpc_device_server_address_unsupported___get_grpc_device_server_location___raises_value_error(
    discovery_client: Mock,
    mocker: MockerFixture,
    grpc_device_server_address: str,
    expected_message: str,
) -> None:
    mocker.patch(
        "ni.measurementlink.sessionmanagement.v1.client._drivers._grpcdevice.GRPC_DEVICE_SERVER_ADDRESS",
        grpc_device_server_address,
    )

    with pytest.raises(ValueError) as exc_info:
        _ = get_grpc_device_server_location(
            discovery_client, fake_driver.GRPC_SERVICE_INTERFACE_NAME
        )

    assert exc_info.value.args[0] == expected_message


def test___default_configuration___get_insecure_grpc_device_server_channel___resolves_service_and_returns_channel_with_configured_address(
    discovery_client: Mock,
    grpc_channel: Mock,
    grpc_channel_pool: Mock,
) -> None:
    discovery_client.resolve_service.return_value = ServiceLocation("localhost", "1234", "")
    grpc_channel_pool.get_channel.return_value = grpc_channel

    returned_channel = get_insecure_grpc_device_server_channel(
        discovery_client, grpc_channel_pool, fake_driver.GRPC_SERVICE_INTERFACE_NAME
    )

    discovery_client.resolve_service.assert_called_with(
        provided_interface=fake_driver.GRPC_SERVICE_INTERFACE_NAME,
        deployment_target="",
        service_class=SERVICE_CLASS,
    )
    grpc_channel_pool.get_channel.assert_called_with("localhost:1234")
    assert returned_channel is grpc_channel


def test___use_grpc_device_server_false___get_insecure_grpc_device_server_channel___returns_none(
    discovery_client: Mock,
    grpc_channel_pool: Mock,
    mocker: MockerFixture,
) -> None:
    mocker.patch(
        "ni.measurementlink.sessionmanagement.v1.client._drivers._grpcdevice.USE_GRPC_DEVICE_SERVER",
        False,
    )

    returned_channel = get_insecure_grpc_device_server_channel(
        discovery_client, grpc_channel_pool, fake_driver.GRPC_SERVICE_INTERFACE_NAME
    )

    assert returned_channel is None


def test___grpc_device_server_address_set___get_insecure_grpc_device_server_channel___returns_channel_with_configured_address(
    discovery_client: Mock,
    grpc_channel: Mock,
    grpc_channel_pool: Mock,
    mocker: MockerFixture,
) -> None:
    mocker.patch(
        "ni.measurementlink.sessionmanagement.v1.client._drivers._grpcdevice.GRPC_DEVICE_SERVER_ADDRESS",
        "http://[::1]:31763",
    )
    grpc_channel_pool.get_channel.return_value = grpc_channel

    returned_channel = get_insecure_grpc_device_server_channel(
        discovery_client, grpc_channel_pool, fake_driver.GRPC_SERVICE_INTERFACE_NAME
    )

    grpc_channel_pool.get_channel.assert_called_with("[::1]:31763")
    assert returned_channel is grpc_channel
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nidaqmx.py sha256=9dcc36a13d6fee43e1c704e1e0eacafb9b34295fe22724ea01b1aec8344e2933 bytes=7076 -->
## FILE: packages/service/tests/unit/_drivers/test_nidaqmx.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/test_nidaqmx.py`
- sha256: `9dcc36a13d6fee43e1c704e1e0eacafb9b34295fe22724ea01b1aec8344e2933`
- bytes: 7076

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import ANY, Mock

import pytest
from ni.measurementlink.sessionmanagement.v1.client import (
    INSTRUMENT_TYPE_NI_DAQMX,
    MultiSessionReservation,
    SessionInitializationBehavior,
)
from pytest_mock import MockerFixture

from tests.unit._drivers._driver_utils import create_mock_session, create_mock_sessions
from tests.unit._reservation_utils import create_grpc_session_infos

try:
    import nidaqmx
except ImportError:
    nidaqmx = None

pytestmark = pytest.mark.skipif(nidaqmx is None, reason="Requires 'nidaqmx' package.")

if nidaqmx:
    create_mock_nidaqmx_task = functools.partial(create_mock_session, nidaqmx.Task)
    create_mock_nidaqmx_tasks = functools.partial(create_mock_sessions, nidaqmx.Task)
    create_nidaqmx_session_infos = functools.partial(
        create_grpc_session_infos, INSTRUMENT_TYPE_NI_DAQMX
    )


def test___single_session_info___create_nidaqmx_task___task_created(
    task_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidaqmx_session_infos(1)
    )
    task = create_mock_nidaqmx_task()
    task_new.side_effect = [task]

    with reservation.create_nidaqmx_task() as session_info:
        assert session_info.session is task

    task_new.assert_called_once_with(nidaqmx.Task, new_task_name="MySession0", grpc_options=ANY)


def test___multiple_session_infos___create_nidaqmx_tasks___tasks_created(
    task_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidaqmx_session_infos(2)
    )
    tasks = create_mock_nidaqmx_tasks(2)
    task_new.side_effect = tasks

    with reservation.create_nidaqmx_tasks() as session_info:
        assert session_info[0].session == tasks[0]
        assert session_info[1].session == tasks[1]

    task_new.assert_any_call(nidaqmx.Task, new_task_name="MySession0", grpc_options=ANY)
    task_new.assert_any_call(nidaqmx.Task, new_task_name="MySession1", grpc_options=ANY)


def test___optional_args___create_nidaqmx_task___optional_args_passed(
    task_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidaqmx_session_infos(1)
    )
    task = create_mock_nidaqmx_task()
    task_new.side_effect = [task]

    with reservation.create_nidaqmx_task(
        initialization_behavior=SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    ):
        pass

    task_new.assert_called_once_with(
        nidaqmx.Task,
        new_task_name="MySession0",
        grpc_options=ANY,
    )
    assert (
        task_new.call_args.kwargs["grpc_options"].initialization_behavior
        == nidaqmx.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
    )


# The NI-DAQmx version of the get_connection(s) test cases uses fully
# qualified channel names.
@pytest.mark.parametrize(
    "kwargs,expected_channel_name,expected_session_index",
    [
        ({"pin_name": "Pin1", "site": 0}, "Dev1/ai0", 0),
        ({"pin_name": "Pin2", "site": 0}, "Dev1/ai1", 0),
        ({"pin_name": "Pin1", "site": 1}, "Dev2/ai2", 0),
        ({"pin_name": "Pin2", "site": 1}, "Dev3/ai0", 1),
    ],
)
def test___task_created___get_nidaqmx_connection___connection_returned(
    kwargs: dict[str, Any],
    expected_channel_name: str,
    expected_session_index: int,
    task_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nidaqmx_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1", site=0, channel="Dev1/ai0"
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin2", site=0, channel="Dev1/ai1"
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1", site=1, channel="Dev2/ai2"
        )
        grpc_session_infos[1].channel_mappings.add(
            pin_or_relay_name="Pin2", site=1, channel="Dev3/ai0"
        )
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        tasks = create_mock_nidaqmx_tasks(2)
        task_new.side_effect = tasks
        session_infos = stack.enter_context(reservation.create_nidaqmx_tasks())

        connection = reservation.get_nidaqmx_connection(**kwargs)

        assert connection.channel_name == expected_channel_name
        assert connection.session is session_infos[expected_session_index].session


@pytest.mark.parametrize(
    "kwargs,expected_channel_names,expected_session_indices",
    [
        ({}, ["Dev1/ai0", "Dev1/ai1", "Dev2/ai2", "Dev3/ai0"], [0, 0, 0, 1]),
        ({"pin_names": "Pin1"}, ["Dev1/ai0", "Dev2/ai2"], [0, 0]),
        ({"pin_names": "Pin2"}, ["Dev1/ai1", "Dev3/ai0"], [0, 1]),
        ({"sites": 0}, ["Dev1/ai0", "Dev1/ai1"], [0, 0]),
        ({"sites": 1}, ["Dev2/ai2", "Dev3/ai0"], [0, 1]),
        (
            {"pin_names": ["Pin2", "Pin1"], "sites": [1, 0]},
            ["Dev3/ai0", "Dev2/ai2", "Dev1/ai1", "Dev1/ai0"],
            [1, 0, 0, 0],
        ),
    ],
)
def test___task_created___get_nidaqmx_connections___connections_returned(
    kwargs: dict[str, Any],
    expected_channel_names: list[str],
    expected_session_indices: list[int],
    task_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nidaqmx_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1", site=0, channel="Dev1/ai0"
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin2", site=0, channel="Dev1/ai1"
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1", site=1, channel="Dev2/ai2"
        )
        grpc_session_infos[1].channel_mappings.add(
            pin_or_relay_name="Pin2", site=1, channel="Dev3/ai0"
        )
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        tasks = create_mock_nidaqmx_tasks(2)
        task_new.side_effect = tasks
        session_infos = stack.enter_context(reservation.create_nidaqmx_tasks())

        connections = reservation.get_nidaqmx_connections(**kwargs)

        assert [conn.channel_name for conn in connections] == expected_channel_names
        assert [conn.session for conn in connections] == [
            session_infos[i].session for i in expected_session_indices
        ]


@pytest.fixture
def task_new(mocker: MockerFixture) -> Mock:
    """A test fixture that patches the Task class's __new__ method."""
    return mocker.patch("nidaqmx.Task.__new__", autospec=True)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nidcpower.py sha256=23302d89cce479dfacb52809b7c6e1f083cf53958048c6e3b9131ab78e1a243e bytes=9355 -->
## FILE: packages/service/tests/unit/_drivers/test_nidcpower.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/test_nidcpower.py`
- sha256: `23302d89cce479dfacb52809b7c6e1f083cf53958048c6e3b9131ab78e1a243e`
- bytes: 9355

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import ANY, Mock

import pytest
from ni.measurementlink.sessionmanagement.v1.client import (
    INSTRUMENT_TYPE_NI_DCPOWER,
    MultiSessionReservation,
    SessionInitializationBehavior,
)
from pytest_mock import MockerFixture

from tests.unit._drivers._driver_utils import (
    create_mock_session,
    create_mock_sessions,
    set_simulation_options,
)
from tests.unit._reservation_utils import create_grpc_session_infos

try:
    import nidcpower
except ImportError:
    nidcpower = None

pytestmark = pytest.mark.skipif(nidcpower is None, reason="Requires 'nidcpower' package.")

if nidcpower:
    create_mock_nidcpower_session = functools.partial(create_mock_session, nidcpower.Session)
    create_mock_nidcpower_sessions = functools.partial(create_mock_sessions, nidcpower.Session)
    create_nidcpower_session_infos = functools.partial(
        create_grpc_session_infos, INSTRUMENT_TYPE_NI_DCPOWER
    )
    set_nidcpower_simulation_options = functools.partial(set_simulation_options, "nidcpower")


def test___single_session_info___initialize_nidcpower_session___session_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidcpower_session_infos(1)
    )
    session = create_mock_nidcpower_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidcpower_session(options={}) as session_info:
        assert session_info.session is session

    session_new.assert_called_once_with(
        nidcpower.Session, resource_name="Dev0", reset=False, options={}, grpc_options=ANY
    )


def test___multiple_session_infos___initialize_nidcpower_sessions___sessions_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidcpower_session_infos(2)
    )
    sessions = create_mock_nidcpower_sessions(3)
    session_new.side_effect = sessions

    with reservation.initialize_nidcpower_sessions(options={}) as session_info:
        assert session_info[0].session == sessions[0]
        assert session_info[1].session == sessions[1]

    session_new.assert_any_call(
        nidcpower.Session, resource_name="Dev0", reset=False, options={}, grpc_options=ANY
    )
    session_new.assert_any_call(
        nidcpower.Session, resource_name="Dev1", reset=False, options={}, grpc_options=ANY
    )


def test___optional_args___initialize_nidcpower_session___optional_args_passed(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidcpower_session_infos(1)
    )
    session = create_mock_nidcpower_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidcpower_session(
        reset=True,
        options={"simulate": False},
        initialization_behavior=SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    ):
        pass

    session_new.assert_called_once_with(
        nidcpower.Session,
        resource_name="Dev0",
        reset=True,
        options={"simulate": False},
        grpc_options=ANY,
    )
    assert (
        session_new.call_args.kwargs["grpc_options"].initialization_behavior
        == nidcpower.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
    )


def test___simulation_configured___initialize_nidcpower_session___simulation_options_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_nidcpower_simulation_options(mocker, True, "PXIe", "4147")
    reservation = MultiSessionReservation(
        session_management_client, create_nidcpower_session_infos(1)
    )
    session = create_mock_nidcpower_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidcpower_session():
        pass

    expected_options = {"simulate": True, "driver_setup": {"BoardType": "PXIe", "Model": "4147"}}
    session_new.assert_called_once_with(
        nidcpower.Session,
        resource_name="Dev0",
        reset=False,
        options=expected_options,
        grpc_options=ANY,
    )


def test___optional_args_and_simulation_configured___initialize_nidcpower_session___optional_args_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_nidcpower_simulation_options(mocker, True, "PXIe", "4147")
    reservation = MultiSessionReservation(
        session_management_client, create_nidcpower_session_infos(1)
    )
    session = create_mock_nidcpower_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidcpower_session(reset=True, options={"simulate": False}):
        pass

    expected_options = {"simulate": False}
    session_new.assert_called_once_with(
        nidcpower.Session,
        resource_name="Dev0",
        reset=True,
        options=expected_options,
        grpc_options=ANY,
    )


# The NI-DCPower version of the get_connection(s) test cases uses fully
# qualified channel names.
@pytest.mark.parametrize(
    "kwargs,expected_channel_name,expected_session_index",
    [
        ({"pin_name": "Pin1", "site": 0}, "Dev1/0", 0),
        ({"pin_name": "Pin2", "site": 0}, "Dev1/1", 0),
        ({"pin_name": "Pin1", "site": 1}, "Dev2/2", 0),
        ({"pin_name": "Pin2", "site": 1}, "Dev3/0", 1),
    ],
)
def test___session_created___get_nidcpower_connection___connection_returned(
    kwargs: dict[str, Any],
    expected_channel_name: str,
    expected_session_index: int,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nidcpower_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1", site=0, channel="Dev1/0"
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin2", site=0, channel="Dev1/1"
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1", site=1, channel="Dev2/2"
        )
        grpc_session_infos[1].channel_mappings.add(
            pin_or_relay_name="Pin2", site=1, channel="Dev3/0"
        )
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_nidcpower_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_nidcpower_sessions())

        connection = reservation.get_nidcpower_connection(**kwargs)

        assert connection.channel_name == expected_channel_name
        assert connection.session is session_infos[expected_session_index].session


@pytest.mark.parametrize(
    "kwargs,expected_channel_names,expected_session_indices",
    [
        ({}, ["Dev1/0", "Dev1/1", "Dev2/2", "Dev3/0"], [0, 0, 0, 1]),
        ({"pin_names": "Pin1"}, ["Dev1/0", "Dev2/2"], [0, 0]),
        ({"pin_names": "Pin2"}, ["Dev1/1", "Dev3/0"], [0, 1]),
        ({"sites": 0}, ["Dev1/0", "Dev1/1"], [0, 0]),
        ({"sites": 1}, ["Dev2/2", "Dev3/0"], [0, 1]),
        (
            {"pin_names": ["Pin2", "Pin1"], "sites": [1, 0]},
            ["Dev3/0", "Dev2/2", "Dev1/1", "Dev1/0"],
            [1, 0, 0, 0],
        ),
    ],
)
def test___session_created___get_nidcpower_connections___connections_returned(
    kwargs: dict[str, Any],
    expected_channel_names: list[str],
    expected_session_indices: list[int],
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nidcpower_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1", site=0, channel="Dev1/0"
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin2", site=0, channel="Dev1/1"
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1", site=1, channel="Dev2/2"
        )
        grpc_session_infos[1].channel_mappings.add(
            pin_or_relay_name="Pin2", site=1, channel="Dev3/0"
        )
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_nidcpower_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_nidcpower_sessions())

        connections = reservation.get_nidcpower_connections(**kwargs)

        assert [conn.channel_name for conn in connections] == expected_channel_names
        assert [conn.session for conn in connections] == [
            session_infos[i].session for i in expected_session_indices
        ]


@pytest.fixture
def session_new(mocker: MockerFixture) -> Mock:
    """A test fixture that patches the Session class's __new__ method."""
    return mocker.patch("nidcpower.Session.__new__", autospec=True)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nidigital.py sha256=a0cc92f1cc0f1fe375b6e34266c2f482e0b569a19b4e09cefb47e057441d67a0 bytes=8969 -->
## FILE: packages/service/tests/unit/_drivers/test_nidigital.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/test_nidigital.py`
- sha256: `a0cc92f1cc0f1fe375b6e34266c2f482e0b569a19b4e09cefb47e057441d67a0`
- bytes: 8969

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import ANY, Mock

import pytest
from ni.measurementlink.sessionmanagement.v1.client import (
    INSTRUMENT_TYPE_NI_DIGITAL_PATTERN,
    MultiSessionReservation,
    SessionInitializationBehavior,
)
from pytest_mock import MockerFixture

from tests.unit._drivers._driver_utils import (
    create_mock_session,
    create_mock_sessions,
    set_simulation_options,
)
from tests.unit._reservation_utils import create_grpc_session_infos

try:
    import nidigital
except ImportError:
    nidigital = None

pytestmark = pytest.mark.skipif(nidigital is None, reason="Requires 'nidigital' package.")

if nidigital:
    create_mock_nidigital_session = functools.partial(create_mock_session, nidigital.Session)
    create_mock_nidigital_sessions = functools.partial(create_mock_sessions, nidigital.Session)
    create_nidigital_session_infos = functools.partial(
        create_grpc_session_infos, INSTRUMENT_TYPE_NI_DIGITAL_PATTERN
    )
    set_nidigital_simulation_options = functools.partial(set_simulation_options, "nidigital")


def test___single_session_info___initialize_nidigital_session___session_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidigital_session_infos(1)
    )
    session = create_mock_nidigital_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidigital_session(options={}) as session_info:
        assert session_info.session is session

    session_new.assert_called_once_with(
        nidigital.Session, resource_name="Dev0", reset_device=False, options={}, grpc_options=ANY
    )


def test___multiple_session_infos___initialize_nidigital_sessions___sessions_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidigital_session_infos(2)
    )
    sessions = create_mock_nidigital_sessions(3)
    session_new.side_effect = sessions

    with reservation.initialize_nidigital_sessions(options={}) as session_info:
        assert session_info[0].session == sessions[0]
        assert session_info[1].session == sessions[1]

    session_new.assert_any_call(
        nidigital.Session, resource_name="Dev0", reset_device=False, options={}, grpc_options=ANY
    )
    session_new.assert_any_call(
        nidigital.Session, resource_name="Dev1", reset_device=False, options={}, grpc_options=ANY
    )


def test___optional_args___initialize_nidigital_session___optional_args_passed(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_nidigital_session_infos(1)
    )
    session = create_mock_nidigital_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidigital_session(
        reset_device=True,
        options={"simulate": False},
        initialization_behavior=SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    ):
        pass

    session_new.assert_called_once_with(
        nidigital.Session,
        resource_name="Dev0",
        reset_device=True,
        options={"simulate": False},
        grpc_options=ANY,
    )
    assert (
        session_new.call_args.kwargs["grpc_options"].initialization_behavior
        == nidigital.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
    )


def test___simulation_configured___initialize_nidigital_session___simulation_options_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_nidigital_simulation_options(mocker, True, "PXIe", "6570")
    reservation = MultiSessionReservation(
        session_management_client, create_nidigital_session_infos(1)
    )
    session = create_mock_nidigital_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidigital_session():
        pass

    expected_options = {
        "simulate": True,
        "driver_setup": {"BoardType": "PXIe", "Model": "6570"},
    }
    session_new.assert_called_once_with(
        nidigital.Session,
        resource_name="Dev0",
        reset_device=False,
        options=expected_options,
        grpc_options=ANY,
    )


def test___optional_args_and_simulation_configured___initialize_nidigital_session___optional_args_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_nidigital_simulation_options(mocker, True, "PXIe", "6570")
    reservation = MultiSessionReservation(
        session_management_client, create_nidigital_session_infos(1)
    )
    session = create_mock_nidigital_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidigital_session(reset_device=True, options={"simulate": False}):
        pass

    expected_options = {"simulate": False}
    session_new.assert_called_once_with(
        nidigital.Session,
        resource_name="Dev0",
        reset_device=True,
        options=expected_options,
        grpc_options=ANY,
    )


@pytest.mark.parametrize(
    "kwargs,expected_channel_name,expected_session_index",
    [
        ({"pin_name": "Pin1", "site": 0}, "0", 0),
        ({"pin_name": "Pin2", "site": 0}, "1", 0),
        ({"pin_name": "Pin1", "site": 1}, "2", 0),
        ({"pin_name": "Pin2", "site": 1}, "0", 1),
    ],
)
def test___session_created___get_nidigital_connection___connection_returned(
    kwargs: dict[str, Any],
    expected_channel_name: str,
    expected_session_index: int,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nidigital_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="1")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="2")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="0")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_nidigital_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_nidigital_sessions())

        connection = reservation.get_nidigital_connection(**kwargs)

        assert connection.channel_name == expected_channel_name
        assert connection.session is session_infos[expected_session_index].session


@pytest.mark.parametrize(
    "kwargs,expected_channel_names,expected_session_indices",
    [
        ({}, ["0", "1", "2", "0"], [0, 0, 0, 1]),
        ({"pin_names": "Pin1"}, ["0", "2"], [0, 0]),
        ({"pin_names": "Pin2"}, ["1", "0"], [0, 1]),
        ({"sites": 0}, ["0", "1"], [0, 0]),
        ({"sites": 1}, ["2", "0"], [0, 1]),
        ({"pin_names": ["Pin2", "Pin1"], "sites": [1, 0]}, ["0", "2", "1", "0"], [1, 0, 0, 0]),
    ],
)
def test___session_created___get_nidigital_connections___connections_returned(
    kwargs: dict[str, Any],
    expected_channel_names: list[str],
    expected_session_indices: list[int],
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nidigital_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="1")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="2")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="0")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_nidigital_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_nidigital_sessions())

        connections = reservation.get_nidigital_connections(**kwargs)

        assert [conn.channel_name for conn in connections] == expected_channel_names
        assert [conn.session for conn in connections] == [
            session_infos[i].session for i in expected_session_indices
        ]


@pytest.fixture
def session_new(mocker: MockerFixture) -> Mock:
    """A test fixture that patches the Session class's __new__ method."""
    return mocker.patch("nidigital.Session.__new__", autospec=True)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nidmm.py sha256=909c7d82ba2f9bd8e13d8ab2cb5661a4b83f22887fe40857b17874e1cdc5fcbd bytes=8755 -->
## FILE: packages/service/tests/unit/_drivers/test_nidmm.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/test_nidmm.py`
- sha256: `909c7d82ba2f9bd8e13d8ab2cb5661a4b83f22887fe40857b17874e1cdc5fcbd`
- bytes: 8755

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import ANY, Mock

import pytest
from ni.measurementlink.sessionmanagement.v1.client import (
    INSTRUMENT_TYPE_NI_DMM,
    MultiSessionReservation,
    SessionInitializationBehavior,
)
from pytest_mock import MockerFixture

from tests.unit._drivers._driver_utils import (
    create_mock_session,
    create_mock_sessions,
    set_simulation_options,
)
from tests.unit._reservation_utils import create_grpc_session_infos

try:
    import nidmm
except ImportError:
    nidmm = None

pytestmark = pytest.mark.skipif(nidmm is None, reason="Requires 'nidmm' package.")

if nidmm:
    create_mock_nidmm_session = functools.partial(create_mock_session, nidmm.Session)
    create_mock_nidmm_sessions = functools.partial(create_mock_sessions, nidmm.Session)
    create_nidmm_session_infos = functools.partial(
        create_grpc_session_infos, INSTRUMENT_TYPE_NI_DMM
    )
    set_nidmm_simulation_options = functools.partial(set_simulation_options, "nidmm")


def test___single_session_info___initialize_nidmm_session___session_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nidmm_session_infos(1))
    session = create_mock_nidmm_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidmm_session(options={}) as session_info:
        assert session_info.session is session

    session_new.assert_called_once_with(
        nidmm.Session, resource_name="Dev0", reset_device=False, options={}, grpc_options=ANY
    )


def test___multiple_session_infos___initialize_nidmm_sessions___sessions_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nidmm_session_infos(2))
    sessions = create_mock_nidmm_sessions(3)
    session_new.side_effect = sessions

    with reservation.initialize_nidmm_sessions(options={}) as session_info:
        assert session_info[0].session == sessions[0]
        assert session_info[1].session == sessions[1]

    session_new.assert_any_call(
        nidmm.Session, resource_name="Dev0", reset_device=False, options={}, grpc_options=ANY
    )
    session_new.assert_any_call(
        nidmm.Session, resource_name="Dev1", reset_device=False, options={}, grpc_options=ANY
    )


def test___optional_args___initialize_nidmm_session___optional_args_passed(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nidmm_session_infos(1))
    session = create_mock_nidmm_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidmm_session(
        reset_device=True,
        options={"simulate": False},
        initialization_behavior=SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    ):
        pass

    session_new.assert_called_once_with(
        nidmm.Session,
        resource_name="Dev0",
        reset_device=True,
        options={"simulate": False},
        grpc_options=ANY,
    )
    assert (
        session_new.call_args.kwargs["grpc_options"].initialization_behavior
        == nidmm.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
    )


def test___simulation_configured___initialize_nidmm_session___simulation_options_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_nidmm_simulation_options(mocker, True, "PXIe", "4081")
    reservation = MultiSessionReservation(session_management_client, create_nidmm_session_infos(1))
    session = create_mock_nidmm_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidmm_session():
        pass

    expected_options = {
        "simulate": True,
        "driver_setup": {"BoardType": "PXIe", "Model": "4081"},
    }
    session_new.assert_called_once_with(
        nidmm.Session,
        resource_name="Dev0",
        reset_device=False,
        options=expected_options,
        grpc_options=ANY,
    )


def test___optional_args_and_simulation_configured___initialize_nidmm_session___optional_args_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_nidmm_simulation_options(mocker, True, "PXIe", "4081")
    reservation = MultiSessionReservation(session_management_client, create_nidmm_session_infos(1))
    session = create_mock_nidmm_session()
    session_new.side_effect = [session]

    with reservation.initialize_nidmm_session(reset_device=True, options={"simulate": False}):
        pass

    expected_options = {"simulate": False}
    session_new.assert_called_once_with(
        nidmm.Session,
        resource_name="Dev0",
        reset_device=True,
        options=expected_options,
        grpc_options=ANY,
    )


# The NI-DMM version of the get_connection(s) test cases is limited to 1 channel
# per session.
@pytest.mark.parametrize(
    "kwargs,expected_channel_name,expected_session_index",
    [
        ({"pin_name": "Pin1", "site": 0}, "0", 0),
        ({"pin_name": "Pin2", "site": 0}, "0", 1),
        ({"pin_name": "Pin1", "site": 1}, "0", 2),
        ({"pin_name": "Pin2", "site": 1}, "0", 3),
    ],
)
def test___session_created___get_nidmm_connection___connection_returned(
    kwargs: dict[str, Any],
    expected_channel_name: str,
    expected_session_index: int,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nidmm_session_infos(4)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="0")
        grpc_session_infos[2].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="0")
        grpc_session_infos[3].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="0")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_nidmm_sessions(4)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_nidmm_sessions())

        connection = reservation.get_nidmm_connection(**kwargs)

        assert connection.channel_name == expected_channel_name
        assert connection.session is session_infos[expected_session_index].session


@pytest.mark.parametrize(
    "kwargs,expected_channel_names,expected_session_indices",
    [
        ({}, ["0", "0", "0", "0"], [0, 1, 2, 3]),
        ({"pin_names": "Pin1"}, ["0", "0"], [0, 2]),
        ({"pin_names": "Pin2"}, ["0", "0"], [1, 3]),
        ({"sites": 0}, ["0", "0"], [0, 1]),
        ({"sites": 1}, ["0", "0"], [2, 3]),
        ({"pin_names": ["Pin2", "Pin1"], "sites": [1, 0]}, ["0", "0", "0", "0"], [3, 2, 1, 0]),
    ],
)
def test___session_created___get_nidmm_connections___connections_returned(
    kwargs: dict[str, Any],
    expected_channel_names: list[str],
    expected_session_indices: list[int],
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nidmm_session_infos(4)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="0")
        grpc_session_infos[2].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="0")
        grpc_session_infos[3].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="0")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_nidmm_sessions(4)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_nidmm_sessions())

        connections = reservation.get_nidmm_connections(**kwargs)

        assert [conn.channel_name for conn in connections] == expected_channel_names
        assert [conn.session for conn in connections] == [
            session_infos[i].session for i in expected_session_indices
        ]


@pytest.fixture
def session_new(mocker: MockerFixture) -> Mock:
    """A test fixture that patches the Session class's __new__ method."""
    return mocker.patch("nidmm.Session.__new__", autospec=True)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_nifgen.py sha256=364087bcde25bcd28e4e9c95e52098bba1260ab77e5d5f39cf9a193ddaef24f9 bytes=8829 -->
## FILE: packages/service/tests/unit/_drivers/test_nifgen.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/test_nifgen.py`
- sha256: `364087bcde25bcd28e4e9c95e52098bba1260ab77e5d5f39cf9a193ddaef24f9`
- bytes: 8829

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import ANY, Mock

import pytest
from ni.measurementlink.sessionmanagement.v1.client import (
    INSTRUMENT_TYPE_NI_FGEN,
    MultiSessionReservation,
    SessionInitializationBehavior,
)
from pytest_mock import MockerFixture

from tests.unit._drivers._driver_utils import (
    create_mock_session,
    create_mock_sessions,
    set_simulation_options,
)
from tests.unit._reservation_utils import create_grpc_session_infos

try:
    import nifgen
except ImportError:
    nifgen = None

pytestmark = pytest.mark.skipif(nifgen is None, reason="Requires 'nifgen' package.")

if nifgen:
    create_mock_nifgen_session = functools.partial(create_mock_session, nifgen.Session)
    create_mock_nifgen_sessions = functools.partial(create_mock_sessions, nifgen.Session)
    create_nifgen_session_infos = functools.partial(
        create_grpc_session_infos, INSTRUMENT_TYPE_NI_FGEN
    )
    set_nifgen_simulation_options = functools.partial(set_simulation_options, "nifgen")


def test___single_session_info___initialize_nifgen_session___session_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifgen_session_infos(1))
    session = create_mock_nifgen_session()
    session_new.side_effect = [session]

    with reservation.initialize_nifgen_session(options={}) as session_info:
        assert session_info.session is session

    session_new.assert_called_once_with(
        nifgen.Session, resource_name="Dev0", reset_device=False, options={}, grpc_options=ANY
    )


def test___multiple_session_infos___initialize_nifgen_sessions___sessions_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifgen_session_infos(2))
    sessions = create_mock_nifgen_sessions(3)
    session_new.side_effect = sessions

    with reservation.initialize_nifgen_sessions(options={}) as session_info:
        assert session_info[0].session == sessions[0]
        assert session_info[1].session == sessions[1]

    session_new.assert_any_call(
        nifgen.Session, resource_name="Dev0", reset_device=False, options={}, grpc_options=ANY
    )
    session_new.assert_any_call(
        nifgen.Session, resource_name="Dev1", reset_device=False, options={}, grpc_options=ANY
    )


def test___optional_args___initialize_nifgen_session___optional_args_passed(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifgen_session_infos(1))
    session = create_mock_nifgen_session()
    session_new.side_effect = [session]

    with reservation.initialize_nifgen_session(
        reset_device=True,
        options={"simulate": False},
        initialization_behavior=SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    ):
        pass

    session_new.assert_called_once_with(
        nifgen.Session,
        resource_name="Dev0",
        reset_device=True,
        options={"simulate": False},
        grpc_options=ANY,
    )
    assert (
        session_new.call_args.kwargs["grpc_options"].initialization_behavior
        == nifgen.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
    )


def test___simulation_configured___initialize_nifgen_session___simulation_options_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_nifgen_simulation_options(mocker, True, "PXIe", "5423 (2CH)")
    reservation = MultiSessionReservation(session_management_client, create_nifgen_session_infos(1))
    session = create_mock_nifgen_session()
    session_new.side_effect = [session]

    with reservation.initialize_nifgen_session():
        pass

    expected_options = {
        "simulate": True,
        "driver_setup": {"BoardType": "PXIe", "Model": "5423 (2CH)"},
    }
    session_new.assert_called_once_with(
        nifgen.Session,
        resource_name="Dev0",
        reset_device=False,
        options=expected_options,
        grpc_options=ANY,
    )


def test___optional_args_and_simulation_configured___initialize_nifgen_session___optional_args_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_nifgen_simulation_options(mocker, True, "PXIe", "5423 (2CH)")
    reservation = MultiSessionReservation(session_management_client, create_nifgen_session_infos(1))
    session = create_mock_nifgen_session()
    session_new.side_effect = [session]

    with reservation.initialize_nifgen_session(reset_device=True, options={"simulate": False}):
        pass

    expected_options = {"simulate": False}
    session_new.assert_called_once_with(
        nifgen.Session,
        resource_name="Dev0",
        reset_device=True,
        options=expected_options,
        grpc_options=ANY,
    )


# The NI-FGEN version of the get_connection(s) test cases is limited to 2
# channels per session.
@pytest.mark.parametrize(
    "kwargs,expected_channel_name,expected_session_index",
    [
        ({"pin_name": "Pin1", "site": 0}, "0", 0),
        ({"pin_name": "Pin2", "site": 0}, "1", 0),
        ({"pin_name": "Pin1", "site": 1}, "0", 1),
        ({"pin_name": "Pin2", "site": 1}, "1", 1),
    ],
)
def test___session_created___get_nifgen_connection___connection_returned(
    kwargs: dict[str, Any],
    expected_channel_name: str,
    expected_session_index: int,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifgen_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="1")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="0")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="1")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_nifgen_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_nifgen_sessions())

        connection = reservation.get_nifgen_connection(**kwargs)

        assert connection.channel_name == expected_channel_name
        assert connection.session is session_infos[expected_session_index].session


@pytest.mark.parametrize(
    "kwargs,expected_channel_names,expected_session_indices",
    [
        ({}, ["0", "1", "0", "1"], [0, 0, 1, 1]),
        ({"pin_names": "Pin1"}, ["0", "0"], [0, 1]),
        ({"pin_names": "Pin2"}, ["1", "1"], [0, 1]),
        ({"sites": 0}, ["0", "1"], [0, 0]),
        ({"sites": 1}, ["0", "1"], [1, 1]),
        ({"pin_names": ["Pin2", "Pin1"], "sites": [1, 0]}, ["1", "0", "1", "0"], [1, 1, 0, 0]),
    ],
)
def test___session_created___get_nifgen_connections___connections_returned(
    kwargs: dict[str, Any],
    expected_channel_names: list[str],
    expected_session_indices: list[int],
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifgen_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="1")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="0")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="1")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_nifgen_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_nifgen_sessions())

        connections = reservation.get_nifgen_connections(**kwargs)

        assert [conn.channel_name for conn in connections] == expected_channel_names
        assert [conn.session for conn in connections] == [
            session_infos[i].session for i in expected_session_indices
        ]


@pytest.fixture
def session_new(mocker: MockerFixture) -> Mock:
    """A test fixture that patches the Session class's __new__ method."""
    return mocker.patch("nifgen.Session.__new__", autospec=True)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_niscope.py sha256=51219255900622b117a63cb099f3317b56db7ccab84d5ad0bb3b19df704c110c bytes=8863 -->
## FILE: packages/service/tests/unit/_drivers/test_niscope.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/test_niscope.py`
- sha256: `51219255900622b117a63cb099f3317b56db7ccab84d5ad0bb3b19df704c110c`
- bytes: 8863

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import ANY, Mock

import pytest
from ni.measurementlink.sessionmanagement.v1.client import (
    INSTRUMENT_TYPE_NI_SCOPE,
    MultiSessionReservation,
    SessionInitializationBehavior,
)
from pytest_mock import MockerFixture

from tests.unit._drivers._driver_utils import (
    create_mock_session,
    create_mock_sessions,
    set_simulation_options,
)
from tests.unit._reservation_utils import create_grpc_session_infos

try:
    import niscope
except ImportError:
    niscope = None

pytestmark = pytest.mark.skipif(niscope is None, reason="Requires 'niscope' package.")

if niscope:
    create_mock_niscope_session = functools.partial(create_mock_session, niscope.Session)
    create_mock_niscope_sessions = functools.partial(create_mock_sessions, niscope.Session)
    create_niscope_session_infos = functools.partial(
        create_grpc_session_infos, INSTRUMENT_TYPE_NI_SCOPE
    )
    set_niscope_simulation_options = functools.partial(set_simulation_options, "niscope")


def test___single_session_info___initialize_niscope_session___session_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_niscope_session_infos(1)
    )
    session = create_mock_niscope_session()
    session_new.side_effect = [session]

    with reservation.initialize_niscope_session(options={}) as session_info:
        assert session_info.session is session

    session_new.assert_called_once_with(
        niscope.Session, resource_name="Dev0", reset_device=False, options={}, grpc_options=ANY
    )


def test___multiple_session_infos___initialize_niscope_sessions___sessions_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_niscope_session_infos(2)
    )
    sessions = create_mock_niscope_sessions(3)
    session_new.side_effect = sessions

    with reservation.initialize_niscope_sessions(options={}) as session_info:
        assert session_info[0].session == sessions[0]
        assert session_info[1].session == sessions[1]

    session_new.assert_any_call(
        niscope.Session, resource_name="Dev0", reset_device=False, options={}, grpc_options=ANY
    )
    session_new.assert_any_call(
        niscope.Session, resource_name="Dev1", reset_device=False, options={}, grpc_options=ANY
    )


def test___optional_args___initialize_niscope_session___optional_args_passed(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_niscope_session_infos(1)
    )
    session = create_mock_niscope_session()
    session_new.side_effect = [session]

    with reservation.initialize_niscope_session(
        reset_device=True,
        options={"simulate": False},
        initialization_behavior=SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    ):
        pass

    session_new.assert_called_once_with(
        niscope.Session,
        resource_name="Dev0",
        reset_device=True,
        options={"simulate": False},
        grpc_options=ANY,
    )
    assert (
        session_new.call_args.kwargs["grpc_options"].initialization_behavior
        == niscope.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
    )


def test___simulation_configured___initialize_niscope_session___simulation_options_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_niscope_simulation_options(mocker, True, "PXIe", "5162 (4CH)")
    reservation = MultiSessionReservation(
        session_management_client, create_niscope_session_infos(1)
    )
    session = create_mock_niscope_session()
    session_new.side_effect = [session]

    with reservation.initialize_niscope_session():
        pass

    expected_options = {
        "simulate": True,
        "driver_setup": {"BoardType": "PXIe", "Model": "5162 (4CH)"},
    }
    session_new.assert_called_once_with(
        niscope.Session,
        resource_name="Dev0",
        reset_device=False,
        options=expected_options,
        grpc_options=ANY,
    )


def test___optional_args_and_simulation_configured___initialize_niscope_session___optional_args_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    set_niscope_simulation_options(mocker, True, "PXIe", "5162 (4CH)")
    reservation = MultiSessionReservation(
        session_management_client, create_niscope_session_infos(1)
    )
    session = create_mock_niscope_session()
    session_new.side_effect = [session]

    with reservation.initialize_niscope_session(reset_device=True, options={"simulate": False}):
        pass

    expected_options = {"simulate": False}
    session_new.assert_called_once_with(
        niscope.Session,
        resource_name="Dev0",
        reset_device=True,
        options=expected_options,
        grpc_options=ANY,
    )


@pytest.mark.parametrize(
    "kwargs,expected_channel_name,expected_session_index",
    [
        ({"pin_name": "Pin1", "site": 0}, "0", 0),
        ({"pin_name": "Pin2", "site": 0}, "1", 0),
        ({"pin_name": "Pin1", "site": 1}, "2", 0),
        ({"pin_name": "Pin2", "site": 1}, "0", 1),
    ],
)
def test___session_created___get_niscope_connection___connection_returned(
    kwargs: dict[str, Any],
    expected_channel_name: str,
    expected_session_index: int,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_niscope_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="1")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="2")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="0")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_niscope_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_niscope_sessions())

        connection = reservation.get_niscope_connection(**kwargs)

        assert connection.channel_name == expected_channel_name
        assert connection.session is session_infos[expected_session_index].session


@pytest.mark.parametrize(
    "kwargs,expected_channel_names,expected_session_indices",
    [
        ({}, ["0", "1", "2", "0"], [0, 0, 0, 1]),
        ({"pin_names": "Pin1"}, ["0", "2"], [0, 0]),
        ({"pin_names": "Pin2"}, ["1", "0"], [0, 1]),
        ({"sites": 0}, ["0", "1"], [0, 0]),
        ({"sites": 1}, ["2", "0"], [0, 1]),
        ({"pin_names": ["Pin2", "Pin1"], "sites": [1, 0]}, ["0", "2", "1", "0"], [1, 0, 0, 0]),
    ],
)
def test___session_created___get_niscope_connections___connections_returned(
    kwargs: dict[str, Any],
    expected_channel_names: list[str],
    expected_session_indices: list[int],
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_niscope_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="1")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="2")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="0")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_niscope_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_niscope_sessions())

        connections = reservation.get_niscope_connections(**kwargs)

        assert [conn.channel_name for conn in connections] == expected_channel_names
        assert [conn.session for conn in connections] == [
            session_infos[i].session for i in expected_session_indices
        ]


@pytest.fixture
def session_new(mocker: MockerFixture) -> Mock:
    """A test fixture that patches the Session class's __new__ method."""
    return mocker.patch("niscope.Session.__new__", autospec=True)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_drivers/test_niswitch.py sha256=7cd2a5a912771d8c81181c25393b9606e222d433858ab7b66d360c119db52bb0 bytes=9992 -->
## FILE: packages/service/tests/unit/_drivers/test_niswitch.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_drivers/test_niswitch.py`
- sha256: `7cd2a5a912771d8c81181c25393b9606e222d433858ab7b66d360c119db52bb0`
- bytes: 9992

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import ANY, Mock

import pytest
from ni.measurementlink.sessionmanagement.v1.client import (
    INSTRUMENT_TYPE_NI_RELAY_DRIVER,
    MultiSessionReservation,
    SessionInitializationBehavior,
)
from pytest_mock import MockerFixture

from ni_measurement_plugin_sdk_service._configuration import NISwitchOptions
from tests.unit._drivers._driver_utils import create_mock_session, create_mock_sessions
from tests.unit._reservation_utils import create_grpc_session_infos

try:
    import niswitch
except ImportError:
    niswitch = None

pytestmark = pytest.mark.skipif(niswitch is None, reason="Requires 'niswitch' package.")

if niswitch:
    create_mock_niswitch_session = functools.partial(create_mock_session, niswitch.Session)
    create_mock_niswitch_sessions = functools.partial(create_mock_sessions, niswitch.Session)
    create_niswitch_session_infos = functools.partial(
        create_grpc_session_infos, INSTRUMENT_TYPE_NI_RELAY_DRIVER
    )


def test___single_session_info___initialize_niswitch_session___session_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_niswitch_session_infos(1)
    )
    session = create_mock_niswitch_session()
    session_new.side_effect = [session]

    with reservation.initialize_niswitch_session(
        topology="Configured Topology",
        simulate=False,
        reset_device=False,
    ) as session_info:
        assert session_info.session is session

    session_new.assert_called_once_with(
        niswitch.Session,
        resource_name="Dev0",
        topology="Configured Topology",
        simulate=False,
        reset_device=False,
        grpc_options=ANY,
    )


def test___multiple_session_infos___initialize_niswitch_sessions___sessions_created(
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_niswitch_session_infos(2)
    )
    sessions = create_mock_niswitch_sessions(3)
    session_new.side_effect = sessions

    with reservation.initialize_niswitch_sessions(
        topology="Configured Topology",
        simulate=False,
        reset_device=False,
    ) as session_info:
        assert session_info[0].session == sessions[0]
        assert session_info[1].session == sessions[1]

    session_new.assert_any_call(
        niswitch.Session,
        resource_name="Dev0",
        topology="Configured Topology",
        simulate=False,
        reset_device=False,
        grpc_options=ANY,
    )
    session_new.assert_any_call(
        niswitch.Session,
        resource_name="Dev1",
        topology="Configured Topology",
        simulate=False,
        reset_device=False,
        grpc_options=ANY,
    )


# For NI-SWITCH, we set resource_name to "" when simulate is True.
@pytest.mark.parametrize("simulate,expected_resource_name", [(False, "Dev0"), (True, "")])
def test___optional_args___initialize_niswitch_session___optional_args_passed(
    simulate: bool,
    expected_resource_name: str,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, create_niswitch_session_infos(1)
    )
    session = create_mock_niswitch_session()
    session_new.side_effect = [session]

    with reservation.initialize_niswitch_session(
        topology="2567/Independent",
        simulate=simulate,
        reset_device=True,
        initialization_behavior=SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    ):
        pass

    session_new.assert_called_once_with(
        niswitch.Session,
        resource_name=expected_resource_name,
        topology="2567/Independent",
        simulate=simulate,
        reset_device=True,
        grpc_options=ANY,
    )
    assert (
        session_new.call_args.kwargs["grpc_options"].initialization_behavior
        == niswitch.SessionInitializationBehavior.INITIALIZE_SERVER_SESSION
    )


def test___simulation_configured___initialize_niswitch_session___simulation_options_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    _set_niswitch_simulation_options(mocker, True, "2567/Independent")
    reservation = MultiSessionReservation(
        session_management_client, create_niswitch_session_infos(1)
    )
    session = create_mock_niswitch_session()
    session_new.side_effect = [session]

    with reservation.initialize_niswitch_session():
        pass

    session_new.assert_called_once_with(
        niswitch.Session,
        resource_name="",
        topology="2567/Independent",
        simulate=True,
        reset_device=False,
        grpc_options=ANY,
    )


def test___optional_args_and_simulation_configured___initialize_niswitch_session___optional_args_passed(
    mocker: MockerFixture,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    _set_niswitch_simulation_options(mocker, True, "2567/Independent")
    reservation = MultiSessionReservation(
        session_management_client, create_niswitch_session_infos(1)
    )
    session = create_mock_niswitch_session()
    session_new.side_effect = [session]

    with reservation.initialize_niswitch_session(
        topology="2529/2-Wire 4x32 Matrix", simulate=False, reset_device=True
    ):
        pass

    session_new.assert_called_once_with(
        niswitch.Session,
        resource_name="Dev0",
        topology="2529/2-Wire 4x32 Matrix",
        simulate=False,
        reset_device=True,
        grpc_options=ANY,
    )


# The NI-SWITCH version of the get_connection(s) test cases uses relay names.
@pytest.mark.parametrize(
    "kwargs,expected_channel_name,expected_session_index",
    [
        ({"relay_name": "Relay1", "site": 0}, "K0", 0),
        ({"relay_name": "Relay2", "site": 0}, "K1", 0),
        ({"relay_name": "Relay1", "site": 1}, "K2", 0),
        ({"relay_name": "Relay2", "site": 1}, "K0", 1),
    ],
)
def test___session_created___get_niswitch_connection___connection_returned(
    kwargs: dict[str, Any],
    expected_channel_name: str,
    expected_session_index: int,
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_niswitch_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Relay1", site=0, channel="K0")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Relay2", site=0, channel="K1")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Relay1", site=1, channel="K2")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Relay2", site=1, channel="K0")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_niswitch_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_niswitch_sessions())

        connection = reservation.get_niswitch_connection(**kwargs)

        assert connection.channel_name == expected_channel_name
        assert connection.session is session_infos[expected_session_index].session


@pytest.mark.parametrize(
    "kwargs,expected_channel_names,expected_session_indices",
    [
        ({}, ["K0", "K1", "K2", "K0"], [0, 0, 0, 1]),
        ({"relay_names": "Relay1"}, ["K0", "K2"], [0, 0]),
        ({"relay_names": "Relay2"}, ["K1", "K0"], [0, 1]),
        ({"sites": 0}, ["K0", "K1"], [0, 0]),
        ({"sites": 1}, ["K2", "K0"], [0, 1]),
        (
            {"relay_names": ["Relay2", "Relay1"], "sites": [1, 0]},
            ["K0", "K2", "K1", "K0"],
            [1, 0, 0, 0],
        ),
    ],
)
def test___session_created___get_niswitch_connections___connections_returned(
    kwargs: dict[str, Any],
    expected_channel_names: list[str],
    expected_session_indices: list[int],
    session_new: Mock,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_niswitch_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Relay1", site=0, channel="K0")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Relay2", site=0, channel="K1")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Relay1", site=1, channel="K2")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Relay2", site=1, channel="K0")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        sessions = create_mock_niswitch_sessions(2)
        session_new.side_effect = sessions
        session_infos = stack.enter_context(reservation.initialize_niswitch_sessions())

        connections = reservation.get_niswitch_connections(**kwargs)

        assert [conn.channel_name for conn in connections] == expected_channel_names
        assert [conn.session for conn in connections] == [
            session_infos[i].session for i in expected_session_indices
        ]


@pytest.fixture
def session_new(mocker: MockerFixture) -> Mock:
    """A test fixture that patches the Session class's __new__ method."""
    return mocker.patch("niswitch.Session.__new__", autospec=True)


def _set_niswitch_simulation_options(mocker: MockerFixture, simulate: bool, topology: str) -> None:
    mocker.patch(
        "ni.measurementlink.sessionmanagement.v1.client._drivers._niswitch.NISWITCH_OPTIONS",
        NISwitchOptions("niswitch", simulate, topology),
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/_reservation_utils.py sha256=357f03f36f304943707f6ba908b0400f488bf36e6327b9e1ee0f10350325679d bytes=1889 -->
## FILE: packages/service/tests/unit/_reservation_utils.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/_reservation_utils.py`
- sha256: `357f03f36f304943707f6ba908b0400f488bf36e6327b9e1ee0f10350325679d`
- bytes: 1889

````python
"""Reservation-related unit test utilities."""

from __future__ import annotations

import session_pb2
from ni.measurementlink.sessionmanagement.v1 import (
    session_management_service_pb2,
)
from ni.measurementlink.sessionmanagement.v1.client import (
    MultiplexerSessionInformation,
    SessionInformation,
)

from tests.utilities import fake_driver, fake_multiplexer_driver


def create_grpc_session_infos(
    instrument_type_id: str,
    session_count: int,
) -> list[session_management_service_pb2.SessionInformation]:
    """Create a list of gRPC SessionInformation messages."""
    return [
        session_management_service_pb2.SessionInformation(
            session=session_pb2.Session(name=f"MySession{i}"),
            resource_name=f"Dev{i}",
            instrument_type_id=instrument_type_id,
        )
        for i in range(session_count)
    ]


def create_grpc_multiplexer_session_infos(
    multiplexer_type_id: str,
    session_count: int,
) -> list[session_management_service_pb2.MultiplexerSessionInformation]:
    """Create a list of gRPC MultiplexerSessionInformation messages."""
    return [
        session_management_service_pb2.MultiplexerSessionInformation(
            session=session_pb2.Session(name=f"MyMultiplexer{i}"),
            resource_name=f"Mux{i}",
            multiplexer_type_id=multiplexer_type_id,
        )
        for i in range(session_count)
    ]


def construct_session(session_info: SessionInformation) -> fake_driver.Session:
    """Constructs a session object."""
    return fake_driver.Session(session_info.resource_name)


def construct_multiplexer_session(
    session_info: MultiplexerSessionInformation,
) -> fake_multiplexer_driver.Session:
    """Constructs a multiplexer session object."""
    return fake_multiplexer_driver.Session(session_info.resource_name)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/conftest.py sha256=aad9442a2c40765cda0dcd8c5bf632b8f601f2543533692f8dc8760c72027748 bytes=3692 -->
## FILE: packages/service/tests/unit/conftest.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/conftest.py`
- sha256: `aad9442a2c40765cda0dcd8c5bf632b8f601f2543533692f8dc8760c72027748`
- bytes: 3692

````python
"""Test fixtures for unit tests."""

from __future__ import annotations

import pathlib
from collections.abc import Generator
from typing import cast
from unittest.mock import Mock

import grpc
import pytest
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.sessionmanagement.v1.client import (
    MultiSessionReservation,
    SessionManagementClient,
    SingleSessionReservation,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool
from pytest_mock import MockerFixture

from ni_measurement_plugin_sdk_service._internal import grpc_servicer
from ni_measurement_plugin_sdk_service._internal.grpc_servicer import (
    MeasurementServiceContext,
)
from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService


@pytest.fixture
def discovery_client(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock DiscoveryClient."""
    return mocker.create_autospec(DiscoveryClient)


@pytest.fixture
def grpc_channel(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock grpc.Channel."""
    return mocker.create_autospec(grpc.Channel)


@pytest.fixture
def grpc_channel_pool(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock GrpcChannelPool."""
    return mocker.create_autospec(GrpcChannelPool)


@pytest.fixture
def measurement_service_context(
    mocker: MockerFixture, measurement_service: Mock
) -> Generator[Mock]:
    """Test fixture that creates and registers a mock MeasurementServiceContext."""
    mock = mocker.create_autospec(MeasurementServiceContext)
    mock.owner = measurement_service
    token = grpc_servicer.measurement_service_context.set(cast(MeasurementServiceContext, mock))
    try:
        yield mock
    finally:
        grpc_servicer.measurement_service_context.reset(token)


@pytest.fixture
def measurement_service(
    mocker: MockerFixture,
    discovery_client: Mock,
    grpc_channel_pool: Mock,
    session_management_client: Mock,
) -> Mock:
    """Test fixture that creates a mock MeasurementService."""
    mock = mocker.create_autospec(MeasurementService)
    mock.channel_pool = grpc_channel_pool
    mock.discovery_client = discovery_client
    mock.session_management_client = session_management_client
    return mock


@pytest.fixture
def multi_session_reservation(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock MultiSessionReservation."""
    return mocker.create_autospec(MultiSessionReservation)


@pytest.fixture
def session_management_client(
    discovery_client: Mock,
    grpc_channel_pool: Mock,
    mocker: MockerFixture,
    multi_session_reservation: Mock,
    single_session_reservation: Mock,
) -> Mock:
    """Test fixture that creates a mock SessionManagementClient."""
    mock = mocker.create_autospec(SessionManagementClient)
    mock._discovery_client = discovery_client
    mock._grpc_channel_pool = grpc_channel_pool
    mock.reserve_session.return_value = single_session_reservation
    mock.reserve_sessions.return_value = multi_session_reservation
    mock.reserve_all_registered_sessions.return_value = multi_session_reservation
    return mock


@pytest.fixture
def single_session_reservation(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock SingleSessionReservation."""
    return mocker.create_autospec(SingleSessionReservation)


@pytest.fixture
def pin_map_directory(test_assets_directory: pathlib.Path) -> pathlib.Path:
    """Test fixture that returns the pin map directory."""
    return test_assets_directory / "unit" / "pin_map"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/grpc/__init__.py sha256=3044bda6a275f0def40c9ca555ef87909e450080f510d6190116388c6cc3f6be bytes=62 -->
## FILE: packages/service/tests/unit/grpc/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/grpc/__init__.py`
- sha256: `3044bda6a275f0def40c9ca555ef87909e450080f510d6190116388c6cc3f6be`
- bytes: 62

````python
"""Unit tests for ni_measurement_plugin_sdk_service.grpc."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/grpc/channelpool/__init__.py sha256=aa9ac9dc8e7a703dfcfad1d146e2c198afb7b9285d2b5327ceb2b16c9f4acc37 bytes=74 -->
## FILE: packages/service/tests/unit/grpc/channelpool/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/grpc/channelpool/__init__.py`
- sha256: `aa9ac9dc8e7a703dfcfad1d146e2c198afb7b9285d2b5327ceb2b16c9f4acc37`
- bytes: 74

````python
"""Unit tests for ni_measurement_plugin_sdk_service.grpc.channelpool."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/grpc/channelpool/test_channel_pool.py sha256=2d4ce329d4fea3418ae250380b02ed59f136c1cd916477818ae46f0aac169f44 bytes=1112 -->
## FILE: packages/service/tests/unit/grpc/channelpool/test_channel_pool.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/grpc/channelpool/test_channel_pool.py`
- sha256: `2d4ce329d4fea3418ae250380b02ed59f136c1cd916477818ae46f0aac169f44`
- bytes: 1112

````python
import pytest
from ni_grpc_extensions.channelpool import GrpcChannelPool


@pytest.mark.parametrize(
    "target,expected_result",
    [
        ("127.0.0.1", False),  # Port must be specified explicitly
        ("[::1]", False),  # Port must be specified explicitly
        ("localhost", False),  # Port must be specified explicitly
        ("127.0.0.1:100", True),
        ("[::1]:100", True),
        ("localhost:100", True),
        ("http://127.0.0.1", False),  # Port must be specified explicitly
        ("http://[::1]", False),  # Port must be specified explicitly
        ("http://localhost", False),  # Port must be specified explicitly
        ("http://127.0.0.1:100", True),
        ("http://[::1]:100", True),
        ("http://localhost:100", True),
        ("1.1.1.1:100", False),
        ("http://www.google.com:80", False),
    ],
)
def test___channel_pool___is_local___returns_expected_result(
    target: str, expected_result: bool
) -> None:
    channel_pool = GrpcChannelPool()

    result = channel_pool._is_local(target)

    assert result == expected_result
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/measurement/__init__.py sha256=b410095976b84b3233ace1ea601c601847c7ea0a19c351f292f4b9c2d49bca99 bytes=69 -->
## FILE: packages/service/tests/unit/measurement/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/measurement/__init__.py`
- sha256: `b410095976b84b3233ace1ea601c601847c7ea0a19c351f292f4b9c2d49bca99`
- bytes: 69

````python
"""Unit tests for ni_measurement_plugin_sdk_service.measurement."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/measurement/service/__init__.py sha256=98a8098b0cbcbc5578257ba7533617abbf2ac706f09c834b7d0f02b466ad1da2 bytes=77 -->
## FILE: packages/service/tests/unit/measurement/service/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/measurement/service/__init__.py`
- sha256: `98a8098b0cbcbc5578257ba7533617abbf2ac706f09c834b7d0f02b466ad1da2`
- bytes: 77

````python
"""Unit tests for ni_measurement_plugin_sdk_service.measurement.service."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/measurement/service/test_measurement_context.py sha256=b85458648953ab08fe02b93bf67aa24a9c67e21031d90269e7ffa369d678308d bytes=4075 -->
## FILE: packages/service/tests/unit/measurement/service/test_measurement_context.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/measurement/service/test_measurement_context.py`
- sha256: `b85458648953ab08fe02b93bf67aa24a9c67e21031d90269e7ffa369d678308d`
- bytes: 4075

````python
from __future__ import annotations

from unittest.mock import Mock

import pytest

from ni_measurement_plugin_sdk_service.measurement.service import MeasurementContext

pytestmark = pytest.mark.usefixtures("measurement_service_context")


def test___single_pin___reserve_session___session_reserved(
    measurement_service_context: Mock,
    session_management_client: Mock,
    single_session_reservation: Mock,
) -> None:
    measurement_context = MeasurementContext()

    reservation = measurement_context.reserve_session("Pin1")

    session_management_client.reserve_session.assert_called_once_with(
        context=measurement_service_context.pin_map_context, pin_or_relay_names="Pin1", timeout=0.0
    )
    assert reservation is single_session_reservation


def test___multiple_pins___reserve_session___session_reserved(
    measurement_service_context: Mock,
    session_management_client: Mock,
    single_session_reservation: Mock,
) -> None:
    measurement_context = MeasurementContext()

    reservation = measurement_context.reserve_session(["Pin1", "Pin2"])

    session_management_client.reserve_session.assert_called_once_with(
        context=measurement_service_context.pin_map_context,
        pin_or_relay_names=["Pin1", "Pin2"],
        timeout=0.0,
    )
    assert reservation is single_session_reservation


@pytest.mark.parametrize("no_pins", ["", [], None])
def test___no_pins___reserve_session___value_error_raised(
    no_pins: str | list[str] | None,
) -> None:
    measurement_context = MeasurementContext()

    with pytest.raises(ValueError):
        _ = measurement_context.reserve_session(no_pins)  # type: ignore[arg-type]


def test___timeout___reserve_session___timeout_specified(
    measurement_service_context: Mock,
    session_management_client: Mock,
) -> None:
    measurement_context = MeasurementContext()

    _ = measurement_context.reserve_session("Pin1", 10.0)

    session_management_client.reserve_session.assert_called_once_with(
        context=measurement_service_context.pin_map_context, pin_or_relay_names="Pin1", timeout=10.0
    )


def test___single_pin___reserve_sessions___session_reserved(
    measurement_service_context: Mock,
    session_management_client: Mock,
    multi_session_reservation: Mock,
) -> None:
    measurement_context = MeasurementContext()

    reservation = measurement_context.reserve_sessions("Pin1")

    session_management_client.reserve_sessions.assert_called_once_with(
        context=measurement_service_context.pin_map_context, pin_or_relay_names="Pin1", timeout=0.0
    )
    assert reservation is multi_session_reservation


def test___multiple_pins___reserve_sessions___session_reserved(
    measurement_service_context: Mock,
    session_management_client: Mock,
    multi_session_reservation: Mock,
) -> None:
    measurement_context = MeasurementContext()

    reservation = measurement_context.reserve_sessions(["Pin1", "Pin2"])

    session_management_client.reserve_sessions.assert_called_once_with(
        context=measurement_service_context.pin_map_context,
        pin_or_relay_names=["Pin1", "Pin2"],
        timeout=0.0,
    )
    assert reservation is multi_session_reservation


@pytest.mark.parametrize("no_pins", ["", [], None])
def test___no_pins___reserve_sessions___value_error_raised(
    no_pins: str | list[str] | None,
) -> None:
    measurement_context = MeasurementContext()

    with pytest.raises(ValueError):
        _ = measurement_context.reserve_sessions(no_pins)  # type: ignore[arg-type]


def test___timeout___reserve_sessions___timeout_specified(
    measurement_service_context: Mock,
    session_management_client: Mock,
) -> None:
    measurement_context = MeasurementContext()

    _ = measurement_context.reserve_sessions("Pin1", 10.0)

    session_management_client.reserve_sessions.assert_called_once_with(
        context=measurement_service_context.pin_map_context, pin_or_relay_names="Pin1", timeout=10.0
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_array_utils.py sha256=31f4c56c7b608c1df4a6653b846732cdd71b99ff8ad33d3ba0f1921f684fb425 bytes=2696 -->
## FILE: packages/service/tests/unit/test_array_utils.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_array_utils.py`
- sha256: `31f4c56c7b608c1df4a6653b846732cdd71b99ff8ad33d3ba0f1921f684fb425`
- bytes: 2696

````python
import numpy
import numpy.typing
from ni.protobuf.types import array_pb2

from tests.utilities import _array_utils


def test___valid_double2darray___double2darray_to_ndarray___converts_data():
    double2darray = array_pb2.Double2DArray(data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], rows=2, columns=3)

    ndarray = _array_utils.double2darray_to_ndarray(double2darray)

    assert numpy.array_equal(ndarray, numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]))


def test___valid_ndarray___ndarray_to_double2darray___converts_data():
    ndarray = numpy.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

    double2darray = _array_utils.ndarray_to_double2darray(ndarray)

    assert double2darray == array_pb2.Double2DArray(
        data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], rows=2, columns=3
    )


def test___valid_list___list_to_double2darray___converts_data():
    data = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

    double2darray = _array_utils.list_to_double2darray(data)

    assert double2darray == array_pb2.Double2DArray(
        data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], rows=2, columns=3
    )


def test___valid_double2darray___double2darray_to_list___converts_data():
    double2darray = array_pb2.Double2DArray(data=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0], rows=2, columns=3)

    data = _array_utils.double2darray_to_list(double2darray)

    assert data == [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]


def test___valid_string2darray___string2darray_to_ndarray___converts_data():
    string2darray = array_pb2.String2DArray(data=["a", "b", "c", "d", "e", "f"], rows=2, columns=3)

    ndarray = _array_utils.string2darray_to_ndarray(string2darray)

    assert numpy.array_equal(ndarray, numpy.array([["a", "b", "c"], ["d", "e", "f"]]))


def test___valid_ndarray___ndarray_to_string2darray___converts_data():
    ndarray = numpy.array([["a", "b", "c"], ["d", "e", "f"]])

    string2darray = _array_utils.ndarray_to_string2darray(ndarray)

    assert string2darray == array_pb2.String2DArray(
        data=["a", "b", "c", "d", "e", "f"], rows=2, columns=3
    )


def test___valid_list___list_to_string2darray___converts_data():
    data = [["a", "b", "c"], ["d", "e", "f"]]

    string2darray = _array_utils.list_to_string2darray(data)

    assert string2darray == array_pb2.String2DArray(
        data=["a", "b", "c", "d", "e", "f"], rows=2, columns=3
    )


def test___valid_string2darray___string2darray_to_list___converts_data():
    string2darray = array_pb2.String2DArray(data=["a", "b", "c", "d", "e", "f"], rows=2, columns=3)

    data = _array_utils.string2darray_to_list(string2darray)

    assert data == [["a", "b", "c"], ["d", "e", "f"]]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_configuration.py sha256=8d1811c3fdf174c068bd7d92f97174dc118c861cdef48bcfe92fc345c43218c8 bytes=2125 -->
## FILE: packages/service/tests/unit/test_configuration.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_configuration.py`
- sha256: `8d1811c3fdf174c068bd7d92f97174dc118c861cdef48bcfe92fc345c43218c8`
- bytes: 2125

````python
from __future__ import annotations

from typing import Any
from unittest.mock import Mock

import pytest
from pytest_mock import MockerFixture

from ni_measurement_plugin_sdk_service._configuration import (
    MIDriverOptions,
    NISwitchOptions,
)


def test___mi_driver_options___update_from_config___reads_config(config: Mock) -> None:
    config_options = {
        "MEASUREMENT_PLUGIN_NIFAKE_SIMULATE": True,
        "MEASUREMENT_PLUGIN_NIFAKE_BOARD_TYPE": "PXI",
        "MEASUREMENT_PLUGIN_NIFAKE_MODEL": "5678",
    }
    config.side_effect = lambda option, default=None, cast=None: config_options[option]

    options = MIDriverOptions("nifake").update_from_config()

    assert options.simulate
    assert options.board_type == "PXI"
    assert options.model == "5678"


@pytest.mark.parametrize(
    "options,expected_dict",
    [
        (MIDriverOptions("nifake"), {}),
        (
            MIDriverOptions("nifake", True, "", "1234"),
            {"simulate": True, "driver_setup": {"Model": "1234"}},
        ),
        (
            MIDriverOptions("nifake", True, "PXIe", "1234"),
            {"simulate": True, "driver_setup": {"BoardType": "PXIe", "Model": "1234"}},
        ),
    ],
)
def test___mi_driver_options___to_dict___returns_options_dict(
    options: MIDriverOptions, expected_dict: dict[str, Any]
) -> None:
    assert options.to_dict() == expected_dict


def test___niswitch_options___update_from_config___reads_config(config: Mock) -> None:
    config_options = {
        "MEASUREMENT_PLUGIN_NIFAKE_SIMULATE": True,
        "MEASUREMENT_PLUGIN_NIFAKE_TOPOLOGY": "5678/Independent",
    }
    config.side_effect = lambda option, default=None, cast=None: config_options[option]

    options = NISwitchOptions("nifake").update_from_config()

    assert options.simulate
    assert options.topology == "5678/Independent"


@pytest.fixture
def config(mocker: MockerFixture) -> Mock:
    """Test fixture that creates a mock decouple config."""
    return mocker.patch("ni_measurement_plugin_sdk_service._configuration._config")
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_decoder.py sha256=cc283abbab6e60c1d1ae18fc902d3f907e80e4c8dd447e2fc1bd6620eb2d09aa bytes=14403 -->
## FILE: packages/service/tests/unit/test_decoder.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_decoder.py`
- sha256: `cc283abbab6e60c1d1ae18fc902d3f907e80e4c8dd447e2fc1bd6620eb2d09aa`
- bytes: 14403

````python
"""Contains tests to validate serializer.py."""

from __future__ import annotations

from collections.abc import Sequence
from enum import Enum, IntEnum

import pytest
from google.protobuf import any_pb2, descriptor_pb2, descriptor_pool, type_pb2
from ni.protobuf.types import xydata_pb2

from ni_measurement_plugin_sdk_service._annotations import (
    ENUM_VALUES_KEY,
    TYPE_SPECIALIZATION_KEY,
)
from ni_measurement_plugin_sdk_service._internal.parameter import (
    decoder,
    serialization_descriptors,
)
from ni_measurement_plugin_sdk_service._internal.parameter.metadata import (
    ParameterMetadata,
    TypeSpecialization,
)
from tests.utilities.stubs.serialization import test_pb2
from tests.utilities.stubs.serialization.bigmessage_pb2 import BigMessage


class DifferentColor(Enum):
    """Non-primary colors used for testing enum-typed config and output."""

    PURPLE = 0
    ORANGE = 1
    TEAL = 2
    BROWN = 3


class Countries(IntEnum):
    """Countries enum used for testing enum-typed config and output."""

    AMERICA = 0
    TAIWAN = 1
    AUSTRALIA = 2
    CANADA = 3


double_xy_data = xydata_pb2.DoubleXYData()
double_xy_data.x_data.append(4)
double_xy_data.y_data.append(6)

double_xy_data2 = xydata_pb2.DoubleXYData()
double_xy_data2.x_data.append(8)
double_xy_data2.y_data.append(10)

double_xy_data_array = [double_xy_data, double_xy_data2]

# This should match the number of fields in bigmessage.proto.
BIG_MESSAGE_SIZE = 100


@pytest.mark.parametrize(
    "values",
    [
        [
            2.0,
            19.2,
            3,
            1,
            2,
            2,
            True,
            "TestString",
            [5.5, 3.3, 1.0],
            [5.5, 3, 1],
            [1, 2, 3, 4],
            [0, 1, 399],
            [1, 2, 3, 4],
            [0, 1, 399],
            [True, False, True],
            ["String1", "String2"],
            DifferentColor.ORANGE,
            [DifferentColor.TEAL, DifferentColor.BROWN],
            Countries.AUSTRALIA,
            [Countries.AUSTRALIA, Countries.CANADA],
            double_xy_data,
            double_xy_data_array,
        ]
    ],
)
def test___serializer___deserialize_parameter___successful_deserialization(values):
    parameter = _get_test_parameter_by_id(values)
    grpc_serialized_data = _get_grpc_serialized_data(values)
    service_name = _test_create_file_descriptor(list(parameter.values()), "deserialize_parameter")

    parameter_value_by_id = decoder.deserialize_parameters(
        parameter,
        grpc_serialized_data,
        service_name=service_name,
    )
    assert list(parameter_value_by_id.values()) == values


def test___empty_buffer___deserialize_parameters___returns_zero_or_empty():
    # Note that we set nonzero defaults to validate that we are getting zero-values
    # as opposed to simply getting the defaults.
    nonzero_defaults = [
        2.0,
        19.2,
        3,
        1,
        2,
        2,
        True,
        "TestString",
        [5.5, 3.3, 1.0],
        [5.5, 3, 1],
        [1, 2, 3, 4],
        [0, 1, 399],
        [1, 2, 3, 4],
        [0, 1, 399],
        [True, False, True],
        ["String1", "String2"],
        DifferentColor.ORANGE,
        [DifferentColor.TEAL, DifferentColor.BROWN],
        Countries.AUSTRALIA,
        [Countries.AUSTRALIA, Countries.CANADA],
        double_xy_data,
        double_xy_data_array,
    ]
    parameter = _get_test_parameter_by_id(nonzero_defaults)
    service_name = _test_create_file_descriptor(list(parameter.values()), "empty_buffer")
    parameter_value_by_id = decoder.deserialize_parameters(
        parameter, b"", service_name=service_name
    )

    for key, value in parameter_value_by_id.items():
        parameter_metadata = parameter[key]
        if parameter_metadata.repeated:
            assert value == list()
        elif parameter_metadata.type == type_pb2.Field.TYPE_ENUM:
            assert value.value == 0
        elif parameter_metadata.type == type_pb2.Field.TYPE_STRING:
            assert value == ""
        elif parameter_metadata.type == type_pb2.Field.TYPE_MESSAGE:
            assert value is None
        else:
            assert value == 0


def test___big_message___deserialize_parameters___returns_parameter_value_by_id() -> None:
    parameter_metadata_by_id = _get_big_message_metadata_by_id()
    values = [123.456 + i for i in range(BIG_MESSAGE_SIZE)]
    message = _get_big_message(values)
    serialized_data = message.SerializeToString()
    expected_parameter_value_by_id = {i + 1: value for (i, value) in enumerate(values)}
    service_name = _test_create_file_descriptor(
        list(parameter_metadata_by_id.values()), "big_message"
    )

    parameter_value_by_id = decoder.deserialize_parameters(
        parameter_metadata_by_id,
        serialized_data,
        service_name=service_name,
    )

    assert parameter_value_by_id == pytest.approx(expected_parameter_value_by_id)


def _get_grpc_serialized_data(values):
    grpc_parameter = _get_test_grpc_message(values)
    parameter_any = any_pb2.Any()
    parameter_any.Pack(grpc_parameter)
    grpc_serialized_data = parameter_any.value
    return grpc_serialized_data


def _get_test_parameter_by_id(default_values):
    parameter_by_id = {
        1: ParameterMetadata.initialize(
            display_name="float_data",
            type=type_pb2.Field.TYPE_FLOAT,
            repeated=False,
            default_value=default_values[0],
            annotations={},
        ),
        2: ParameterMetadata.initialize(
            display_name="double_data",
            type=type_pb2.Field.TYPE_DOUBLE,
            repeated=False,
            default_value=default_values[1],
            annotations={},
        ),
        3: ParameterMetadata.initialize(
            display_name="int32_data",
            type=type_pb2.Field.TYPE_INT32,
            repeated=False,
            default_value=default_values[2],
            annotations={},
        ),
        4: ParameterMetadata.initialize(
            display_name="uint32_data",
            type=type_pb2.Field.TYPE_INT64,
            repeated=False,
            default_value=default_values[3],
            annotations={},
        ),
        5: ParameterMetadata.initialize(
            display_name="int64_data",
            type=type_pb2.Field.TYPE_UINT32,
            repeated=False,
            default_value=default_values[4],
            annotations={},
        ),
        6: ParameterMetadata.initialize(
            display_name="uint64_data",
            type=type_pb2.Field.TYPE_UINT64,
            repeated=False,
            default_value=default_values[5],
            annotations={},
        ),
        7: ParameterMetadata.initialize(
            display_name="bool_data",
            type=type_pb2.Field.TYPE_BOOL,
            repeated=False,
            default_value=default_values[6],
            annotations={},
        ),
        8: ParameterMetadata.initialize(
            display_name="string_data",
            type=type_pb2.Field.TYPE_STRING,
            repeated=False,
            default_value=default_values[7],
            annotations={},
        ),
        9: ParameterMetadata.initialize(
            display_name="double_array_data",
            type=type_pb2.Field.TYPE_DOUBLE,
            repeated=True,
            default_value=default_values[8],
            annotations={},
        ),
        10: ParameterMetadata.initialize(
            display_name="float_array_data",
            type=type_pb2.Field.TYPE_FLOAT,
            repeated=True,
            default_value=default_values[9],
            annotations={},
        ),
        11: ParameterMetadata.initialize(
            display_name="int32_array_data",
            type=type_pb2.Field.TYPE_INT32,
            repeated=True,
            default_value=default_values[10],
            annotations={},
        ),
        12: ParameterMetadata.initialize(
            display_name="uint32_array_data",
            type=type_pb2.Field.TYPE_UINT32,
            repeated=True,
            default_value=default_values[11],
            annotations={},
        ),
        13: ParameterMetadata.initialize(
            display_name="int64_array_data",
            type=type_pb2.Field.TYPE_INT64,
            repeated=True,
            default_value=default_values[12],
            annotations={},
        ),
        14: ParameterMetadata.initialize(
            display_name="uint64_array_data",
            type=type_pb2.Field.TYPE_UINT64,
            repeated=True,
            default_value=default_values[13],
            annotations={},
        ),
        15: ParameterMetadata.initialize(
            display_name="bool_array_data",
            type=type_pb2.Field.TYPE_BOOL,
            repeated=True,
            default_value=default_values[14],
            annotations={},
        ),
        16: ParameterMetadata.initialize(
            display_name="string_array_data",
            type=type_pb2.Field.TYPE_STRING,
            repeated=True,
            default_value=default_values[15],
            annotations={},
        ),
        17: ParameterMetadata.initialize(
            display_name="enum_data",
            type=type_pb2.Field.TYPE_ENUM,
            repeated=False,
            default_value=default_values[16],
            annotations={
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"PURPLE": 0, "ORANGE": 1, "TEAL": 2, "BROWN": 3}',
            },
            enum_type=DifferentColor,
        ),
        18: ParameterMetadata.initialize(
            display_name="enum_array_data",
            type=type_pb2.Field.TYPE_ENUM,
            repeated=True,
            default_value=default_values[17],
            annotations={
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"PURPLE": 0, "ORANGE": 1, "TEAL": 2, "BROWN": 3}',
            },
            enum_type=DifferentColor,
        ),
        19: ParameterMetadata.initialize(
            display_name="int_enum_data",
            type=type_pb2.Field.TYPE_ENUM,
            repeated=False,
            default_value=default_values[18],
            annotations={
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"AMERICA": 0, "TAIWAN": 1, "AUSTRALIA": 2, "CANADA": 3}',
            },
            enum_type=Countries,
        ),
        20: ParameterMetadata.initialize(
            display_name="int_enum_array_data",
            type=type_pb2.Field.TYPE_ENUM,
            repeated=True,
            default_value=default_values[19],
            annotations={
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"AMERICA": 0, "TAIWAN": 1, "AUSTRALIA": 2, "CANADA": 3}',
            },
            enum_type=Countries,
        ),
        21: ParameterMetadata.initialize(
            display_name="xy_data",
            type=type_pb2.Field.TYPE_MESSAGE,
            repeated=False,
            default_value=default_values[20],
            annotations={},
            message_type=xydata_pb2.DoubleXYData.DESCRIPTOR.full_name,
        ),
        22: ParameterMetadata.initialize(
            display_name="xy_data_array",
            type=type_pb2.Field.TYPE_MESSAGE,
            repeated=True,
            default_value=default_values[21],
            annotations={},
            message_type=xydata_pb2.DoubleXYData.DESCRIPTOR.full_name,
        ),
    }
    return parameter_by_id


def _get_test_grpc_message(test_values):
    parameter = test_pb2.MeasurementParameter()
    parameter.float_data = test_values[0]
    parameter.double_data = test_values[1]
    parameter.int32_data = test_values[2]
    parameter.uint32_data = test_values[3]
    parameter.int64_data = test_values[4]
    parameter.uint64_data = test_values[5]
    parameter.bool_data = test_values[6]
    parameter.string_data = test_values[7]
    parameter.double_array_data.extend(test_values[8])
    parameter.float_array_data.extend(test_values[9])
    parameter.int32_array_data.extend(test_values[10])
    parameter.uint32_array_data.extend(test_values[11])
    parameter.int64_array_data.extend(test_values[12])
    parameter.uint64_array_data.extend(test_values[13])
    parameter.bool_array_data.extend(test_values[14])
    parameter.string_array_data.extend(test_values[15])
    parameter.enum_data = test_values[16].value
    parameter.enum_array_data.extend(list(map(lambda x: x.value, test_values[17])))
    parameter.int_enum_data = test_values[18].value
    parameter.int_enum_array_data.extend(list(map(lambda x: x.value, test_values[19])))
    parameter.xy_data.x_data.append(test_values[20].x_data[0])
    parameter.xy_data.y_data.append(test_values[20].y_data[0])
    parameter.xy_data_array.extend(test_values[21])
    return parameter


def _get_big_message_metadata_by_id() -> dict[int, ParameterMetadata]:
    return {
        i
        + 1: ParameterMetadata.initialize(
            display_name=f"field{i + 1}",
            type=type_pb2.Field.TYPE_DOUBLE,
            repeated=False,
            default_value=-1.0,
            annotations={},
        )
        for i in range(BIG_MESSAGE_SIZE)
    }


def _get_big_message(values: Sequence[float]) -> BigMessage:
    assert len(values) == BIG_MESSAGE_SIZE
    return BigMessage(**{f"field{i + 1}": value for (i, value) in enumerate(values)})


def _test_create_file_descriptor(metadata: list[ParameterMetadata], file_name: str) -> str:
    pool = descriptor_pool.Default()
    try:
        pool.FindMessageTypeByName(f"{file_name}.test")
    except KeyError:
        file_descriptor = descriptor_pb2.FileDescriptorProto()
        file_descriptor.name = file_name
        file_descriptor.package = file_name
        serialization_descriptors._create_message_type(metadata, "test", file_descriptor)
        pool.Add(file_descriptor)
    return file_name + ".test"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_default_value.py sha256=9efe646bc1f62a2a5ce08ebcfc3f6e3d19662c44a8177701d8c09b8c06a850a2 bytes=1081 -->
## FILE: packages/service/tests/unit/test_default_value.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_default_value.py`
- sha256: `9efe646bc1f62a2a5ce08ebcfc3f6e3d19662c44a8177701d8c09b8c06a850a2`
- bytes: 1081

````python
"""Contains tests to validate the serializationstrategy.py."""

import pytest
from google.protobuf import type_pb2

from ni_measurement_plugin_sdk_service._internal.parameter import (
    _get_type,
)


@pytest.mark.parametrize(
    "type,is_repeated,expected_default_value",
    [
        (type_pb2.Field.TYPE_FLOAT, False, 0.0),
        (type_pb2.Field.TYPE_DOUBLE, False, 0.0),
        (type_pb2.Field.TYPE_INT32, False, 0),
        (type_pb2.Field.TYPE_INT64, False, 0),
        (type_pb2.Field.TYPE_UINT32, False, 0),
        (type_pb2.Field.TYPE_UINT64, False, 0),
        (type_pb2.Field.TYPE_BOOL, False, False),
        (type_pb2.Field.TYPE_STRING, False, ""),
        (type_pb2.Field.TYPE_ENUM, False, 0),
        (type_pb2.Field.TYPE_MESSAGE, False, None),
        (type_pb2.Field.TYPE_MESSAGE, True, []),
    ],
)
def test___get_default_value___returns_type_defaults(type, is_repeated, expected_default_value):
    test_default_value = _get_type.get_type_default(type, is_repeated)

    assert test_default_value == expected_default_value
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_dotenvpath.py sha256=73e10cd1e0ea178866acd29a9b9e2740eb2d0286f0058975bf1bd5d89ad464c4 bytes=1142 -->
## FILE: packages/service/tests/unit/test_dotenvpath.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_dotenvpath.py`
- sha256: `73e10cd1e0ea178866acd29a9b9e2740eb2d0286f0058975bf1bd5d89ad464c4`
- bytes: 1142

````python
from pathlib import Path

import pytest

from ni_measurement_plugin_sdk_service import _dotenvpath


@pytest.mark.parametrize("dotenv_exists", [False, True])
def test___dotenv_exists_varies___has_dotenv_file___matches_dotenv_exists(
    dotenv_exists: bool, tmp_path: Path
) -> None:
    if dotenv_exists:
        (tmp_path / ".env").write_text("")
    subdirs = [tmp_path / "a", tmp_path / "a" / "b", tmp_path / "a" / "b" / "c"]
    for dir in subdirs:
        dir.mkdir()

    assert _dotenvpath._has_dotenv_file(tmp_path) == dotenv_exists
    assert all([_dotenvpath._has_dotenv_file(p) == dotenv_exists for p in subdirs])


def test___get_caller_path___returns_this_modules_path() -> None:
    assert _dotenvpath._get_caller_path() == Path(__file__)


def test___get_package_path___returns_package_dir() -> None:
    assert _dotenvpath._get_package_path() == Path(_dotenvpath.__file__).parent


def test___get_script_or_exe_path___returns_pytest_path() -> None:
    path = _dotenvpath._get_script_or_exe_path()

    assert path is not None
    assert "pytest" in path.parts or "pytest.exe" in path.parts
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_drivers.py sha256=f38fa0d637ab32465fdcddde05289de39fe8561b5901dcd170de73d295d71c54 bytes=4323 -->
## FILE: packages/service/tests/unit/test_drivers.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_drivers.py`
- sha256: `f38fa0d637ab32465fdcddde05289de39fe8561b5901dcd170de73d295d71c54`
- bytes: 4323

````python
import pytest
from ni.measurementlink.sessionmanagement.v1.client import (
    SessionInitializationBehavior,
)
from ni.measurementlink.sessionmanagement.v1.client._drivers import (
    closing_session_with_ts_code_module_support,
)

from tests.utilities import fake_driver
from tests.utilities.fake_driver import (
    SessionInitializationBehavior as FakeDriverSessionInitializationBehavior,
)

_INITIALIZATION_BEHAVIOR = {
    SessionInitializationBehavior.AUTO: FakeDriverSessionInitializationBehavior.AUTO,
    SessionInitializationBehavior.INITIALIZE_SERVER_SESSION: FakeDriverSessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION: FakeDriverSessionInitializationBehavior.ATTACH_TO_SERVER_SESSION,
    SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH: FakeDriverSessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH,
    SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE: FakeDriverSessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE,
}


@pytest.mark.parametrize(
    "initialization_behavior",
    [
        SessionInitializationBehavior.AUTO,
        SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
        SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE,
    ],
)
def test___initialization_behavior_close___with_closing_session_with_ts_code_module_support___session_closed(
    initialization_behavior: SessionInitializationBehavior,
) -> None:
    with closing_session_with_ts_code_module_support(
        initialization_behavior,
        fake_driver.Session("Dev1", _INITIALIZATION_BEHAVIOR[initialization_behavior]),
    ) as session:
        assert isinstance(session, fake_driver.Session)
        assert not session.is_closed

    assert session.is_closed


@pytest.mark.parametrize(
    "initialization_behavior",
    [
        SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION,
        SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH,
    ],
)
def test___initialization_behavior_detach___with_closing_session_with_ts_code_module_support___session_detached(
    initialization_behavior: SessionInitializationBehavior,
) -> None:
    with closing_session_with_ts_code_module_support(
        initialization_behavior,
        fake_driver.Session("Dev1", _INITIALIZATION_BEHAVIOR[initialization_behavior]),
    ) as session:
        assert isinstance(session, fake_driver.Session)
        assert not session.is_closed

    assert not session.is_closed


@pytest.mark.parametrize(
    "initialization_behavior",
    [
        SessionInitializationBehavior.AUTO,
        SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
        SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION,
        SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE,
        SessionInitializationBehavior.INITIALIZE_SESSION_THEN_DETACH,
    ],
)
def test___session_not_closable___with_closing_session_with_ts_code_module_support___raises_type_error(
    initialization_behavior: SessionInitializationBehavior,
) -> None:
    with pytest.raises(TypeError) as exc_info:
        with closing_session_with_ts_code_module_support(
            initialization_behavior,
            fake_driver.ContextManagerSession(
                "Dev1", _INITIALIZATION_BEHAVIOR[initialization_behavior]
            ),
        ):
            pass

    assert "Session must have a close() method." in exc_info.value.args[0]


@pytest.mark.parametrize(
    "initialization_behavior",
    [
        SessionInitializationBehavior.AUTO,
        SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
        SessionInitializationBehavior.ATTACH_TO_SERVER_SESSION,
    ],
)
def test___session_not_context_manager___with_closing_session_with_ts_code_module_support___raises_type_error(
    initialization_behavior: SessionInitializationBehavior,
) -> None:
    with pytest.raises(TypeError) as exc_info:
        with closing_session_with_ts_code_module_support(
            initialization_behavior,
            fake_driver.ClosableSession("Dev1", _INITIALIZATION_BEHAVIOR[initialization_behavior]),
        ):
            pass

    assert "Session must be a context manager." in exc_info.value.args[0]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_encoder.py sha256=c5ae3166810b235fa5041a9a0f572d0bf85ca1fc831172dc2fae01f4c3a50139 bytes=7658 -->
## FILE: packages/service/tests/unit/test_encoder.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_encoder.py`
- sha256: `c5ae3166810b235fa5041a9a0f572d0bf85ca1fc831172dc2fae01f4c3a50139`
- bytes: 7658

````python
"""Contains tests to validate serializer.py."""

from __future__ import annotations

from enum import Enum, IntEnum

import pytest
from google.protobuf import descriptor_pb2, descriptor_pool
from ni.protobuf.types import xydata_pb2

from ni_measurement_plugin_sdk_service._internal.parameter import (
    encoder,
    metadata,
    serialization_descriptors,
)
from tests.unit.test_decoder import (
    _get_big_message,
    _get_big_message_metadata_by_id,
    _get_grpc_serialized_data,
    _get_test_parameter_by_id,
)
from tests.utilities.stubs.serialization.bigmessage_pb2 import BigMessage


class DifferentColor(Enum):
    """Non-primary colors used for testing enum-typed config and output."""

    PURPLE = 0
    ORANGE = 1
    TEAL = 2
    BROWN = 3


class Countries(IntEnum):
    """Countries enum used for testing enum-typed config and output."""

    AMERICA = 0
    TAIWAN = 1
    AUSTRALIA = 2
    CANADA = 3


double_xy_data = xydata_pb2.DoubleXYData()
double_xy_data.x_data.append(4)
double_xy_data.y_data.append(6)

double_xy_data2 = xydata_pb2.DoubleXYData()
double_xy_data2.x_data.append(8)
double_xy_data2.y_data.append(10)

double_xy_data_array = [double_xy_data, double_xy_data2]

# This should match the number of fields in bigmessage.proto.
BIG_MESSAGE_SIZE = 100


@pytest.mark.parametrize(
    "test_values",
    [
        [
            2.0,
            19.2,
            3,
            1,
            2,
            2,
            True,
            "TestString",
            [5.5, 3.3, 1],
            [5.5, 3.3, 1],
            [1, 2, 3, 4],
            [0, 1, 399],
            [1, 2, 3, 4],
            [0, 1, 399],
            [True, False, True],
            ["String1, String2"],
            DifferentColor.ORANGE,
            [DifferentColor.TEAL, DifferentColor.BROWN],
            Countries.AUSTRALIA,
            [Countries.AUSTRALIA, Countries.CANADA],
            double_xy_data,
            double_xy_data_array,
        ],
        [
            -0.9999,
            -0.9999,
            -13,
            1,
            1000,
            2,
            True,
            "",
            [5.5, -13.3, 1, 0.0, -99.9999],
            [5.5, 3.3, 1],
            [1, 2, 3, 4],
            [0, 1, 399],
            [1, 2, 3, 4],
            [0, 1, 399],
            [True, False, True],
            ["String1, String2"],
            DifferentColor.ORANGE,
            [DifferentColor.TEAL, DifferentColor.BROWN],
            Countries.AUSTRALIA,
            [Countries.AUSTRALIA, Countries.CANADA],
            double_xy_data,
            double_xy_data_array,
        ],
    ],
)
def test___serializer___serialize_parameter___successful_serialization(test_values):
    default_values = test_values
    parameter = _get_test_parameter_by_id(default_values)
    service_name = _test_create_file_descriptor(list(parameter.values()), "serialize_parameter")

    # Custom Serialization
    custom_serialized_bytes = encoder.serialize_parameters(
        parameter,
        test_values,
        service_name=service_name,
    )

    _validate_serialized_bytes(custom_serialized_bytes, test_values)


@pytest.mark.parametrize(
    "default_values",
    [
        [
            2.0,
            19.2,
            3,
            1,
            2,
            2,
            True,
            "TestString",
            [5.5, 3.3, 1],
            [5.5, 3.3, 1],
            [1, 2, 3, 4],
            [0, 1, 399],
            [1, 2, 3, 4],
            [0, 1, 399],
            [True, False, True],
            ["String1, String2"],
            DifferentColor.ORANGE,
            [DifferentColor.TEAL, DifferentColor.BROWN],
            Countries.AUSTRALIA,
            [Countries.AUSTRALIA, Countries.CANADA],
            double_xy_data,
            double_xy_data_array,
        ],
        [
            -0.9999,
            -0.9999,
            -13,
            1,
            1000,
            2,
            False,
            "////",
            [5.5, -13.3, 1, 0.0, -99.9999],
            [5.5, 3.3, 1],
            [1, 2, 3, 4],
            [0, 1, 399],
            [1, 2, 3, 4],
            [0, 1, 399],
            [True, False, True],
            ["String1, String2"],
            DifferentColor.ORANGE,
            [DifferentColor.TEAL, DifferentColor.BROWN],
            Countries.AUSTRALIA,
            [Countries.AUSTRALIA, Countries.CANADA],
            double_xy_data,
            double_xy_data_array,
        ],
    ],
)
def test___serializer___serialize_default_parameter___successful_serialization(default_values):
    parameter = _get_test_parameter_by_id(default_values)
    service_name = _test_create_file_descriptor(list(parameter.values()), "default_serialize")

    # Custom Serialization
    custom_serialized_bytes = encoder.serialize_default_values(parameter, service_name=service_name)

    _validate_serialized_bytes(custom_serialized_bytes, default_values)


def test___big_message___serialize_parameters___returns_serialized_data() -> None:
    parameter_metadata_by_id = _get_big_message_metadata_by_id()
    values = [123.456 + i for i in range(BIG_MESSAGE_SIZE)]
    expected_message = _get_big_message(values)
    service_name = _test_create_file_descriptor(
        list(parameter_metadata_by_id.values()), "big_message"
    )

    serialized_data = encoder.serialize_parameters(
        parameter_metadata_by_id,
        values,
        service_name=service_name,
    )

    message = BigMessage.FromString(serialized_data)
    assert message.ListFields() == pytest.approx(expected_message.ListFields())


@pytest.mark.parametrize(
    "test_values",
    [
        [
            2.0,
            19.2,
            3,
            1,
            2,
            2,
            True,
            "TestString",
            [5.5, 3.3, 1],
            [5.5, 3.3, 1],
            [1, 2, 3, 4],
            [0, 1, 399],
            [1, 2, 3, 4],
            [0, 1, 399],
            [True, False, True],
            ["String1, String2"],
            DifferentColor.ORANGE,
            [DifferentColor.TEAL, DifferentColor.BROWN],
            Countries.AUSTRALIA,
            [Countries.AUSTRALIA, Countries.CANADA],
            double_xy_data,
            double_xy_data_array,
        ],
    ],
)
def test___serialize_parameter_multiple_times___returns_one_message_type(test_values):
    for i in range(100):
        test___serializer___serialize_parameter___successful_serialization(test_values)
    pool = descriptor_pool.Default()
    file_descriptor = pool.FindFileByName("serialize_parameter")
    message_dict = file_descriptor.message_types_by_name
    assert len(message_dict) == 1


def _validate_serialized_bytes(custom_serialized_bytes, values):
    # Serialization using gRPC Any
    grpc_serialized_data = _get_grpc_serialized_data(values)
    assert grpc_serialized_data == custom_serialized_bytes


def _test_create_file_descriptor(metadata: list[metadata.ParameterMetadata], file_name: str) -> str:
    pool = descriptor_pool.Default()
    try:
        pool.FindMessageTypeByName(f"{file_name}.test")
    except KeyError:
        file_descriptor = descriptor_pb2.FileDescriptorProto()
        file_descriptor.name = file_name
        file_descriptor.package = file_name
        serialization_descriptors._create_message_type(metadata, "test", file_descriptor)
        pool.Add(file_descriptor)
    return file_name + ".test"
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_featuretoggles.py sha256=e56dfb0c0e7b2ec39b1d686e2865d746b223e8dff1ef2e58087c0d8e68efe527 bytes=4036 -->
## FILE: packages/service/tests/unit/test_featuretoggles.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_featuretoggles.py`
- sha256: `e56dfb0c0e7b2ec39b1d686e2865d746b223e8dff1ef2e58087c0d8e68efe527`
- bytes: 4036

````python
from __future__ import annotations

import pytest
from pytest_mock import MockerFixture

from ni_measurement_plugin_sdk_service._featuretoggles import (
    CodeReadiness,
    FeatureNotSupportedError,
    FeatureToggle,
    get_code_readiness_level,
    requires_feature,
)

RELEASE_FEATURE = FeatureToggle("RELEASE_FEATURE", CodeReadiness.RELEASE)
NEXT_RELEASE_FEATURE = FeatureToggle("NEXT_RELEASE_FEATURE", CodeReadiness.NEXT_RELEASE)
INCOMPLETE_FEATURE = FeatureToggle("INCOMPLETE_FEATURE", CodeReadiness.INCOMPLETE)
PROTOTYPE_FEATURE = FeatureToggle("PROTOTYPE_FEATURE", CodeReadiness.PROTOTYPE)


@requires_feature(PROTOTYPE_FEATURE)
def _prototype_function(x: int, y: str, z: list[int]) -> str:
    return _prototype_function_impl(x, y, z)


def _prototype_function_impl(x: int, y: str, z: list[int]) -> str:
    return ""


def test___default_code_readiness_level___get_code_readiness_level___equals_prototype() -> None:
    assert get_code_readiness_level() == CodeReadiness.PROTOTYPE


@pytest.mark.use_code_readiness(CodeReadiness.RELEASE)
def test___use_release_readiness___get_code_readiness_level___equals_release() -> None:
    assert get_code_readiness_level() == CodeReadiness.RELEASE


@pytest.mark.use_code_readiness(CodeReadiness.NEXT_RELEASE)
def test___use_next_release_readiness___get_code_readiness_level___equals_next_release() -> None:
    assert get_code_readiness_level() == CodeReadiness.NEXT_RELEASE


def test___default_code_readiness_level___is_enabled___returns_true() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert INCOMPLETE_FEATURE.is_enabled
    assert PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.INCOMPLETE)
def test___use_incomplete_readiness___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.NEXT_RELEASE)
def test___use_next_release_readiness___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert NEXT_RELEASE_FEATURE.is_enabled
    assert not INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.use_code_readiness(CodeReadiness.RELEASE)
def test___release_readiness_level___is_enabled___reflects_code_readiness_level() -> None:
    assert RELEASE_FEATURE.is_enabled
    assert not NEXT_RELEASE_FEATURE.is_enabled
    assert not INCOMPLETE_FEATURE.is_enabled
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.enable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_enabled___is_enabled___returns_true() -> None:
    assert PROTOTYPE_FEATURE.is_enabled


@pytest.mark.disable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_disabled___is_enabled___returns_false() -> None:
    assert not PROTOTYPE_FEATURE.is_enabled


@pytest.mark.enable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_enabled___call_decorated_function___impl_called(
    mocker: MockerFixture,
) -> None:
    impl = mocker.patch("tests.unit.test_featuretoggles._prototype_function_impl")
    impl.return_value = "def"

    result = _prototype_function(123, "abc", [4, 5, 6])

    impl.assert_called_once_with(123, "abc", [4, 5, 6])
    assert result == "def"


@pytest.mark.disable_feature_toggle(PROTOTYPE_FEATURE)
def test___feature_toggle_disabled___call_decorated_function___error_raised(
    mocker: MockerFixture,
) -> None:
    impl = mocker.patch("tests.unit.test_featuretoggles._prototype_function_impl")
    impl.return_value = "def"

    with pytest.raises(FeatureNotSupportedError) as exc_info:
        _ = _prototype_function(123, "abc", [4, 5, 6])

    impl.assert_not_called()
    assert "set MEASUREMENT_PLUGIN_ENABLE_PROTOTYPE_FEATURE" in exc_info.value.args[0]
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_metadata.py sha256=210d68f5a2cdd766ce648bc4eb70bcb920fdc7fae5275775dfc29cf993a84912 bytes=5545 -->
## FILE: packages/service/tests/unit/test_metadata.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_metadata.py`
- sha256: `210d68f5a2cdd766ce648bc4eb70bcb920fdc7fae5275775dfc29cf993a84912`
- bytes: 5545

````python
"""Contains tests to validate metadata.py."""

from enum import Enum, IntEnum

import pytest

from ni_measurement_plugin_sdk_service import _datatypeinfo
from ni_measurement_plugin_sdk_service._annotations import (
    ENUM_VALUES_KEY,
    TYPE_SPECIALIZATION_KEY,
)
from ni_measurement_plugin_sdk_service._internal.parameter import metadata
from ni_measurement_plugin_sdk_service.measurement.info import (
    DataType,
    TypeSpecialization,
)


class Color(Enum):
    """Primary colors used for testing enum-typed config and output."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class DifferentColor(Enum):
    """Non-primary colors used for testing enum-typed config and output."""

    NONE = 0
    ORANGE = 1
    TEAL = 2
    BROWN = 3


class Countries(IntEnum):
    """Countries enum used for testing IntEnum-typed config and output."""

    AMERICA = 0
    TAIWAN = 1
    AUSTRALIA = 2
    CANADA = 3


@pytest.mark.parametrize(
    "type,default_value,annotations",
    [
        (DataType.Int32, "string_default_value", {}),
        (DataType.Int32, 2.0, {}),
        (DataType.Boolean, 1, {}),
        (DataType.Boolean, 0, {}),
        (DataType.String, True, {}),
        (DataType.DoubleArray1D, 0.5, {}),
        (
            DataType.Enum,
            1.0,
            {
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"NONE":0, "RED": 1, "GREEN": 2, "BLUE": 3}',
            },
        ),
        (
            DataType.Enum,
            DifferentColor.TEAL,
            {
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"NONE":0, "RED": 1, "GREEN": 2, "BLUE": 3}',
            },
        ),
        (DataType.EnumArray1D, 1, {}),
        (
            DataType.EnumArray1D,
            [1.0, 2.0],
            {
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"NONE":0, "RED": 1, "GREEN": 2, "BLUE": 3}',
            },
        ),
    ],
)
def test___default_value_different_from_type___validate___raises_type_exception(
    type, default_value, annotations
):
    data_type_info = _datatypeinfo.get_type_info(type)
    parameter_metadata = metadata.ParameterMetadata(
        "test_display_name",
        data_type_info.grpc_field_type,
        data_type_info.repeated,
        default_value,
        annotations,
    )

    with pytest.raises(TypeError):
        metadata._validate_default_value_type(parameter_metadata)


@pytest.mark.parametrize(
    "type,default_value,annotations",
    [
        (DataType.Int32, 1, {}),
        (DataType.Boolean, True, {}),
        (DataType.String, "string_default_value", {}),
        (DataType.DoubleArray1D, [0.5, 0.1], {}),
        (DataType.Double, 1.0, {}),
        (DataType.Double, 1, {}),
        (DataType.DoubleArray1D, [], {}),
        (
            DataType.Enum,
            Color.BLUE,
            {
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"NONE":0, "RED": 1, "GREEN": 2, "BLUE": 3}',
            },
        ),
        (
            DataType.EnumArray1D,
            [Color.BLUE, Color.GREEN],
            {
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"NONE":0, "RED": 1, "GREEN": 2, "BLUE": 3}',
            },
        ),
        (
            DataType.Enum,
            Countries.AUSTRALIA,
            {
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"AMERICA":0, "TAIWAN": 1, "AUSTRALIA": 2, "CANADA": 3}',
            },
        ),
        (
            DataType.EnumArray1D,
            [Countries.AUSTRALIA, Countries.CANADA],
            {
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"AMERICA":0, "TAIWAN": 1, "AUSTRALIA": 2, "CANADA": 3}',
            },
        ),
        (
            DataType.EnumArray1D,
            [],
            {
                TYPE_SPECIALIZATION_KEY: TypeSpecialization.Enum.value,
                ENUM_VALUES_KEY: '{"NONE":0, "RED": 1, "GREEN": 2, "BLUE": 3}',
            },
        ),
    ],
)
def test___default_value_same_as_type___validate___raises_no_exception(
    type, default_value, annotations
):
    data_type_info = _datatypeinfo.get_type_info(type)
    parameter_metadata = metadata.ParameterMetadata(
        "test_display_name",
        data_type_info.grpc_field_type,
        data_type_info.repeated,
        default_value,
        annotations,
    )

    metadata._validate_default_value_type(parameter_metadata)  # implicitly assert does not throw


@pytest.mark.parametrize(
    "display_name",
    [
        " test_string",
        "_____()!",
        "test@string",
        "",
    ],
)
def test___display_name_invalid_characters___validate___raises_value_exception(display_name):
    with pytest.raises(ValueError):
        metadata._validate_display_name(display_name)


@pytest.mark.parametrize(
    "display_name",
    [
        "teststring()",
        "tEsT StRIng?",
        "test_string!",
        "Test String: -10",
    ],
)
def test___display_name_valid_characters___validate___raises_no_exception(display_name):
    metadata._validate_display_name(display_name)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_pin_map_client.py sha256=d73b3bc635dfe7322645afdfb58fb6a69fe0a3dbbc7f84eef1ca494b1e0b64b3 bytes=2638 -->
## FILE: packages/service/tests/unit/test_pin_map_client.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_pin_map_client.py`
- sha256: `d73b3bc635dfe7322645afdfb58fb6a69fe0a3dbbc7f84eef1ca494b1e0b64b3`
- bytes: 2638

````python
"""Contains tests to validate the pin_map_client.py."""

from __future__ import annotations

import pathlib
from typing import cast
from unittest.mock import Mock

import grpc
import pytest
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.pinmap.v1.client import PinMapClient
from ni.measurementlink.pinmap.v1.pin_map_service_pb2 import (
    PinMap,
    UpdatePinMapFromXmlRequest,
)
from ni.measurementlink.pinmap.v1.pin_map_service_pb2_grpc import (
    PinMapServiceStub,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool
from pytest_mock import MockerFixture


def test___valid_pin_map_file___register_pin_map___returns_pin_map_id(
    pin_map_client: PinMapClient,
    pin_map_stub: Mock,
    pin_map_directory: pathlib.Path,
) -> None:
    pin_map_path = str(pin_map_directory / "1Smu1ChannelGroup1Pin1Site.pinmap")
    pin_map_stub.UpdatePinMapFromXml.return_value = PinMap(pin_map_id=pin_map_path)

    registered_pin_map_id = pin_map_client.update_pin_map(pin_map_path)

    pin_map_stub.UpdatePinMapFromXml.assert_called_once()
    request: UpdatePinMapFromXmlRequest = pin_map_stub.UpdatePinMapFromXml.call_args.args[0]
    assert request.pin_map_id == pin_map_path
    assert request.pin_map_xml == _get_pin_map_file_contents(pin_map_path)
    assert registered_pin_map_id == pin_map_path


def test___invalid_pin_map_file_path___register_pin_map___raises_file_not_found_error(
    pin_map_client: PinMapClient,
) -> None:
    pin_map_path = "InvalidPinMap.pinmap"

    with pytest.raises(FileNotFoundError):
        _ = pin_map_client.update_pin_map(pin_map_path)


def _get_pin_map_file_contents(pin_map_path: str) -> str:
    return pathlib.Path(pin_map_path).read_text(encoding="utf-8-sig")


@pytest.fixture
def pin_map_client(
    discovery_client: Mock,
    grpc_channel_pool: Mock,
    mocker: MockerFixture,
    pin_map_stub: Mock,
) -> PinMapClient:
    """Create a Client with a mock PinMapServiceStub."""
    mocker.patch(
        "ni.measurementlink.pinmap.v1.client.PinMapClient._get_stub",
        return_value=pin_map_stub,
    )
    client = PinMapClient(
        discovery_client=cast(DiscoveryClient, discovery_client),
        grpc_channel_pool=cast(GrpcChannelPool, grpc_channel_pool),
    )
    return client


@pytest.fixture
def pin_map_stub(mocker: MockerFixture) -> Mock:
    """Create a mock PinMapServiceStub."""
    stub = mocker.create_autospec(PinMapServiceStub)
    stub.UpdatePinMapFromXml = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    return stub
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_reservation.py sha256=e00ea40635ee5e548063d9e870fff29ed7013c0a4d0e8ac47b277a09b04b7b59 bytes=38528 -->
## FILE: packages/service/tests/unit/test_reservation.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_reservation.py`
- sha256: `e00ea40635ee5e548063d9e870fff29ed7013c0a4d0e8ac47b277a09b04b7b59`
- bytes: 38528

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import Mock

import pytest
from ni.measurementlink.sessionmanagement.v1 import (
    session_management_service_pb2,
)
from ni.measurementlink.sessionmanagement.v1.client import (
    SITE_SYSTEM_PINS,
    MultiSessionReservation,
    SessionInformation,
    SingleSessionReservation,
)

from tests.unit._reservation_utils import construct_session, create_grpc_session_infos
from tests.utilities import fake_driver
from tests.utilities.connection_subset import ConnectionSubset, get_connection_subset

create_nifake_session_infos = functools.partial(create_grpc_session_infos, "nifake")
create_nifoo_session_infos = functools.partial(create_grpc_session_infos, "nifoo")


def test___single_session_info___initialize_session___session_info_yielded(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(1))

    with reservation.initialize_session(construct_session, "nifake") as session_info:
        assert session_info.session_name == "MySession0"
        assert session_info.resource_name == "Dev0"
        assert session_info.instrument_type_id == "nifake"


def test___single_session_info___initialize_session___session_created(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(1))

    with reservation.initialize_session(construct_session, "nifake") as session_info:
        assert isinstance(session_info.session, fake_driver.Session)
        assert session_info.session.resource_name == "Dev0"


def test___single_session_info___initialize_session___session_lifetime_tracked(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(1))

    with reservation.initialize_session(construct_session, "nifake") as session_info:
        assert reservation._session_cache["MySession0"] is session_info.session
        assert not session_info.session.is_closed

    assert len(reservation._session_cache) == 0
    assert session_info.session.is_closed


def test___empty_instrument_type_id___initialize_session___value_error_raised(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(1))

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_session(construct_session, ""):
            pass

    assert "This method requires an instrument type ID." in exc_info.value.args[0]


def test___no_session_infos___initialize_session___value_error_raised(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(0))

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_session(construct_session, "nifake"):
            pass

    assert "No reserved sessions matched instrument type ID 'nifake'." in exc_info.value.args[0]


def test___multiple_session_infos___initialize_session___value_error_raised(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(2))

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_session(construct_session, "nifake"):
            pass

    assert (
        "Too many reserved sessions matched instrument type ID 'nifake'." in exc_info.value.args[0]
    )


def test___session_already_exists___initialize_session___runtime_error_raised(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(1))

    with reservation.initialize_session(construct_session, "nifake"):
        with pytest.raises(RuntimeError) as exc_info:
            with reservation.initialize_session(construct_session, "nifake"):
                pass

    assert "Session 'MySession0' already exists." in exc_info.value.args[0]


def test___heterogenous_session_infos___initialize_session___grouped_by_instrument_type(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifoo_session_infos(2)
    grpc_session_infos[1].instrument_type_id = "nibar"
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    with reservation.initialize_session(
        construct_session, "nifoo"
    ) as nifoo_info, reservation.initialize_session(construct_session, "nibar") as nibar_info:
        assert nifoo_info.session_name == "MySession0"
        assert nifoo_info.instrument_type_id == "nifoo"
        assert nibar_info.session_name == "MySession1"
        assert nibar_info.instrument_type_id == "nibar"


def test___multiple_session_infos___initialize_sessions___session_infos_yielded(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(3))

    with reservation.initialize_sessions(construct_session, "nifake") as session_infos:
        assert [info.session_name for info in session_infos] == [
            "MySession0",
            "MySession1",
            "MySession2",
        ]
        assert [info.resource_name for info in session_infos] == ["Dev0", "Dev1", "Dev2"]
        assert [info.instrument_type_id for info in session_infos] == ["nifake", "nifake", "nifake"]


def test___multiple_session_infos___initialize_sessions___sessions_created(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(3))

    with reservation.initialize_sessions(construct_session, "nifake") as session_infos:
        assert all([isinstance(info.session, fake_driver.Session) for info in session_infos])
        assert [info.session.resource_name for info in session_infos] == ["Dev0", "Dev1", "Dev2"]


def test___multiple_session_infos___initialize_sessions___session_lifetime_tracked(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(3))

    with reservation.initialize_sessions(construct_session, "nifake") as session_infos:
        assert reservation._session_cache["MySession0"] is session_infos[0].session
        assert reservation._session_cache["MySession1"] is session_infos[1].session
        assert reservation._session_cache["MySession2"] is session_infos[2].session
        assert all([not info.session.is_closed for info in session_infos])

    assert len(reservation._session_cache) == 0
    assert all([info.session.is_closed for info in session_infos])


def test___empty_instrument_type_id___initialize_sessions___value_error_raised(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(3))

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_sessions(construct_session, ""):
            pass

    assert "This method requires an instrument type ID." in exc_info.value.args[0]


def test___no_session_infos___initialize_sessions___value_error_raised(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, [])

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_sessions(construct_session, "nifake"):
            pass

    assert "No reserved sessions matched instrument type ID 'nifake'." in exc_info.value.args[0]


def test___session_already_exists___initialize_sessions___runtime_error_raised(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(3))

    with reservation.initialize_sessions(construct_session, "nifake"):
        with pytest.raises(RuntimeError) as exc_info:
            with reservation.initialize_sessions(construct_session, "nifake"):
                pass

    assert "Session 'MySession0' already exists." in exc_info.value.args[0]


def test___heterogenous_session_infos___initialize_sessions___grouped_by_instrument_type(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifoo_session_infos(3)
    grpc_session_infos[1].instrument_type_id = "nibar"
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    with reservation.initialize_sessions(
        construct_session, "nifoo"
    ) as nifoo_infos, reservation.initialize_sessions(construct_session, "nibar") as nibar_infos:
        assert [info.session_name for info in nifoo_infos] == ["MySession0", "MySession2"]
        assert [info.instrument_type_id for info in nifoo_infos] == ["nifoo", "nifoo"]
        assert [info.session_name for info in nibar_infos] == ["MySession1"]
        assert [info.instrument_type_id for info in nibar_infos] == ["nibar"]


def test___single_connection___get_connection___connection_returned(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        session_info = stack.enter_context(
            reservation.initialize_session(construct_session, "nifake")
        )

        connection = reservation.get_connection(fake_driver.Session)

        assert connection.pin_or_relay_name == "Pin1"
        assert connection.site == 2
        assert connection.channel_name == "3"
        assert connection.session_info == session_info


def test___session_reserved_using_pin_group___get_connection_by_pin___returns_connection(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=2, channel="2")
        group_mappings = {"PinGroup1": ["Pin1", "Pin2"]}
        reservation = MultiSessionReservation(
            session_management_client,
            grpc_session_infos,
            pin_or_relay_group_mappings=group_mappings,
            reserved_pin_or_relay_names=["PinGroup1"],
        )
        session_info = stack.enter_context(
            reservation.initialize_session(construct_session, "nifake")
        )

        connection = reservation.get_connection(fake_driver.Session, pin_or_relay_name="Pin2")

        assert connection.pin_or_relay_name == "Pin2"
        assert connection.site == 2
        assert connection.channel_name == "2"
        assert connection.session_info == session_info


def test___duplicate_pins___get_connections___returns_single_connection(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        session_info = stack.enter_context(
            reservation.initialize_session(construct_session, "nifake")
        )

        connections = reservation.get_connections(
            fake_driver.Session, pin_or_relay_names=["Pin1", "Pin1"]
        )

        assert len(connections) == 1
        assert connections[0].pin_or_relay_name == "Pin1"
        assert connections[0].site == 2
        assert connections[0].channel_name == "3"
        assert connections[0].session_info == session_info


def test___session_reserved___get_connections_by_pin_group___returns_connections(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=2, channel="2")
        group_mappings = {"PinGroup1": ["Pin1", "Pin2"]}
        reservation = MultiSessionReservation(
            session_management_client,
            grpc_session_infos,
            pin_or_relay_group_mappings=group_mappings,
            reserved_pin_or_relay_names=["PinGroup1"],
        )
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        connections = reservation.get_connections(
            fake_driver.Session, pin_or_relay_names=["PinGroup1"]
        )

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("Pin1", 2, "Dev0", "3"),
            ConnectionSubset("Pin2", 2, "Dev0", "2"),
        ]


def test___multiple_connections___get_connection___value_error_raised(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin4", site=5, channel="6")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        with pytest.raises(ValueError) as exc_info:
            _ = reservation.get_connection(fake_driver.Session)

        assert (
            "Too many reserved connections matched the specified criteria."
            in exc_info.value.args[0]
        )


@pytest.mark.parametrize(
    "kwargs,expected_message",
    [
        (
            {"pin_or_relay_name": ["Pin1"]},
            "The pin_or_relay_name parameter must be a str or None, not ['Pin1'].",
        ),
        ({"site": [2]}, "The site parameter must be an int or None, not [2]."),
        (
            {"instrument_type_id": ["nifake"]},
            "The instrument_type_id parameter must be a str or None, not ['nifake'].",
        ),
    ],
)
def test___invalid_argument_type___get_connection___type_error_raised(
    kwargs: dict[str, Any],
    expected_message: str,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        with pytest.raises(TypeError) as exc_info:
            _ = reservation.get_connection(fake_driver.Session, **kwargs)

        assert expected_message in exc_info.value.args[0]


def test___wrong_pins___get_connections___value_error_raised(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        with pytest.raises(ValueError) as exc_info:
            _ = reservation.get_connections(fake_driver.Session, ["Pin1", "Pin2", "Pin3"])

        assert (
            "No reserved connections matched pin or relay name(s) 'Pin2', 'Pin3'."
            in exc_info.value.args[0]
        )


def test___wrong_sites___get_connections___value_error_raised(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        with pytest.raises(ValueError) as exc_info:
            _ = reservation.get_connections(fake_driver.Session, sites=[1, 2, 3])

        assert "No reserved connections matched site(s) 1, 3." in exc_info.value.args[0]


def test___wrong_instrument_type_id___get_connections___value_error_raised(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        with pytest.raises(ValueError) as exc_info:
            _ = reservation.get_connections(fake_driver.Session, instrument_type_id="nifoo")

        assert (
            "No reserved connections matched instrument type ID 'nifoo'." in exc_info.value.args[0]
        )


@pytest.mark.parametrize("pin_name,site,channel_name", [("Pin1", 2, "3"), ("Pin4", 5, "6")])
def test___multiple_connections___get_connection_with_pin_name___connection_returned(
    session_management_client: Mock,
    pin_name: str,
    site: int,
    channel_name: str,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin4", site=5, channel="6")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        session_info = stack.enter_context(
            reservation.initialize_session(construct_session, "nifake")
        )

        connection = reservation.get_connection(fake_driver.Session, pin_name)

        assert connection.pin_or_relay_name == pin_name
        assert connection.site == site
        assert connection.channel_name == channel_name
        assert connection.session_info == session_info


@pytest.mark.parametrize("pin_name,site,channel_name", [("Pin1", 2, "3"), ("Pin4", 5, "6")])
def test___multiple_connections___get_connection_with_site___connection_returned(
    session_management_client: Mock,
    pin_name: str,
    site: int,
    channel_name: str,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin4", site=5, channel="6")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        session_info = stack.enter_context(
            reservation.initialize_session(construct_session, "nifake")
        )

        connection = reservation.get_connection(fake_driver.Session, site=site)

        assert connection.pin_or_relay_name == pin_name
        assert connection.site == site
        assert connection.channel_name == channel_name
        assert connection.session_info == session_info


@pytest.mark.parametrize(
    "instrument_type_id,pin_name,site,channel_name",
    [("nifoo", "Pin1", 2, "3"), ("nibar", "Pin4", 5, "6")],
)
def test___heterogenous_session_infos___get_connection_with_instrument_type_id___connection_returned(
    session_management_client: Mock,
    instrument_type_id: str,
    pin_name: str,
    site: int,
    channel_name: str,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifoo_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin4", site=5, channel="6")
        grpc_session_infos[1].instrument_type_id = "nibar"
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        nifoo_info = stack.enter_context(reservation.initialize_session(construct_session, "nifoo"))
        nibar_info = stack.enter_context(reservation.initialize_session(construct_session, "nibar"))

        connection = reservation.get_connection(
            fake_driver.Session, instrument_type_id=instrument_type_id
        )

        assert connection.pin_or_relay_name == pin_name
        assert connection.site == site
        assert connection.channel_name == channel_name
        if instrument_type_id == "nifoo":
            assert connection.session_info == nifoo_info
        else:
            assert connection.session_info == nibar_info


def test___heterogenous_session_infos___get_connections___connections_returned(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifoo_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin4", site=5, channel="6")
        grpc_session_infos[1].instrument_type_id = "nibar"
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        nifoo_info = stack.enter_context(reservation.initialize_session(construct_session, "nifoo"))
        nibar_info = stack.enter_context(reservation.initialize_session(construct_session, "nibar"))

        connections = reservation.get_connections(fake_driver.Session)

        assert [get_connection_subset(conn) for conn in connections] == [
            ConnectionSubset("Pin1", 2, "Dev0", "3"),
            ConnectionSubset("Pin4", 5, "Dev1", "6"),
        ]
        assert [conn.session for conn in connections] == [nifoo_info.session, nibar_info.session]


@pytest.mark.parametrize(
    "kwargs,expected_message",
    [
        (
            {"pin_or_relay_names": "Pin1", "sites": 5},
            "No reserved connections matched pin or relay name(s) 'Pin1' with the specified criteria: site(s) 5",
        ),
        (
            {"pin_or_relay_names": "Pin4", "sites": 2},
            "No reserved connections matched pin or relay name(s) 'Pin4' with the specified criteria: site(s) 2",
        ),
        (
            {"pin_or_relay_names": "Pin1", "instrument_type_id": "nibar"},
            "No reserved connections matched pin or relay name(s) 'Pin1' with the specified criteria: instrument type ID 'nibar'",
        ),
        (
            {"pin_or_relay_names": ["Pin1", "Pin4"], "instrument_type_id": "nibar"},
            "No reserved connections matched pin or relay name(s) 'Pin1' with the specified criteria: instrument type ID 'nibar'",
        ),
        (
            {"sites": 2, "instrument_type_id": "nibar"},
            "No reserved connections matched the specified criteria: site(s) 2; instrument type ID 'nibar'",
        ),
    ],
)
def test___heterogenous_session_infos___get_connections_with_partially_matching_criteria___value_error_raised(
    kwargs: dict[str, Any],
    expected_message: str,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifoo_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin4", site=5, channel="6")
        grpc_session_infos[1].instrument_type_id = "nibar"
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifoo"))
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nibar"))

        with pytest.raises(ValueError) as exc_info:
            _ = reservation.get_connections(fake_driver.Session, **kwargs)

        assert expected_message in exc_info.value.args[0]


def test___wrong_session_type___get_connection___type_error_raised(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
        reservation = MultiSessionReservation(session_management_client, grpc_session_infos)
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        with pytest.raises(TypeError) as exc_info:
            _ = reservation.get_connection(int)

        assert "Incorrect type for session 'MySession0'." in exc_info.value.args[0]
        assert (
            "Expected <class 'int'>, got <class 'tests.utilities.fake_driver.Session'>."
            in exc_info.value.args[0]
        )


def test___session_not_created___get_connection___type_error_raised(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    with pytest.raises(TypeError) as exc_info:
        _ = reservation.get_connection(fake_driver.Session)

    assert "Incorrect type for session 'MySession0'." in exc_info.value.args[0]
    assert (
        "Expected <class 'tests.utilities.fake_driver.Session'>, got <class 'NoneType'>."
        in exc_info.value.args[0]
    )


def test___session_not_created___get_connection_with_session_type_object___connection_returned(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=2, channel="3")
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    connection = reservation.get_connection(object)

    assert connection.pin_or_relay_name == "Pin1"
    assert connection.site == 2
    assert connection.channel_name == "3"
    assert connection.session is None


def test___no_connections___get_connection_with_session_type_object___value_error_raised(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(0)
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    with pytest.raises(ValueError) as exc_info:
        _ = reservation.get_connection(object)

    assert "No reserved connections matched the specified criteria." in exc_info.value.args[0]


def test___no_connections___get_connections_with_session_type_object___empty_list_returned(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(0)
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    connections = reservation.get_connections(object)

    assert connections == []


def test___reservation_order___get_connections_with_specified_order___connections_returned_in_specified_order(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = _create_grpc_session_infos_for_ordering()
    reservation = MultiSessionReservation(
        session_management_client,
        grpc_session_infos,
        reserved_pin_or_relay_names=["Pin3", "Pin1", "Pin4", "Pin2"],
        reserved_sites=[1, 0],
    )

    connections = [
        reservation.get_connections(
            object,
            pin_or_relay_names=["Pin1", "Pin3", "Pin2"],
            sites=[0, 1],
            instrument_type_id="nifoo",
        ),
        reservation.get_connections(
            object, pin_or_relay_names=["Pin4"], sites=[0, 1], instrument_type_id="nibar"
        ),
    ]

    assert [[get_connection_subset(conn) for conn in group] for group in connections] == [
        [
            ConnectionSubset("Pin1", 0, "Dev0", "0"),
            ConnectionSubset("Pin3", 0, "Dev1", "2"),
            ConnectionSubset("Pin2", 0, "Dev0", "1"),
            ConnectionSubset("Pin1", 1, "Dev1", "3"),
            ConnectionSubset("Pin3", 1, "Dev2", "5"),
            ConnectionSubset("Pin2", 1, "Dev2", "4"),
        ],
        [
            ConnectionSubset("Pin4", 0, "Dev3", "6"),
            ConnectionSubset("Pin4", 1, "Dev3", "7"),
        ],
    ]


def test___reservation_order___get_connections___connections_returned_in_reservation_order(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = _create_grpc_session_infos_for_ordering()
    reservation = MultiSessionReservation(
        session_management_client,
        grpc_session_infos,
        reserved_pin_or_relay_names=["Pin3", "Pin1", "Pin4", "Pin2"],
        reserved_sites=[1, 0],
    )

    connections = reservation.get_connections(object)

    assert [get_connection_subset(conn) for conn in connections] == [
        ConnectionSubset("Pin3", 1, "Dev2", "5"),
        ConnectionSubset("Pin1", 1, "Dev1", "3"),
        ConnectionSubset("Pin4", 1, "Dev3", "7"),
        ConnectionSubset("Pin2", 1, "Dev2", "4"),
        ConnectionSubset("Pin3", 0, "Dev1", "2"),
        ConnectionSubset("Pin1", 0, "Dev0", "0"),
        ConnectionSubset("Pin4", 0, "Dev3", "6"),
        ConnectionSubset("Pin2", 0, "Dev0", "1"),
    ]


def test___no_reservation_order___get_connections___connections_returned_in_default_order(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = _create_grpc_session_infos_for_ordering()
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    connections = reservation.get_connections(object)

    assert [get_connection_subset(conn) for conn in connections] == [
        ConnectionSubset("Pin1", 0, "Dev0", "0"),
        ConnectionSubset("Pin2", 0, "Dev0", "1"),
        ConnectionSubset("Pin3", 0, "Dev1", "2"),
        ConnectionSubset("Pin4", 0, "Dev3", "6"),
        ConnectionSubset("Pin1", 1, "Dev1", "3"),
        ConnectionSubset("Pin2", 1, "Dev2", "4"),
        ConnectionSubset("Pin3", 1, "Dev2", "5"),
        ConnectionSubset("Pin4", 1, "Dev3", "7"),
    ]


def test___system_pins___get_connections___system_pins_returned_in_default_order(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = _create_grpc_session_infos_with_system_pins()
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    connections = reservation.get_connections(object)

    assert [get_connection_subset(conn) for conn in connections] == [
        ConnectionSubset("SystemPin1", -1, "Dev0", "4"),
        ConnectionSubset("SystemPin2", -1, "Dev1", "5"),
        ConnectionSubset("Pin1", 0, "Dev0", "0"),
        ConnectionSubset("Pin2", 0, "Dev0", "1"),
        ConnectionSubset("Pin1", 1, "Dev1", "2"),
        ConnectionSubset("Pin2", 1, "Dev1", "3"),
    ]


def test___system_pins___get_connections_by_site___system_pins_also_returned(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = _create_grpc_session_infos_with_system_pins()
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    connections = [reservation.get_connections(object, sites=site) for site in [0, 1]]

    assert [[get_connection_subset(conn) for conn in group] for group in connections] == [
        [
            ConnectionSubset("Pin1", 0, "Dev0", "0"),
            ConnectionSubset("Pin2", 0, "Dev0", "1"),
            ConnectionSubset("SystemPin1", -1, "Dev0", "4"),
            ConnectionSubset("SystemPin2", -1, "Dev1", "5"),
        ],
        [
            ConnectionSubset("Pin1", 1, "Dev1", "2"),
            ConnectionSubset("Pin2", 1, "Dev1", "3"),
            ConnectionSubset("SystemPin1", -1, "Dev0", "4"),
            ConnectionSubset("SystemPin2", -1, "Dev1", "5"),
        ],
    ]


def test___system_pins___get_connection_with_system_pins_constant___only_system_pins_returned(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = _create_grpc_session_infos_with_system_pins()
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    connections = reservation.get_connections(object, sites=SITE_SYSTEM_PINS)

    assert [get_connection_subset(conn) for conn in connections] == [
        ConnectionSubset("SystemPin1", -1, "Dev0", "4"),
        ConnectionSubset("SystemPin2", -1, "Dev1", "5"),
    ]


def test___system_pins___get_connection_with_site_list___system_pins_returned_in_specified_order(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = _create_grpc_session_infos_with_system_pins()
    reservation = MultiSessionReservation(session_management_client, grpc_session_infos)

    connections = reservation.get_connections(object, sites=[0, SITE_SYSTEM_PINS, 1])

    assert [get_connection_subset(conn) for conn in connections] == [
        ConnectionSubset("Pin1", 0, "Dev0", "0"),
        ConnectionSubset("Pin2", 0, "Dev0", "1"),
        ConnectionSubset("SystemPin1", -1, "Dev0", "4"),
        ConnectionSubset("SystemPin2", -1, "Dev1", "5"),
        ConnectionSubset("Pin1", 1, "Dev1", "2"),
        ConnectionSubset("Pin2", 1, "Dev1", "3"),
    ]


def test___single_session_reserved___get_session_info___session_info_returned_with_null_session(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client, create_nifake_session_infos(1)
    )
    expected_session_info = SessionInformation("MySession0", "Dev0", "", "nifake", False, [], None)

    assert reservation.session_info == expected_session_info
    assert reservation.session_info.session is None


def test___single_session_created___get_session_info___session_info_returned_with_valid_session(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        reservation = SingleSessionReservation(
            session_management_client, create_nifake_session_infos(1)
        )
        expected_session_info = stack.enter_context(
            reservation.initialize_session(construct_session, "nifake")
        )

        assert reservation.session_info == expected_session_info
        assert isinstance(reservation.session_info.session, fake_driver.Session)


def test___multiple_sessions_reserved___get_session_info___session_info_returned_with_null_session(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, create_nifake_session_infos(3))
    expected_session_infos = [
        SessionInformation("MySession0", "Dev0", "", "nifake", False, [], None),
        SessionInformation("MySession1", "Dev1", "", "nifake", False, [], None),
        SessionInformation("MySession2", "Dev2", "", "nifake", False, [], None),
    ]

    assert reservation.session_info == expected_session_infos
    assert all([info.session is None for info in reservation.session_info])


def test___multiple_sessions_created___get_session_info___session_info_returned_with_valid_session(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        reservation = MultiSessionReservation(
            session_management_client, create_nifake_session_infos(3)
        )
        expected_session_infos = stack.enter_context(
            reservation.initialize_sessions(construct_session, "nifake")
        )

        assert reservation.session_info == expected_session_infos
        assert all(
            [isinstance(info.session, fake_driver.Session) for info in reservation.session_info]
        )


def _create_grpc_session_infos_for_ordering() -> (
    list[session_management_service_pb2.SessionInformation]
):
    grpc_session_infos = create_nifoo_session_infos(4)
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="1")
    grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin3", site=0, channel="2")
    grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="3")
    grpc_session_infos[2].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="4")
    grpc_session_infos[2].channel_mappings.add(pin_or_relay_name="Pin3", site=1, channel="5")
    grpc_session_infos[3].channel_mappings.add(pin_or_relay_name="Pin4", site=0, channel="6")
    grpc_session_infos[3].channel_mappings.add(pin_or_relay_name="Pin4", site=1, channel="7")
    grpc_session_infos[3].instrument_type_id = "nibar"
    return grpc_session_infos


def _create_grpc_session_infos_with_system_pins() -> (
    list[session_management_service_pb2.SessionInformation]
):
    grpc_session_infos = create_nifoo_session_infos(2)
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="SystemPin1", site=-1, channel="4")
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=0, channel="1")
    grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin1", site=1, channel="2")
    grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="3")
    grpc_session_infos[1].channel_mappings.add(pin_or_relay_name="SystemPin2", site=-1, channel="5")
    return grpc_session_infos
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_reservation_multiplexer.py sha256=53e93d647e0400c0684143b3940b474dfaf76f7fb5d2ceee9384c27bb7761cc3 bytes=37473 -->
## FILE: packages/service/tests/unit/test_reservation_multiplexer.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_reservation_multiplexer.py`
- sha256: `53e93d647e0400c0684143b3940b474dfaf76f7fb5d2ceee9384c27bb7761cc3`
- bytes: 37473

````python
from __future__ import annotations

import functools
from contextlib import ExitStack
from typing import Any
from unittest.mock import Mock

import pytest
from ni.measurementlink.sessionmanagement.v1 import (
    session_management_service_pb2,
)
from ni.measurementlink.sessionmanagement.v1.client import (
    MultiplexerSessionInformation,
    MultiSessionReservation,
    SingleSessionReservation,
)

from tests.unit._reservation_utils import (
    construct_multiplexer_session,
    construct_session,
    create_grpc_multiplexer_session_infos,
    create_grpc_session_infos,
)
from tests.utilities import fake_multiplexer_driver
from tests.utilities.connection_subset import (
    ConnectionSubset,
    get_connection_subset_with_multiplexer,
)

create_nifake_session_infos = functools.partial(create_grpc_session_infos, "nifake")
create_nimultiplexer_session_infos = functools.partial(
    create_grpc_multiplexer_session_infos, "nimultiplexer"
)


@pytest.mark.parametrize(
    "kwargs,expected_message",
    [
        (
            {"multiplexer_type_id": ["nimultiplexer"]},
            "The multiplexer_type_id parameter must be a str or None, not ['nimultiplexer'].",
        ),
    ],
)
def test___invalid_argument_type___intialize_multiplexer_session___raises_type_error(
    kwargs: dict[str, Any],
    expected_message: str,
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1",
            site=2,
            channel="3",
            multiplexer_resource_name="Mux0",
            multiplexer_route="route0",
        )
        reservation = SingleSessionReservation(
            session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
        )

        with pytest.raises(TypeError) as exc_info:
            _ = stack.enter_context(
                reservation.initialize_multiplexer_session(construct_multiplexer_session, **kwargs)
            )

        assert expected_message in exc_info.value.args[0]


def test___single_multiplexer_session_info___initialize_multiplexer_session___yeilds_session_info(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(1),
    )

    with reservation.initialize_multiplexer_session(construct_multiplexer_session) as session_info:
        assert session_info.session is not None
        assert session_info.session_name == "MyMultiplexer0"
        assert session_info.resource_name == "Mux0"


def test___single_multiplexer_session_info___initialize_multiplexer_session___creates_session(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(1),
    )

    with reservation.initialize_multiplexer_session(construct_multiplexer_session) as session_info:
        assert isinstance(session_info.session, fake_multiplexer_driver.Session)
        assert session_info.session.resource_name == "Mux0"


def test___single_multiplexer_session_info___initialize_multiplexer_session___session_lifetime_tracked(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(1),
    )

    with reservation.initialize_multiplexer_session(construct_multiplexer_session) as session_info:
        assert reservation._multiplexer_session_cache["MyMultiplexer0"] is session_info.session
        assert not session_info.session.is_closed

    assert len(reservation._multiplexer_session_cache) == 0
    assert session_info.session.is_closed


def test___no_multiplexer_session_infos___initialize_multiplexer_session___raises_value_error(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client,
        create_nifake_session_infos(0),
        create_nimultiplexer_session_infos(0),
    )

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_multiplexer_session(construct_multiplexer_session):
            pass

    assert "No multiplexer sessions available to initialize." in exc_info.value.args[0]


def test___multiple_multiplexer_session_infos___initialize_multiplexer_session___raises_value_error(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client,
        create_nifake_session_infos(2),
        create_nimultiplexer_session_infos(2),
    )

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_multiplexer_session(construct_multiplexer_session):
            pass

    assert (
        "Too many multiplexer sessions matched the specified criteria. Expected single multiplexer session, got 2 sessions."
        in exc_info.value.args[0]
    )


def test___multiplexer_session_already_exists___initialize_multiplexer_session___raises_runtime_error(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(1),
    )

    with reservation.initialize_multiplexer_session(construct_multiplexer_session):
        with pytest.raises(RuntimeError) as exc_info:
            with reservation.initialize_multiplexer_session(construct_multiplexer_session):
                pass

    assert "Multiplexer session 'MyMultiplexer0' already exists." in exc_info.value.args[0]


def test___wrong_multiplexer_type_id___initialize_multiplexer_session___raises_value_error(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
    reservation = SingleSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_multiplexer_session(
            construct_multiplexer_session, multiplexer_type_id="invalid_type_id"
        ):
            pass

    assert (
        "No multiplexer sessions matched multiplexer type id 'invalid_type_id'."
        in exc_info.value.args[0]
    )


def test___multiple_multiplexer_session_infos___initialize_multiplexer_session_with_type_id___creates_session_for_specified_type_id(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(3)
    grpc_multiplexer_session_infos[1].multiplexer_type_id = "nibar"
    reservation = SingleSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    with reservation.initialize_multiplexer_session(
        construct_multiplexer_session, multiplexer_type_id="nibar"
    ) as session_info:
        assert session_info.session_name == "MyMultiplexer1"
        assert session_info.multiplexer_type_id == "nibar"


def test___multiple_multiplexer_session_infos___initialize_multiplexer_sessions___yeilds_session_infos(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(3),
    )

    with reservation.initialize_multiplexer_sessions(
        construct_multiplexer_session
    ) as session_infos:
        assert [info.session_name for info in session_infos] == [
            "MyMultiplexer0",
            "MyMultiplexer1",
            "MyMultiplexer2",
        ]
        assert [info.resource_name for info in session_infos] == ["Mux0", "Mux1", "Mux2"]
        assert [info.multiplexer_type_id for info in session_infos] == [
            "nimultiplexer",
            "nimultiplexer",
            "nimultiplexer",
        ]


def test___multiple_multiplexer_session_infos___initialize_multiplexer_sessions___creates_sessions(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(3),
    )

    with reservation.initialize_multiplexer_sessions(
        construct_multiplexer_session
    ) as session_infos:
        assert all(
            [isinstance(info.session, fake_multiplexer_driver.Session) for info in session_infos]
        )
        assert [info.session.resource_name for info in session_infos] == ["Mux0", "Mux1", "Mux2"]


def test___multiple_multiplexer_session_infos___initialize_multiplexer_sessions___session_lifetime_tracked(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(3),
    )

    with reservation.initialize_multiplexer_sessions(
        construct_multiplexer_session
    ) as session_infos:
        assert reservation._multiplexer_session_cache["MyMultiplexer0"] is session_infos[0].session
        assert reservation._multiplexer_session_cache["MyMultiplexer1"] is session_infos[1].session
        assert reservation._multiplexer_session_cache["MyMultiplexer2"] is session_infos[2].session
        assert all([not info.session.is_closed for info in session_infos])

    assert len(reservation._multiplexer_session_cache) == 0
    assert all([info.session.is_closed for info in session_infos])


def test___no_multiplexer_session_infos___initialize_multiplexer_sessions___raises_value_error(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(session_management_client, [])

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_multiplexer_sessions(construct_multiplexer_session):
            pass

    assert "No multiplexer sessions available to initialize." in exc_info.value.args[0]


def test___session_already_exists___initialize_multiplexer_sessions___raises_runtime_error(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(2),
    )

    with reservation.initialize_multiplexer_sessions(construct_multiplexer_session):
        with pytest.raises(RuntimeError) as exc_info:
            with reservation.initialize_multiplexer_sessions(construct_multiplexer_session):
                pass

    assert "Multiplexer session 'MyMultiplexer0' already exists." in exc_info.value.args[0]


def test___heterogenous_multiplexer_session_infos___initialize_multiplexer_sessions___creates_all_sessions(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(2)
    grpc_multiplexer_session_infos[1].multiplexer_type_id = "nibar"
    reservation = SingleSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    with reservation.initialize_multiplexer_sessions(
        construct_multiplexer_session
    ) as session_infos:
        assert session_infos[0].session_name == "MyMultiplexer0"
        assert session_infos[0].multiplexer_type_id == "nimultiplexer"
        assert session_infos[1].session_name == "MyMultiplexer1"
        assert session_infos[1].multiplexer_type_id == "nibar"


def test___heterogenous_multiplexer_session_infos___initialize_multiplexer_sessions_with_type_id___creates_sessions_for_specified_type_id(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(3)
    grpc_multiplexer_session_infos[1].multiplexer_type_id = "nibar"
    reservation = SingleSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    with reservation.initialize_multiplexer_sessions(
        construct_multiplexer_session, multiplexer_type_id="nimultiplexer"
    ) as session_infos:
        assert len(session_infos) == 2
        assert session_infos[0].session_name == "MyMultiplexer0"
        assert session_infos[1].session_name == "MyMultiplexer2"
        assert [info.multiplexer_type_id for info in session_infos] == [
            "nimultiplexer",
            "nimultiplexer",
        ]


def test___wrong_multiplexer_type_id___initialize_multiplexer_sessions___raises_value_error(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
    reservation = SingleSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    with pytest.raises(ValueError) as exc_info:
        with reservation.initialize_multiplexer_sessions(
            construct_multiplexer_session, multiplexer_type_id="invalid_type_id"
        ):
            pass

    assert (
        "No multiplexer sessions matched multiplexer type id 'invalid_type_id'."
        in exc_info.value.args[0]
    )


def test___single_connection___get_connection_with_multiplexer___returns_connection(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1",
            site=2,
            channel="3",
            multiplexer_resource_name="Mux0",
            multiplexer_route="route0",
        )
        reservation = MultiSessionReservation(
            session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
        )
        session_info = stack.enter_context(
            reservation.initialize_multiplexer_session(construct_multiplexer_session)
        )

        connection = reservation.get_connection_with_multiplexer(
            object, fake_multiplexer_driver.Session
        )

        assert get_connection_subset_with_multiplexer(connection) == ConnectionSubset(
            "Pin1", 2, "Dev0", "3", "Mux0", "route0"
        )
        assert connection.multiplexer_session_info == session_info


def test___multiple_connections___get_connection_with_multiplexer___raises_value_error(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1",
            site=2,
            channel="3",
            multiplexer_resource_name="Mux0",
            multiplexer_route="route0",
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin4",
            site=5,
            channel="6",
            multiplexer_resource_name="Mux0",
            multiplexer_route="route1",
        )
        reservation = MultiSessionReservation(
            session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
        )
        _ = stack.enter_context(
            reservation.initialize_multiplexer_session(construct_multiplexer_session)
        )

        with pytest.raises(ValueError) as exc_info:
            _ = reservation.get_connection_with_multiplexer(object, fake_multiplexer_driver.Session)

        assert (
            "Too many reserved connections matched the specified criteria."
            in exc_info.value.args[0]
        )


def test___multiplexer_session_not_created___get_connection_with_multiplexer___raises_type_error(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1",
            site=2,
            channel="3",
            multiplexer_resource_name="Mux0",
            multiplexer_route="route1",
        )
        reservation = MultiSessionReservation(
            session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
        )
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        with pytest.raises(TypeError) as exc_info:
            _ = reservation.get_connection_with_multiplexer(object, fake_multiplexer_driver.Session)

        assert "Incorrect type for multiplexer session 'MyMultiplexer0'." in exc_info.value.args[0]
        assert (
            "Expected <class 'tests.utilities.fake_multiplexer_driver.Session'>, got <class 'NoneType'>."
            in exc_info.value.args[0]
        )


def test___multiplexer_session_not_created___get_connection_with_multiplexer_using_object_type___returns_connection(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1",
            site=2,
            channel="3",
            multiplexer_resource_name="Mux0",
            multiplexer_route="route1",
        )
        reservation = MultiSessionReservation(
            session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
        )
        _ = stack.enter_context(reservation.initialize_session(construct_session, "nifake"))

        connection = reservation.get_connection_with_multiplexer(object, object)

        assert get_connection_subset_with_multiplexer(connection) == ConnectionSubset(
            "Pin1", 2, "Dev0", "3", "Mux0", "route1"
        )
        assert connection.multiplexer_session is None


def test___no_connection___get_connection_with_multiplexer___raises_value_error(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(0)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(0)
    reservation = MultiSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    with pytest.raises(ValueError) as exc_info:
        _ = reservation.get_connection_with_multiplexer(object, object)

    assert "No reserved connections matched the specified criteria." in exc_info.value.args[0]


def test___no_connections___get_connections_with_multiplexer_using_object_type___returns_empty_list(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(0)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(0)
    reservation = MultiSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    connections = reservation.get_connections_with_multiplexer(object, object)

    assert connections == []


def test___reservation_order___get_connections_with_multiplexer_in_specific_order___returns_connections_in_specified_order(
    session_management_client: Mock,
) -> None:
    (
        grpc_session_infos,
        grpc_multiplexer_session_infos,
    ) = _create_grpc_session_and_multiplexer_session_infos_for_ordering()
    reservation = MultiSessionReservation(
        session_management_client,
        grpc_session_infos,
        grpc_multiplexer_session_infos,
        reserved_pin_or_relay_names=["Pin3", "Pin1", "Pin4", "Pin2"],
        reserved_sites=[1, 0],
    )

    connections = [
        reservation.get_connections_with_multiplexer(
            object,
            object,
            pin_or_relay_names=["Pin1", "Pin3", "Pin2"],
            sites=[0, 1],
            instrument_type_id="nifake",
        ),
        reservation.get_connections_with_multiplexer(
            object, object, pin_or_relay_names=["Pin4"], sites=[0, 1], instrument_type_id="nibar"
        ),
    ]

    assert [
        [get_connection_subset_with_multiplexer(conn) for conn in group] for group in connections
    ] == [
        [
            ConnectionSubset("Pin1", 0, "Dev0", "0", "Mux0", "route1"),
            ConnectionSubset("Pin3", 0, "Dev1", "2", "Mux0", "route3"),
            ConnectionSubset("Pin2", 0, "Dev0", "1", "Mux0", "route2"),
            ConnectionSubset("Pin1", 1, "Dev1", "3", "Mux0", "route4"),
            ConnectionSubset("Pin3", 1, "Dev2", "5", "Mux0", "route6"),
            ConnectionSubset("Pin2", 1, "Dev2", "4", "Mux0", "route5"),
        ],
        [
            ConnectionSubset("Pin4", 0, "Dev3", "6", "Mux0", "route7"),
            ConnectionSubset("Pin4", 1, "Dev3", "7", "Mux0", "route8"),
        ],
    ]


def test___reservation_order___get_connections_with_multiplexer___returns_connections_in_reservation_order(
    session_management_client: Mock,
) -> None:
    (
        grpc_session_infos,
        grpc_multiplexer_session_infos,
    ) = _create_grpc_session_and_multiplexer_session_infos_for_ordering()
    reservation = MultiSessionReservation(
        session_management_client,
        grpc_session_infos,
        grpc_multiplexer_session_infos,
        reserved_pin_or_relay_names=["Pin3", "Pin1", "Pin4", "Pin2"],
        reserved_sites=[1, 0],
    )

    connections = reservation.get_connections_with_multiplexer(object, object)

    assert [get_connection_subset_with_multiplexer(conn) for conn in connections] == [
        ConnectionSubset("Pin3", 1, "Dev2", "5", "Mux0", "route6"),
        ConnectionSubset("Pin1", 1, "Dev1", "3", "Mux0", "route4"),
        ConnectionSubset("Pin4", 1, "Dev3", "7", "Mux0", "route8"),
        ConnectionSubset("Pin2", 1, "Dev2", "4", "Mux0", "route5"),
        ConnectionSubset("Pin3", 0, "Dev1", "2", "Mux0", "route3"),
        ConnectionSubset("Pin1", 0, "Dev0", "0", "Mux0", "route1"),
        ConnectionSubset("Pin4", 0, "Dev3", "6", "Mux0", "route7"),
        ConnectionSubset("Pin2", 0, "Dev0", "1", "Mux0", "route2"),
    ]


def test___no_reservation_order___get_connections_with_multiplexer___returns_connections_in_default_order(
    session_management_client: Mock,
) -> None:
    (
        grpc_session_infos,
        grpc_multiplexer_session_infos,
    ) = _create_grpc_session_and_multiplexer_session_infos_for_ordering()
    reservation = MultiSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    connections = reservation.get_connections_with_multiplexer(object, object)

    assert [get_connection_subset_with_multiplexer(conn) for conn in connections] == [
        ConnectionSubset("Pin1", 0, "Dev0", "0", "Mux0", "route1"),
        ConnectionSubset("Pin2", 0, "Dev0", "1", "Mux0", "route2"),
        ConnectionSubset("Pin3", 0, "Dev1", "2", "Mux0", "route3"),
        ConnectionSubset("Pin4", 0, "Dev3", "6", "Mux0", "route7"),
        ConnectionSubset("Pin1", 1, "Dev1", "3", "Mux0", "route4"),
        ConnectionSubset("Pin2", 1, "Dev2", "4", "Mux0", "route5"),
        ConnectionSubset("Pin3", 1, "Dev2", "5", "Mux0", "route6"),
        ConnectionSubset("Pin4", 1, "Dev3", "7", "Mux0", "route8"),
    ]


def test___partial_multiplexed_connections___get_connections_with_multiplexer_using_session_type___returns_all_specified_pin_connections(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
    grpc_session_infos[0].channel_mappings.add(
        pin_or_relay_name="Pin2",
        site=0,
        channel="1",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route1",
    )
    grpc_session_infos[0].channel_mappings.add(
        pin_or_relay_name="Pin3",
        site=1,
        channel="1",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route2",
    )
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin4", site=0, channel="3")
    reservation = MultiSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    connections = reservation.get_connections_with_multiplexer(object, object)

    assert [get_connection_subset_with_multiplexer(conn) for conn in connections] == [
        ConnectionSubset("Pin1", 0, "Dev0", "0", "", ""),
        ConnectionSubset("Pin2", 0, "Dev0", "1", "Mux0", "route1"),
        ConnectionSubset("Pin4", 0, "Dev0", "3", "", ""),
        ConnectionSubset("Pin3", 1, "Dev0", "1", "Mux0", "route2"),
    ]


def test____connection_with_no_multiplexers___get_connection_with_multiplexer___returns_connection(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
    reservation = SingleSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    connection = reservation.get_connection_with_multiplexer(object, object)

    assert get_connection_subset_with_multiplexer(connection) == ConnectionSubset(
        "Pin1", 0, "Dev0", "0", "", ""
    )


def test____connections_with_no_multiplexers___get_connections_with_multiplexer___returns_all_connections(
    session_management_client: Mock,
) -> None:
    grpc_session_infos = create_nifake_session_infos(1)
    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin1", site=0, channel="0")
    grpc_session_infos[0].channel_mappings.add(pin_or_relay_name="Pin2", site=1, channel="2")
    reservation = SingleSessionReservation(
        session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
    )

    connections = reservation.get_connections_with_multiplexer(object, object)

    assert [get_connection_subset_with_multiplexer(conn) for conn in connections] == [
        ConnectionSubset("Pin1", 0, "Dev0", "0", "", ""),
        ConnectionSubset("Pin2", 1, "Dev0", "2", "", ""),
    ]


def test___created_multiplexer_session___get_connection_with_multiplexer___returns_connection_with_multiplexer_session(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1",
            site=0,
            channel="1",
            multiplexer_resource_name="Mux0",
            multiplexer_route="route1",
        )
        reservation = MultiSessionReservation(
            session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
        )
        _ = stack.enter_context(
            reservation.initialize_multiplexer_session(construct_multiplexer_session)
        )

        connection = reservation.get_connection_with_multiplexer(
            object, fake_multiplexer_driver.Session
        )

        assert isinstance(connection.multiplexer_session, fake_multiplexer_driver.Session)
        assert get_connection_subset_with_multiplexer(connection) == ConnectionSubset(
            "Pin1", 0, "Dev0", "1", "Mux0", "route1"
        )


def test___created_multiplexer_sessions___get_connections_with_multiplexer___returns_connections_with_multiplexer_sessions(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        grpc_session_infos = create_nifake_session_infos(1)
        grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(2)
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin1",
            site=0,
            channel="1",
            multiplexer_resource_name="Mux0",
            multiplexer_route="route1",
        )
        grpc_session_infos[0].channel_mappings.add(
            pin_or_relay_name="Pin2",
            site=1,
            channel="1",
            multiplexer_resource_name="Mux1",
            multiplexer_route="route2",
        )
        reservation = MultiSessionReservation(
            session_management_client, grpc_session_infos, grpc_multiplexer_session_infos
        )
        _ = stack.enter_context(
            reservation.initialize_multiplexer_sessions(construct_multiplexer_session)
        )

        connections = reservation.get_connections_with_multiplexer(
            object, fake_multiplexer_driver.Session
        )

        assert all(
            [
                isinstance(conn.multiplexer_session, fake_multiplexer_driver.Session)
                for conn in connections
            ]
        )
        assert [get_connection_subset_with_multiplexer(conn) for conn in connections] == [
            ConnectionSubset("Pin1", 0, "Dev0", "1", "Mux0", "route1"),
            ConnectionSubset("Pin2", 1, "Dev0", "1", "Mux1", "route2"),
        ]


def test___reserved_single_session_with_single_multiplexer___get_multiplexer_session_info___returns_multiplexer_session_info_with_null_session(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(1),
    )
    expected_multiplexer_session_info = MultiplexerSessionInformation(
        "MyMultiplexer0", "Mux0", "nimultiplexer", False, None
    )

    assert reservation.multiplexer_session_info[0] == expected_multiplexer_session_info
    assert reservation.multiplexer_session_info[0].session is None


def test___reserved_single_session_with_multiple_multiplexers___get_multiplexer_session_info___returns_multiplexer_session_info_with_null_session(
    session_management_client: Mock,
) -> None:
    reservation = SingleSessionReservation(
        session_management_client,
        create_nifake_session_infos(1),
        create_nimultiplexer_session_infos(3),
    )
    expected_multiplexer_session_infos = [
        MultiplexerSessionInformation("MyMultiplexer0", "Mux0", "nimultiplexer", False, None),
        MultiplexerSessionInformation("MyMultiplexer1", "Mux1", "nimultiplexer", False, None),
        MultiplexerSessionInformation("MyMultiplexer2", "Mux2", "nimultiplexer", False, None),
    ]

    assert reservation.multiplexer_session_info == expected_multiplexer_session_infos
    assert all([info.session is None for info in reservation.multiplexer_session_info])


def test___created_single_multiplexer_session___get_multiplexer_session_info___returns_multiplexer_session_info_with_valid_session(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        reservation = SingleSessionReservation(
            session_management_client,
            create_nifake_session_infos(1),
            create_nimultiplexer_session_infos(1),
        )
        expected_session_info = stack.enter_context(
            reservation.initialize_multiplexer_session(construct_multiplexer_session)
        )

        assert reservation.multiplexer_session_info[0] == expected_session_info
        assert isinstance(
            reservation.multiplexer_session_info[0].session, fake_multiplexer_driver.Session
        )


def test___reserved_multiple_sessions_with_single_multiplexer___get_multiplexer_session_info___returns_multiplexer_session_info_with_null_session(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client,
        create_nifake_session_infos(2),
        create_nimultiplexer_session_infos(1),
    )
    expected_multiplexer_session_info = MultiplexerSessionInformation(
        "MyMultiplexer0", "Mux0", "nimultiplexer", False, None
    )

    assert reservation.multiplexer_session_info[0] == expected_multiplexer_session_info
    assert reservation.multiplexer_session_info[0].session is None


def test___reserved_multiple_sessions_with_multiple_multiplexers___get_multiplexer_session_info___returns_multiplexer_session_info_with_null_session(
    session_management_client: Mock,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client,
        create_nifake_session_infos(2),
        create_nimultiplexer_session_infos(3),
    )
    expected_multiplexer_session_infos = [
        MultiplexerSessionInformation("MyMultiplexer0", "Mux0", "nimultiplexer", False, None),
        MultiplexerSessionInformation("MyMultiplexer1", "Mux1", "nimultiplexer", False, None),
        MultiplexerSessionInformation("MyMultiplexer2", "Mux2", "nimultiplexer", False, None),
    ]

    assert reservation.multiplexer_session_info == expected_multiplexer_session_infos
    assert all([info.session is None for info in reservation.multiplexer_session_info])


def test___created_multiple_multiplexer_sessions___get_multiplexer_session_info___returns_multiplexer_session_info_with_valid_session(
    session_management_client: Mock,
) -> None:
    with ExitStack() as stack:
        reservation = MultiSessionReservation(
            session_management_client,
            create_nifake_session_infos(2),
            create_nimultiplexer_session_infos(2),
        )
        expected_session_infos = stack.enter_context(
            reservation.initialize_multiplexer_sessions(construct_multiplexer_session)
        )

        assert reservation.multiplexer_session_info == expected_session_infos
        assert all(
            [
                isinstance(info.session, fake_multiplexer_driver.Session)
                for info in reservation.multiplexer_session_info
            ]
        )


def _create_grpc_session_and_multiplexer_session_infos_for_ordering() -> tuple[
    list[session_management_service_pb2.SessionInformation],
    list[session_management_service_pb2.MultiplexerSessionInformation],
]:
    grpc_session_infos = create_nifake_session_infos(4)
    grpc_session_infos[0].channel_mappings.add(
        pin_or_relay_name="Pin1",
        site=0,
        channel="0",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route1",
    )
    grpc_session_infos[0].channel_mappings.add(
        pin_or_relay_name="Pin2",
        site=0,
        channel="1",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route2",
    )
    grpc_session_infos[1].channel_mappings.add(
        pin_or_relay_name="Pin3",
        site=0,
        channel="2",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route3",
    )
    grpc_session_infos[1].channel_mappings.add(
        pin_or_relay_name="Pin1",
        site=1,
        channel="3",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route4",
    )
    grpc_session_infos[2].channel_mappings.add(
        pin_or_relay_name="Pin2",
        site=1,
        channel="4",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route5",
    )
    grpc_session_infos[2].channel_mappings.add(
        pin_or_relay_name="Pin3",
        site=1,
        channel="5",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route6",
    )
    grpc_session_infos[3].channel_mappings.add(
        pin_or_relay_name="Pin4",
        site=0,
        channel="6",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route7",
    )
    grpc_session_infos[3].channel_mappings.add(
        pin_or_relay_name="Pin4",
        site=1,
        channel="7",
        multiplexer_resource_name="Mux0",
        multiplexer_route="route8",
    )
    grpc_session_infos[3].instrument_type_id = "nibar"

    grpc_multiplexer_session_infos = create_nimultiplexer_session_infos(1)
    return (grpc_session_infos, grpc_multiplexer_session_infos)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_service.py sha256=cbd3ed400ba80a80baf577dc790abb9c537e7be1278c8574d8b3292ba4d7fbcc bytes=19296 -->
## FILE: packages/service/tests/unit/test_service.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_service.py`
- sha256: `cbd3ed400ba80a80baf577dc790abb9c537e7be1278c8574d8b3292ba4d7fbcc`
- bytes: 19296

````python
"""Tests to validated user facing decorators in service.py."""

from __future__ import annotations

import pathlib
from enum import Enum

import pytest
from ni.protobuf.types import xydata_pb2
from pytest_mock import MockerFixture

from ni_measurement_plugin_sdk_service import _datatypeinfo
from ni_measurement_plugin_sdk_service._annotations import TYPE_SPECIALIZATION_KEY
from ni_measurement_plugin_sdk_service.measurement.info import (
    DataType,
    TypeSpecialization,
)
from ni_measurement_plugin_sdk_service.measurement.service import MeasurementService


class Color(Enum):
    """Primary colors used for testing enum-typed config and output."""

    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3


class ColorWithoutZeroValue(Enum):
    """Enum with missing zero value used for testing enum-typed config and output."""

    RED = 1
    GREEN = 2
    BLUE = 3


double_xy_data = xydata_pb2.DoubleXYData()
double_xy_data.x_data.append(4)
double_xy_data.y_data.append(6)


def test___measurement_service___register_measurement_method___method_registered(
    measurement_service: MeasurementService,
):
    """Test to validate register_measurement decorator."""
    measurement_service.register_measurement(_fake_measurement_function)

    measurement_service._measure_function == _fake_measurement_function


@pytest.mark.parametrize(
    "display_name,type,default_value",
    [
        ("BoolConfiguration", DataType.Boolean, True),
        ("StringConfiguration", DataType.String, "DefaultString"),
        ("DoubleConfiguration", DataType.Double, 0.899),
        ("Float", DataType.Float, 0.100),
        ("IntFloat", DataType.Float, 1),
        ("Double1DArray", DataType.DoubleArray1D, [1.009, -1.0009]),
        ("Int32", DataType.Int32, -8799),
        ("Int64", DataType.Int64, -999),
        ("UInt32", DataType.UInt32, 3994),
        ("UInt64", DataType.UInt64, 3456),
        ("UInt64", DataType.UInt64, False),
    ],
)
def test___measurement_service___add_configuration__configuration_added(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
):
    measurement_service.configuration(display_name, type, default_value)(_fake_measurement_function)
    data_type_info = _datatypeinfo.get_type_info(type)

    assert any(
        param.display_name == display_name
        and param.type == data_type_info.grpc_field_type
        and param.repeated == data_type_info.repeated
        and param.default_value == default_value
        and param.message_type == data_type_info.message_type
        for param in measurement_service._configuration_parameter_list
    )


@pytest.mark.parametrize(
    "display_name,type,default_value,instrument_type",
    [
        ("PinConfiguration", DataType.Pin, "Pin1", "test instrument"),
        ("PinArrayConfiguration", DataType.PinArray1D, ["Pin1", "Pin2"], "test instrument 2"),
    ],
)
def test___measurement_service___add_pin_configuration__pin_configuration_added_with_deprecation_warning(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
    instrument_type: str,
):
    with pytest.deprecated_call():
        measurement_service.configuration(
            display_name, type, default_value, instrument_type=instrument_type
        )(_fake_measurement_function)
    data_type_info = _datatypeinfo.get_type_info(type)

    assert any(
        param.display_name == display_name
        and param.type == data_type_info.grpc_field_type
        and param.repeated == data_type_info.repeated
        and param.default_value == default_value
        and param.annotations
        == {
            TYPE_SPECIALIZATION_KEY: TypeSpecialization.Pin.value,
            "ni/pin.instrument_type": instrument_type,
        }
        for param in measurement_service._configuration_parameter_list
    )


@pytest.mark.parametrize(
    "display_name,type,default_value,instrument_type",
    [
        ("IOResourceConfiguration", DataType.IOResource, "Pin1", "test instrument"),
        (
            "IOResourceArrayConfiguration",
            DataType.IOResourceArray1D,
            ["Pin1", "Pin2"],
            "test instrument 2",
        ),
    ],
)
def test___measurement_service___add_ioresource_configuration__ioresource_configuration_added(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
    instrument_type: str,
):
    measurement_service.configuration(
        display_name, type, default_value, instrument_type=instrument_type
    )(_fake_measurement_function)
    data_type_info = _datatypeinfo.get_type_info(type)

    assert any(
        param.display_name == display_name
        and param.type == data_type_info.grpc_field_type
        and param.repeated == data_type_info.repeated
        and param.default_value == default_value
        and param.annotations
        == {
            TYPE_SPECIALIZATION_KEY: TypeSpecialization.IOResource.value,
            "ni/ioresource.instrument_type": instrument_type,
        }
        for param in measurement_service._configuration_parameter_list
    )


@pytest.mark.parametrize(
    "display_name,type,default_value",
    [
        ("BoolConfiguration", DataType.Boolean, True),
        ("StringConfiguration", DataType.String, "DefaultString"),
        ("DoubleConfiguration", DataType.Double, 0.899),
        ("Float", DataType.Float, 0.100),
        ("Double1DArray", DataType.DoubleArray1D, [1.009, -1.0009]),
        ("Int32", DataType.Int32, -8799),
        ("Int64", DataType.Int64, -999),
        ("UInt32", DataType.UInt32, 3994),
        ("UInt44", DataType.UInt64, 3456),
        ("UInt44", DataType.UInt64, False),
    ],
)
def test___measurement_service___add_non_pin_configuration__pin_type_annotations_not_added(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
):
    measurement_service.configuration(display_name, type, default_value)(_fake_measurement_function)

    assert not all(
        param.annotations.get(TYPE_SPECIALIZATION_KEY) == TypeSpecialization.Pin.value
        for param in measurement_service._configuration_parameter_list
    )


@pytest.mark.parametrize(
    "display_name,type,default_value",
    [
        ("BoolConfiguration", DataType.Boolean, True),
        ("StringConfiguration", DataType.String, "DefaultString"),
        ("DoubleConfiguration", DataType.Double, 0.899),
        ("Float", DataType.Float, 0.100),
        ("Double1DArray", DataType.DoubleArray1D, [1.009, -1.0009]),
        ("Int32", DataType.Int32, -8799),
        ("Int64", DataType.Int64, -999),
        ("UInt32", DataType.UInt32, 3994),
        ("UInt44", DataType.UInt64, 3456),
        ("UInt44", DataType.UInt64, False),
    ],
)
def test___measurement_service___add_non_ioresource_configuration__ioresource_type_annotations_not_added(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
):
    measurement_service.configuration(display_name, type, default_value)(_fake_measurement_function)

    assert not all(
        param.annotations.get(TYPE_SPECIALIZATION_KEY) == TypeSpecialization.IOResource.value
        for param in measurement_service._configuration_parameter_list
    )


@pytest.mark.parametrize(
    "display_name,type,default_value",
    [
        ("PathConfiguration", DataType.Path, "path1"),
        ("PathArrayConfiguration", DataType.PathArray1D, ["path1", "path2"]),
    ],
)
def test___measurement_service___add_path_configuration__path_configuration_added(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
):
    measurement_service.configuration(display_name, type, default_value)(_fake_measurement_function)
    data_type_info = _datatypeinfo.get_type_info(type)

    assert any(
        param.display_name == display_name
        and param.type == data_type_info.grpc_field_type
        and param.repeated == data_type_info.repeated
        and param.default_value == default_value
        and param.annotations
        == {
            TYPE_SPECIALIZATION_KEY: TypeSpecialization.Path.value,
        }
        for param in measurement_service._configuration_parameter_list
    )


@pytest.mark.parametrize(
    "display_name,type,default_value",
    [
        ("BoolConfiguration", DataType.Boolean, True),
        ("StringConfiguration", DataType.String, "DefaultString"),
        ("DoubleConfiguration", DataType.Double, 0.899),
        ("Float", DataType.Float, 0.100),
        ("Double1DArray", DataType.DoubleArray1D, [1.009, -1.0009]),
        ("Int32", DataType.Int32, -8799),
        ("Int64", DataType.Int64, -999),
        ("UInt32", DataType.UInt32, 3994),
        ("UInt64", DataType.UInt64, 3456),
    ],
)
def test___measurement_service___add_non_path_configuration__path_type_annotations_not_added(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
):
    """Test to validate the configuration decorator."""
    measurement_service.configuration(display_name, type, default_value)(_fake_measurement_function)

    assert not all(
        param.annotations.get(TYPE_SPECIALIZATION_KEY) == TypeSpecialization.Path.value
        for param in measurement_service._configuration_parameter_list
    )


@pytest.mark.parametrize(
    "display_name,type,default_value",
    [
        ("BoolConfiguration", DataType.Boolean, "MismatchDefaultValue"),
        ("StringConfiguration", DataType.String, True),
        ("DoubleConfiguration", DataType.Double, ""),
        ("Double1DArray", DataType.DoubleArray1D, ""),
        ("Int32", DataType.Int32, 1.0),
        ("Int64", DataType.Int64, 1.0),
        ("UInt32", DataType.UInt32, [1.009, -1.0009]),
        ("UInt44", DataType.UInt64, ""),
        ("Pin", DataType.Pin, 1.0),
        ("Pin1DArray", DataType.PinArray1D, [1.009, -1.0009]),
        ("IOResource", DataType.IOResource, 1.0),
        ("IOResource1DArray", DataType.IOResourceArray1D, [1.009, -1.0009]),
        ("Path", DataType.Path, 1.0),
        ("Path1DArray", DataType.PathArray1D, [1.009, -1.0009]),
    ],
)
@pytest.mark.filterwarnings("ignore:.*Pin.*:DeprecationWarning")
def test___measurement_service___add_configuration_with_mismatch_default_value__raises_type_error(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
):
    with pytest.raises(TypeError):
        measurement_service.configuration(display_name, type, default_value)(
            _fake_measurement_function
        )


@pytest.mark.parametrize(
    "display_name,type",
    [
        ("BoolConfiguration", DataType.Boolean),
        ("StringConfiguration", DataType.String),
        ("DoubleConfiguration", DataType.Double),
        ("Float", DataType.Float),
        ("Double1DArray", DataType.DoubleArray1D),
        ("Int32", DataType.Int32),
        ("Int64", DataType.Int64),
        ("UInt32", DataType.UInt32),
        ("UInt64", DataType.UInt64),
        ("DoubleXYData", DataType.DoubleXYData),
        ("DoubleXYDataArray", DataType.DoubleXYDataArray1D),
        ("Double2DArray", DataType.Double2DArray),
        ("String2DArray", DataType.String2DArray),
    ],
)
def test___measurement_service___add_output__output_added(
    measurement_service: MeasurementService, display_name: str, type: DataType
):
    measurement_service.output(display_name, type)(_fake_measurement_function)
    data_type_info = _datatypeinfo.get_type_info(type)

    assert any(
        param.display_name == display_name
        and param.type == data_type_info.grpc_field_type
        and param.repeated == data_type_info.repeated
        and param.message_type == data_type_info.message_type
        for param in measurement_service._output_parameter_list
    )


def _fake_measurement_function():
    pass


no_annotations: dict[str, str] = {}


@pytest.mark.parametrize(
    "service_config,display_name,version,provided_interfaces,provided_annotations",
    [
        (
            "example.serviceconfig",
            "SampleMeasurement",
            "1.0.1",
            [
                "ni.measurementlink.measurement.v1.MeasurementService",
                "ni.measurementlink.measurement.v2.MeasurementService",
            ],
            {
                "ni/service.description": "Measure inrush current with a shorted load and validate results against configured limits.",
                "ni/service.collection": "CurrentTests.Inrush",
                "ni/service.tags": '["powerup","current"]',
            },
        ),
        (
            "example.v1.serviceconfig",
            "SampleMeasurement",
            "1.0.1",
            ["ni.measurementlink.measurement.v1.MeasurementService"],
            no_annotations,
        ),
        (
            "example.v2.serviceconfig",
            "SampleMeasurement",
            "1.0.3",
            ["ni.measurementlink.measurement.v2.MeasurementService"],
            no_annotations,
        ),
        (
            "example.OnlyCollection.serviceconfig",
            "SampleMeasurement",
            "1.0.4",
            ["ni.measurementlink.measurement.v2.MeasurementService"],
            {"ni/service.collection": "CurrentTests.Inrush"},
        ),
        (
            "example.OnlyTags.serviceconfig",
            "SampleMeasurement",
            "1.0.5",
            ["ni.measurementlink.measurement.v2.MeasurementService"],
            {"ni/service.tags": '["powerup","current","voltage"]'},
        ),
        (
            "example.AllAnnotations.serviceconfig",
            "SampleMeasurement",
            "1.0.6",
            ["ni.measurementlink.measurement.v2.MeasurementService"],
            {
                "ni/service.description": "Testing extra Client info",
                "client/extra.NumberID": "500",
                "client/extra.Parts": '["A25898","A25412"]',
                "client/extra.GroupName": '{"SpeakerType":"true","PhoneType":"false"}',
            },
        ),
        (
            "example.CustomAnnotations.serviceconfig",
            "SampleMeasurement",
            "1.0.7",
            ["ni.measurementlink.measurement.v1.MeasurementService"],
            {
                "description": "An annotated test measurement service.",
                "collection": "Tests.Measurements",
                "tags": '["test","measurement"]',
                "custom": '{"foo":"bar","baz":["qux","quux","quuux"],"snork":{"blarg":"flarp","oogle":'
                + '["foogle","boogle"],"ork":["zork","gork","bork"]}}',
            },
        ),
        (
            "example.localized.serviceconfig",
            "示例测量",
            "1.0.8",
            ["ni.measurementlink.measurement.v2.MeasurementService"],
            no_annotations,
        ),
    ],
)
def test___service_config___create_measurement_service___service_info_matches_service_config(
    test_assets_directory: pathlib.Path,
    service_config: str,
    display_name: str,
    version: str,
    provided_interfaces: list[str],
    provided_annotations: dict[str, str],
):
    measurement_service = MeasurementService(
        service_config_path=test_assets_directory / service_config,
        ui_file_paths=[],
    )

    assert measurement_service.service_info.display_name == display_name
    assert measurement_service.service_info.versions[0] == version
    assert measurement_service.service_info.service_class == "SampleMeasurement_Python"
    assert set(measurement_service.service_info.provided_interfaces) >= set(provided_interfaces)
    assert (
        measurement_service.service_info.description_url
        == "https://www.example.com/SampleMeasurement.html"
    )
    assert measurement_service.service_info.annotations == provided_annotations


def test___service_config___create_measurement_service_with_version___version_differs_from_service_config(
    test_assets_directory: pathlib.Path,
):
    with pytest.raises(RuntimeError) as version_error:
        with pytest.deprecated_call():
            MeasurementService(
                service_config_path=test_assets_directory / "example.serviceconfig",
                version="2.0.1",
            )

    assert "Version mismatch" in str(version_error.value)


def test___service_config___create_measurement_service_with_version___service_config_has_no_version(
    test_assets_directory: pathlib.Path,
):
    with pytest.deprecated_call():
        measurement_service = MeasurementService(
            service_config_path=test_assets_directory / "example.NoVersion.serviceconfig",
            version="2.0.1",
        )

    assert not measurement_service.service_info.versions[0]


@pytest.mark.parametrize(
    "service_config,version",
    [
        ("example.serviceconfig", "1.0.1"),
        ("example.v1.serviceconfig", "1.0.1"),
    ],
)
def test___service_config___create_measurement_service_with_version___version_is_used(
    test_assets_directory: pathlib.Path,
    service_config: str,
    version: str,
):
    with pytest.deprecated_call():
        service = MeasurementService(
            service_config_path=test_assets_directory / service_config,
            version=version,
        )

    assert service.service_info.versions[0] == version


@pytest.mark.parametrize(
    "display_name,type,default_value,enum_type",
    [
        ("EnumConfiguration", DataType.Enum, Color.GREEN, None),
        ("EnumConfiguration", DataType.Enum, ColorWithoutZeroValue.GREEN, ColorWithoutZeroValue),
    ],
)
def test___measurement_service___add_configuration_with_invalid_enum_type___raises_type_error(
    measurement_service: MeasurementService,
    display_name: str,
    type: DataType,
    default_value: object,
    enum_type: type[Enum],
):
    with pytest.raises(ValueError):
        measurement_service.configuration(display_name, type, default_value)(
            _fake_measurement_function
        )


def test___measurement_service___host_service_with_grpc_service_not_started___raises_error(
    measurement_service: MeasurementService,
    mocker: MockerFixture,
):
    measurement_service.register_measurement(_fake_measurement_function)
    mocker.patch(
        "ni_measurement_plugin_sdk_service._internal.service_manager.GrpcService.start",
        side_effect=Exception,
    )

    with pytest.raises(Exception):
        measurement_service.host_service()


@pytest.fixture
def measurement_service(test_assets_directory: pathlib.Path) -> MeasurementService:
    """Create a MeasurementService."""
    return MeasurementService(service_config_path=test_assets_directory / "example.serviceconfig")
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/unit/test_session_management.py sha256=ba8174a75c65369255808ab29104e7370542623b09839ef36d42ff4901511472 bytes=41640 -->
## FILE: packages/service/tests/unit/test_session_management.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/unit/test_session_management.py`
- sha256: `ba8174a75c65369255808ab29104e7370542623b09839ef36d42ff4901511472`
- bytes: 41640

````python
from __future__ import annotations

from typing import cast
from unittest.mock import Mock

import grpc
import pytest
import session_pb2
from ni.measurementlink.discovery.v1.client import DiscoveryClient
from ni.measurementlink.sessionmanagement.v1 import (
    session_management_service_pb2,
)
from ni.measurementlink.sessionmanagement.v1.client import (
    MultiplexerSessionInformation,
    MultiSessionReservation,
    PinMapContext,
    SessionInformation,
    SessionManagementClient,
    SingleSessionReservation,
    TypedSessionInformation,
)
from ni.measurementlink.sessionmanagement.v1.session_management_service_pb2_grpc import (
    SessionManagementServiceStub,
)
from ni_grpc_extensions.channelpool import GrpcChannelPool
from pytest_mock import MockerFixture


def test___all_optional_args___reserve_session___sends_request_with_args(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    _ = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names=["Pin1", "Pin2"],
        instrument_type_id="MyInstrumentType",
        timeout=123.456,
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.pin_map_context.pin_map_id == "MyPinMap"
    assert request.pin_map_context.sites == [0, 1]
    assert request.pin_or_relay_names == ["Pin1", "Pin2"]
    assert request.instrument_type_id == "MyInstrumentType"
    assert request.timeout_in_milliseconds == 123456


def test___no_optional_args___reserve_session___sends_request_with_defaults(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    _ = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0, 1]),
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.pin_or_relay_names == []
    assert request.instrument_type_id == ""
    assert request.timeout_in_milliseconds == 0.0


def test___explicit_none___reserve_session___sends_request_with_defaults(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    _ = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names=None,
        instrument_type_id=None,
        timeout=None,
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.pin_or_relay_names == []
    assert request.instrument_type_id == ""
    assert request.timeout_in_milliseconds == 0.0


def test___single_pin___reserve_session___sends_request_with_single_pin(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    _ = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names="Pin1",
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.pin_or_relay_names == ["Pin1"]


@pytest.mark.parametrize("timeout", [-1, -1.0])
def test___infinite_timeout___reserve_session___sends_request_with_infinite_timeout(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    timeout: float,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    _ = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0, 1]), timeout=timeout
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.timeout_in_milliseconds == -1


def test___negative_timeout___reserve_session___warns_and_sends_request_with_infinite_timeout(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    with pytest.warns(RuntimeWarning):
        _ = session_management_client.reserve_session(PinMapContext("MyPinMap", [0, 1]), timeout=-2)

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.timeout_in_milliseconds == -1


def test___single_session___reserve_session___returns_single_session_info(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    reservation = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names=["Pin1", "Pin2"],
        instrument_type_id="MyInstrumentType",
        timeout=123.456,
    )

    assert isinstance(reservation, SingleSessionReservation)
    assert reservation.session_info.session_name == "MySession0"


def test___no_sessions___reserve_session___raises_no_sessions_value_error(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse()
    )

    with pytest.raises(ValueError, match="No sessions reserved."):
        _ = session_management_client.reserve_session(
            PinMapContext("MyPinMap", [0, 1]),
            pin_or_relay_names=["Pin1", "Pin2"],
            instrument_type_id="MyInstrumentType",
            timeout=123.456,
        )


def test___too_many_sessions___reserve_session___raises_too_many_sessions_value_error(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(2)
        )
    )

    with pytest.raises(ValueError, match="Too many sessions reserved."):
        _ = session_management_client.reserve_session(
            PinMapContext("MyPinMap", [0, 1]),
            pin_or_relay_names=["Pin1", "Pin2"],
            instrument_type_id="MyInstrumentType",
            timeout=123.456,
        )


def test___all_optional_args___reserve_session___args_passed_to_reservation(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    reservation = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [1, 0, 3, 2]),
        pin_or_relay_names=["Pin3", "Pin1", "Pin4", "Pin2"],
        instrument_type_id="MyInstrumentType",
        timeout=123.456,
    )

    assert list(reservation._reserved_pin_or_relay_names) == ["Pin3", "Pin1", "Pin4", "Pin2"]
    assert list(reservation._reserved_sites) == [1, 0, 3, 2]


def test___all_optional_args___reserve_sessions___sends_request_with_args(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse()
    )

    _ = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names=["Pin1", "Pin2"],
        instrument_type_id="MyInstrumentType",
        timeout=123.456,
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.pin_map_context.pin_map_id == "MyPinMap"
    assert request.pin_map_context.sites == [0, 1]
    assert request.pin_or_relay_names == ["Pin1", "Pin2"]
    assert request.instrument_type_id == "MyInstrumentType"
    assert request.timeout_in_milliseconds == 123456


def test___no_optional_args___reserve_sessions___sends_request_with_defaults(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse()
    )

    _ = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0, 1]),
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.pin_or_relay_names == []
    assert request.instrument_type_id == ""
    assert request.timeout_in_milliseconds == 0.0


def test___explicit_none___reserve_sessions___sends_request_with_defaults(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse()
    )

    _ = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names=None,
        instrument_type_id=None,
        timeout=None,
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.pin_or_relay_names == []
    assert request.instrument_type_id == ""
    assert request.timeout_in_milliseconds == 0.0


def test___single_pin___reserve_sessions___sends_request_with_single_pin(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse()
    )

    _ = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names="Pin1",
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.pin_or_relay_names == ["Pin1"]


@pytest.mark.parametrize("timeout", [-1, -1.0])
def test___infinite_timeout___reserve_sessions___sends_request_with_infinite_timeout(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    timeout: float,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    _ = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0, 1]), timeout=timeout
    )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.timeout_in_milliseconds == -1


def test___negative_timeout___reserve_sessions___warns_and_sends_request_with_infinite_timeout(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1)
        )
    )

    with pytest.warns(RuntimeWarning):
        _ = session_management_client.reserve_sessions(
            PinMapContext("MyPinMap", [0, 1]), timeout=-2
        )

    session_management_stub.ReserveSessions.assert_called_once()
    (request,) = session_management_stub.ReserveSessions.call_args.args
    assert request.timeout_in_milliseconds == -1


@pytest.mark.parametrize("session_count", [0, 1, 2])
def test___varying_session_count___reserve_sessions___returns_multiple_session_infos(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    session_count: int,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(session_count)
        )
    )

    reservation = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names=["Pin1", "Pin2"],
        instrument_type_id="MyInstrumentType",
        timeout=123.456,
    )

    assert isinstance(reservation, MultiSessionReservation)
    assert len(reservation.session_info) == session_count
    assert [s.session_name for s in reservation.session_info] == [
        f"MySession{i}" for i in range(session_count)
    ]


def test___all_optional_args___reserve_sessions___args_passed_to_reservation(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse()
    )

    reservation = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [1, 0, 3, 2]),
        pin_or_relay_names=["Pin3", "Pin1", "Pin4", "Pin2"],
        instrument_type_id="MyInstrumentType",
        timeout=123.456,
    )

    assert list(reservation._reserved_pin_or_relay_names) == ["Pin3", "Pin1", "Pin4", "Pin2"]
    assert list(reservation._reserved_sites) == [1, 0, 3, 2]


@pytest.mark.parametrize("session_count", [0, 1, 2])
def test___varying_session_count___unreserve___sends_request(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    session_count: int,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, _create_grpc_session_infos(session_count)
    )
    session_management_stub.UnreserveSessions.return_value = (
        session_management_service_pb2.UnreserveSessionsResponse()
    )

    reservation.unreserve()

    session_management_stub.UnreserveSessions.assert_called_once()
    (request,) = session_management_stub.UnreserveSessions.call_args.args
    assert len(request.sessions) == session_count
    assert [s.session.name for s in request.sessions] == [
        f"MySession{i}" for i in range(session_count)
    ]


@pytest.mark.parametrize("session_count", [0, 1, 2])
def test___varying_session_count___exit_reservation___sends_request(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    session_count: int,
) -> None:
    reservation = MultiSessionReservation(
        session_management_client, _create_grpc_session_infos(session_count)
    )
    session_management_stub.UnreserveSessions.return_value = (
        session_management_service_pb2.UnreserveSessionsResponse()
    )

    with reservation:
        pass

    session_management_stub.UnreserveSessions.assert_called_once()
    (request,) = session_management_stub.UnreserveSessions.call_args.args
    assert len(request.sessions) == session_count
    assert [s.session.name for s in request.sessions] == [
        f"MySession{i}" for i in range(session_count)
    ]


@pytest.mark.parametrize("session_count", [0, 1, 2])
def test___varying_session_count___register_sessions___sends_request(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    session_count: int,
) -> None:
    session_management_stub.RegisterSessions.return_value = (
        session_management_service_pb2.RegisterSessionsResponse()
    )

    session_management_client.register_sessions(_create_session_infos(session_count))

    session_management_stub.RegisterSessions.assert_called_once()
    (request,) = session_management_stub.RegisterSessions.call_args.args
    assert len(request.sessions) == session_count
    assert [s.session.name for s in request.sessions] == [
        f"MySession{i}" for i in range(session_count)
    ]


@pytest.mark.parametrize("session_count", [0, 1, 2])
def test___varying_session_count___unregister_sessions___sends_request(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    session_count: int,
) -> None:
    session_management_stub.UnregisterSessions.return_value = (
        session_management_service_pb2.UnregisterSessionsResponse()
    )

    session_management_client.unregister_sessions(_create_session_infos(session_count))

    session_management_stub.UnregisterSessions.assert_called_once()
    (request,) = session_management_stub.UnregisterSessions.call_args.args
    assert len(request.sessions) == session_count
    assert [s.session.name for s in request.sessions] == [
        f"MySession{i}" for i in range(session_count)
    ]


def test___all_optional_args___reserve_all_registered_sessions___sends_request_with_args(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveAllRegisteredSessions.return_value = (
        session_management_service_pb2.ReserveAllRegisteredSessionsResponse()
    )

    _ = session_management_client.reserve_all_registered_sessions(
        instrument_type_id="MyInstrumentType", timeout=123.456
    )

    session_management_stub.ReserveAllRegisteredSessions.assert_called_once()
    (request,) = session_management_stub.ReserveAllRegisteredSessions.call_args.args
    assert request.instrument_type_id == "MyInstrumentType"
    assert request.timeout_in_milliseconds == 123456


def test___no_optional_args___reserve_all_registered_sessions___sends_request_with_defaults(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveAllRegisteredSessions.return_value = (
        session_management_service_pb2.ReserveAllRegisteredSessionsResponse()
    )

    _ = session_management_client.reserve_all_registered_sessions()

    session_management_stub.ReserveAllRegisteredSessions.assert_called_once()
    (request,) = session_management_stub.ReserveAllRegisteredSessions.call_args.args
    assert request.instrument_type_id == ""
    assert request.timeout_in_milliseconds == 10000


def test___explicit_none___reserve_all_registered_sessions___sends_request_with_defaults(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveAllRegisteredSessions.return_value = (
        session_management_service_pb2.ReserveAllRegisteredSessionsResponse()
    )

    _ = session_management_client.reserve_all_registered_sessions(
        instrument_type_id=None, timeout=None
    )

    session_management_stub.ReserveAllRegisteredSessions.assert_called_once()
    (request,) = session_management_stub.ReserveAllRegisteredSessions.call_args.args
    assert request.instrument_type_id == ""
    assert request.timeout_in_milliseconds == 0


@pytest.mark.parametrize("timeout", [-1, -1.0])
def test___infinite_timeout___reserve_all_registered_sessions___sends_request_with_infinite_timeout(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    timeout: float,
) -> None:
    session_management_stub.ReserveAllRegisteredSessions.return_value = (
        session_management_service_pb2.ReserveAllRegisteredSessionsResponse()
    )

    _ = session_management_client.reserve_all_registered_sessions(timeout=timeout)

    session_management_stub.ReserveAllRegisteredSessions.assert_called_once()
    (request,) = session_management_stub.ReserveAllRegisteredSessions.call_args.args
    assert request.timeout_in_milliseconds == -1


def test___negative_timeout___reserve_all_registered_sessions___warns_and_sends_request_with_infinite_timeout(
    session_management_client: SessionManagementClient, session_management_stub: Mock
) -> None:
    session_management_stub.ReserveAllRegisteredSessions.return_value = (
        session_management_service_pb2.ReserveAllRegisteredSessionsResponse()
    )

    with pytest.warns(RuntimeWarning):
        _ = session_management_client.reserve_all_registered_sessions(timeout=-2)

    session_management_stub.ReserveAllRegisteredSessions.assert_called_once()
    (request,) = session_management_stub.ReserveAllRegisteredSessions.call_args.args
    assert request.timeout_in_milliseconds == -1


@pytest.mark.parametrize("session_count", [0, 1, 2])
def test___varying_session_count___reserve_all_registered_sessions___returns_session_infos(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    session_count: int,
) -> None:
    session_management_stub.ReserveAllRegisteredSessions.return_value = (
        session_management_service_pb2.ReserveAllRegisteredSessionsResponse(
            sessions=_create_grpc_session_infos(session_count)
        )
    )

    reservation = session_management_client.reserve_all_registered_sessions(
        instrument_type_id="MyInstrumentType", timeout=123.456
    )

    assert len(reservation.session_info) == session_count
    assert [s.session_name for s in reservation.session_info] == [
        f"MySession{i}" for i in range(session_count)
    ]


def test___use_reservation_type___reports_deprecated_warning_and_aliases_to_multi_session_reservation(
    session_management_client: SessionManagementClient,
) -> None:
    with pytest.deprecated_call():
        from ni.measurementlink.sessionmanagement.v1.client import Reservation

        reservation = Reservation(session_management_client, _create_grpc_session_infos(3))

    assert isinstance(reservation, MultiSessionReservation)


def test___session_information___type_check___implements_typed_session_information_object() -> None:
    # This is a type-checking test. It does nothing at run time.
    def f(typed_session_info: TypedSessionInformation[object]) -> None:
        pass

    f(SessionInformation("MySession", "Dev1", "0", "niDCPower", False, []))


@pytest.mark.parametrize("multiplexer_session_count", [1, 2, 3])
def test___single_session_with_varying_multiplexer_count___reserve_session___returns_session_info_and_multiplexer_infos(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    multiplexer_session_count: int,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1),
            multiplexer_sessions=_create_grpc_multiplexer_session_infos(multiplexer_session_count),
        )
    )

    reservation = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0]),
        pin_or_relay_names=["Pin1", "Pin2", "Pin3"],
    )

    assert isinstance(reservation, SingleSessionReservation)
    assert reservation.session_info.session_name == "MySession0"
    assert [info.session_name for info in reservation.multiplexer_session_info] == [
        f"MyMultiplexer{i}" for i in range(multiplexer_session_count)
    ]
    assert [info.multiplexer_type_id for info in reservation.multiplexer_session_info] == [
        f"MyMultiplexerType{i}" for i in range(multiplexer_session_count)
    ]


@pytest.mark.parametrize("multiplexer_session_count", [1, 2, 3])
def test___multiple_sessions_with_varying_multiplexer_count___reserve_sessions___returns_session_infos_and_multiplexer_infos(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    multiplexer_session_count: int,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(2),
            multiplexer_sessions=_create_grpc_multiplexer_session_infos(multiplexer_session_count),
        )
    )

    reservation = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0]),
        pin_or_relay_names=["Pin1", "Pin2", "Pin3"],
    )

    assert isinstance(reservation, MultiSessionReservation)
    assert [info.session_name for info in reservation.session_info] == [
        f"MySession{i}" for i in range(2)
    ]
    assert [info.session_name for info in reservation.multiplexer_session_info] == [
        f"MyMultiplexer{i}" for i in range(multiplexer_session_count)
    ]
    assert [info.multiplexer_type_id for info in reservation.multiplexer_session_info] == [
        f"MyMultiplexerType{i}" for i in range(multiplexer_session_count)
    ]


@pytest.mark.parametrize("multiplexer_session_count", [1, 2])
def test___single_session_with_shared_pins_and_varying_multiplexer_count___reserve_session___returns_session_and_multiplexer_infos_for_all_sites(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    multiplexer_session_count: int,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1),
            multiplexer_sessions=_create_grpc_multiplexer_session_infos(multiplexer_session_count),
        )
    )

    reservation = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names=["Pin1"],
    )

    assert isinstance(reservation, SingleSessionReservation)
    assert list(reservation._reserved_sites) == [0, 1]
    assert [info.session_name for info in reservation.multiplexer_session_info] == [
        f"MyMultiplexer{i}" for i in range(multiplexer_session_count)
    ]
    assert [info.multiplexer_type_id for info in reservation.multiplexer_session_info] == [
        f"MyMultiplexerType{i}" for i in range(multiplexer_session_count)
    ]


@pytest.mark.parametrize("multiplexer_session_count", [1, 2])
def test___multiple_sessions_with_shared_pins_and_varying_multiplexer_count___reserve_sessions___returns_session_and_multiplexer_infos_for_all_sites(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    multiplexer_session_count: int,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(2),
            multiplexer_sessions=_create_grpc_multiplexer_session_infos(multiplexer_session_count),
        )
    )

    reservation = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0, 1]),
        pin_or_relay_names=["Pin1"],
    )

    assert isinstance(reservation, MultiSessionReservation)
    assert list(reservation._reserved_sites) == [0, 1]
    assert [info.session_name for info in reservation.multiplexer_session_info] == [
        f"MyMultiplexer{i}" for i in range(multiplexer_session_count)
    ]
    assert [info.multiplexer_type_id for info in reservation.multiplexer_session_info] == [
        f"MyMultiplexerType{i}" for i in range(multiplexer_session_count)
    ]


def test___single_session_without_multiplexer___get_multiplexer_session_info___returns_empty_list(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(1),
            multiplexer_sessions=_create_grpc_multiplexer_session_infos(0),
        )
    )
    reservation = session_management_client.reserve_session(
        PinMapContext("MyPinMap", [0]),
        pin_or_relay_names=["Pin1"],
    )

    multiplexer_session_info = reservation.multiplexer_session_info

    assert isinstance(reservation, SingleSessionReservation)
    assert len(multiplexer_session_info) == 0


def test___multiple_sessions_without_multiplexer___get_multiplexer_session_info___returns_empty_list(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
) -> None:
    session_management_stub.ReserveSessions.return_value = (
        session_management_service_pb2.ReserveSessionsResponse(
            sessions=_create_grpc_session_infos(2),
            multiplexer_sessions=_create_grpc_multiplexer_session_infos(0),
        )
    )
    reservation = session_management_client.reserve_sessions(
        PinMapContext("MyPinMap", [0]),
        pin_or_relay_names=["Pin1", "Pin2"],
    )

    multiplexer_session_info = reservation.multiplexer_session_info

    assert isinstance(reservation, MultiSessionReservation)
    assert len(multiplexer_session_info) == 0


@pytest.mark.parametrize("multiplexer_session_count", [0, 1, 2])
def test___varying_multiplexer_session_count___register_multiplexer_sessions___sends_request(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    multiplexer_session_count: int,
) -> None:
    session_management_stub.RegisterMultiplexerSessions.return_value = (
        session_management_service_pb2.RegisterMultiplexerSessionsResponse()
    )

    session_management_client.register_multiplexer_sessions(
        _create_multiplexer_session_infos(multiplexer_session_count)
    )

    session_management_stub.RegisterMultiplexerSessions.assert_called_once()
    (request,) = session_management_stub.RegisterMultiplexerSessions.call_args.args
    assert len(request.multiplexer_sessions) == multiplexer_session_count
    assert [s.session.name for s in request.multiplexer_sessions] == [
        f"MyMultiplexer{i}" for i in range(multiplexer_session_count)
    ]


@pytest.mark.parametrize("multiplexer_session_count", [0, 1, 2])
def test___varying_multiplexer_session_count___unregister_multiplexer_sessions___sends_request(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    multiplexer_session_count: int,
) -> None:
    session_management_stub.UnregisterMultiplexerSessions.return_value = (
        session_management_service_pb2.UnregisterMultiplexerSessionsResponse()
    )

    session_management_client.unregister_multiplexer_sessions(
        _create_multiplexer_session_infos(multiplexer_session_count)
    )

    session_management_stub.UnregisterMultiplexerSessions.assert_called_once()
    (request,) = session_management_stub.UnregisterMultiplexerSessions.call_args.args
    assert len(request.multiplexer_sessions) == multiplexer_session_count
    assert [s.session.name for s in request.multiplexer_sessions] == [
        f"MyMultiplexer{i}" for i in range(multiplexer_session_count)
    ]


def test___optional_arg___get_multiplexer_sessions___sends_request_with_args(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
) -> None:
    session_management_stub.GetMultiplexerSessions.return_value = (
        session_management_service_pb2.GetMultiplexerSessionsResponse()
    )

    session_management_client.get_multiplexer_sessions(
        PinMapContext("MyPinMap", [0, 1]), "multiplexer_type_id"
    )

    session_management_stub.GetMultiplexerSessions.assert_called_once()
    (request,) = session_management_stub.GetMultiplexerSessions.call_args.args
    assert request.pin_map_context.pin_map_id == "MyPinMap"
    assert request.pin_map_context.sites == [0, 1]
    assert request.multiplexer_type_id == "multiplexer_type_id"


def test___no_optional_args___get_multiplexer_sessions___sends_request_with_default(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
) -> None:
    session_management_stub.GetMultiplexerSessions.return_value = (
        session_management_service_pb2.GetMultiplexerSessionsResponse()
    )

    session_management_client.get_multiplexer_sessions(PinMapContext("MyPinMap", [0, 1]))

    session_management_stub.GetMultiplexerSessions.assert_called_once()
    (request,) = session_management_stub.GetMultiplexerSessions.call_args.args
    assert request.pin_map_context.pin_map_id == "MyPinMap"
    assert request.pin_map_context.sites == [0, 1]
    assert request.multiplexer_type_id == ""


def test___explicit_none___get_multiplexer_sessions___sends_request_with_default(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
) -> None:
    session_management_stub.GetMultiplexerSessions.return_value = (
        session_management_service_pb2.GetMultiplexerSessionsResponse()
    )

    session_management_client.get_multiplexer_sessions(PinMapContext("MyPinMap", [0, 1]), None)

    session_management_stub.GetMultiplexerSessions.assert_called_once()
    (request,) = session_management_stub.GetMultiplexerSessions.call_args.args
    assert request.pin_map_context.pin_map_id == "MyPinMap"
    assert request.pin_map_context.sites == [0, 1]
    assert request.multiplexer_type_id == ""


@pytest.mark.parametrize("multiplexer_session_count", [0, 1, 2])
def test___varying_multiplexers___get_multiplexer_sessions___returns_multiplexer_session_infos(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    multiplexer_session_count: int,
) -> None:
    session_management_stub.GetMultiplexerSessions.return_value = (
        session_management_service_pb2.GetMultiplexerSessionsResponse(
            multiplexer_sessions=_create_grpc_multiplexer_session_infos(multiplexer_session_count)
        )
    )

    result = session_management_client.get_multiplexer_sessions(PinMapContext("MyPinMap", [0, 1]))

    session_management_stub.GetMultiplexerSessions.assert_called_once()
    assert len(result.multiplexer_session_info) == multiplexer_session_count
    assert [info.session_name for info in result.multiplexer_session_info] == [
        f"MyMultiplexer{i}" for i in range(multiplexer_session_count)
    ]


def test___optional_arg___get_all_registered_multiplexer_sessions___sends_request_with_args(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
) -> None:
    session_management_stub.GetAllRegisteredMultiplexerSessions.return_value = (
        session_management_service_pb2.GetAllRegisteredMultiplexerSessionsResponse()
    )

    session_management_client.get_all_registered_multiplexer_sessions("multiplexer_type_id")

    session_management_stub.GetAllRegisteredMultiplexerSessions.assert_called_once()
    (request,) = session_management_stub.GetAllRegisteredMultiplexerSessions.call_args.args
    assert request.multiplexer_type_id == "multiplexer_type_id"


def test___no_optional_args___get_all_registered_multiplexer_sessions___sends_request_with_default(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
) -> None:
    session_management_stub.GetAllRegisteredMultiplexerSessions.return_value = (
        session_management_service_pb2.GetAllRegisteredMultiplexerSessionsResponse()
    )

    session_management_client.get_all_registered_multiplexer_sessions()

    session_management_stub.GetAllRegisteredMultiplexerSessions.assert_called_once()
    (request,) = session_management_stub.GetAllRegisteredMultiplexerSessions.call_args.args
    assert request.multiplexer_type_id == ""


def test___explicit_none___get_all_registered_multiplexer_sessions___sends_request_with_default(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
) -> None:
    session_management_stub.GetAllRegisteredMultiplexerSessions.return_value = (
        session_management_service_pb2.GetAllRegisteredMultiplexerSessionsResponse()
    )

    session_management_client.get_all_registered_multiplexer_sessions(None)

    session_management_stub.GetAllRegisteredMultiplexerSessions.assert_called_once()
    (request,) = session_management_stub.GetAllRegisteredMultiplexerSessions.call_args.args
    assert request.multiplexer_type_id == ""


@pytest.mark.parametrize("multiplexer_session_count", [0, 1, 2])
def test___varying_registered_multiplexers___get_all_registered_multiplexer_sessions___returns_multiplexer_session_infos(
    session_management_client: SessionManagementClient,
    session_management_stub: Mock,
    multiplexer_session_count: int,
) -> None:
    session_management_stub.GetAllRegisteredMultiplexerSessions.return_value = (
        session_management_service_pb2.GetAllRegisteredMultiplexerSessionsResponse(
            multiplexer_sessions=_create_grpc_multiplexer_session_infos(multiplexer_session_count)
        )
    )

    result = session_management_client.get_all_registered_multiplexer_sessions()

    session_management_stub.GetAllRegisteredMultiplexerSessions.assert_called_once()
    assert len(result.multiplexer_session_info) == multiplexer_session_count
    assert [info.session_name for info in result.multiplexer_session_info] == [
        f"MyMultiplexer{i}" for i in range(multiplexer_session_count)
    ]


def _create_session_infos(session_count: int) -> list[SessionInformation]:
    return [
        SessionInformation(f"MySession{i}", "", "", "", False, []) for i in range(session_count)
    ]


def _create_multiplexer_session_infos(
    multiplexer_session_count: int,
) -> list[MultiplexerSessionInformation]:
    return [
        MultiplexerSessionInformation(f"MyMultiplexer{i}", "", "", False)
        for i in range(multiplexer_session_count)
    ]


def _create_grpc_session_infos(
    session_count: int,
) -> list[session_management_service_pb2.SessionInformation]:
    return [
        session_management_service_pb2.SessionInformation(
            session=session_pb2.Session(name=f"MySession{i}")
        )
        for i in range(session_count)
    ]


def _create_grpc_multiplexer_session_infos(
    session_count: int,
) -> list[session_management_service_pb2.MultiplexerSessionInformation]:
    return [
        session_management_service_pb2.MultiplexerSessionInformation(
            session=session_pb2.Session(name=f"MyMultiplexer{i}"),
            multiplexer_type_id=f"MyMultiplexerType{i}",
        )
        for i in range(session_count)
    ]


@pytest.fixture
def session_management_client(
    discovery_client: Mock,
    grpc_channel_pool: Mock,
    mocker: MockerFixture,
    session_management_stub: Mock,
) -> SessionManagementClient:
    """Create a Client with a mock SessionManagementServiceStub."""
    mocker.patch(
        "ni.measurementlink.sessionmanagement.v1.client.SessionManagementClient._get_stub",
        return_value=session_management_stub,
    )
    client = SessionManagementClient(
        discovery_client=cast(DiscoveryClient, discovery_client),
        grpc_channel_pool=cast(GrpcChannelPool, grpc_channel_pool),
    )
    return client


@pytest.fixture
def session_management_stub(mocker: MockerFixture) -> Mock:
    """Create a mock SessionManagementServiceStub."""
    stub = mocker.create_autospec(SessionManagementServiceStub)
    stub.ReserveSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    stub.UnreserveSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    stub.RegisterSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    stub.UnregisterSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    stub.ReserveAllRegisteredSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    stub.RegisterMultiplexerSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    stub.UnregisterMultiplexerSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    stub.GetMultiplexerSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    stub.GetAllRegisteredMultiplexerSessions = mocker.create_autospec(grpc.UnaryUnaryMultiCallable)
    return stub
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/__init__.py sha256=f542971f42f1281c2dfd4f94e34a300368c302ab199414d24bd18e248fd813f6 bytes=32 -->
## FILE: packages/service/tests/utilities/__init__.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/__init__.py`
- sha256: `f542971f42f1281c2dfd4f94e34a300368c302ab199414d24bd18e248fd813f6`
- bytes: 32

````python
"""Contains test utilities."""
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/_array_utils.py sha256=4c5e853ec4118b87bc74b4325e900d92055e1c0922af72a3560f90748e08ddd5 bytes=2738 -->
## FILE: packages/service/tests/utilities/_array_utils.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/_array_utils.py`
- sha256: `4c5e853ec4118b87bc74b4325e900d92055e1c0922af72a3560f90748e08ddd5`
- bytes: 2738

````python
"""2DArray Conversion Utilities."""

from __future__ import annotations

from typing import TYPE_CHECKING

from ni.protobuf.types import array_pb2

if TYPE_CHECKING:
    import numpy as np
    import numpy.typing as npt


def double2darray_to_ndarray(double2darray: array_pb2.Double2DArray) -> npt.NDArray[np.float64]:
    """Convert Double2DArray to numpy NDArray."""
    import numpy as np

    return np.array(double2darray.data, dtype=np.float64).reshape(
        double2darray.rows, double2darray.columns
    )


def ndarray_to_double2darray(ndarray: npt.NDArray[np.float64]) -> array_pb2.Double2DArray:
    """Convert numpy NDArray to Double2DArray."""
    return array_pb2.Double2DArray(
        data=ndarray.flatten().tolist(), rows=ndarray.shape[0], columns=ndarray.shape[1]
    )


def list_to_double2darray(data: list[list[float]]) -> array_pb2.Double2DArray:
    """Convert list of lists to Double2DArray."""
    rows = len(data)
    columns = len(data[0]) if rows > 0 else 0
    flattened_data = [item for sublist in data for item in sublist]
    return array_pb2.Double2DArray(data=flattened_data, rows=rows, columns=columns)


def double2darray_to_list(double2darray: array_pb2.Double2DArray) -> list[list[float]]:
    """Convert Double2DArray to list of lists."""
    data = double2darray.data
    rows = double2darray.rows
    columns = double2darray.columns
    return [data[i * columns : (i + 1) * columns] for i in range(rows)]


def string2darray_to_ndarray(string2darray: array_pb2.String2DArray) -> npt.NDArray[np.str_]:
    """Convert String2DArray to numpy NDArray."""
    import numpy as np

    return np.array(string2darray.data, dtype=np.str_).reshape(
        string2darray.rows, string2darray.columns
    )


def ndarray_to_string2darray(ndarray: npt.NDArray[np.str_]) -> array_pb2.String2DArray:
    """Convert numpy NDArray to String2DArray."""
    return array_pb2.String2DArray(
        data=ndarray.flatten().tolist(), rows=ndarray.shape[0], columns=ndarray.shape[1]
    )


def string2darray_to_list(string2darray: array_pb2.String2DArray) -> list[list[str]]:
    """Convert String2DArray to list of lists."""
    data = string2darray.data
    rows = string2darray.rows
    columns = string2darray.columns
    return [data[i * columns : (i + 1) * columns] for i in range(rows)]


def list_to_string2darray(data: list[list[str]]) -> array_pb2.String2DArray:
    """Convert list of lists to String2DArray."""
    rows = len(data)
    columns = len(data[0]) if rows > 0 else 0
    flattened_data = [item for sublist in data for item in sublist]
    return array_pb2.String2DArray(data=flattened_data, rows=rows, columns=columns)
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/connection_subset.py sha256=82d443717d591ef58d8df3fc4a42bd062e6c969743b1012eb24caec55bc567ed bytes=1465 -->
## FILE: packages/service/tests/utilities/connection_subset.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/connection_subset.py`
- sha256: `82d443717d591ef58d8df3fc4a42bd062e6c969743b1012eb24caec55bc567ed`
- bytes: 1465

````python
"""Utility to create and construct connection subset."""

from __future__ import annotations

from typing import NamedTuple, TypeVar

from ni.measurementlink.sessionmanagement.v1.client import (
    Connection,
    TypedConnection,
    TypedConnectionWithMultiplexer,
)

_T = TypeVar("_T")
_TMultiplexer = TypeVar("_TMultiplexer")


class ConnectionSubset(NamedTuple):
    """An object that holds a subset of connection data."""

    pin_or_relay_name: str
    site: int
    resource_name: str
    channel_name: str

    multiplexer_resource_name: str = ""
    multiplexer_route: str = ""


def get_connection_subset(connection: Connection | TypedConnection[_T]) -> ConnectionSubset:
    """Constructs and returns a ConnectionSubset object."""
    return ConnectionSubset(
        connection.pin_or_relay_name,
        connection.site,
        connection.session_info.resource_name,
        connection.channel_name,
    )


def get_connection_subset_with_multiplexer(
    connection: Connection | TypedConnectionWithMultiplexer[_T, _TMultiplexer],
) -> ConnectionSubset:
    """Constructs and returns a ConnectionSubset object with multiplexer data."""
    return ConnectionSubset(
        connection.pin_or_relay_name,
        connection.site,
        connection.session_info.resource_name,
        connection.channel_name,
        connection.multiplexer_resource_name,
        connection.multiplexer_route,
    )
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/discovery_service_process.py sha256=e0a3fcb5518025d0c8a0b0c79b25f3d702b91a17f0fc3c7664b2c64d200b9db3 bytes=1594 -->
## FILE: packages/service/tests/utilities/discovery_service_process.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/discovery_service_process.py`
- sha256: `e0a3fcb5518025d0c8a0b0c79b25f3d702b91a17f0fc3c7664b2c64d200b9db3`
- bytes: 1594

````python
"""Class to create and terminate Discovery Service instance."""

from __future__ import annotations

from types import TracebackType

from ni.measurementlink.discovery.v1.client._support import (
    _get_discovery_service_location,
    _get_key_file_path,
    _service_already_running,
    _start_service,
)
from typing_extensions import Self


class DiscoveryServiceProcess:
    """Maintains the processes involved in creating and terminating discovery service."""

    def __init__(self) -> None:
        """Creates a DiscoveryServiceProcess instance."""
        try:
            self._proc = None
            key_file_path = _get_key_file_path()
            if _service_already_running(key_file_path):
                return
            self._proc = _start_service(_get_discovery_service_location(), key_file_path)
        except Exception:
            self._close_discovery_service()
            raise

    def __enter__(self: Self) -> Self:
        """Returns the DiscoveryServiceProcess instance."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        """Closes the DiscoveryServiceProcess instance."""
        self._close_discovery_service()

    def _close_discovery_service(self) -> None:
        if self._proc is not None:
            self._proc.kill()
            # Use communicate() to close the stdout pipe and wait for the server process to exit.
            self._proc.communicate()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/fake_discovery_service.py sha256=840e5aebb5814d0df7dae47619944c037da2e364c23cd5135d11dfa755cb8f42 bytes=1550 -->
## FILE: packages/service/tests/utilities/fake_discovery_service.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/fake_discovery_service.py`
- sha256: `840e5aebb5814d0df7dae47619944c037da2e364c23cd5135d11dfa755cb8f42`
- bytes: 1550

````python
"""Contains Test Doubles related to Discovery service."""

import uuid


class FakeRegistrationResponse:
    """Fake Registration Response."""

    registration_id: str


class FakeDiscoveryServiceStub:
    """Fake Registry Service Stub."""

    def RegisterService(self, request):  # noqa: N802 - function name should be lowercase
        """Fake gRPC registration call to discovery service."""
        self.request = request
        response = FakeRegistrationResponse()
        response.registration_id = str(uuid.uuid4())
        self.registration_done = True
        return response

    def UnregisterService(self, request):  # noqa: N802 - function name should be lowercase
        """Fake gRPC un-registration call to discovery service."""
        pass


class FakeDiscoveryServiceStubError(FakeDiscoveryServiceStub):
    """Fake Registry Service Stub that throws error to mimic unavailability of discovery service."""

    def RegisterService(self, request):  # noqa: N802 - function name should be lowercase
        """Fake gRPC registration call to discovery service."""
        raise FakeDiscoveryServiceError("TestException")

    def UnregisterService(self, request):  # noqa: N802 - function name should be lowercase
        """Fake gRPC un-registration call to discovery service."""
        raise FakeDiscoveryServiceError("TestException")


class FakeDiscoveryServiceError(Exception):
    """Fake discovery service error to mimic the exceptions thrown from  discovery service."""

    pass
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/fake_driver.py sha256=f2a419f4d419200dfea118ac4853b27b17f1f063795345a1bdd141114405b3d4 bytes=4821 -->
## FILE: packages/service/tests/utilities/fake_driver.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/fake_driver.py`
- sha256: `f2a419f4d419200dfea118ac4853b27b17f1f063795345a1bdd141114405b3d4`
- bytes: 4821

````python
"""Fake driver API for testing."""

from __future__ import annotations

import sys
from enum import Enum, IntEnum
from types import TracebackType
from typing import TYPE_CHECKING, Any, ContextManager

if TYPE_CHECKING:
    import grpc

    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self


GRPC_SERVICE_INTERFACE_NAME = "nifake_grpc.NiFake"

# The GrpcSessionOptions classes in nimi-python and nidaqmx-python have an api_key field.
_API_KEY = "00000000-0000-0000-0000-000000000000"


class SessionInitializationBehavior(IntEnum):
    """Specifies whether to initialize a new session or attach to an existing session."""

    AUTO = 0
    INITIALIZE_SERVER_SESSION = 1
    ATTACH_TO_SERVER_SESSION = 2
    INITIALIZE_SESSION_THEN_DETACH = 3
    ATTACH_TO_SESSION_THEN_CLOSE = 4


_CLOSE_BEHAVIORS = [
    SessionInitializationBehavior.AUTO,
    SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE,
]


class GrpcSessionOptions:
    """gRPC session options."""

    def __init__(
        self,
        grpc_channel: grpc.Channel,
        session_name: str,
        *,
        api_key: str = _API_KEY,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
    ) -> None:
        """Initialize the gRPC session options."""
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.api_key = api_key
        self.initialization_behavior = initialization_behavior


class MeasurementType(Enum):
    """Measurement type."""

    VOLTAGE = 1
    CURRENT = 2


class _Acquisition:
    def __init__(self, session: _SessionBase) -> None:
        self._session = session

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self._session.abort()


class _SessionBase:
    """Base class for driver sessions."""

    def __init__(
        self,
        resource_name: str,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
        options: dict[str, Any] = {},
    ) -> None:
        """Initialize the session."""
        self.resource_name = resource_name
        self.initialization_behavior = initialization_behavior
        self.options = options
        self.is_closed = False

    def configure(self, measurement_type: MeasurementType, range: float) -> None:
        """Configure the session."""
        pass

    def initiate(self) -> ContextManager[object]:
        """Initiate an acquisition."""
        return _Acquisition(self)

    def abort(self) -> None:
        """Abort (stop) the acquisition."""
        pass

    def read(self) -> float:
        """Read a sample."""
        return 0.0


class ClosableSession(_SessionBase):
    """A driver session that supports close()."""

    def close(self) -> None:
        """Close the session."""
        self.is_closed = True


class ContextManagerSession(_SessionBase):
    """A driver session that supports the context manager protocol."""

    def __enter__(self) -> Self:
        """Enter the session's runtime context."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the session's runtime context."""
        self.is_closed = True


class Session(_SessionBase):
    """A driver session that supports both close() and the context manager protocol."""

    def __init__(
        self,
        resource_name: str,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
        options: dict[str, Any] = {},
    ) -> None:
        """Initialize the session."""
        self.resource_name = resource_name
        self.initialization_behavior = initialization_behavior
        self.options = options
        self.is_closed = False

    def close(self) -> None:
        """Close the session."""
        self.is_closed = True

    def __enter__(self) -> Self:
        """Enter the session's runtime context."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the session's runtime context."""
        if self.initialization_behavior in _CLOSE_BEHAVIORS:
            self.close()
````

<!--NI_OSS_SOURCE repo=measurement-plugin-python path=packages/service/tests/utilities/fake_multiplexer_driver.py sha256=7c6e6f65aecf20328840c48af7c39c3071713442e1fc48efab36b4716da3431b bytes=4915 -->
## FILE: packages/service/tests/utilities/fake_multiplexer_driver.py

- repository: `ni/measurement-plugin-python`
- source_path: `packages/service/tests/utilities/fake_multiplexer_driver.py`
- sha256: `7c6e6f65aecf20328840c48af7c39c3071713442e1fc48efab36b4716da3431b`
- bytes: 4915

````python
"""Fake driver API for testing."""

from __future__ import annotations

import sys
from enum import Enum, IntEnum
from types import TracebackType
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import grpc

    if sys.version_info >= (3, 11):
        from typing import Self
    else:
        from typing_extensions import Self


GRPC_SERVICE_INTERFACE_NAME = "nifake_grpc.NiFake"

# The GrpcSessionOptions classes in nimi-python and nidaqmx-python have an api_key field.
_API_KEY = "00000000-0000-0000-0000-000000000000"


class SessionInitializationBehavior(IntEnum):
    """Specifies whether to initialize a new session or attach to an existing session."""

    AUTO = 0
    INITIALIZE_SERVER_SESSION = 1
    ATTACH_TO_SERVER_SESSION = 2
    INITIALIZE_SESSION_THEN_DETACH = 3
    ATTACH_TO_SESSION_THEN_CLOSE = 4


_CLOSE_BEHAVIORS = [
    SessionInitializationBehavior.AUTO,
    SessionInitializationBehavior.INITIALIZE_SERVER_SESSION,
    SessionInitializationBehavior.ATTACH_TO_SESSION_THEN_CLOSE,
]


class GrpcSessionOptions:
    """gRPC session options."""

    def __init__(
        self,
        grpc_channel: grpc.Channel,
        session_name: str,
        *,
        api_key: str = _API_KEY,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
    ) -> None:
        """Initialize the gRPC session options."""
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.api_key = api_key
        self.initialization_behavior = initialization_behavior


class RelayAction(Enum):
    """Relay action."""

    OPEN = 1
    CLOSE = 2


class _MultiplexerSessionBase:
    """Base class for multiplexer driver sessions."""

    def __init__(
        self,
        resource_name: str,
        topology: str | None = None,
        reset_device: bool = True,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
    ) -> None:
        """Initialize the multiplexer session."""
        self.resource_name = resource_name
        self.topology = topology
        self.reset_device = reset_device
        self.initialization_behavior = initialization_behavior
        self.is_closed = False

    def relay_control(self, relay_name: str, relay_action: RelayAction) -> None:
        """Controls individual relays of the switch."""
        pass

    def connect_multiple(self, connection_list: str) -> None:
        """Creates the connections between channels specified in connection list."""
        pass

    def disconnect_multiple(self, connection_list: str) -> None:
        """Breaks the connections between channels specified in disconnection list."""
        pass

    def wait_for_debounce(self) -> None:
        """Pauses until all created paths have settled."""
        pass

    def abort(self) -> None:
        """Abort (stop) the acquisition."""
        pass


class ClosableSession(_MultiplexerSessionBase):
    """A driver session that supports close()."""

    def close(self) -> None:
        """Close the session."""
        self.is_closed = True


class ContextManagerSession(_MultiplexerSessionBase):
    """A driver session that supports the context manager protocol."""

    def __enter__(self) -> Self:
        """Enter the session's runtime context."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the session's runtime context."""
        self.is_closed = True


class Session(_MultiplexerSessionBase):
    """A multiplexer driver session that supports both close() and the context manager protocol."""

    def __init__(
        self,
        resource_name: str,
        topology: str | None = None,
        reset_device: bool = True,
        initialization_behavior: SessionInitializationBehavior = SessionInitializationBehavior.AUTO,
    ) -> None:
        """Initialize the multiplexer session."""
        self.resource_name = resource_name
        self.topology = topology
        self.reset_device = reset_device
        self.initialization_behavior = initialization_behavior
        self.is_closed = False

    def close(self) -> None:
        """Close the session."""
        self.is_closed = True

    def __enter__(self) -> Self:
        """Enter the session's runtime context."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the session's runtime context."""
        if self.initialization_behavior in _CLOSE_BEHAVIORS:
            self.close()
````
