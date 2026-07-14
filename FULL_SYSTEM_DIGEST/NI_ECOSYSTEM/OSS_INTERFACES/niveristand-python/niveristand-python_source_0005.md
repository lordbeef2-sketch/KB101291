# NI OSS SOURCE SNAPSHOT: niveristand-python

<!--NI_OSS_SNAPSHOT repo=ni/niveristand-python commit=9ced536d3414f04a8b6b9315ce4c71b879d02a96 -->

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/systemdefinitionapi/modelsupport/_auto_generated_classes.py sha256=9c994b7c02a102d478c2535d615f582990e5234a8627dfd05b25b73dba0959cb bytes=43015 -->
## FILE: src/niveristand/systemdefinitionapi/modelsupport/_auto_generated_classes.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/systemdefinitionapi/modelsupport/_auto_generated_classes.py`
- sha256: `9c994b7c02a102d478c2535d615f582990e5234a8627dfd05b25b73dba0959cb`
- bytes: 43015

````python
"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport  # type: ignore
import System  # type: ignore

from ... import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.systemdefinitionapi.modelsupport.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.systemdefinitionapi.modelsupport.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        return int(self._dotnet_instance)


def _is_iterable(arg: Any) -> bool:
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]:
    insertion_index = -1
    if out_params:
        use_out_param = False
        for signature, out_param in out_params.items():
            if not signature:
                use_out_param = True
            elif len(args) == len(signature):
                use_out_param = True
                for arg, sig_type in zip(args, signature):
                    if not isinstance(arg, sig_type):
                        use_out_param = False
                        break
            if use_out_param:
                insertion_index, insertion_value = out_param
                break

    for index, arg in enumerate(args):
        # insert the extra value then continue
        if index == insertion_index:
            yield insertion_value

        if hasattr(arg, "_dotnet_instance"):
            yield arg._dotnet_instance
        elif arg and _is_iterable(arg) and hasattr(next(iter(arg)), "_dotnet_instance"):
            yield [item._dotnet_instance for item in arg]
        else:
            yield arg
    # insert the extra value if at the end
    if len(args) == insertion_index:
        yield insertion_value


_wrap_sentinel_value = object()

def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]:
    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _wrap_dotnet_instance(dotnetitem: Any):
        if type(dotnetitem) != NationalInstruments.VeriStand.Error:
            pytype = eval(type(dotnetitem).__name__)
            return pytype(dotnetitem)
        elif dotnetitem.IsError:
            raise VeriStandSdfError(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg):
            first = next(iter(arg), _wrap_sentinel_value)
            if first is _wrap_sentinel_value:
                return []  # empty Python list preferable to an empty .NET list or enumerable
            elif _is_ni_type(first):
                return [_wrap_dotnet_instance(item) for item in arg]
            else:
                return [item for item in arg]
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        return arg

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [x for x in wrapped if x is not _wrap_sentinel_value]
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None


class IModelDescriptor(_DotNetBase):
    """Holds information from the model descriptor"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.IModelDescriptor:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IModelDescriptor")

    @property
    def model_name(self) -> str:
        """Name of the model"""
        dotnet_result = self._dotnet_instance.ModelName
        return _wrap(dotnet_result)

    @property
    def model_generation_toolchain_version(self) -> Tuple[int, int, int, int]:
        """Version of the tool that was used to generate the model"""
        dotnet_result = self._dotnet_instance.ModelGenerationToolchainVersion
        return _wrap(dotnet_result)

    @property
    def model_version(self) -> Tuple[int, int, int, int]:
        """Version of the model"""
        dotnet_result = self._dotnet_instance.ModelVersion
        return _wrap(dotnet_result)

    @property
    def author(self) -> str:
        """Model author"""
        dotnet_result = self._dotnet_instance.Author
        return _wrap(dotnet_result)

    @property
    def model_description(self) -> str:
        """Description of the model"""
        dotnet_result = self._dotnet_instance.ModelDescription
        return _wrap(dotnet_result)

    @property
    def target_platforms(self) -> Iterable[str]:
        """Target platforms supported by the model"""
        dotnet_result = self._dotnet_instance.TargetPlatforms
        return _wrap(dotnet_result)


class ModelParamType(_DotNetBase):
    """RESERVED FOR INTERNAL USE. Wraps model parameter information."""

    @overload
    def __init__(self, idx: int, id: str, name: str, type: int, dims: Sequence[int], value: Sequence[float]):
        ...

    @overload
    def __init__(self, idx: int, id: str, name: str, type: int, dims: Sequence[int], value: Sequence[float], enum_value_table: Sequence[Tuple[str,int]], enum_class_name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelParamType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelParamType(*unwrapped)

    @property
    def idx(self) -> int:
        dotnet_result = self._dotnet_instance.Idx
        return _wrap(dotnet_result)

    @property
    def id(self) -> str:
        dotnet_result = self._dotnet_instance.ID
        return _wrap(dotnet_result)

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @property
    def data_type(self) -> int:
        dotnet_result = self._dotnet_instance.DataType
        return _wrap(dotnet_result)

    @property
    def enum_class_name(self) -> str:
        dotnet_result = self._dotnet_instance.EnumClassName
        return _wrap(dotnet_result)

    @property
    def dims(self) -> Sequence[int]:
        """RESERVED FOR INTERNAL USE."""
        dotnet_result = self._dotnet_instance.Dims
        return _wrap(dotnet_result)

    @property
    def value(self) -> Sequence[float]:
        """RESERVED FOR INTERNAL USE."""
        dotnet_result = self._dotnet_instance.Value
        return _wrap(dotnet_result)

    @property
    def enum_value_table(self) -> Sequence[Tuple[str,int]]:
        """EnumValueTable for parameters"""
        dotnet_result = self._dotnet_instance.EnumValueTable
        return _wrap(dotnet_result)

    @enum_value_table.setter
    def enum_value_table(self, value: Sequence[Tuple[str,int]]):
        """EnumValueTable for parameters"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnumValueTable = next(unwrapped)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class ModelPortType(_DotNetBase):
    """RESERVED FOR INTERNAL USE. Wraps model port information."""

    @overload
    def __init__(self, name: str, index: int, task_id: int, is_input: bool, dims: Sequence[int]):
        ...

    @overload
    def __init__(self, name: str, index: int, task_id: int, is_input: bool, dims: Sequence[int], enum_value_table: Sequence[Tuple[str,int]], enum_class_name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelPortType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelPortType(*unwrapped)

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @property
    def index(self) -> int:
        dotnet_result = self._dotnet_instance.Index
        return _wrap(dotnet_result)

    @property
    def task_id(self) -> int:
        dotnet_result = self._dotnet_instance.TaskID
        return _wrap(dotnet_result)

    @property
    def is_input(self) -> bool:
        dotnet_result = self._dotnet_instance.IsInput
        return _wrap(dotnet_result)

    @property
    def enum_class_name(self) -> str:
        dotnet_result = self._dotnet_instance.EnumClassName
        return _wrap(dotnet_result)

    @property
    def dims(self) -> Sequence[int]:
        """RESERVED FOR INTERNAL USE."""
        dotnet_result = self._dotnet_instance.Dims
        return _wrap(dotnet_result)

    @property
    def enum_value_table(self) -> Sequence[Tuple[str,int]]:
        """EnumValueTable for inports and outports"""
        dotnet_result = self._dotnet_instance.EnumValueTable
        return _wrap(dotnet_result)

    @enum_value_table.setter
    def enum_value_table(self, value: Sequence[Tuple[str,int]]):
        """EnumValueTable for inports and outports"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnumValueTable = next(unwrapped)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class ModelSignalType(_DotNetBase):
    """RESERVED FOR INTERNAL USE. Wraps signal info from a model."""

    @overload
    def __init__(self, idx: int, id: str, name: str, block_name: str, port_number: int, datatype: int, dims: Sequence[int]):
        ...

    @overload
    def __init__(self, idx: int, id: str, name: str, block_name: str, port_number: int, datatype: int, dims: Sequence[int], enum_value_table: Sequence[Tuple[str,int]], enum_class_name: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelSignalType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.ModelSignalType(*unwrapped)

    @property
    def idx(self) -> int:
        dotnet_result = self._dotnet_instance.Idx
        return _wrap(dotnet_result)

    @property
    def id(self) -> str:
        dotnet_result = self._dotnet_instance.ID
        return _wrap(dotnet_result)

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @property
    def block_name(self) -> str:
        dotnet_result = self._dotnet_instance.BlockName
        return _wrap(dotnet_result)

    @property
    def data_type(self) -> int:
        dotnet_result = self._dotnet_instance.DataType
        return _wrap(dotnet_result)

    @property
    def port_number(self) -> int:
        dotnet_result = self._dotnet_instance.PortNumber
        return _wrap(dotnet_result)

    @property
    def enum_class_name(self) -> str:
        dotnet_result = self._dotnet_instance.EnumClassName
        return _wrap(dotnet_result)

    @property
    def dims(self) -> Sequence[int]:
        """RESERVED FOR INTERNAL USE."""
        dotnet_result = self._dotnet_instance.Dims
        return _wrap(dotnet_result)

    @property
    def enum_value_table(self) -> Sequence[Tuple[str,int]]:
        """EnumValueTable for signals"""
        dotnet_result = self._dotnet_instance.EnumValueTable
        return _wrap(dotnet_result)

    @enum_value_table.setter
    def enum_value_table(self, value: Sequence[Tuple[str,int]]):
        """EnumValueTable for signals"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnumValueTable = next(unwrapped)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class VsModelEnumTypeDefinitionItems(_DotNetBase):
    """VsModelEnumTypeDefinitionItems type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelEnumTypeDefinitionItems:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelEnumTypeDefinitionItems(*unwrapped)

    @property
    def enum_values(self) -> Sequence[int]:
        """Enum Values for the enum"""
        dotnet_result = self._dotnet_instance.EnumValues
        return _wrap(dotnet_result)

    @enum_values.setter
    def enum_values(self, value: Sequence[int]):
        """Enum Values for the enum"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnumValues = next(unwrapped)

    @property
    def enum_names(self) -> Sequence[str]:
        """Enum name for the enum"""
        dotnet_result = self._dotnet_instance.EnumNames
        return _wrap(dotnet_result)

    @enum_names.setter
    def enum_names(self, value: Sequence[str]):
        """Enum name for the enum"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnumNames = next(unwrapped)


class VsModelFeatureSet(_DotNetBase):
    """Provides information about supported features of a specific version of .vsmodel"""

    @overload
    def __init__(self, vsmodel_version: str):
        ...

    @overload
    def __init__(self, vsmodel_version: System.Version):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelFeatureSet:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelFeatureSet(*unwrapped)

    @_staticproperty
    def first_released_vs_model_addon_version_string() -> str:
        """The first released VsModel addon version as string"""
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelFeatureSet.FirstReleasedVsModelAddonVersionString
        return _wrap(dotnet_result)

    @_staticproperty
    def highest_supported_vs_model_addon_version_string() -> str:
        """Highest supported VsModel addon version as string"""
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelFeatureSet.HighestSupportedVsModelAddonVersionString
        return _wrap(dotnet_result)

    @property
    def supports_non_virtual_bus(self) -> bool:
        """Indicates whether the vsmodel has support for non virtual buses"""
        dotnet_result = self._dotnet_instance.SupportsNonVirtualBus
        return _wrap(dotnet_result)

    @property
    def generated_using_latest_addon_version(self) -> bool:
        """Indicates whether the vsmodel was built with the latest VsModel addon"""
        dotnet_result = self._dotnet_instance.GeneratedUsingLatestAddonVersion
        return _wrap(dotnet_result)

    @property
    def supports_signals(self) -> bool:
        """Indicates whether the vsmodel has support for signals"""
        dotnet_result = self._dotnet_instance.SupportsSignals
        return _wrap(dotnet_result)


class VsModelItemBaseType(_DotNetBase):
    """Class containing information about a model item type. The item can be input, output or parameter"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelItemBaseType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelItemBaseType(*unwrapped)

    @property
    def name(self) -> str:
        """Name of the element"""
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @name.setter
    def name(self, value: str):
        """Name of the element"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Name = next(unwrapped)

    @property
    def data_type(self) -> str:
        """Model item data type"""
        dotnet_result = self._dotnet_instance.DataType
        return _wrap(dotnet_result)

    @data_type.setter
    def data_type(self, value: str):
        """Model item data type"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataType = next(unwrapped)

    @property
    def c_api_type(self) -> str:
        """Type used by Simulink in the generated C code"""
        dotnet_result = self._dotnet_instance.CApiType
        return _wrap(dotnet_result)

    @c_api_type.setter
    def c_api_type(self, value: str):
        """Type used by Simulink in the generated C code"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.CApiType = next(unwrapped)

    @property
    def dimensions(self) -> Any:
        """Model item dimensions"""
        dotnet_result = self._dotnet_instance.Dimensions
        return _wrap(dotnet_result)

    @dimensions.setter
    def dimensions(self, value: Any):
        """Model item dimensions"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Dimensions = next(unwrapped)

    @property
    def elements(self) -> Sequence[VsModelElement]:
        """Model item elements - has content when the item is Bus"""
        dotnet_result = self._dotnet_instance.Elements
        return _wrap(dotnet_result)

    @elements.setter
    def elements(self, value: Sequence[VsModelElement]):
        """Model item elements - has content when the item is Bus"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Elements = next(unwrapped)

    @property
    def enum_class_name(self) -> str:
        """Model item EnumClassName"""
        dotnet_result = self._dotnet_instance.EnumClassName
        return _wrap(dotnet_result)

    @enum_class_name.setter
    def enum_class_name(self, value: str):
        """Model item EnumClassName"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnumClassName = next(unwrapped)

    @overload
    def is_valid(self) -> bool:
        ...

    def is_valid(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsValid(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def is_supported_fixed_point_type(self) -> bool:
        ...

    def is_supported_fixed_point_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsSupportedFixedPointType(*unwrapped)
        return _wrap(dotnet_result)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class VsModelItemType(VsModelItemBaseType):
    """Model item type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelItemType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelItemType(*unwrapped)

    @property
    def unit(self) -> str:
        """Model item unit"""
        dotnet_result = self._dotnet_instance.Unit
        return _wrap(dotnet_result)

    @unit.setter
    def unit(self, value: str):
        """Model item unit"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Unit = next(unwrapped)


class VsModelJsonFileDescriptor(_DotNetBase):
    """Class containing information for deserializing the VsModel descriptor JSON file"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptor:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptor(*unwrapped)

    @property
    def version(self) -> str:
        """Model version"""
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @version.setter
    def version(self, value: str):
        """Model version"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Version = next(unwrapped)

    @property
    def model_name(self) -> str:
        """Model name"""
        dotnet_result = self._dotnet_instance.ModelName
        return _wrap(dotnet_result)

    @model_name.setter
    def model_name(self, value: str):
        """Model name"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ModelName = next(unwrapped)

    @property
    def metadata(self) -> VsModelMetadata:
        """Model metadata"""
        dotnet_result = self._dotnet_instance.Metadata
        return _wrap(dotnet_result)

    @metadata.setter
    def metadata(self, value: VsModelMetadata):
        """Model metadata"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Metadata = next(unwrapped)

    @property
    def inports(self) -> Sequence[VsModelInport]:
        """Inport list"""
        dotnet_result = self._dotnet_instance.Inports
        return _wrap(dotnet_result)

    @inports.setter
    def inports(self, value: Sequence[VsModelInport]):
        """Inport list"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Inports = next(unwrapped)

    @property
    def outports(self) -> Sequence[VsModelOutport]:
        """Outport list"""
        dotnet_result = self._dotnet_instance.Outports
        return _wrap(dotnet_result)

    @outports.setter
    def outports(self, value: Sequence[VsModelOutport]):
        """Outport list"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Outports = next(unwrapped)

    @property
    def parameters(self) -> Sequence[VsModelParameter]:
        """Parameter list"""
        dotnet_result = self._dotnet_instance.Parameters
        return _wrap(dotnet_result)

    @parameters.setter
    def parameters(self, value: Sequence[VsModelParameter]):
        """Parameter list"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Parameters = next(unwrapped)

    @property
    def signals(self) -> Sequence[VsModelSignal]:
        """Signals list"""
        dotnet_result = self._dotnet_instance.Signals
        return _wrap(dotnet_result)

    @signals.setter
    def signals(self, value: Sequence[VsModelSignal]):
        """Signals list"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Signals = next(unwrapped)

    @property
    def enum_type_definitions(self) -> System.Collections.Generic.IReadOnlyDictionary[System.String,NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelEnumTypeDefinitionItems]:
        """EnumTypeDefinitions dictionary"""
        dotnet_result = self._dotnet_instance.EnumTypeDefinitions
        return _wrap(dotnet_result)

    @enum_type_definitions.setter
    def enum_type_definitions(self, value: System.Collections.Generic.IReadOnlyDictionary[System.String,NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelEnumTypeDefinitionItems]):
        """EnumTypeDefinitions dictionary"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnumTypeDefinitions = next(unwrapped)


class VsModelJsonFileDescriptorUtilities(_DotNetBase):
    """Utility methods for VsModelJsonFileDescriptor"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptorUtilities:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for VsModelJsonFileDescriptorUtilities")

    @staticmethod
    @overload
    def get_dimensions(dimensions: Any) -> Sequence[int]:
        ...

    def get_dimensions(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptorUtilities.GetDimensions(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def is_scalar(dimensions: Any) -> bool:
        ...

    def is_scalar(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelJsonFileDescriptorUtilities.IsScalar(*unwrapped)
        return _wrap(dotnet_result)


class VsModelMetadata(_DotNetBase):
    """VsModel metadata"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelMetadata:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelMetadata(*unwrapped)

    @property
    def slx_file_path(self) -> str:
        """.slx file path"""
        dotnet_result = self._dotnet_instance.SLXFilePath
        return _wrap(dotnet_result)

    @slx_file_path.setter
    def slx_file_path(self, value: str):
        """.slx file path"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SLXFilePath = next(unwrapped)

    @property
    def simulink_release(self) -> str:
        """Simulink release"""
        dotnet_result = self._dotnet_instance.SimulinkRelease
        return _wrap(dotnet_result)

    @simulink_release.setter
    def simulink_release(self, value: str):
        """Simulink release"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SimulinkRelease = next(unwrapped)

    @property
    def simulink_version(self) -> str:
        """Simulink version"""
        dotnet_result = self._dotnet_instance.SimulinkVersion
        return _wrap(dotnet_result)

    @simulink_version.setter
    def simulink_version(self, value: str):
        """Simulink version"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SimulinkVersion = next(unwrapped)

    @property
    def release_description(self) -> str:
        """Simulink release descripton"""
        dotnet_result = self._dotnet_instance.ReleaseDescription
        return _wrap(dotnet_result)

    @release_description.setter
    def release_description(self, value: str):
        """Simulink release descripton"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ReleaseDescription = next(unwrapped)

    @property
    def author(self) -> str:
        """Model file author"""
        dotnet_result = self._dotnet_instance.Author
        return _wrap(dotnet_result)

    @author.setter
    def author(self, value: str):
        """Model file author"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Author = next(unwrapped)

    @property
    def description(self) -> str:
        """Model description"""
        dotnet_result = self._dotnet_instance.Description
        return _wrap(dotnet_result)

    @description.setter
    def description(self, value: str):
        """Model description"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Description = next(unwrapped)

    @property
    def model_version(self) -> str:
        """Model version"""
        dotnet_result = self._dotnet_instance.ModelVersion
        return _wrap(dotnet_result)

    @model_version.setter
    def model_version(self, value: str):
        """Model version"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ModelVersion = next(unwrapped)

    @property
    def time_step(self) -> str:
        """Model time step"""
        dotnet_result = self._dotnet_instance.TimeStep
        return _wrap(dotnet_result)

    @time_step.setter
    def time_step(self, value: str):
        """Model time step"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TimeStep = next(unwrapped)

    @property
    def target_platforms(self) -> Sequence[str]:
        """Target platform the model was compiled for"""
        dotnet_result = self._dotnet_instance.TargetPlatforms
        return _wrap(dotnet_result)

    @target_platforms.setter
    def target_platforms(self, value: Sequence[str]):
        """Target platform the model was compiled for"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TargetPlatforms = next(unwrapped)

    @property
    def bitness(self) -> int:
        """Model bitness"""
        dotnet_result = self._dotnet_instance.Bitness
        return _wrap(dotnet_result)

    @bitness.setter
    def bitness(self, value: int):
        """Model bitness"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Bitness = next(unwrapped)

    @property
    def number_of_sample_times(self) -> int:
        """Number of sample times"""
        dotnet_result = self._dotnet_instance.NumberOfSampleTimes
        return _wrap(dotnet_result)

    @number_of_sample_times.setter
    def number_of_sample_times(self, value: int):
        """Number of sample times"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.NumberOfSampleTimes = next(unwrapped)

    @property
    def external_mode(self) -> str:
        """External mode setting: on or off"""
        dotnet_result = self._dotnet_instance.ExternalMode
        return _wrap(dotnet_result)

    @external_mode.setter
    def external_mode(self, value: str):
        """External mode setting: on or off"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ExternalMode = next(unwrapped)


class VsModelParameter(VsModelItemType):
    """Parameter type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelParameter:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelParameter(*unwrapped)

    @property
    def default_value(self) -> Any:
        """Default value"""
        dotnet_result = self._dotnet_instance.DefaultValue
        return _wrap(dotnet_result)

    @default_value.setter
    def default_value(self, value: Any):
        """Default value"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DefaultValue = next(unwrapped)


class VsModelSignal(VsModelItemType):
    """Signal type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelSignal:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelSignal(*unwrapped)

    @property
    def block_path(self) -> str:
        """Name of the source block for the signal."""
        dotnet_result = self._dotnet_instance.BlockPath
        return _wrap(dotnet_result)

    @block_path.setter
    def block_path(self, value: str):
        """Name of the source block for the signal."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BlockPath = next(unwrapped)

    @property
    def port_number(self) -> int:
        """Port number of the block that is the source of the signal."""
        dotnet_result = self._dotnet_instance.PortNumber
        return _wrap(dotnet_result)

    @port_number.setter
    def port_number(self, value: int):
        """Port number of the block that is the source of the signal."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.PortNumber = next(unwrapped)

    @property
    def signal_label(self) -> str:
        """Name of the signal"""
        dotnet_result = self._dotnet_instance.SignalLabel
        return _wrap(dotnet_result)

    @signal_label.setter
    def signal_label(self, value: str):
        """Name of the signal"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SignalLabel = next(unwrapped)

    @property
    def is_connected_to_virtual_bus(self) -> bool:
        """Whether the signal is connected to a virtual bus."""
        dotnet_result = self._dotnet_instance.IsConnectedToVirtualBus
        return _wrap(dotnet_result)

    @is_connected_to_virtual_bus.setter
    def is_connected_to_virtual_bus(self, value: bool):
        """Whether the signal is connected to a virtual bus."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IsConnectedToVirtualBus = next(unwrapped)


class FmuModelDescriptor(IModelDescriptor):
    @overload
    def __init__(self, model_path: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.FmuModelDescriptor:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.FmuModelDescriptor(*unwrapped)

    @property
    def target_platforms(self) -> Iterable[str]:
        dotnet_result = self._dotnet_instance.TargetPlatforms
        return _wrap(dotnet_result)

    @target_platforms.setter
    def target_platforms(self, value: Iterable[str]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TargetPlatforms = next(unwrapped)

    @property
    def fmi_version(self) -> str:
        """FMI version"""
        dotnet_result = self._dotnet_instance.FmiVersion
        return _wrap(dotnet_result)

    @fmi_version.setter
    def fmi_version(self, value: str):
        """FMI version"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.FmiVersion = next(unwrapped)

    @property
    def generation_tool(self) -> str:
        """Model generation tool"""
        dotnet_result = self._dotnet_instance.GenerationTool
        return _wrap(dotnet_result)

    @generation_tool.setter
    def generation_tool(self, value: str):
        """Model generation tool"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.GenerationTool = next(unwrapped)

    @property
    def fmu_file_size(self) -> int:
        """Model file size"""
        dotnet_result = self._dotnet_instance.FmuFileSize
        return _wrap(dotnet_result)


class VsModelDescriptorExtended(VsModelJsonFileDescriptor, IModelDescriptor):
    """VsModel descriptor containing both information needed for deserialization and other vsmodel properties"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelDescriptorExtended:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelDescriptorExtended(*unwrapped)

    @property
    def enum_value_table_by_enum_class_name(self) -> dict[str, Sequence[Tuple[str, int]]]:
        """EnumValueTable by enum class name of the model"""
        dotnet_result = self._dotnet_instance.EnumValueTableByEnumClassName
        return _wrap(dotnet_result)

    @enum_value_table_by_enum_class_name.setter
    def enum_value_table_by_enum_class_name(self, value: dict[str, Sequence[Tuple[str, int]]]):
        """EnumValueTable by enum class name of the model"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.EnumValueTableByEnumClassName = next(unwrapped)

    @staticmethod
    @overload
    def deserialize_from(stream_reader: System.IO.StreamReader) -> VsModelDescriptorExtended:
        ...

    def deserialize_from(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelDescriptorExtended.DeserializeFrom(*unwrapped)
        return _wrap(dotnet_result)


class VsModelElement(VsModelItemBaseType):
    """Element type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelElement:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelElement(*unwrapped)


class VsModelInportOutportType(VsModelItemType):
    """Inport and Outports type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelInportOutportType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelInportOutportType(*unwrapped)


class VsModelOutport(VsModelInportOutportType):
    """Outport type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelOutport:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelOutport(*unwrapped)

    @property
    def is_connected_to_virtual_bus(self) -> bool:
        """Whether the outport is connected to a virtual bus."""
        dotnet_result = self._dotnet_instance.IsConnectedToVirtualBus
        return _wrap(dotnet_result)

    @is_connected_to_virtual_bus.setter
    def is_connected_to_virtual_bus(self, value: bool):
        """Whether the outport is connected to a virtual bus."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IsConnectedToVirtualBus = next(unwrapped)


class VsModelInport(VsModelInportOutportType):
    """Inport type"""

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelInport:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VsModelInport(*unwrapped)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/__init__.py sha256=2a331e40bb654ade79c540a3ce1176d205ee97bfe5da2a194644934f37a226fa bytes=196 -->
## FILE: src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/__init__.py`
- sha256: `2a331e40bb654ade79c540a3ce1176d205ee97bfe5da2a194644934f37a226fa`
- bytes: 196

````python
"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from ._auto_generated_classes import *
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/_auto_generated_classes.py sha256=c9fa0536b6c565f74849471fe25024e4660150eebbf44ad216a133770febbfb6 bytes=16867 -->
## FILE: src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/_auto_generated_classes.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/systemdefinitionapi/modelsupport/virtualecusupport/_auto_generated_classes.py`
- sha256: `c9fa0536b6c565f74849471fe25024e4660150eebbf44ad216a133770febbfb6`
- bytes: 16867

````python
"""Module for NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemDefinitionAPI")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport  # type: ignore
import System  # type: ignore

from ... import *
from .... import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.systemdefinitionapi.modelsupport.virtualecusupport.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.systemdefinitionapi.modelsupport.virtualecusupport.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        return int(self._dotnet_instance)


def _is_iterable(arg: Any) -> bool:
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]:
    insertion_index = -1
    if out_params:
        use_out_param = False
        for signature, out_param in out_params.items():
            if not signature:
                use_out_param = True
            elif len(args) == len(signature):
                use_out_param = True
                for arg, sig_type in zip(args, signature):
                    if not isinstance(arg, sig_type):
                        use_out_param = False
                        break
            if use_out_param:
                insertion_index, insertion_value = out_param
                break

    for index, arg in enumerate(args):
        # insert the extra value then continue
        if index == insertion_index:
            yield insertion_value

        if hasattr(arg, "_dotnet_instance"):
            yield arg._dotnet_instance
        elif arg and _is_iterable(arg) and hasattr(next(iter(arg)), "_dotnet_instance"):
            yield [item._dotnet_instance for item in arg]
        else:
            yield arg
    # insert the extra value if at the end
    if len(args) == insertion_index:
        yield insertion_value


_wrap_sentinel_value = object()

def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]:
    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _wrap_dotnet_instance(dotnetitem: Any):
        if type(dotnetitem) != NationalInstruments.VeriStand.Error:
            pytype = eval(type(dotnetitem).__name__)
            return pytype(dotnetitem)
        elif dotnetitem.IsError:
            raise VeriStandSdfError(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg):
            first = next(iter(arg), _wrap_sentinel_value)
            if first is _wrap_sentinel_value:
                return []  # empty Python list preferable to an empty .NET list or enumerable
            elif _is_ni_type(first):
                return [_wrap_dotnet_instance(item) for item in arg]
            else:
                return [item for item in arg]
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        return arg

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [x for x in wrapped if x is not _wrap_sentinel_value]
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None


class CANConfiguration(ICANConfiguration):
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, other: ICANConfiguration):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.CANConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.CANConfiguration(*unwrapped)

    @property
    def connect_to_real_network(self) -> bool:
        """Value indicating whether to connect to the real network."""
        dotnet_result = self._dotnet_instance.ConnectToRealNetwork
        return _wrap(dotnet_result)

    @connect_to_real_network.setter
    def connect_to_real_network(self, value: bool):
        """Value indicating whether to connect to the real network."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ConnectToRealNetwork = next(unwrapped)

    @property
    def use_database(self) -> bool:
        """Value indicating whether to use a database."""
        dotnet_result = self._dotnet_instance.UseDatabase
        return _wrap(dotnet_result)

    @use_database.setter
    def use_database(self, value: bool):
        """Value indicating whether to use a database."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.UseDatabase = next(unwrapped)

    @property
    def database_alias(self) -> str:
        """Database alias value."""
        dotnet_result = self._dotnet_instance.DatabaseAlias
        return _wrap(dotnet_result)

    @database_alias.setter
    def database_alias(self, value: str):
        """Database alias value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DatabaseAlias = next(unwrapped)


class Constants(_DotNetBase):
    """Contains constants for VirtualECU"""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.Constants:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for Constants")

    @_staticproperty
    def ecu_network_cluster_file_extension() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.Constants.ECUNetworkClusterFileExtension
        return _wrap(dotnet_result)


class ECUNetworkClusterConfiguration(IECUNetworkClusterConfiguration):
    """Class for serializing and de-serializing ECU network cluster configuration."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, other: IECUNetworkClusterConfiguration):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration(*unwrapped)

    @property
    def version(self) -> str:
        """Version of the json file."""
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @version.setter
    def version(self, value: str):
        """Version of the json file."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Version = next(unwrapped)

    @property
    def database_path(self) -> str:
        """Database path."""
        dotnet_result = self._dotnet_instance.DatabasePath
        return _wrap(dotnet_result)

    @database_path.setter
    def database_path(self, value: str):
        """Database path."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DatabasePath = next(unwrapped)

    @property
    def virtual_ecu_list(self) -> Sequence[str]:
        """Virtual ECUs that have been added to the cluster."""
        dotnet_result = self._dotnet_instance.VirtualECUList
        return _wrap(dotnet_result)

    @virtual_ecu_list.setter
    def virtual_ecu_list(self, value: Sequence[str]):
        """Virtual ECUs that have been added to the cluster."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VirtualECUList = next(unwrapped)

    @property
    def lin_master_model_linux_path(self) -> str:
        """LIN Master Model path."""
        dotnet_result = self._dotnet_instance.LINMasterModelLinuxPath
        return _wrap(dotnet_result)

    @lin_master_model_linux_path.setter
    def lin_master_model_linux_path(self, value: str):
        """LIN Master Model path."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.LINMasterModelLinuxPath = next(unwrapped)

    @property
    def svb_configuration(self) -> SVBConfiguration:
        """Represents the configuration for Synopsys Virtual Bus (SVB)."""
        dotnet_result = self._dotnet_instance.SVBConfiguration
        return _wrap(dotnet_result)

    @svb_configuration.setter
    def svb_configuration(self, value: SVBConfiguration):
        """Represents the configuration for Synopsys Virtual Bus (SVB)."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.SVBConfiguration = next(unwrapped)

    @overload
    def serialize_to(self, cluster_configuration_file_path: str):
        ...

    def serialize_to(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SerializeTo(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def try_deserialize_from(model_path: str) -> Tuple[bool, IECUNetworkClusterConfiguration]:
        ...

    def try_deserialize_from(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration.TryDeserializeFrom(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def deserialize_from(file_path: str) -> IECUNetworkClusterConfiguration:
        ...

    def deserialize_from(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.ECUNetworkClusterConfiguration.DeserializeFrom(*unwrapped)
        return _wrap(dotnet_result)


class EthernetConfiguration(IEthernetConfiguration):
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, other: IEthernetConfiguration):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.EthernetConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.EthernetConfiguration(*unwrapped)

    @property
    def connect_to_real_network(self) -> bool:
        """Value indicating whether to connect to the real network."""
        dotnet_result = self._dotnet_instance.ConnectToRealNetwork
        return _wrap(dotnet_result)

    @connect_to_real_network.setter
    def connect_to_real_network(self, value: bool):
        """Value indicating whether to connect to the real network."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ConnectToRealNetwork = next(unwrapped)

    @property
    def virtual_ecumac_addresses(self) -> Sequence[str]:
        """Virtual ECU MAC Addresses."""
        dotnet_result = self._dotnet_instance.VirtualECUMACAddresses
        return _wrap(dotnet_result)

    @virtual_ecumac_addresses.setter
    def virtual_ecumac_addresses(self, value: Sequence[str]):
        """Virtual ECU MAC Addresses."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VirtualECUMACAddresses = next(unwrapped)


class LINConfiguration(ILINConfiguration):
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, other: ILINConfiguration):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.LINConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.LINConfiguration(*unwrapped)

    @property
    def connect_to_real_network(self) -> bool:
        """Value indicating whether to connect to the real network."""
        dotnet_result = self._dotnet_instance.ConnectToRealNetwork
        return _wrap(dotnet_result)

    @connect_to_real_network.setter
    def connect_to_real_network(self, value: bool):
        """Value indicating whether to connect to the real network."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ConnectToRealNetwork = next(unwrapped)

    @property
    def use_database(self) -> bool:
        """Value indicating whether to use a database."""
        dotnet_result = self._dotnet_instance.UseDatabase
        return _wrap(dotnet_result)

    @use_database.setter
    def use_database(self, value: bool):
        """Value indicating whether to use a database."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.UseDatabase = next(unwrapped)

    @property
    def database_alias(self) -> str:
        """Database alias value."""
        dotnet_result = self._dotnet_instance.DatabaseAlias
        return _wrap(dotnet_result)

    @database_alias.setter
    def database_alias(self, value: str):
        """Database alias value."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DatabaseAlias = next(unwrapped)

    @property
    def virtual_tx_frame_i_ds(self) -> Sequence[int]:
        """Virtual transmission frame IDs."""
        dotnet_result = self._dotnet_instance.VirtualTxFrameIDs
        return _wrap(dotnet_result)

    @virtual_tx_frame_i_ds.setter
    def virtual_tx_frame_i_ds(self, value: Sequence[int]):
        """Virtual transmission frame IDs."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.VirtualTxFrameIDs = next(unwrapped)


class SVBConfiguration(_DotNetBase):
    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.SVBConfiguration:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemDefinitionAPI.ModelSupport.VirtualECUSupport.SVBConfiguration(*unwrapped)

    @property
    def rx_fifo_capacity(self) -> int:
        dotnet_result = self._dotnet_instance.RxFifoCapacity
        return _wrap(dotnet_result)

    @rx_fifo_capacity.setter
    def rx_fifo_capacity(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RxFifoCapacity = next(unwrapped)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/systemstorage/__init__.py sha256=84d314acccca259d0d9a4714a4103bda4ed76d3e3bde1aad132fa0d4fe01915f bytes=159 -->
## FILE: src/niveristand/systemstorage/__init__.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/systemstorage/__init__.py`
- sha256: `84d314acccca259d0d9a4714a4103bda4ed76d3e3bde1aad132fa0d4fe01915f`
- bytes: 159

````python
"""Module for NationalInstruments.VeriStand.SystemStorage."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from ._auto_generated_classes import *
````

<!--NI_OSS_SOURCE repo=niveristand-python path=src/niveristand/systemstorage/_auto_generated_classes.py sha256=dcde98b6754b15857bed831d5a6086c6c5c891cd949910a1a00a79c6c52db837 bytes=118171 -->
## FILE: src/niveristand/systemstorage/_auto_generated_classes.py

- repository: `ni/niveristand-python`
- source_path: `src/niveristand/systemstorage/_auto_generated_classes.py`
- sha256: `dcde98b6754b15857bed831d5a6086c6c5c891cd949910a1a00a79c6c52db837`
- bytes: 118171

````python
"""Module for NationalInstruments.VeriStand.SystemStorage."""
### AUTO-GENERATED CODE - DO NOT MODIFY DIRECTLY ###

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Optional, overload, Sequence, Tuple, Union

import clr

clr.AddReference("NationalInstruments.VeriStand.SystemStorage")
import NationalInstruments.VeriStand  # type: ignore
import NationalInstruments.VeriStand.SystemStorage  # type: ignore
import System  # type: ignore

from .. import *


class _staticproperty(staticmethod):
    def __get__(self, *_):
        return self.__func__()


class _DotNetBase:
    def __eq__(self, other) -> bool:
        return self._dotnet_instance == other._dotnet_instance if isinstance(other, _DotNetBase) else False

    def __repr__(self) -> str:
        qualname = type(self).__qualname__
        return f"<niveristand.systemstorage.{qualname}{self._custom_repr()} object at {hex(id(self))}>"

    def _custom_repr(self) -> str:
        return ""


class _DotNetEnum(_DotNetBase):
    def __repr__(self) -> str:
        return f"<niveristand.systemstorage.{type(self).__qualname__}.{self._py_field_name}: {int(self)}>"

    def __str__(self) -> str:
        return f"{type(self).__qualname__}.{self._py_field_name}"

    def __int__(self) -> int:
        return int(self._dotnet_instance)


def _is_iterable(arg: Any) -> bool:
    return not isinstance(arg, str) and isinstance(arg, Iterable)


def _unwrap(out_params: Dict[Optional[Tuple[str, ...]], Tuple[int, Any]], *args: Tuple[Any]) -> Iterable[Any]:
    insertion_index = -1
    if out_params:
        use_out_param = False
        for signature, out_param in out_params.items():
            if not signature:
                use_out_param = True
            elif len(args) == len(signature):
                use_out_param = True
                for arg, sig_type in zip(args, signature):
                    if not isinstance(arg, sig_type):
                        use_out_param = False
                        break
            if use_out_param:
                insertion_index, insertion_value = out_param
                break

    for index, arg in enumerate(args):
        # insert the extra value then continue
        if index == insertion_index:
            yield insertion_value

        if hasattr(arg, "_dotnet_instance"):
            yield arg._dotnet_instance
        elif arg and _is_iterable(arg) and hasattr(next(iter(arg)), "_dotnet_instance"):
            yield [item._dotnet_instance for item in arg]
        else:
            yield arg
    # insert the extra value if at the end
    if len(args) == insertion_index:
        yield insertion_value


_wrap_sentinel_value = object()

def _wrap(one_or_many_args: Union[Any, Tuple[Any]]) -> Union[Any, Tuple[Any]]:
    def _is_ni_type(item: Any):
        return type(item).__module__.startswith("NationalInstruments.")

    def _wrap_dotnet_instance(dotnetitem: Any):
        if type(dotnetitem) != NationalInstruments.VeriStand.Error:
            pytype = eval(type(dotnetitem).__name__)
            return pytype(dotnetitem)
        elif dotnetitem.IsError:
            raise VeriStandSdfError(dotnetitem)
        else:
            return _wrap_sentinel_value

    def _wrap_core(arg: Any) -> Any:
        if _is_iterable(arg):
            first = next(iter(arg), _wrap_sentinel_value)
            if first is _wrap_sentinel_value:
                return []  # empty Python list preferable to an empty .NET list or enumerable
            elif _is_ni_type(first):
                return [_wrap_dotnet_instance(item) for item in arg]
            else:
                return [item for item in arg]
        elif _is_ni_type(arg):
            return _wrap_dotnet_instance(arg)
        elif str(type(arg)) == "<class 'System.Version'>":
            # System.Version uses `Build` as the third element, not the fourth
            return (arg.Major, arg.Minor, arg.Build, arg.Revision)
        return arg

    if isinstance(one_or_many_args, Tuple):
        wrapped = [_wrap_core(x) for x in one_or_many_args]
        result = [x for x in wrapped if x is not _wrap_sentinel_value]
        # if we have two parameters, and one is Error, only return the non-error one
        return result[0] if len(result) == 1 and len(wrapped) == 2 else tuple(result)
    else:
        result = _wrap_core(one_or_many_args)
        return result if result is not _wrap_sentinel_value else None


class BaseNodeType(_DotNetBase):
    """Base class for all nodes in the tree. All actual nodes in the tree is a specialized type of this base class."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: BaseNodeType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.BaseNodeType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.BaseNodeType(*unwrapped)

    @property
    def node_path_array(self) -> Sequence[str]:
        """Get the node path of the node as path array."""
        dotnet_result = self._dotnet_instance.NodePathArray
        return _wrap(dotnet_result)

    @property
    def node_path(self) -> str:
        """Get the node path of the node as a string."""
        dotnet_result = self._dotnet_instance.NodePath
        return _wrap(dotnet_result)

    @property
    def errors_array(self) -> Sequence[ErrorEntry]:
        dotnet_result = self._dotnet_instance.ErrorsArray
        return _wrap(dotnet_result)

    @errors_array.setter
    def errors_array(self, value: Sequence[ErrorEntry]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ErrorsArray = next(unwrapped)

    @property
    def bfs_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return a Breath First Search enumerator. This enumerator iterates through all children of
            then node directly before diving into the hierarchy. For leaf type nodes it will return only itself."""
        dotnet_result = self._dotnet_instance.BFSEnumerator
        return _wrap(dotnet_result)

    @property
    def dfs_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return a Depth First Search enumerator. This enumerator iterates into the hiearchy of the
            first children it found."""
        dotnet_result = self._dotnet_instance.DFSEnumerator
        return _wrap(dotnet_result)

    @property
    def child_only_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return enumerator that allow user to enumerate through the children of this node only."""
        dotnet_result = self._dotnet_instance.ChildOnlyEnumerator
        return _wrap(dotnet_result)

    @property
    def child_only_object_enumerator(self) -> System.Collections.IEnumerator:
        """Return non generic enumerator that allow user to enumerate through the children of this node only."""
        dotnet_result = self._dotnet_instance.ChildOnlyObjectEnumerator
        return _wrap(dotnet_result)

    @property
    def trav_parent_enumerator(self) -> System.IEnumerator[NationalInstruments.VeriStand.SystemStorage.BaseNodeType]:
        """Return enumerator that allow user to enumerate through the parent."""
        dotnet_result = self._dotnet_instance.TravParentEnumerator
        return _wrap(dotnet_result)

    @property
    def id(self) -> int:
        """ID"""
        dotnet_result = self._dotnet_instance.ID
        return _wrap(dotnet_result)

    @id.setter
    def id(self, value: int):
        """ID"""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ID = next(unwrapped)

    @property
    def temp_properties(self) -> Sequence[PropertyType]:
        dotnet_result = self._dotnet_instance.TempProperties
        return _wrap(dotnet_result)

    @temp_properties.setter
    def temp_properties(self, value: Sequence[PropertyType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TempProperties = next(unwrapped)

    @property
    def description(self) -> str:
        dotnet_result = self._dotnet_instance.Description
        return _wrap(dotnet_result)

    @description.setter
    def description(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Description = next(unwrapped)

    @property
    def properties(self) -> Sequence[PropertyType]:
        dotnet_result = self._dotnet_instance.Properties
        return _wrap(dotnet_result)

    @properties.setter
    def properties(self, value: Sequence[PropertyType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Properties = next(unwrapped)

    @property
    def errors(self) -> Sequence[ErrorEntry]:
        dotnet_result = self._dotnet_instance.Errors
        return _wrap(dotnet_result)

    @errors.setter
    def errors(self, value: Sequence[ErrorEntry]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Errors = next(unwrapped)

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @name.setter
    def name(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Name = next(unwrapped)

    @property
    def type_guid(self) -> str:
        dotnet_result = self._dotnet_instance.TypeGUID
        return _wrap(dotnet_result)

    @type_guid.setter
    def type_guid(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TypeGUID = next(unwrapped)

    @property
    def identifier(self) -> System.Guid:
        dotnet_result = self._dotnet_instance.Identifier
        return _wrap(dotnet_result)

    @identifier.setter
    def identifier(self, value: System.Guid):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Identifier = next(unwrapped)

    @overload
    def add_error(self, key: str, is_error: bool, err_code: int, message: str):
        ...

    def add_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_error(self, key: str):
        ...

    def remove_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_all_error(self):
        ...

    def remove_all_error(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveAllError(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def duplicate_public_errors(self, other_node: BaseNodeType):
        ...

    def duplicate_public_errors(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DuplicatePublicErrors(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_all_errors(self) -> Sequence[ErrorEntry]:
        ...

    def get_all_errors(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.getAllErrors(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def on_collection_changed(self, e: System.Collections.Specialized.NotifyCollectionChangedEventArgs):
        ...

    def on_collection_changed(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.OnCollectionChanged(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def compare_to(self, obj: Any) -> int:
        ...

    @overload
    def compare_to(self, other: BaseNodeType) -> int:
        ...

    def compare_to(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CompareTo(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def to_string(self) -> str:
        ...

    def to_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ToString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_type(self) -> NodeType:
        ...

    def get_node_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_children(self, deep: bool, mode: TraversalMode) -> Sequence[BaseNodeType]:
        ...

    def get_node_children(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeChildren(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_sorted_node_children(self, deep_traversal: bool, natural_sort: bool, guids_to_skip_child_sort: Sequence[str]) -> Sequence[BaseNodeType]:
        ...

    @overload
    def get_sorted_node_children(self, deep_traversal: bool, natural_sort: bool, guids_to_skip_child_sort: Sequence[str], leaf_filter: ITraverseNodeFilter, branch_filter: ITraverseNodeFilter) -> Sequence[BaseNodeType]:
        ...

    def get_sorted_node_children(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSortedNodeChildren(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_node_in_array(self, list: Sequence[BaseNodeType]) -> int:
        ...

    def find_node_in_array(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNodeInArray(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def filter_base_node_types(self, list: Sequence[BaseNodeType], filter: ITraverseNodeFilter) -> Sequence[BaseNodeType]:
        ...

    def filter_base_node_types(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FilterBaseNodeTypes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def is_reference_same_object(self, node_to_compare: BaseNodeType) -> bool:
        ...

    def is_reference_same_object(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsReferenceSameObject(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def rename_node(self, new_name: str) -> bool:
        ...

    def rename_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RenameNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def is_node_relative(self, node_to_check: BaseNodeType) -> bool:
        ...

    def is_node_relative(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsNodeRelative(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def accept(self, visitor: IVisitor):
        ...

    @overload
    def accept(self, visitor_inspection: IVisitorWithInspection) -> IInspectorResult:
        ...

    def accept(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Accept(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_root(self) -> RootType:
        ...

    def get_node_root(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeRoot(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_parent(self) -> Tuple[bool, BaseNodeType]:
        ...

    def get_parent(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetParent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_duplicate_reference(self) -> BaseNodeType:
        ...

    def get_duplicate_reference(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDuplicateReference(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_node(self, id: int) -> Tuple[bool, BaseNodeType]:
        ...

    @overload
    def find_node(self, path: Sequence[str]) -> Tuple[bool, BaseNodeType]:
        ...

    def find_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_first_child_node_with_name(self, name: str) -> Tuple[bool, BaseNodeType]:
        ...

    def find_first_child_node_with_name(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindFirstChildNodeWithName(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_node_match_guid(self, guid: str, recurse: bool) -> Sequence[BaseNodeType]:
        ...

    @overload
    def find_node_match_guid(self, guid: str) -> BaseNodeType:
        ...

    @overload
    def find_node_match_guid(self, guids: Sequence[str], recurse: bool) -> Tuple[Sequence[BaseNodeType], str]:
        ...

    def find_node_match_guid(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNodeMatchGUID(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_nodesby_guid(self, guids: Sequence[str], recurse: bool, traversal_mode: TraversalMode) -> Tuple[bool, Sequence[BaseNodeType]]:
        ...

    def find_nodesby_guid(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindNodesbyGUID(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def find_guid_up(self, guid: str) -> Tuple[bool, BaseNodeType]:
        ...

    @overload
    def find_guid_up(self, guid: Sequence[str]) -> Tuple[bool, BaseNodeType, str]:
        ...

    def find_guid_up(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FindGUIDUp(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_node(self):
        ...

    @overload
    def remove_node(self, for_reuse: bool):
        ...

    def remove_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def move_node_to(self, new_parent: BaseNodeType) -> bool:
        ...

    def move_node_to(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.MoveNodeTo(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def attached_child_node(self, node_to_attached: BaseNodeType) -> bool:
        ...

    def attached_child_node(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AttachedChildNode(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_properties(self) -> Tuple[Sequence[str], Sequence[PropertyContent]]:
        ...

    def get_node_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodeProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_node_property_type(self, name: str) -> Tuple[bool, PropertyContent]:
        ...

    def get_node_property_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetNodePropertyType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_all_properties_with_type(self, prop_type: PropertyContent) -> Sequence[str]:
        ...

    def get_all_properties_with_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAllPropertiesWithType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def has_node_property(self, name: str) -> Tuple[bool, PropertyContent]:
        ...

    def has_node_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.HasNodeProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clear_properties(self):
        ...

    def clear_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ClearProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def duplicate_properties(self, other_node: BaseNodeType):
        ...

    def duplicate_properties(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DuplicateProperties(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_property(self, name: str, value: str) -> bool:
        ...

    def set_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_binary_string_property(self, name: str, value: Sequence[int]) -> bool:
        ...

    def set_binary_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBinaryStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_boolean_property(self, name: str, value: bool) -> bool:
        ...

    def set_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_property(self, name: str, value: int) -> bool:
        ...

    def set_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i16_property(self, name: str, value: int) -> bool:
        ...

    def set_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i64_property(self, name: str, value: int) -> bool:
        ...

    def set_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_property(self, name: str, value: int) -> bool:
        ...

    def set_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u16_property(self, name: str, value: int) -> bool:
        ...

    def set_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_property(self, name: str, value: float) -> bool:
        ...

    def set_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u64_property(self, name: str, value: int) -> bool:
        ...

    def set_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_variant_property(self, name: str, type: Sequence[int], data: Sequence[int]) -> bool:
        ...

    def set_variant_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetVariantProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_double_array_property(self, name: str, data: Sequence[float]) -> bool:
        ...

    def set_double_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDoubleArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_boolean_array_property(self, name: str, data: Sequence[bool]) -> bool:
        ...

    def set_boolean_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetBooleanArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u64_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u64_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU64ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u32_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_u16_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_u16_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetU16ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i64_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i64_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI64ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i32_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_i16_array_property(self, name: str, data: Sequence[int]) -> bool:
        ...

    def set_i16_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetI16ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_string_array_property(self, name: str, data: Sequence[str]) -> bool:
        ...

    def set_string_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetStringArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dictionary_property(self, name: str, data: DictionaryProperty) -> bool:
        ...

    def set_dictionary_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDictionaryProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dictionary_array_property(self, name: str, data: Sequence[DictionaryProperty]) -> bool:
        ...

    def set_dictionary_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDictionaryArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dependent_file_value(self, name: str, file_path: str, type: DependentFilePropertyType, version: str, force_download: bool, rt_dest: str, supported_target: str, md5: str) -> bool:
        ...

    def set_dependent_file_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDependentFileValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_dependent_node_value(self, name: str, node: BaseNodeType) -> bool:
        ...

    @overload
    def set_dependent_node_value(self, name: str, node_path: str) -> bool:
        ...

    def set_dependent_node_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDependentNodeValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_data_source_value(self, name: str, node: BaseNodeType) -> bool:
        ...

    @overload
    def set_data_source_value(self, name: str, node_path: str) -> bool:
        ...

    def set_data_source_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetDataSourceValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_property(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_binary_string_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_binary_string_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBinaryStringProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_property(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_boolean_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double_property(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_property(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64Property(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_variant_value(self, name: str) -> Tuple[bool, Sequence[int], Sequence[int]]:
        ...

    def get_variant_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetVariantValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double_array_property(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_double_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDoubleArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_boolean_array_property(self, name: str) -> Tuple[bool, Sequence[bool]]:
        ...

    def get_boolean_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBooleanArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u64_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_u16_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i64_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i32_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16_array_property(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_i16_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16ArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string_array_property(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_string_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetStringArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dictionary_property(self, name: str) -> Tuple[bool, DictionaryProperty]:
        ...

    def get_dictionary_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDictionaryProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dictionary_array_property(self, name: str) -> Tuple[bool, Sequence[DictionaryProperty]]:
        ...

    def get_dictionary_array_property(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDictionaryArrayProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_dependent_node_value_str(self, name: str) -> Tuple[bool, str]:
        ...

    def get_dependent_node_value_str(self, *args):
        for method in NationalInstruments.VeriStand.SystemStorage.BaseNodeType().GetType().GetMethods():
            if str(method) == 'Boolean GetDependentNodeValue(System.String, System.String ByRef)':
                params_tuple = tuple(_unwrap({None: (1, "")}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

    @overload
    def get_dependent_node_value_basenodetype(self, name: str) -> Tuple[bool, BaseNodeType]:
        ...

    def get_dependent_node_value_basenodetype(self, *args):
        for method in NationalInstruments.VeriStand.SystemStorage.BaseNodeType().GetType().GetMethods():
            if str(method) == 'Boolean GetDependentNodeValue(System.String, NationalInstruments.VeriStand.SystemStorage.BaseNodeType ByRef)':
                params_tuple = tuple(_unwrap({None: (1, None)}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

    @overload
    def get_data_source_node_value_str(self, name: str) -> Tuple[bool, str]:
        ...

    def get_data_source_node_value_str(self, *args):
        for method in NationalInstruments.VeriStand.SystemStorage.BaseNodeType().GetType().GetMethods():
            if str(method) == 'Boolean GetDataSourceNodeValue(System.String, System.String ByRef)':
                params_tuple = tuple(_unwrap({None: (1, "")}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

    @overload
    def get_data_source_node_value_basenodetype(self, name: str) -> Tuple[bool, BaseNodeType]:
        ...

    def get_data_source_node_value_basenodetype(self, *args):
        for method in NationalInstruments.VeriStand.SystemStorage.BaseNodeType().GetType().GetMethods():
            if str(method) == 'Boolean GetDataSourceNodeValue(System.String, NationalInstruments.VeriStand.SystemStorage.BaseNodeType ByRef)':
                params_tuple = tuple(_unwrap({None: (1, None)}, *args))
                # Object[] needed to get out parameters
                params_array = System.Array[System.Object](len(params_tuple))
                for i, param in enumerate(params_tuple):
                    params_array[i] = param
                dotnet_result = method.Invoke(self._dotnet_instance, params_array)
                return _wrap((dotnet_result, params_array[1]))

    @overload
    def get_dependent_file_value(self, name: str) -> Tuple[bool, str, DependentFilePropertyType, str, bool, str, str, str]:
        ...

    def get_dependent_file_value(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDependentFileValue(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_property(self, name: str) -> bool:
        ...

    def remove_property(self, *args):
        unwrapped = _unwrap({None: (1, NationalInstruments.VeriStand.Error.NoError)}, *args)
        dotnet_result = self._dotnet_instance.RemoveProperty(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clone(self) -> BaseNodeType:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def shallow_copy(self) -> BaseNodeType:
        ...

    def shallow_copy(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ShallowCopy(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def deep_copy(self) -> BaseNodeType:
        ...

    def deep_copy(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.DeepCopy(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def start_monitoring_dependent(self, dependent: BaseNodeType, id: str):
        ...

    def start_monitoring_dependent(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.startMonitoringDependent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def stop_monitoring_dependent(self, dependent: BaseNodeType, id: str):
        ...

    def stop_monitoring_dependent(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.stopMonitoringDependent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_observing_nodes(self) -> Iterable[BaseNodeType]:
        ...

    def get_observing_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetObservingNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def notify_observing_nodes(self, arg: OnNodeChangeEventArgs):
        ...

    def notify_observing_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.notifyObservingNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def get_enumerator(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetEnumerator(*unwrapped)
        return _wrap(dotnet_result)

    def _custom_repr(self) -> str:
        return f"(node_path={self.node_path}, name={self.name})"


class PropertyContent(_DotNetEnum):
    """Type of specialized item that can be contained inside a single propertytype."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.PropertyContent:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for PropertyContent")

    @_staticproperty
    def K_STRING() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_STRING")
        return PropertyContent(dotnet_result, "K_STRING")

    @_staticproperty
    def K_BOOL() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BOOL")
        return PropertyContent(dotnet_result, "K_BOOL")

    @_staticproperty
    def K_I32() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I32")
        return PropertyContent(dotnet_result, "K_I32")

    @_staticproperty
    def K_U32() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U32")
        return PropertyContent(dotnet_result, "K_U32")

    @_staticproperty
    def K_DOUBLE() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DOUBLE")
        return PropertyContent(dotnet_result, "K_DOUBLE")

    @_staticproperty
    def K_U64() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U64")
        return PropertyContent(dotnet_result, "K_U64")

    @_staticproperty
    def K_VARIANT() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_VARIANT")
        return PropertyContent(dotnet_result, "K_VARIANT")

    @_staticproperty
    def K_DEPENDENTFILE() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DEPENDENTFILE")
        return PropertyContent(dotnet_result, "K_DEPENDENTFILE")

    @_staticproperty
    def K_DEPENDENTNODE() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DEPENDENTNODE")
        return PropertyContent(dotnet_result, "K_DEPENDENTNODE")

    @_staticproperty
    def K_DATASOURCENODE() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DATASOURCENODE")
        return PropertyContent(dotnet_result, "K_DATASOURCENODE")

    @_staticproperty
    def K_U16() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U16")
        return PropertyContent(dotnet_result, "K_U16")

    @_staticproperty
    def K_DBLARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DBLARR")
        return PropertyContent(dotnet_result, "K_DBLARR")

    @_staticproperty
    def K_U32_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U32ARR")
        return PropertyContent(dotnet_result, "K_U32_ARR")

    @_staticproperty
    def K_I32_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I32ARR")
        return PropertyContent(dotnet_result, "K_I32_ARR")

    @_staticproperty
    def K_STRINGARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_STRINGARR")
        return PropertyContent(dotnet_result, "K_STRINGARR")

    @_staticproperty
    def K_DICTIONARY() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DICTIONARY")
        return PropertyContent(dotnet_result, "K_DICTIONARY")

    @_staticproperty
    def K_DICTIONARYARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_DICTIONARYARR")
        return PropertyContent(dotnet_result, "K_DICTIONARYARR")

    @_staticproperty
    def K_BINARYSTRING() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BINARYSTRING")
        return PropertyContent(dotnet_result, "K_BINARYSTRING")

    @_staticproperty
    def K_I16() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I16")
        return PropertyContent(dotnet_result, "K_I16")

    @_staticproperty
    def K_I64() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I64")
        return PropertyContent(dotnet_result, "K_I64")

    @_staticproperty
    def K_BOOLARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_BOOLARR")
        return PropertyContent(dotnet_result, "K_BOOLARR")

    @_staticproperty
    def K_U64_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U64ARR")
        return PropertyContent(dotnet_result, "K_U64_ARR")

    @_staticproperty
    def K_U16_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_U16ARR")
        return PropertyContent(dotnet_result, "K_U16_ARR")

    @_staticproperty
    def K_I64_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I64ARR")
        return PropertyContent(dotnet_result, "K_I64_ARR")

    @_staticproperty
    def K_I16_ARR() -> PropertyContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.PropertyContent, "K_I16ARR")
        return PropertyContent(dotnet_result, "K_I16_ARR")


class WaveformTypeDataType(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for WaveformTypeDataType")

    @_staticproperty
    def DOUBLE() -> WaveformTypeDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType, "Double")
        return WaveformTypeDataType(dotnet_result, "DOUBLE")

    @_staticproperty
    def COMPLEX_DOUBLE() -> WaveformTypeDataType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.WaveformTypeDataType, "ComplexDouble")
        return WaveformTypeDataType(dotnet_result, "COMPLEX_DOUBLE")


class DocumentType(_DotNetBase):
    """Document class that handle serializing the document."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, filepath: str):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DocumentType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DocumentType(*unwrapped)

    @property
    def no_namespace_schema_location(self) -> str:
        dotnet_result = self._dotnet_instance.noNamespaceSchemaLocation
        return _wrap(dotnet_result)

    @no_namespace_schema_location.setter
    def no_namespace_schema_location(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.noNamespaceSchemaLocation = next(unwrapped)

    @_staticproperty
    def project_version() -> Tuple[int, int, int, int]:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.DocumentType.ProjectVersion
        return _wrap(dotnet_result)

    @_staticproperty
    def schema_uri() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.DocumentType.SchemaUri
        return _wrap(dotnet_result)

    @property
    def storage_watcher(self) -> SystemStorageWatcher:
        dotnet_result = self._dotnet_instance.StorageWatcher
        return _wrap(dotnet_result)

    @property
    def document_file_path(self) -> str:
        """Access the document file path."""
        dotnet_result = self._dotnet_instance.DocumentFilePath
        return _wrap(dotnet_result)

    @document_file_path.setter
    def document_file_path(self, value: str):
        """Access the document file path."""
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DocumentFilePath = next(unwrapped)

    @property
    def md5_checksum(self) -> str:
        dotnet_result = self._dotnet_instance.MD5Checksum
        return _wrap(dotnet_result)

    @md5_checksum.setter
    def md5_checksum(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.MD5Checksum = next(unwrapped)

    @property
    def version(self) -> VersionType:
        dotnet_result = self._dotnet_instance.Version
        return _wrap(dotnet_result)

    @version.setter
    def version(self, value: VersionType):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Version = next(unwrapped)

    @property
    def content(self) -> DocumentTypeContent:
        dotnet_result = self._dotnet_instance.Content
        return _wrap(dotnet_result)

    @content.setter
    def content(self, value: DocumentTypeContent):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Content = next(unwrapped)

    @property
    def item(self) -> BaseNodeType:
        dotnet_result = self._dotnet_instance.Item
        return _wrap(dotnet_result)

    @item.setter
    def item(self, value: BaseNodeType):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Item = next(unwrapped)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def save_system_storage_file(self) -> Tuple[bool, str]:
        ...

    @overload
    def save_system_storage_file(self, filepath: str) -> Tuple[bool, str]:
        ...

    def save_system_storage_file(self, *args):
        unwrapped = _unwrap({(): (0, ""), (str,): (1, "")}, *args)
        dotnet_result = self._dotnet_instance.SaveSystemStorageFile(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def load_system_storage_file(self, filepath: str, schemapath: str) -> Tuple[bool, str]:
        ...

    @overload
    def load_system_storage_file(self, filepath: str, schemapath: str, version_to_mutate: Sequence[XMLVersionInfo], xslst_file_paths: Sequence[str]) -> Tuple[bool, str]:
        ...

    def load_system_storage_file(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.LoadSystemStorageFile(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def load_project_xml_file(self, filepath: str) -> Tuple[bool, str, bool]:
        ...

    def load_project_xml_file(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.LoadProjectXMLFile(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def get_system_definition_file_path(project_file_path: str) -> str:
        ...

    def get_system_definition_file_path(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.DocumentType.GetSystemDefinitionFilePath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_content(self, node: BaseNodeType):
        ...

    def set_content(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetContent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_duplicate_reference(self) -> DocumentType:
        ...

    def get_duplicate_reference(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDuplicateReference(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def read_version_info(version_tag: str, file_path: str) -> XMLVersionInfo:
        ...

    def read_version_info(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.DocumentType.ReadVersionInfo(*unwrapped)
        return _wrap(dotnet_result)


class VersionType(_DotNetBase):
    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.VersionType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.VersionType(*unwrapped)

    @property
    def major(self) -> int:
        dotnet_result = self._dotnet_instance.Major
        return _wrap(dotnet_result)

    @major.setter
    def major(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Major = next(unwrapped)

    @property
    def minor(self) -> int:
        dotnet_result = self._dotnet_instance.Minor
        return _wrap(dotnet_result)

    @minor.setter
    def minor(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Minor = next(unwrapped)

    @property
    def fix(self) -> int:
        dotnet_result = self._dotnet_instance.Fix
        return _wrap(dotnet_result)

    @fix.setter
    def fix(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Fix = next(unwrapped)

    @property
    def build(self) -> int:
        dotnet_result = self._dotnet_instance.Build
        return _wrap(dotnet_result)

    @build.setter
    def build(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Build = next(unwrapped)


class DependentFilePropertyType(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DependentFilePropertyType")

    @_staticproperty
    def ABSOLUTE() -> DependentFilePropertyType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "Absolute")
        return DependentFilePropertyType(dotnet_result, "ABSOLUTE")

    @_staticproperty
    def RELATIVE() -> DependentFilePropertyType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "Relative")
        return DependentFilePropertyType(dotnet_result, "RELATIVE")

    @_staticproperty
    def TO_COMMON_DOC_DIR() -> DependentFilePropertyType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "ToCommonDocDir")
        return DependentFilePropertyType(dotnet_result, "TO_COMMON_DOC_DIR")

    @_staticproperty
    def TO_APPLICATION_DATA_DIR() -> DependentFilePropertyType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DependentFilePropertyType, "ToApplicationDataDir")
        return DependentFilePropertyType(dotnet_result, "TO_APPLICATION_DATA_DIR")


class ErrorEntry(_DotNetBase):
    """ErrorEntry represent an error on the basenodetype."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, key: str, is_error: bool, code: int, msg: str):
        ...

    @overload
    def __init__(self, to_copy: ErrorEntry):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.ErrorEntry:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ErrorEntry(*unwrapped)

    @property
    def message(self) -> str:
        dotnet_result = self._dotnet_instance.Message
        return _wrap(dotnet_result)

    @message.setter
    def message(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Message = next(unwrapped)

    @property
    def key(self) -> str:
        dotnet_result = self._dotnet_instance.Key
        return _wrap(dotnet_result)

    @key.setter
    def key(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Key = next(unwrapped)

    @property
    def is_error(self) -> bool:
        dotnet_result = self._dotnet_instance.IsError
        return _wrap(dotnet_result)

    @is_error.setter
    def is_error(self, value: bool):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.IsError = next(unwrapped)

    @property
    def code(self) -> int:
        dotnet_result = self._dotnet_instance.Code
        return _wrap(dotnet_result)

    @code.setter
    def code(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Code = next(unwrapped)

    @overload
    def clone(self) -> ErrorEntry:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def equals(self, other: ErrorEntry) -> bool:
        ...

    @overload
    def equals(self, obj: Any) -> bool:
        ...

    def equals(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Equals(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_hash_code(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetHashCode(*unwrapped)
        return _wrap(dotnet_result)


class PropertyType(_DotNetBase):
    """This class represent a single property of a BaseNodeType.
            The class contains a name of the property and the actual property value."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, to_copy: PropertyType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.PropertyType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.PropertyType(*unwrapped)

    @property
    def type(self) -> PropertyContent:
        """Akin to reflection method to return the actual property type."""
        dotnet_result = self._dotnet_instance.Type
        return _wrap(dotnet_result)

    @property
    def item(self) -> Any:
        dotnet_result = self._dotnet_instance.Item
        return _wrap(dotnet_result)

    @item.setter
    def item(self, value: Any):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Item = next(unwrapped)

    @property
    def name(self) -> str:
        dotnet_result = self._dotnet_instance.Name
        return _wrap(dotnet_result)

    @name.setter
    def name(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Name = next(unwrapped)

    @overload
    def clone(self) -> PropertyType:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)

    def _custom_repr(self) -> str:
        return f"(name={self.name})"


class NodeType(_DotNetEnum):
    """Type of actual node."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.NodeType:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for NodeType")

    @_staticproperty
    def K_BASE() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_BASE")
        return NodeType(dotnet_result, "K_BASE")

    @_staticproperty
    def K_ALIAS() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_ALIAS")
        return NodeType(dotnet_result, "K_ALIAS")

    @_staticproperty
    def K_CHANNEL() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_CHANNEL")
        return NodeType(dotnet_result, "K_CHANNEL")

    @_staticproperty
    def K_SECTION() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_SECTION")
        return NodeType(dotnet_result, "K_SECTION")

    @_staticproperty
    def K_TARGET() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_TARGET")
        return NodeType(dotnet_result, "K_TARGET")

    @_staticproperty
    def K_TARGETSECTION() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_TARGETSECTION")
        return NodeType(dotnet_result, "K_TARGETSECTION")

    @_staticproperty
    def K_ROOT() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_ROOT")
        return NodeType(dotnet_result, "K_ROOT")

    @_staticproperty
    def K_WAVEFORM() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_WAVEFORM")
        return NodeType(dotnet_result, "K_WAVEFORM")

    @_staticproperty
    def K_PARAMETER() -> NodeType:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.NodeType, "K_PARAMETER")
        return NodeType(dotnet_result, "K_PARAMETER")


class TraversalMode(_DotNetEnum):
    """Type of enumeration that is supported when we are traversing the tree of nodes."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.TraversalMode:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for TraversalMode")

    @_staticproperty
    def K_BFS() -> TraversalMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_BFS")
        return TraversalMode(dotnet_result, "K_BFS")

    @_staticproperty
    def K_DFS() -> TraversalMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_DFS")
        return TraversalMode(dotnet_result, "K_DFS")

    @_staticproperty
    def K_CHILDONLY() -> TraversalMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_CHILDONLY")
        return TraversalMode(dotnet_result, "K_CHILDONLY")

    @_staticproperty
    def K_UP() -> TraversalMode:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.TraversalMode, "K_UP")
        return TraversalMode(dotnet_result, "K_UP")


class ITraverseNodeFilter(_DotNetBase):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.ITraverseNodeFilter:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for ITraverseNodeFilter")

    @overload
    def check_with_filter(self, node: BaseNodeType) -> bool:
        ...

    def check_with_filter(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.CheckWithFilter(*unwrapped)
        return _wrap(dotnet_result)


class IVisitor(_DotNetBase):
    """For every type element in the tree declare a visit function for it."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.IVisitor:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IVisitor")

    @overload
    def visit(self, element: BaseNodeType):
        ...

    @overload
    def visit(self, element: ChannelType):
        ...

    @overload
    def visit(self, element: SectionType):
        ...

    @overload
    def visit(self, element: AliasType):
        ...

    @overload
    def visit(self, element: ParameterType):
        ...

    @overload
    def visit(self, element: TargetType):
        ...

    @overload
    def visit(self, element: RootType):
        ...

    @overload
    def visit(self, element: TargetSectionsType):
        ...

    def visit(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Visit(*unwrapped)
        return _wrap(dotnet_result)


class IVisitorWithInspection(_DotNetBase):
    """For every type element in the tree declare a visit function for it.
             This is a variant of the visitor function where we allow an object
             to be returned by the visitor class so the caller can do some post-processing
             based on the object value.
             This allows postwalk operation on the tree."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.IVisitorWithInspection:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IVisitorWithInspection")

    @overload
    def visit(self, element: BaseNodeType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: ChannelType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: SectionType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: AliasType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: ParameterType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: TargetType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: RootType) -> IInspectorResult:
        ...

    @overload
    def visit(self, element: TargetSectionsType) -> IInspectorResult:
        ...

    def visit(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Visit(*unwrapped)
        return _wrap(dotnet_result)


class IInspectorResult(_DotNetBase):
    """The generic return value that the IVisitorWithInspection support."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.IInspectorResult:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for IInspectorResult")

    @overload
    def result(self) -> Any:
        ...

    def result(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Result(*unwrapped)
        return _wrap(dotnet_result)


class RootType(BaseNodeType):
    """Specialized class that denotes a root of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: RootType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.RootType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.RootType(*unwrapped)

    @property
    def target_sections(self) -> TargetSectionsType:
        dotnet_result = self._dotnet_instance.TargetSections
        return _wrap(dotnet_result)

    @target_sections.setter
    def target_sections(self, value: TargetSectionsType):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.TargetSections = next(unwrapped)

    @property
    def section(self) -> Sequence[SectionType]:
        dotnet_result = self._dotnet_instance.Section
        return _wrap(dotnet_result)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Section = next(unwrapped)

    @overload
    def get_owning_document_file_path(self) -> str:
        ...

    def get_owning_document_file_path(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetOwningDocumentFilePath(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def refresh_node_dependencies(self):
        ...

    def refresh_node_dependencies(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RefreshNodeDependencies(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def set_target_section(self, new_target_section: TargetSectionsType) -> bool:
        ...

    @overload
    def set_target_section(self, new_target_section: TargetSectionsType, relink: bool) -> bool:
        ...

    def set_target_section(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SetTargetSection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleSectionType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)


class BaseCustomNodeProperty(_DotNetBase):
    """Base Class for Property Type that encapsulate basic data type. This
            allow for the class to automatically register the owning BaseNodeType
            to changes that happened to the encapsulated data type."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, to_copy: BaseCustomNodeProperty):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.BaseCustomNodeProperty:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.BaseCustomNodeProperty(*unwrapped)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def clone(self) -> BaseCustomNodeProperty:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)


class DictionaryProperty(BaseCustomNodeProperty):
    """Dictionary property implementation implement cloneable so we can clone property savely."""

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, to_copy: DictionaryProperty):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DictionaryProperty:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DictionaryProperty(*unwrapped)

    @property
    def count(self) -> int:
        dotnet_result = self._dotnet_instance.Count
        return _wrap(dotnet_result)

    @property
    def elem(self) -> Sequence[DictionaryElement]:
        dotnet_result = self._dotnet_instance.Elem
        return _wrap(dotnet_result)

    @elem.setter
    def elem(self, value: Sequence[DictionaryElement]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Elem = next(unwrapped)

    @overload
    def clear(self):
        ...

    def clear(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clear(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def remove_element(self, key: str) -> bool:
        ...

    def remove_element(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.RemoveElement(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_string(self, name: str, value: str) -> bool:
        ...

    def add_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_boolean(self, name: str, value: bool) -> bool:
        ...

    def add_boolean(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddBoolean(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i32(self, name: str, value: int) -> bool:
        ...

    def add_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i16(self, name: str, value: int) -> bool:
        ...

    def add_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_i64(self, name: str, value: int) -> bool:
        ...

    def add_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u32(self, name: str, value: int) -> bool:
        ...

    def add_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u16(self, name: str, value: int) -> bool:
        ...

    def add_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_double(self, name: str, value: float) -> bool:
        ...

    def add_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_u64(self, name: str, value: int) -> bool:
        ...

    def add_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_double(self, name: str, value: Sequence[float]) -> bool:
        ...

    def add_arr_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_boolean(self, name: str, value: Sequence[bool]) -> bool:
        ...

    def add_arr_boolean(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrBoolean(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_u64(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_u32(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_u16(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_i64(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_i32(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_i16(self, name: str, value: Sequence[int]) -> bool:
        ...

    def add_arr_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_arr_string(self, name: str, value: Sequence[str]) -> bool:
        ...

    def add_arr_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddArrString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_string(self, name: str) -> Tuple[bool, str]:
        ...

    def get_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetString(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_bool(self, name: str) -> Tuple[bool, bool]:
        ...

    def get_bool(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetBool(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_i64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u32(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u16(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_double(self, name: str) -> Tuple[bool, float]:
        ...

    def get_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_u64(self, name: str) -> Tuple[bool, int]:
        ...

    def get_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_double(self, name: str) -> Tuple[bool, Sequence[float]]:
        ...

    def get_arr_double(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrDouble(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_boolean(self, name: str) -> Tuple[bool, Sequence[bool]]:
        ...

    def get_arr_boolean(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrBoolean(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_u64(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrU64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_u32(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrU32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_u16(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_u16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrU16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_i64(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i64(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrI64(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_i32(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i32(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrI32(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_i16(self, name: str) -> Tuple[bool, Sequence[int]]:
        ...

    def get_arr_i16(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrI16(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_arr_string(self, name: str) -> Tuple[bool, Sequence[str]]:
        ...

    def get_arr_string(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetArrString(*unwrapped)
        return _wrap(dotnet_result)


class OnNodeChangeEventArgs(_DotNetBase):
    """Event data that get send when the node change argument is fired."""

    @overload
    def __init__(self, action: str, data: Sequence[int]):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs(*unwrapped)

    @_staticproperty
    def k_deleted() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_DELETED
        return _wrap(dotnet_result)

    @_staticproperty
    def k_error() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_ERROR
        return _wrap(dotnet_result)

    @_staticproperty
    def k_no_error() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_NO_ERROR
        return _wrap(dotnet_result)

    @_staticproperty
    def k_property_changed() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_PROPERTY_CHANGED
        return _wrap(dotnet_result)

    @_staticproperty
    def k_collection_changed() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.OnNodeChangeEventArgs.K_COLLECTION_CHANGED
        return _wrap(dotnet_result)

    @property
    def m_action(self) -> str:
        """public field to access the action"""
        dotnet_result = self._dotnet_instance.m_action
        return _wrap(dotnet_result)

    @property
    def m_data(self) -> Sequence[int]:
        """public field to access the generic data field."""
        dotnet_result = self._dotnet_instance.m_data
        return _wrap(dotnet_result)


class ChannelType(BaseNodeType):
    """Specialized class to denote the channel type of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: ChannelType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.ChannelType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ChannelType(*unwrapped)

    @property
    def is_readable(self) -> bool:
        """field to indicate if channel is readable"""
        dotnet_result = self._dotnet_instance.IsReadable
        return _wrap(dotnet_result)

    @property
    def is_writable(self) -> bool:
        """field to indicate if channel is writable"""
        dotnet_result = self._dotnet_instance.IsWritable
        return _wrap(dotnet_result)

    @property
    def is_faultable(self) -> bool:
        """field to indicate if channel is faultable"""
        dotnet_result = self._dotnet_instance.IsFaultable
        return _wrap(dotnet_result)

    @property
    def is_scalable(self) -> bool:
        """field to indicate if channel is scalable"""
        dotnet_result = self._dotnet_instance.IsScalable
        return _wrap(dotnet_result)

    @property
    def data_length(self) -> int:
        """return the data length of the channel."""
        dotnet_result = self._dotnet_instance.DataLength
        return _wrap(dotnet_result)

    @property
    def default_value(self) -> Sequence[float]:
        dotnet_result = self._dotnet_instance.DefaultValue
        return _wrap(dotnet_result)

    @default_value.setter
    def default_value(self, value: Sequence[float]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DefaultValue = next(unwrapped)

    @property
    def row_dim(self) -> int:
        dotnet_result = self._dotnet_instance.RowDim
        return _wrap(dotnet_result)

    @row_dim.setter
    def row_dim(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RowDim = next(unwrapped)

    @property
    def col_dim(self) -> int:
        dotnet_result = self._dotnet_instance.ColDim
        return _wrap(dotnet_result)

    @col_dim.setter
    def col_dim(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ColDim = next(unwrapped)

    @property
    def units(self) -> str:
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)

    @units.setter
    def units(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Units = next(unwrapped)

    @property
    def bit_fields(self) -> int:
        dotnet_result = self._dotnet_instance.BitFields
        return _wrap(dotnet_result)

    @bit_fields.setter
    def bit_fields(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.BitFields = next(unwrapped)

    @overload
    def is_under_target(self, target_to_check: TargetType) -> bool:
        ...

    def is_under_target(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsUnderTarget(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def get_value_table(channel: ChannelType) -> Tuple[bool, Sequence[str], Sequence[float]]:
        ...

    def get_value_table(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.ChannelType.GetValueTable(*unwrapped)
        return _wrap(dotnet_result)

    @staticmethod
    @overload
    def set_value_table(channel: ChannelType, names: Sequence[str], values: Sequence[float]):
        ...

    def set_value_table(*args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.ChannelType.SetValueTable(*unwrapped)
        return _wrap(dotnet_result)


class SystemStorageWatcher(_DotNetBase):
    """Public class to abstract the actual watcher node internals."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.SystemStorageWatcher:
            self._dotnet_instance = args[0]
        else:
            raise ValueError("No instance constructor for SystemStorageWatcher")

    @_staticproperty
    def k_system_storage_watcher_dependentid() -> str:
        dotnet_result = NationalInstruments.VeriStand.SystemStorage.SystemStorageWatcher.K_SYSTEM_STORAGE_WATCHER_DEPENDENTID
        return _wrap(dotnet_result)

    @property
    def error_count(self) -> int:
        """Gets the current error count"""
        dotnet_result = self._dotnet_instance.ErrorCount
        return _wrap(dotnet_result)

    @property
    def has_modification(self) -> bool:
        dotnet_result = self._dotnet_instance.HasModification
        return _wrap(dotnet_result)

    @property
    def error_in_system(self) -> Sequence[BaseNodeType]:
        dotnet_result = self._dotnet_instance.ErrorInSystem
        return _wrap(dotnet_result)

    @property
    def has_any_error(self) -> bool:
        dotnet_result = self._dotnet_instance.HasAnyError
        return _wrap(dotnet_result)

    @overload
    def reset_modification_flag(self):
        ...

    def reset_modification_flag(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ResetModificationFlag(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def fire_count_event(self):
        ...

    def fire_count_event(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.FireCountEvent(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def supress_notification(self):
        ...

    def supress_notification(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.SupressNotification(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def unsupress_notification(self):
        ...

    def unsupress_notification(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.UnsupressNotification(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def is_node_in_error_collection(self, node: BaseNodeType) -> bool:
        ...

    def is_node_in_error_collection(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.IsNodeInErrorCollection(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def dispose(self):
        ...

    def dispose(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Dispose(*unwrapped)
        return _wrap(dotnet_result)


class DocumentTypeContent(_DotNetEnum):
    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DocumentTypeContent")

    @_staticproperty
    def DEFINITION() -> DocumentTypeContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "Definition")
        return DocumentTypeContent(dotnet_result, "DEFINITION")

    @_staticproperty
    def EXPORT() -> DocumentTypeContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "Export")
        return DocumentTypeContent(dotnet_result, "EXPORT")

    @_staticproperty
    def SLSC() -> DocumentTypeContent:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DocumentTypeContent, "SLSC")
        return DocumentTypeContent(dotnet_result, "SLSC")


class SectionType(BaseNodeType):
    """Specialized node that implement Section"""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: SectionType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.SectionType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.SectionType(*unwrapped)

    @property
    def section(self) -> Sequence[SectionType]:
        dotnet_result = self._dotnet_instance.Section
        return _wrap(dotnet_result)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Section = next(unwrapped)

    @property
    def channel(self) -> Sequence[ChannelType]:
        dotnet_result = self._dotnet_instance.Channel
        return _wrap(dotnet_result)

    @channel.setter
    def channel(self, value: Sequence[ChannelType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Channel = next(unwrapped)

    @property
    def alias(self) -> Sequence[AliasType]:
        dotnet_result = self._dotnet_instance.Alias
        return _wrap(dotnet_result)

    @alias.setter
    def alias(self, value: Sequence[AliasType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Alias = next(unwrapped)

    @property
    def parameter(self) -> Sequence[ParameterType]:
        dotnet_result = self._dotnet_instance.Parameter
        return _wrap(dotnet_result)

    @parameter.setter
    def parameter(self, value: Sequence[ParameterType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Parameter = next(unwrapped)

    @property
    def waveform(self) -> Sequence[WaveformType]:
        dotnet_result = self._dotnet_instance.Waveform
        return _wrap(dotnet_result)

    @waveform.setter
    def waveform(self, value: Sequence[WaveformType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Waveform = next(unwrapped)

    @overload
    def attached_child_node_without_check(self, node: BaseNodeType):
        ...

    def attached_child_node_without_check(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AttachedChildNodeWithoutCheck(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleSectionType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_channel_type(self, new_nodes: Sequence[ChannelType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_channel_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleChannelType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_channel_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_channel_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderChannelTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_channel_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_channel_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetChannelTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_alias_type(self, new_nodes: Sequence[AliasType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_alias_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleAliasType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_alias_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_alias_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderAliasTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_alias_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_alias_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetAliasTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_parameter_type(self, new_nodes: Sequence[ParameterType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_parameter_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleParameterType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_parameter_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_parameter_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderParameterTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_parameter_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_parameter_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetParameterTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def add_multiple_waveform_type(self, new_nodes: Sequence[WaveformType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_waveform_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleWaveformType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_waveform_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_waveform_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderWaveformTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_waveform_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_waveform_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetWaveformTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)


class AliasType(BaseNodeType):
    """Specialized class to denote the alias type of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: AliasType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.AliasType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.AliasType(*unwrapped)

    @property
    def resolve_alias_reference(self) -> BaseNodeType:
        """Gets the referenced channel."""
        dotnet_result = self._dotnet_instance.ResolveAliasReference
        return _wrap(dotnet_result)


class ParameterType(BaseNodeType):
    """Specialized class to denote the parameter type of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: ParameterType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.ParameterType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.ParameterType(*unwrapped)

    @property
    def row_dim(self) -> int:
        dotnet_result = self._dotnet_instance.RowDim
        return _wrap(dotnet_result)

    @row_dim.setter
    def row_dim(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.RowDim = next(unwrapped)

    @property
    def col_dim(self) -> int:
        dotnet_result = self._dotnet_instance.ColDim
        return _wrap(dotnet_result)

    @col_dim.setter
    def col_dim(self, value: int):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.ColDim = next(unwrapped)


class TargetType(BaseNodeType):
    """Specialized node that implement Target"""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: TargetType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.TargetType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.TargetType(*unwrapped)

    @property
    def dfs_object_enumerator(self) -> System.Collections.IEnumerator:
        """Return a non generic Depth First Search enumerator. This enumerator iterates into the hiearchy of the
            first children it found."""
        dotnet_result = self._dotnet_instance.DFSObjectEnumerator
        return _wrap(dotnet_result)

    @property
    def section(self) -> Sequence[SectionType]:
        dotnet_result = self._dotnet_instance.Section
        return _wrap(dotnet_result)

    @section.setter
    def section(self, value: Sequence[SectionType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Section = next(unwrapped)

    @overload
    def add_multiple_section_type(self, new_nodes: Sequence[SectionType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_section_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleSectionType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_section_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_section_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_section_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetSectionTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)


class TargetSectionsType(BaseNodeType):
    """Specialized node that implement TargetSections"""

    @overload
    def __init__(self, node_name: str, type_guid: str):
        ...

    @overload
    def __init__(self, to_copy: TargetSectionsType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.TargetSectionsType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.TargetSectionsType(*unwrapped)

    @property
    def target(self) -> Sequence[TargetType]:
        dotnet_result = self._dotnet_instance.Target
        return _wrap(dotnet_result)

    @target.setter
    def target(self, value: Sequence[TargetType]):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Target = next(unwrapped)

    @overload
    def add_multiple_target_type(self, new_nodes: Sequence[TargetType], op: DuplicateOp) -> bool:
        ...

    def add_multiple_target_type(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.AddMultipleTargetType(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def reorder_target_type_child_nodes(self, ordered_list: Sequence[BaseNodeType]) -> bool:
        ...

    def reorder_target_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.ReorderTargetTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)

    @overload
    def get_target_type_child_nodes(self) -> Sequence[BaseNodeType]:
        ...

    def get_target_type_child_nodes(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.GetTargetTypeChildNodes(*unwrapped)
        return _wrap(dotnet_result)


class DuplicateOp(_DotNetEnum):
    """Operations possible when adding nodes and duplicates are found."""

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len in [1,2] and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DuplicateOp:
            self._dotnet_instance = args[0]
            self._py_field_name = args[1] if args_len == 2 else ""
        else:
            raise ValueError("No instance constructor for DuplicateOp")

    @_staticproperty
    def ASSERT() -> DuplicateOp:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "Assert")
        return DuplicateOp(dotnet_result, "ASSERT")

    @_staticproperty
    def RENAME() -> DuplicateOp:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "Rename")
        return DuplicateOp(dotnet_result, "RENAME")

    @_staticproperty
    def UNIQUE_ONLY() -> DuplicateOp:
        dotnet_result = getattr(NationalInstruments.VeriStand.SystemStorage.DuplicateOp, "UniqueOnly")
        return DuplicateOp(dotnet_result, "UNIQUE_ONLY")


class DictionaryElement(_DotNetBase):
    """Dictionary Element implementation implement cloneable so we can clone Dictionary Element savely."""

    @overload
    def __init__(self, to_copy: DictionaryElement):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.DictionaryElement:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.DictionaryElement(*unwrapped)

    @property
    def item(self) -> Any:
        dotnet_result = self._dotnet_instance.Item
        return _wrap(dotnet_result)

    @item.setter
    def item(self, value: Any):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Item = next(unwrapped)

    @property
    def key(self) -> str:
        dotnet_result = self._dotnet_instance.Key
        return _wrap(dotnet_result)

    @key.setter
    def key(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Key = next(unwrapped)

    @overload
    def clone(self) -> DictionaryElement:
        ...

    def clone(self, *args):
        unwrapped = _unwrap(None, *args)
        dotnet_result = self._dotnet_instance.Clone(*unwrapped)
        return _wrap(dotnet_result)


class WaveformType(BaseNodeType):
    """Specialized class to denote the waveform type of the tree storage."""

    @overload
    def __init__(self, node_name: str, type_guid: str, data_type: WaveformTypeDataType):
        ...

    @overload
    def __init__(self, to_copy: WaveformType):
        ...

    def __init__(self, *args):
        """Create a new instance."""
        args_len = len(args)
        if args_len == 1 and type(args[0]) == NationalInstruments.VeriStand.SystemStorage.WaveformType:
            self._dotnet_instance = args[0]
        else:
            unwrapped = _unwrap(None, *args)
            self._dotnet_instance = NationalInstruments.VeriStand.SystemStorage.WaveformType(*unwrapped)

    @property
    def data_type(self) -> WaveformTypeDataType:
        dotnet_result = self._dotnet_instance.DataType
        return _wrap(dotnet_result)

    @data_type.setter
    def data_type(self, value: WaveformTypeDataType):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.DataType = next(unwrapped)

    @property
    def units(self) -> str:
        dotnet_result = self._dotnet_instance.Units
        return _wrap(dotnet_result)

    @units.setter
    def units(self, value: str):
        unwrapped = _unwrap(None, value)
        self._dotnet_instance.Units = next(unwrapped)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/README.md sha256=dcbb0f2478c883b5b41ba8eaede663afb9d4e5ce5ea41f984afce1286b414d13 bytes=493 -->
## FILE: tests/legacy/README.md

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/README.md`
- sha256: `dcbb0f2478c883b5b41ba8eaede663afb9d4e5ce5ea41f984afce1286b414d13`
- bytes: 493

````markdown
## How to test the Legacy API with these tests:

1. Install **VeriStand 2020 R6** or older (newer versions will fail some of the tests because the models used in them were deprecated)
2. call `pytest tests/legacy` on the `main` directory (or just `pytest` on the `tests/legacy` directory)
3. Some of the tests open VeriStand if not already opened, but other tests do not, so if you are running a subtest of the tests, you'll need to have VeriStand running (but nothing should be deployed).
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_alarm2_api.py sha256=a51bbef1df5c3bf0d2e0d6e6b490b1ca46e599bcc5b45f1bbd0767ff0ed85934 bytes=5023 -->
## FILE: tests/legacy/test_legacy_alarm2_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_alarm2_api.py`
- sha256: `a51bbef1df5c3bf0d2e0d6e6b490b1ca46e599bcc5b45f1bbd0767ff0ed85934`
- bytes: 5023

````python
import os
import time

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
import pytest

TEST_ID = 12234


def test_alarm2_api():
    # Ensures NI VeriStand is running.
    NIVeriStand.LaunchNIVeriStand()
    NIVeriStand.WaitForNIVeriStandReady()
    workspace = NIVeriStand.Workspace2("localhost")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\TestAlarmAPI\TestAlarmAPI.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.ConnectToSystem(system_definition, True, 20000)

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        print("Testing Alarm manager Get Alarm List")
        alarmMgr = NIVeriStand.AlarmManager2("localhost")
        result = alarmMgr.GetAlarmList("Controller")
        assert len(result) == 3, "Expected 3 alarms returned from the system"

        with pytest.raises(NIVeriStandException):
            alarmMgr.GetAlarmList("Invalid Controller")

        print("Testing Alarm manager Read Alarm Data")
        alarms = ("Alarm Group/AlarmTest1", "Alarm Group/AlarmTest2", "ConstantBoundAlarm")
        result = alarmMgr.GetMultipleAlarmsData("Controller", alarms, 60000)
        print("Verifying alarm data returned")
        assert len(result) == 3, "Expected to get 3 alarms data back"

        with pytest.raises(NIVeriStandException):
            alarmMgr.GetMultipleAlarmsData("INVALID CONTROLLER", alarms, 60000)

        print("Verifying Alarm Data")
        alarmTest1 = result[0]
        constantBoundAlarm = result[2]
        print(alarmTest1)
        assert (
            alarmTest1["WatchChannel"] == r"Aliases/AlarmChannel1"
        ), "Fail to confirm alarm channel"
        assert (alarmTest1["HighLimitIsConstant"] == 0) or (
            alarmTest1["HighLimitChannel"] == r"AlarmChannel1High"
        ), "Fail to confirm high limit"
        assert (alarmTest1["LowLimitIsConstant"] == 0) or (
            alarmTest1["LowLimitChannel"] == r"AlarmChannel1Low"
        ), "Fail to confirm low limit"
        assert alarmTest1["DelayDuration"] == 0.5, "Fail to confirm delay duration"
        assert alarmTest1["ProcedureName"] == r"ResetAlarmTest1", "Fail to confirm procedure"
        assert alarmTest1["Priority"] == 2, "Fail to confirm priority (deprecated)"
        assert alarmTest1["PriorityNumber"] == 5, "Fail to confirm priority number"
        assert alarmTest1["State"] == 1, "Fail to confirm state"
        assert alarmTest1["Mode"] == 0, "Fail to confirm mode"
        assert alarmTest1["GroupNumber"] == 1, "Fail to confirm alarm group"

        BoundAlarmRef = NIVeriStand.Alarm("ConstantBoundAlarm", "Controller", "localhost")
        result = BoundAlarmRef.GetAlarmData(30000)
        assert (
            result == constantBoundAlarm
        ), "Alarm data from alarm interface differ from alarm manager"

        print("Test modifying alarm data")
        modAlarmData = result
        modAlarmData["HighLimit"] = 3
        modAlarmData["LowLimit"] = -3
        BoundAlarmRef.SetAlarmData2(modAlarmData)
        time.sleep(1)
        result = BoundAlarmRef.GetAlarmData(30000)
        assert result == modAlarmData, "Alarm data set cannot be confirmed"

        print("Test modifying alarm state and mode")
        BoundAlarmRef.SetEnabledState(0)
        # indicate only
        BoundAlarmRef.SetAlarmMode(1)
        time.sleep(1)

        result = BoundAlarmRef.GetAlarmData(30000)
        assert result["State"] == 0, "Alarm Mode is wrong"

        assert result["Mode"] == 1, "Alarm Mode is wrong"

        BoundAlarmRef.SetEnabledState(1)
        BoundAlarmRef.SetAlarmMode(0)
        time.sleep(2)
        workspace.SetSingleChannelValue(r"Controller/User Channel/AlarmChannel1", 20)
        workspace.SetSingleChannelValue(r"Controller/User Channel/AlarmChannel2", 10)
        time.sleep(2)

        print("Testing alarm mutual exclusion within a group")
        AlarmTest2Ref = NIVeriStand.Alarm("Alarm Group/AlarmTest2")
        AlarmTest1Ref = NIVeriStand.Alarm("Alarm Group/AlarmTest1")
        result = AlarmTest1Ref.GetAlarmData(30000)
        result2 = AlarmTest2Ref.GetAlarmData(30000)
        assert result["State"] == 2, "Alarm should be tripped"
        assert (
            result2["State"] != 2
        ), "Alarm should not be running due to an execution of a higher priority."

        # print("Testing Alarm Execution Across Groups")
        # result = BoundAlarmRef.GetAlarmData(30000)
        # result2 = AlarmTest2Ref.GetAlarmData(30000)
        # assert ((result['State'] == 2) and (result2['State'] == 2)), " Two alarms should be tripped simulteneously."

        print("Test PASSED")
        print("")
    finally:
        workspace.DisconnectFromSystem("", True)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_alarm_api.py sha256=ecb9300e666eeacaeaab93c34972bbed2fca2d141e4b351c3328cefea486e177 bytes=5349 -->
## FILE: tests/legacy/test_legacy_alarm_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_alarm_api.py`
- sha256: `ecb9300e666eeacaeaab93c34972bbed2fca2d141e4b351c3328cefea486e177`
- bytes: 5349

````python
import os
import time

from niveristand.legacy import NIVeriStand

TEST_ID = 12234


def test_alarm_api():
    workspace = NIVeriStand.Workspace()
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\TestAlarmAPI\TestAlarmAPI.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        print("Testing Alarm manager functionality")
        alarmMgr = NIVeriStand.AlarmManager()
        result = alarmMgr.GetAlarmList()
        assert len(result) == 3, "Expected 3 alarms returned from the system"

        print("Testing support for deprecated GetAlarmStatus() function")
        result = alarmMgr.GetAlarmsStatus()
        print(result)
        assert result["HighAlarm"] == 0, "Not expecting any alarm to be trigger"
        assert result["MediumAlarm"] == 0, "Not expecting any alarm to be trigger"
        assert result["LowAlarm"] == 0, "Not expecting any alarm to be trigger"

        print("Testing Read Alarm Data")
        alarms = ("Alarm Group/AlarmTest1", "Alarm Group/AlarmTest2", "ConstantBoundAlarm")
        result = alarmMgr.GetMultipleAlarmsData(alarms, 60000)
        print("Verifying alarm data returned")
        assert len(result) == 3, "Expected to get 3 alarms data back"

        print("Verifying Alarm Data")
        alarmTest1 = result[0]
        constantBoundAlarm = result[2]
        print(alarmTest1)
        # assert (alarmTest1['WatchChannel'] == r"AlarmChannel1"), "Fail to confirm alarm channel"
        assert (alarmTest1["HighLimitIsConstant"] == 0) | (
            alarmTest1["HighLimitChannel"] == r"AlarmChannel1High"
        ), "Fail to confirm high limit"
        assert (alarmTest1["LowLimitIsConstant"] == 0) | (
            alarmTest1["LowLimitChannel"] == r"AlarmChannel1Low"
        ), "Fail to confirm low limit"
        assert alarmTest1["DelayDuration"] == 0.5, "Fail to confirm delay duration"
        assert alarmTest1["ProcedureName"] == r"ResetAlarmTest1", "Fail to confirm procedure"
        assert alarmTest1["Priority"] == 2, "Fail to confirm priority enum (deprecated)"
        # TODO: PriorityNumber not found key
        assert alarmTest1["PriorityNumber"] == 5, "Fail to confirm priority number"
        assert alarmTest1["State"] == 1, "Fail to confirm state"
        assert alarmTest1["Mode"] == 0, "Fail to confirm mode"
        # TODO: GroupNumber not found key
        assert alarmTest1["GroupNumber"] == 1, "Fail to confirm group number"

        print("Test alarm interface")
        BoundAlarmRef = NIVeriStand.Alarm("ConstantBoundAlarm")
        result = BoundAlarmRef.GetAlarmData(30000)
        assert (
            result == constantBoundAlarm
        ), "Alarm data from alarm interface differ from alarm manager"

        print("Test modifying alarm data")
        modAlarmData = result
        modAlarmData["HighLimit"] = 3
        modAlarmData["LowLimit"] = -3

        print("Testing support for deprecated SetAlarmData() function")
        BoundAlarmRef.SetAlarmData(modAlarmData)
        time.sleep(1)
        result = BoundAlarmRef.GetAlarmData(30000)
        assert result == modAlarmData, "Alarm data set cannot be confirmed on deprecated function"

        # TODO: SetAlarmData2 not implemented.
        print("Testing support using SetAlarmData2() function")
        BoundAlarmRef.SetAlarmData2(modAlarmData)
        time.sleep(1)
        result = BoundAlarmRef.GetAlarmData(30000)
        assert result == modAlarmData, "Alarm data set cannot be confirmed on function"

        print("Test modifying alarm state and mode")
        BoundAlarmRef.SetEnabledState(0)
        # indicate only
        BoundAlarmRef.SetAlarmMode(1)
        time.sleep(1)

        result = BoundAlarmRef.GetAlarmData(30000)
        assert result["State"] == 0, "Alarm Mode is wrong"

        assert result["Mode"] == 1, "Alarm Mode is wrong"

        BoundAlarmRef.SetEnabledState(1)
        BoundAlarmRef.SetAlarmMode(0)
        time.sleep(2)
        workspace.SetSingleChannelValue(r"Controller/User Channel/AlarmChannel1", 20)
        workspace.SetSingleChannelValue(r"Controller/User Channel/AlarmChannel2", 10)
        time.sleep(2)

        print("Testing alarm mutual exclusion within a group")
        AlarmTest2Ref = NIVeriStand.Alarm("Alarm Group/AlarmTest2")
        AlarmTest1Ref = NIVeriStand.Alarm("Alarm Group/AlarmTest1")
        result = AlarmTest1Ref.GetAlarmData(30000)
        result2 = AlarmTest2Ref.GetAlarmData(30000)
        assert result["State"] == 2, "Alarm should be tripped"
        assert (
            result2["State"] != 2
        ), "Alarm should not be running due to an execution of a higher priority."

        # print("Testing Alarm Execution Across Groups")
        # result = BoundAlarmRef.GetAlarmData(30000)
        # result2 = AlarmTest2Ref.GetAlarmData(30000)
        # assert ((result['State'] == 2) and (result2['State'] == 2)), " Two alarms should be tripped simulteneously."

        print("Test PASSED")

    finally:
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_calc_channel.py sha256=d603801820e10796d7b35ee28e9e166eb932924123f8c070f816a959db13e4a6 bytes=5534 -->
## FILE: tests/legacy/test_legacy_calc_channel.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_calc_channel.py`
- sha256: `d603801820e10796d7b35ee28e9e166eb932924123f8c070f816a959db13e4a6`
- bytes: 5534

````python
import os
import time

from niveristand.legacy import NIVeriStand


def test_calculated_channel_legacy():
    TEST_ID = 1112
    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(
        os.getcwd(),
        r"tests\testutilities\legacy_files\CalculatedChannelTest\CalculatedChannelTest.nivssdf",
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        print("Checking Get Constant")
        channels = ("MaxConstant", "MinConstant")
        expectedResults = [5, -5]
        results = workspace.GetMultipleChannelValues(channels)
        for i in range(0, len(expectedResults)):
            assert (
                results[i] == expectedResults[i]
            ), "%s Expected %f Return Value %f not expected" % (
                channels[i],
                expectedResults[i],
                results[i],
            )

        print("Checking Max Min Mode")
        channels = ("MaxUV1", "MaxUV2", "MinUV1", "MinUV2")
        channelsValues = (-1000, -1000.1, 1000, 1000.1)
        workspace.SetMultipleChannelValues(channels, channelsValues)
        time.sleep(1)
        # verifying the value get set on these channels
        results = workspace.GetMultipleChannelValues(channels)
        for i in range(0, len(results)):
            assert (
                results[i] == channelsValues[i]
            ), "%s Expected %f Return Value %f not expected" % (
                channels[i],
                channelsValues[i],
                results[i],
            )
        # verifying the new max min value is correct
        outchannels = (
            "MaxUV1ToConstVal5",
            "MaxUV2ToConstVal10",
            "MinUV1ToConstVal2",
            "MinUV2ToConstVal3",
            "Max2Var",
            "Min2Var",
        )
        expectedResults = [5, 10, 2, 3, -1000, 1000]
        results = workspace.GetMultipleChannelValues(outchannels)
        for i in range(0, len(expectedResults)):
            assert (
                results[i] == expectedResults[i]
            ), "%s Expected %f Return Value %f not expected" % (
                outchannels[i],
                expectedResults[i],
                results[i],
            )
        # verifying that the new max min value take the value of the variable.
        channelsValues = (10, 15, 1, -1)
        workspace.SetMultipleChannelValues(channels, channelsValues)
        time.sleep(1)
        results = workspace.GetMultipleChannelValues(outchannels)
        expectedResults = [10, 15, 1, -1, 15, -1]
        for i in range(0, len(expectedResults)):
            assert (
                results[i] == expectedResults[i]
            ), "%s Expected %f Return Value %f values not expected" % (
                outchannels[i],
                expectedResults[i],
                results[i],
            )

        print("Checking Acceleration Mode - assuming delta T for low priority loop is .2")
        channels = (
            "AccelerationOnDistanceChannel",
            "VelocityChan",
            "DistanceChannel",
            "VelocityChanPrevIteration",
            "DistanceChannelPrevIteration",
        )
        results = workspace.GetMultipleChannelValues(channels)
        accelerationCalculated = round((results[1] - results[3]) / 0.2)
        assert accelerationCalculated == round(
            results[0]
        ), "%s Expected %f Return Value %f value not expected" % (
            channels[0],
            accelerationCalculated,
            results[0],
        )

        print("Computing velocity")
        velocityCalculated = round((results[2] - results[4]) / 0.2)
        assert velocityCalculated == round(
            results[1]
        ), "%s Expected %f Return Value %f value not expected" % (
            channels[1],
            velocityCalculated,
            results[1],
        )

        print("Checking Averaging Mode")
        # Get a list of the last 6 points.  if we take a sum of the complete 3 elements
        # we are bound to find the correct average.
        channels = (
            "3PointAverager",
            "ChanToAverage",
            "ChanToAverageMin1Step",
            "ChanToAverageMin2Step",
            "ChanToAverageMin3Step",
            "ChanToAverageMin4Step",
            "ChanToAverageMin5Step",
            "ChanToAverageMin6Step",
        )
        results = workspace.GetMultipleChannelValues(channels)

        i = 0
        for channel in channels:
            print(("%s value is %f" % (channel, round(results[i], 3))))
            i = i + 1

        possibleAverages = []
        for i in range(0, 4):
            temp = 0
            for y in range(0, 3):
                temp = temp + results[1 + i + y]
            possibleAverages.append(temp / 3)

        found = 0
        for potentialAverage in possibleAverages:
            print(("Potential Averages %f" % round(potentialAverage, 3)))
            if round(potentialAverage, 3) == round(results[0], 3):
                found = 1

        assert found == 1, "Fail to auto check averaging module"

        print("Test PASSED")

    finally:
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_calc_channel_formula.py sha256=ed5ab38a6e8ee4fe80b4fca1ff402a1ca9f143cb73ae42f92dd765004e00c960 bytes=12338 -->
## FILE: tests/legacy/test_legacy_calc_channel_formula.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_calc_channel_formula.py`
- sha256: `ed5ab38a6e8ee4fe80b4fca1ff402a1ca9f143cb73ae42f92dd765004e00c960`
- bytes: 12338

````python
import math
import os
import time

from niveristand.legacy import NIVeriStand


def test_calculated_channel_formula_legacy():
    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(
        os.getcwd(),
        r"tests\testutilities\legacy_files\CalcChanFormulaTest\CalcChanFormulaTest.nivssdf",
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        # Compute Machine Epsilon: The smallest floating point number when
        # added to one is greater than one.

        eps = 1.0
        while (1.0 + eps) > 1.0:
            epsLast = eps
            eps = eps / 2.0
        eps = epsLast
        print("Machine Epsilon = %g" % (eps))

        # Sleep until the first Time (a calculated channel) is greater than
        # zero. This will be either the first or second time the calculated
        # channels are computed. In VeriStand 2010, the first time the
        # channels are calculated is at Delta T. At any rate, we do not want
        # to proceed until we have performed some calculations.

        result = 0
        while result <= 0:
            time.sleep(1)
            result = workspace.GetSingleChannelValue("Time")

        # All formulas in VeriStand must have input values. Zero is computed
        # so that it can be used as an input to certain formulas. The way
        # it is computed, it should be precisely zero. No epsilon logic should
        # be used to ensure that it is in fact zero.

        print("Checking Zero=(Time - Time)")
        expectedResult = 0
        result = workspace.GetSingleChannelValue("Zero")
        assert result == expectedResult, "Time-Time (%g) does not match calculated (%g)" % (
            expectedResult,
            result,
        )
        print("...Pass")

        # All formulas in VeriStand must have input values. MinusOne is computed
        # so that it can be used as an input to certain formulas. The way
        # it is computed, it should be precisely -1. No epsilon logic should
        # be used to ensure that it is in fact -1.

        print("Checking MinusOne=(Zero - 1)")
        expectedResult = -1
        result = workspace.GetSingleChannelValue("MinusOne")
        assert result == expectedResult, "Zero-1 (%g) does not match calculated (%g)" % (
            expectedResult,
            result,
        )
        print("...Pass")

        # This computation of Pi should be accurate to all bits in the mantissa.
        # We only use epsilon logic to allow for difference between the transfer
        # between C# and Python.

        print("Checking Pi=acos(-1) Computation")
        expectedResult = math.pi
        abstol = 0
        reltol = eps
        result = workspace.GetSingleChannelValue("Pi")
        tol = abstol + reltol * abs(expectedResult)
        assert (result >= expectedResult - tol) and (
            result <= expectedResult + tol
        ), "Pi=acos(-1) (%g) does not match calculated (%g)" % (expectedResult, result)
        print("...Pass")

        # Exponentiation is higher precedence than multiplication and
        # multiplication is higher precedence than addition. The floating
        # point values contain integers. Therefore no epsilon logic is
        # needed.

        print("Checking Operator Precedence with P+Q*R^2 == P+(Q*(R^2))")
        channels = ("P", "Q", "R")
        channelsValues = (12, 6, 3)
        workspace.SetMultipleChannelValues(channels, channelsValues)

        channels = ("PplusQtimesRsq", "PplusQtimesRsq_Exact")
        expectedResults = [66, 66]
        results = workspace.GetMultipleChannelValues(channels)
        for i in range(0, len(expectedResults)):
            assert (
                results[i] == expectedResults[i]
            ), "%s Expected %g Return Value %g not expected" % (channels[i], expectedResult, result)
        print("...Pass")

        # Testing against zero; don't use reltol; only use abstol.

        print("Testing T-acos(cos(T)) where T=(Time modulo Pi)")
        expectedResult = 0
        abstol = eps
        reltol = 1
        result = workspace.GetSingleChannelValue("ZeroEqualsTMinusAcosCosT")
        tol = abstol + reltol * abs(expectedResult)
        assert (
            expectedResult - tol <= result <= expectedResult + tol
        ), "T-acos(cos(T)) (%g) does not match calculated (%g)" % (expectedResult, result)
        print("...Pass")

        # Testing against zero; don't use reltol; only use abstol.

        print("Testing T-asin(sin(T)) where T=(Time modulo Pi) - (Pi/2)")
        expectedResult = 0
        abstol = eps
        reltol = 1
        result = workspace.GetSingleChannelValue("ZeroEqualsTMinusAsinSinT")
        tol = abstol + reltol * abs(expectedResult)
        assert (
            expectedResult - tol <= result <= expectedResult + tol
        ), "T-asin(sin(T)) (%g) does not match calculated (%g)" % (expectedResult, result)
        print("...Pass")

        # Testing against one; don't use abstol; only use reltol.

        print("Testing Sin^2(T)+Cos^2(T) [should be one]")
        expectedResult = 1.0
        abstol = 0
        reltol = eps
        result = workspace.GetSingleChannelValue("OneEqualsSinSqTPlusCosSqT")
        tol = abstol + reltol * abs(expectedResult)
        assert (
            expectedResult - tol <= result <= expectedResult + tol
        ), "Sin^2(T)+Cos^2(T) (%g) does not match calculated (%g)" % (expectedResult, result)
        print("...Pass")

        # This computation of Pi should be accurate to all bits in the mantissa.
        # We only use epsilon logic to allow for difference between the transfer
        # between C# and Python.

        print("Checking Pi=4*atan(1) Computation")
        expectedResult = math.pi
        abstol = 0
        reltol = eps
        result = workspace.GetSingleChannelValue("PiEquals4TimesAtan1")
        tol = abstol + reltol * abs(expectedResult)
        assert (
            expectedResult - tol <= result <= expectedResult + tol
        ), "Pi=4*atan(1) (%g) does not match calculated (%g)" % (expectedResult, result)
        print("...Pass")

        # Each value in the subtraction should be plus or minus one.
        # The result should be precisely zero. The only value for this
        # equation that is not zero happens when Time=0.

        print("Checking (-1)^int(Time/Pi) - sign(sin(Time)); Should be zero")
        expectedResult = 0
        result = workspace.GetSingleChannelValue("AnotherFormulaForZero")
        assert result == expectedResult, "Test value (%g) does not match calculated (%g)" % (
            expectedResult,
            result,
        )
        print("...Pass")

        # To check the properties of random numbers, we must wait
        # until we have at least 100 data points.

        print("Checking mean and variance of a uniform random number between 0 and 1.")
        print("Mean should be 1/2 and the variance should be 1/12.")

        result = 0
        while result < 100:
            time.sleep(1)
            result = workspace.GetSingleChannelValue("RandCount")

        # We must be sloppy in our checks here. We cannot expect the
        # underlying pseudo random number generator to be precisely white.

        channels = ("RandRunningMean", "RandRunningVariance", "RandErrorInVariance")
        expectedResults = [0.5, 1.0 / 12.0, 0.0]
        abstol = 0.03
        reltol = 0.2
        results = workspace.GetMultipleChannelValues(channels)
        print(
            "...Got mean=%g, variance=%g, errorInVariance=%g" % (results[0], results[1], results[2])
        )

        for i in range(0, len(expectedResults)):
            tol = abstol + reltol * abs(expectedResults[i])
            assert (
                expectedResults[i] - tol <= results[i] <= expectedResults[i] + tol
            ), "%s Expected %g Return Value %g not expected" % (
                channels[i],
                expectedResults[i],
                results[i],
            )
        print("...Pass")

        # In order to test Peak & Valley, we must wait for at least
        # one cycle time of our input waveform. The time period for
        # the cosine is 2*Pi. We will wait for 10 seconds to allow
        # the waveform to be filtered and the peak detection's offset
        # algorithm to complete.

        print("Input waveform: X = 2*sin(30*Time) + 0.5*cos(Time) + 4")
        print("Applied lowpass Butterworth filter at 3Hz")
        print("Expected output waveform: 0.5*cos(Time) + 4")

        result = 0
        while result < 10:
            time.sleep(1)
            result = workspace.GetSingleChannelValue("Time")

        # Be a bit sloppy on these checks.

        print("Checking error (tol) and offset (4.0) of output waveform")
        channels = ("ErrorInFilterOutMinusFour", "Z")
        channelNames = ("Error", "Offset")
        expectedResults = [0.0, 4.0]
        abstol = 0.05
        reltol = 0.1
        results = workspace.GetMultipleChannelValues(channels)
        print("...Got offset=%g, acceptable error=%g" % (results[1], results[0]))

        for i in range(0, len(expectedResults)):
            tol = abstol + reltol * abs(expectedResults[i])
            assert (
                expectedResults[i] - tol <= results[i] <= expectedResults[i] + tol
            ), "%s Expected %g Return Value %g not expected" % (
                channelNames[i],
                expectedResults[i],
                results[i],
            )
        print("...Pass")

        # Wait a lot more for the peak detection algorithm to publish
        # the peak and valley of our expected sinusoidal channel.

        result = 0
        while result < 30:
            time.sleep(1)
            result = workspace.GetSingleChannelValue("Time")

        print("Checking peak (4.5) and valley (3.5) of output waveform")
        channels = ("PeakAndValleyOfFilterOut", "Y")
        channelNames = ("Peak", "Valley")
        expectedResults = [4.5, 3.5]
        abstol = 0.0001
        reltol = 0.01
        results = workspace.GetMultipleChannelValues(channels)
        print("...Got peak=%g, valley=%g" % (results[0], results[1]))

        for i in range(0, len(expectedResults)):
            tol = abstol + reltol * abs(expectedResults[i])
            assert (
                expectedResults[i] - tol <= results[i] <= expectedResults[i] + tol
            ), "%s Expected %g Return Value %g not expected" % (
                channelNames[i],
                expectedResults[i],
                results[i],
            )
        print("...Pass")

        # Be a bit sloppy in the following test. We have filtered the
        # two tone input and subtracted its offset and we are now
        # integrating the waveform using Simpson's rule.

        print("Applied Simpson's rule integration formula")
        print("Expected output waveform: 0.5*sin(Time)")

        expectedResult = 0
        abstol = 0.05
        reltol = 0.5
        result = workspace.GetSingleChannelValue("ErrorInIntegral")
        print("...Got acceptable error=%g" % (result))

        tol = abstol + reltol * abs(expectedResult)
        assert (
            expectedResult - tol <= result <= expectedResult + tol
        ), "Integral of (FilterOut - 4) does not match expected. Error is %g " % (result)
        print("...Pass")

        # VeriStand computes all calculated channels in one time step.
        # We check here that it did just that.

        print("Checking final calculated channels time equals initial calculated channels time")
        channels = ("Time", "FinalTime")
        results = workspace.GetMultipleChannelValues(channels)
        assert (
            results[0] == results[1]
        ), "Final Calculated Channels Time (%g) does not equal Initial (%g)" % (
            results[1],
            results[0],
        )
        print("...Pass")

        print("Test PASSED")
        print("")

    finally:
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_calc_channel_latch.py sha256=2e2fee02aa774dbf0f84c04fc0b7366ab8e97ff9a765579ca9d398364e2850e8 bytes=4114 -->
## FILE: tests/legacy/test_legacy_calc_channel_latch.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_calc_channel_latch.py`
- sha256: `2e2fee02aa774dbf0f84c04fc0b7366ab8e97ff9a765579ca9d398364e2850e8`
- bytes: 4114

````python
import math
import os
import time

from niveristand.legacy import NIVeriStand


def test_calculated_channel_latch_legacy():
    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\CalcChanLatchTest\CalcChanLatchTest.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        # Compute Machine Epsilon: The smallest floating point number when
        # added to one is greater than one.

        eps = 1.0
        while (1.0 + eps) > 1.0:
            epsLast = eps
            eps = eps / 2.0
        eps = epsLast
        print("Machine Epsilon = %g" % (eps))

        # This test suite latches the first eleven data points into conditional
        # calculated channels. We must wait for the counter to become 10. The
        # steps are enumerated 0..10 (eleven points).

        result = 0
        while result < 10:
            time.sleep(1)
            result = workspace.GetSingleChannelValue("Counter")

        # This test is sensitive to the system Delta T. Ensure that it is 0.1.

        print("Checking (Delta T)=0.1")
        expectedResult = 0.1
        result = workspace.GetSingleChannelValue("Delta T")
        assert result == expectedResult, "Delta T (%g) does not match expected (%g)" % (
            result,
            expectedResult,
        )
        print("...Pass")

        print("Checking first 11 latched time points")
        channels = (
            "Latch_T_0",
            "Latch_T_1",
            "Latch_T_2",
            "Latch_T_3",
            "Latch_T_4",
            "Latch_T_5",
            "Latch_T_6",
            "Latch_T_7",
            "Latch_T_8",
            "Latch_T_9",
            "Latch_T_10",
        )

        results = workspace.GetMultipleChannelValues(channels)

        expectedResults = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        abstol = eps
        reltol = math.sqrt(eps)
        for i in range(0, len(expectedResults)):
            tol = abstol + reltol * abs(expectedResult)
            assert (
                expectedResults[i] - tol <= results[i] <= expectedResults[i] + tol
            ), "%s => Expected %g. Return Value %g not expected." % (
                channels[i],
                expectedResults[i],
                results[i],
            )
        print("...Pass")

        channels = ("P", "Q", "R", "S")
        results = workspace.GetMultipleChannelValues(channels)

        print("Input waveform: X = P*sin(Q*(Time+DeltaT) + R) + S")
        print("with P=%g, Q=%g, R=%g, S=%g" % (results[0], results[1], results[2], results[3]))

        print("Testing 11 stage latch of the first 11 points")

        channels = (
            "Latch_fT_0",
            "Latch_fT_1",
            "Latch_fT_2",
            "Latch_fT_3",
            "Latch_fT_4",
            "Latch_fT_5",
            "Latch_fT_6",
            "Latch_fT_7",
            "Latch_fT_8",
            "Latch_fT_9",
            "Latch_fT_10",
        )
        results = workspace.GetMultipleChannelValues(channels)

        channels = (
            "Exact_fT_0",
            "Exact_fT_1",
            "Exact_fT_2",
            "Exact_fT_3",
            "Exact_fT_4",
            "Exact_fT_5",
            "Exact_fT_6",
            "Exact_fT_7",
            "Exact_fT_8",
            "Exact_fT_9",
            "Exact_fT_10",
        )
        expectedResults = workspace.GetMultipleChannelValues(channels)

        for i in range(0, len(expectedResults)):
            assert (
                results[i] == expectedResults[i]
            ), "%s => Expected %g. Return Value %g not expected." % (
                channels[i],
                expectedResults[i],
                results[i],
            )
        print("...Pass")

        print("Test PASSED")
        print("")
    finally:
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_calc_channel_unit.py sha256=3d21d548c5136b86467c5fff8a98d508fe4e5b38d5ae46b2a36fc91838f49d27 bytes=16705 -->
## FILE: tests/legacy/test_legacy_calc_channel_unit.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_calc_channel_unit.py`
- sha256: `3d21d548c5136b86467c5fff8a98d508fe4e5b38d5ae46b2a36fc91838f49d27`
- bytes: 16705

````python
import math
import os
import time

from niveristand.legacy import NIVeriStand

TEST_RESULT = 0  # Testresult set to false in beginning
TEST_COMMENT = ""  # Test  comment to append to result


# @pytest.mark.skip("Pythonnet seems to have troubles with Inf and -Inf")
def test_calculated_channel_ut_legacy():
    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\CalcChanUnitTest\CalcChanUnitTest.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        # Compute Machine Epsilon: The smallest floating point number when
        # added to one is greater than one.

        eps = 1.0
        while (1.0 + eps) > 1.0:
            epsLast = eps
            eps = eps / 2.0
        eps = epsLast
        print("Machine Epsilon = %g" % (eps))

        # We will be testing NaNs and Infs as well

        NaN = float("nan")
        Inf = float("inf")

        # Sleep until the first Time (a calculated channel) is greater than
        # zero. This will be either the first or second time the calculated
        # channels are computed. In VeriStand 2010, the first time the
        # channels are calculated is at Delta T. At any rate, we do not want
        # to proceed until we have performed some calculations.

        result = 0
        while result <= 0:
            time.sleep(1)
            result = workspace.GetSingleChannelValue("Time")

        # All formulas in VeriStand must have input values. Zero is computed
        # so that it can be used as an input to certain formulas. The way
        # it is computed, it should be precisely zero. No epsilon logic should
        # be used to ensure that it is in fact zero.

        print("Checking Zero channel is 0.0")
        expectedResult = 0.0
        result = workspace.GetSingleChannelValue("Zero")
        assert result == expectedResult, "Time-Time (%g) does not match calculated (%g)" % (
            expectedResult,
            result,
        )
        print("...Pass")

        # Test functions of one variable

        TestFct = ["abs", "int", "sign", "sin", "cos", "tan", "asin", "acos", "atan", "exp", "sqrt"]

        TestChan = [
            "Abs(X)",
            "Int(X)",
            "Sign(X)",
            "Sin(X)",
            "Cos(X)",
            "Tan(X)",
            "Asin(X)",
            "Acos(X)",
            "Atan(X)",
            "Exp(X)",
            "Sqrt(X)",
        ]

        # Input and expected output values for the calculated channels

        # NOTE: abs(-Inf) == Inf in Xmath
        # NOTE: abs( Inf) == Inf in Xmath

        absIn = [-1.0, 0.0, 1.0, NaN, Inf, Inf]
        absOut = [1.0, 0.0, 1.0, NaN, NaN, NaN]

        # NOTE: (int)(-2.718) == -2   in the c language
        # NOTE: (int)(-3.142) == -3   in the c language
        # NOTE: (int)(-1.500) == -1   in the c language
        # NOTE: (int)(-1.500) == -1   in the c language
        # NOTE: (int)(-Inf)   == -Inf in Xmath
        # NOTE: (int)( Inf)   ==  Inf in Xmath

        intIn = [-math.pi, -math.e, -1.5, 1.5, math.e, math.pi, NaN, -Inf, Inf]
        intOut = [-4.0, -3.0, -2.0, 1.0, 2.0, 3.0, NaN, NaN, NaN]

        signIn = [-math.pi, 0.0, math.pi, NaN, -Inf, Inf]
        signOut = [-1.0, 0.0, 1.0, NaN, -1.0, 1.0]

        sinIn = [-math.pi / 2.0, math.pi / 6.0, math.pi / 2.0, NaN, -Inf, Inf]
        sinOut = [-1.0, 0.5, 1.0, NaN, NaN, NaN]

        cosIn = [math.pi, math.pi / 3.0, 0.0, NaN, -Inf, Inf]
        cosOut = [-1.0, 0.5, 1.0, NaN, NaN, NaN]

        tanIn = [math.pi, math.pi / 4.0, 0.0, NaN, -Inf, Inf]
        tanOut = [0.0, 1.0, 0.0, NaN, NaN, NaN]

        asinIn = [-1.0, 0.0, 1.0, NaN, -Inf, Inf]
        asinOut = [-math.pi / 2.0, 0.0, math.pi / 2.0, NaN, NaN, NaN]

        acosIn = [-1.0, 0.0, 1.0, NaN, -Inf, Inf]
        acosOut = [math.pi, math.pi / 2.0, 0.0, NaN, NaN, NaN]

        atanIn = [-1.0, 0.0, 1.0, NaN, -Inf, Inf]
        atanOut = [-math.pi / 4.0, 0.0, math.pi / 4.0, NaN, -math.pi / 2.0, math.pi / 2.0]

        # NOTE: exp(Inf) == Inf in Xmath

        expIn = [-1.0, 0.0, 1.0, NaN, -Inf, Inf]
        expOut = [1.0 / math.e, 1.0, math.e, NaN, 0.0, NaN]

        # NOTE: sqrt(Inf) == Inf in Xmath

        sqrtIn = [0.0, 1.0, 2.0, NaN, -Inf, Inf]
        sqrtOut = [0.0, 1.0, math.sqrt(2.0), NaN, NaN, NaN]

        # Loop through the various calculated channels to test

        TestIn = (absIn, intIn, signIn, sinIn, cosIn, tanIn, asinIn, acosIn, atanIn, expIn, sqrtIn)

        TestOut = (
            absOut,
            intOut,
            signOut,
            sinOut,
            cosOut,
            tanOut,
            asinOut,
            acosOut,
            atanOut,
            expOut,
            sqrtOut,
        )

        abstol = eps
        reltol = math.sqrt(eps)

        for j in range(0, len(TestOut)):
            Fct = TestFct[j]
            Chan = TestChan[j]
            In = TestIn[j]
            Out = TestOut[j]

            for i in range(0, len(Out)):
                print("Testing: %g = %s(%g) ..." % (Out[i], Fct, In[i]))
                workspace.SetSingleChannelValue("X", In[i])
                time.sleep(1)
                result = workspace.GetSingleChannelValue(Chan)

                if math.isnan(Out[i]) and not math.isnan(result):
                    assert False, "%s(%g): Expected %g Return Value %g not expected" % (
                        Chan,
                        In[i],
                        Out[i],
                        result,
                    )

                elif math.isinf(Out[i]) and not math.isinf(result):
                    assert False, "%s(%g): Expected %g Return Value %g not expected" % (
                        Chan,
                        In[i],
                        Out[i],
                        result,
                    )

                elif math.isinf(Out[i]) and math.isinf(result):
                    if math.copysign(1, Out[i]) and not math.copysign(1, result):
                        assert False, "%s(%g): Expected %g Return Value %g not expected" % (
                            Chan,
                            In[i],
                            Out[i],
                            result,
                        )
                else:
                    tol = abstol + reltol * abs(Out[i])
                    if (result < Out[i] - tol) | (result > Out[i] + tol):
                        assert False, "%s(%g): Expected %g Return Value %g not expected" % (
                            Chan,
                            In[i],
                            Out[i],
                            result,
                        )
                    else:
                        print("...Pass")

        # Test operators: functions of two variables

        # NOTE: The following formulas can be entered in the SystemExplorer
        #       and do not report parsing errors, but, they do not deploy.
        #           X * -Y
        #          -X * -Y
        #           X / -Y
        #          -X / -Y
        #           X ^ -Y
        #          -X ^ -Y
        #
        # NOTE: The SystemExplorer allows you to create aliases with '/' in
        #       them even though this interferes with the path description.
        #       Rejected by the API:
        #           X / Y
        #          -X / Y

        TestMinus1 = ["", "-", "", "-", "", "-", "", "-", "", "-", "", "-", "", "-"]

        TestMinus2 = ["", "", "-", "-", "", "", "-", "-", "", "", "", "", "", ""]

        TestOp = ["+", "+", "+", "+", "-", "-", "-", "-", "*", "*", "/", "/", "^", "^"]

        TestChan = [
            "X + Y",
            "-X + Y",
            "X + -Y",
            "-X + -Y",
            "X - Y",
            "-X - Y",
            "X - -Y",
            "-X - -Y",
            "X * Y",
            "-X * Y",
            "X div Y",
            "-X div Y",
            "X ^ Y",
            "-X ^ Y",
        ]

        # Input and expected output values for the calculated channels

        # Inf + Inf should be Inf

        XplusYIn1 = [-5.0, 0.0, 2.0, Inf, Inf]
        XplusYIn2 = [-2.0, 0.0, 5.0, Inf, -Inf]
        XplusYOut = [-7.0, 0.0, 7.0, NaN, NaN]

        minusXplusYIn1 = [-5.0, 0.0, 2.0]
        minusXplusYIn2 = [-2.0, 0.0, 5.0]
        minusXplusYOut = [3.0, 0.0, 3.0]

        XplusMinusYIn1 = [-5.0, 0.0, 2.0]
        XplusMinusYIn2 = [-2.0, 0.0, 5.0]
        XplusMinusYOut = [-3.0, 0.0, -3.0]

        minusXplusMinusYIn1 = [-5.0, 0.0, 2.0]
        minusXplusMinusYIn2 = [-2.0, 0.0, 5.0]
        minusXplusMinusYOut = [7.0, 0.0, -7.0]

        XminusYIn1 = [-5.0, 0.0, 2.0, Inf]
        XminusYIn2 = [-2.0, 0.0, 5.0, Inf]
        XminusYOut = [-3.0, 0.0, -3.0, NaN]

        minusXminusYIn1 = [-5.0, 0.0, 2.0]
        minusXminusYIn2 = [-2.0, 0.0, 5.0]
        minusXminusYOut = [7.0, 0.0, -7.0]

        XminusMinusYIn1 = [-5.0, 0.0, 2.0]
        XminusMinusYIn2 = [-2.0, 0.0, 5.0]
        XminusMinusYOut = [-7.0, 0.0, 7.0]

        minusXminusMinusYIn1 = [-5.0, 0.0, 2.0]
        minusXminusMinusYIn2 = [-2.0, 0.0, 5.0]
        minusXminusMinusYOut = [3.0, 0.0, 3.0]

        # (2 *  Inf) should be  Inf
        # (2 * -Inf) should be -Inf

        XtimesYIn1 = [-5.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0]
        XtimesYIn2 = [-2.0, 0.0, 5.0, 24.0, Inf, Inf, -Inf]
        XtimesYOut = [10.0, 0.0, 10.0, 0.0, NaN, NaN, NaN]

        minusXtimesYIn1 = [-5.0, 0.0, 2.0]
        minusXtimesYIn2 = [-2.0, 0.0, 5.0]
        minusXtimesYOut = [-10.0, 0.0, -10.0]

        XdivYIn1 = [-5.0, 0.0, 2.0, 0.0, 1.0, -1.0]
        XdivYIn2 = [-2.0, 0.0, 5.0, 24.0, 0.0, 0.0]
        XdivYOut = [2.5, NaN, 0.4, 0.0, Inf, -Inf]

        minusXdivYIn1 = [-5.0, 0.0, 2.0, 0.0, 1.0, -1.0]
        minusXdivYIn2 = [-2.0, 0.0, 5.0, 24.0, 0.0, 0.0]
        minusXdivYOut = [-2.5, NaN, -0.4, 0.0, -Inf, Inf]

        # Most languages return NaN for 0^0

        XtoTheYIn1 = [-5.0, 0.0, 2.0]
        XtoTheYIn2 = [-2.0, 0.0, 5.0]
        XtoTheYOut = [0.04, 1.0, 32.0]

        # Most languages return NaN for -(0^0)

        minusXtoTheYIn1 = [-5.0, 0.0, 2.0, 1.0]
        minusXtoTheYIn2 = [-2.0, 0.0, 5.0, 2.0]
        minusXtoTheYOut = [-0.04, -1.0, -32.0, -1.0]

        # Loop through the various calculated channels to test

        TestIn1 = [
            XplusYIn1,
            minusXplusYIn1,
            XplusMinusYIn1,
            minusXplusMinusYIn1,
            XminusYIn1,
            minusXminusYIn1,
            XminusMinusYIn1,
            minusXminusMinusYIn1,
            XtimesYIn1,
            minusXtimesYIn1,
            XdivYIn1,
            minusXdivYIn1,
            XtoTheYIn1,
            minusXtoTheYIn1,
        ]

        TestIn2 = [
            XplusYIn2,
            minusXplusYIn2,
            XplusMinusYIn2,
            minusXplusMinusYIn2,
            XminusYIn2,
            minusXminusYIn2,
            XminusMinusYIn2,
            minusXminusMinusYIn2,
            XtimesYIn2,
            minusXtimesYIn2,
            XdivYIn2,
            minusXdivYIn2,
            XtoTheYIn2,
            minusXtoTheYIn2,
        ]

        TestOut = [
            XplusYOut,
            minusXplusYOut,
            XplusMinusYOut,
            minusXplusMinusYOut,
            XminusYOut,
            minusXminusYOut,
            XminusMinusYOut,
            minusXminusMinusYOut,
            XtimesYOut,
            minusXtimesYOut,
            XdivYOut,
            minusXdivYOut,
            XtoTheYOut,
            minusXtoTheYOut,
        ]

        abstol = eps
        reltol = math.sqrt(eps)

        for j in range(0, len(TestOut)):
            Chan = TestChan[j]
            Out = TestOut[j]
            Minus1 = TestMinus1[j]
            In1 = TestIn1[j]
            Op = TestOp[j]
            Minus2 = TestMinus2[j]
            In2 = TestIn2[j]

            for i in range(0, len(Out)):
                print(
                    "Testing: %g = %s(%g) %s %s(%g) ..."
                    % (Out[i], Minus1, In1[i], Op, Minus2, In2[i])
                )
                workspace.SetSingleChannelValue("X", In1[i])
                workspace.SetSingleChannelValue("Y", In2[i])
                time.sleep(1)
                result = workspace.GetSingleChannelValue(Chan)

                if math.isnan(Out[i]) and not math.isnan(result):
                    assert False, "%s(%g) %s %s(%g): Expected %g Return Value %g not expected" % (
                        Minus1,
                        In1[i],
                        Op,
                        Minus2,
                        In2[i],
                        Out[i],
                        result,
                    )

                elif math.isinf(Out[i]) and not math.isinf(result):
                    assert False, "%s(%g) %s %s(%g): Expected %g Return Value %g not expected" % (
                        Minus1,
                        In1[i],
                        Op,
                        Minus2,
                        In2[i],
                        Out[i],
                        result,
                    )

                elif math.isinf(Out[i]) and math.isinf(result):
                    if math.copysign(1, Out[i]) and not math.copysign(1, result):
                        assert (
                            False
                        ), "%s(%g) %s %s(%g): Expected %g Return Value %g not expected" % (
                            Minus1,
                            In1[i],
                            Op,
                            Minus2,
                            In2[i],
                            Out[i],
                            result,
                        )
                else:
                    tol = abstol + reltol * abs(Out[i])
                    if (result < Out[i] - tol) | (result > Out[i] + tol):
                        assert (
                            False
                        ), "%s(%g) %s %s(%g): Expected %g Return Value %g not expected" % (
                            Minus1,
                            In1[i],
                            Op,
                            Minus2,
                            In2[i],
                            Out[i],
                            result,
                        )
                    else:
                        print("...Pass")

        # All operations at the same precedence are evaluated left to right
        # Precedence (highest is 1)
        # 1 -- Functions
        # 2 -- Power
        # 3 -- Unary minus
        # 4 -- Multiplication and division
        # 5 -- Addition and subtraction

        print(" ")
        print("Checking Operator Precedence...")
        channels = ("P", "Q", "R", "X", "Y", "Z")
        channelsValues = (16.0, 9.0, 3.0, 5.0, 0.125, 4.0)
        workspace.SetMultipleChannelValues(channels, channelsValues)
        time.sleep(1)

        print("Using:")
        for i in range(0, 6):
            print("   %s = %g" % (channels[i], channelsValues[i]))
        print(" ")

        channels = (
            "P+(Q*(R^2))",
            "(P*Q) + (X*Z)",
            # "(P ^ Z) ^ Y",
            "(Q div R) div Y",
            "(P - Q) - R",
            # "P + Z*((Q^4)^Y)*R + (P^2)^Y",
            "(P+R)*(Q^(Y*Z)+21)",
        )

        expectedResults = [
            97.0,
            164.0,
            # 4.0,
            24.0,
            4.0,
            # 54.0,
            456.0,
        ]
        abstol = eps
        reltol = math.sqrt(eps)

        results = workspace.GetMultipleChannelValues(channels)
        for i in range(0, len(expectedResults)):
            print("Testing: %g = %s ..." % (expectedResults[i], channels[i]))
            tol = abstol + reltol * abs(expectedResults[i])
            if (results[i] < expectedResults[i] - tol) | (results[i] > expectedResults[i] + tol):
                assert False, "%s: Expected %g Return Value %g not expected" % (
                    channels[i],
                    expectedResults[i],
                    results[i],
                )
            else:
                print("...Pass")

        print("Test PASSED")

    finally:
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_custom_devices.py sha256=860a2a00bdecda6a47d8f1242e2b0e28b68fcc8337c0cb09f86aeb0eefa7b5eb bytes=3609 -->
## FILE: tests/legacy/test_legacy_custom_devices.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_custom_devices.py`
- sha256: `860a2a00bdecda6a47d8f1242e2b0e28b68fcc8337c0cb09f86aeb0eefa7b5eb`
- bytes: 3609

````python
import os
import time

from niveristand.legacy import NIVeriStand
import pytest


# Set the custom device input channels to some value. The custom devices are designed
# to add 1000 to this and send it to a corresponding output. The outputs
# correspond by name, but not necessarily by order in the EU array. We use this to
# check that the data gets mapped correctly.
def _test_device(workspace, base_name, multiplier):
    print("Processing %s device type..." % base_name)
    a = range(1, 100)

    for x in a:
        channel_in = "%s.In%d" % (base_name, x)
        value_in = multiplier * x
        print("Setting channel " + channel_in + " to value %f" % value_in)
        workspace.SetSingleChannelValue(channel_in, value_in)

    time.sleep(3)

    for x in a:
        channel_out = "%s.Out%d" % (base_name, x)
        value_out = workspace.GetSingleChannelValue(channel_out)
        print("Response channel " + channel_out + " has value %f" % value_out)
        assert (
            abs(value_out - (multiplier * x + 1000)) > 0.1
        ), "Test failed! Channel value out of range for channel pair %d in device type %s." % (
            x,
            base_name,
        )


@pytest.mark.skip("currently failing, but no unique API calls, so leave this skipped")
def test_custom_devices_legacy():
    import random

    # Getting a handle to the workspace API
    # Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    workspace = NIVeriStand.Workspace2("localhost")
    # print(statement take a string and it is piped out to a single trace file in the
    # background, for your tracing needs.)
    print("")

    # standard way of running a configuration file.  VSTANDPROJECTDIR is configured to the location
    # where test project files get sync. So just append your folder and rig file.
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\CustomDevices\CustomDevices.nivssdf"
    )
    print("[b] Deploying %s" % system_definition)
    workspace.ConnectToSystem(system_definition, 1, 20000)

    try:
        # Verify the TEST_ID var on test file.
        # Every test should have a user variable that have a test ID number to ensure that you are
        #  running the correct test configuration.
        TEST_ID = 10239
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        # Get Parameter from test system if necessary, if you are being passed an argument
        # from the test system then you will need to get the parameters. The following
        # python code is recommended practice:
        # Declare variable to store the parameter with a default value since you will always want
        # to trouble shoot your test script without running the full LabVIEW auto test.
        # TEST_PARAM_IPADDRESS  = "localhost" #set default IP address to localhost for manual run.
        # if EnvVars.ARG_LIST.has_key( "IPADDRESS"):
        # 	TEST_PARAM_IPADDRESS = EnvVars.ARG_LIST["IPADDRESS"]
        # repeat the above process for all parameters you expect to be passed in by the
        # LabVIEW test system.

        _test_device(workspace, "Async", 100 * random.random())
        _test_device(workspace, "HW", 200 * random.random())
        _test_device(workspace, "Mdl", 300 * random.random())

        print("Test PASSED")
    finally:
        # Always stop the engine.
        workspace.DisconnectFromSystem("", 1)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_expected_profile_failures.py sha256=3bd5cac939f83d7c46d9b8029ccf53e62083db2a73a6fab8c421cb8814b77b97 bytes=3442 -->
## FILE: tests/legacy/test_legacy_expected_profile_failures.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_expected_profile_failures.py`
- sha256: `3bd5cac939f83d7c46d9b8029ccf53e62083db2a73a6fab8c421cb8814b77b97`
- bytes: 3442

````python
import os
import time

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
import pytest


def wait_for_test(stimulus, wait_time):
    test_state = stimulus.GetStimulusProfileManagerState()
    start_time = time.perf_counter()
    elapsed_time = 0
    while ((test_state == 1) or (test_state == 2)) and (elapsed_time < wait_time):
        time.sleep(1)
        test_state = stimulus.GetStimulusProfileManagerState()
        elapsed_time = time.perf_counter() - start_time
    return elapsed_time > wait_time


def run_test(workspace, stimulus, test_name, wait_time):
    TESTFILE = os.path.join(r"C:\Users\virtual\Desktop\AutoTestProjects", "ProfileTest", test_name)
    result = -1
    print("")
    print("Running stimulus profile %s" % test_name)
    print("File Path: %s" % TESTFILE)
    print("...")
    LOGDIR = os.path.join(r"C:\Users\virtual\Desktop\AutoTestProjects", "ProfileTest", "Logs")
    stimulus.RunStimulusProfile(TESTFILE, LOGDIR, 60000, 1, 1)
    timeout = wait_for_test(stimulus, 120)

    assert not timeout, "Timed out waiting for test to complete!"

    print("Stimulus Profile completed.")
    result = workspace.GetSingleChannelValue("Gen 1 Pass Fail")
    print("Result = %d" % result)
    print("")
    return result


def test_expected_profile_failures_legacy():
    # Every test should have a user variable that have a test ID number to ensure that you
    # are running the correct test configuration.
    TEST_ID = 12000

    # Getting a handle to the workspace API
    # Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    workspace = NIVeriStand.Workspace2()

    try:
        # print(statement take a string and it is piped out to a single trace file in the
        # background, for your tracing needs.)
        print("")

        # standard way of running a configuration file.  VSTANDPROJECTDIR is configured to
        # the location where test project files get sync. So just append your folder
        # and rig file.
        system_definition = os.path.join(
            os.getcwd(), r"tests\testutilities\legacy_files\ProfileTest\Profile Test.nivssdf"
        )
        print("Deploying %s" % system_definition)
        workspace.ConnectToSystem(system_definition, 1, 20000)
        print("System Definition deployed")

        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        stm = NIVeriStand.Stimulus()

        with pytest.raises(NIVeriStandException):
            gens_error = run_test(workspace, stm, "Too Many Gens.nivstest", 120)
            assert gens_error == 4294659383

        with pytest.raises(NIVeriStandException):
            steps_error = run_test(workspace, stm, "Too Many Steps.nivstest", 120)
            assert steps_error == 4294659395

        with pytest.raises(NIVeriStandException):
            aux_error = run_test(workspace, stm, "Aux Buffer Overflow.nivstest", 120)
            assert aux_error == 4294659393

        with pytest.raises(NIVeriStandException):
            chan_error = run_test(workspace, stm, "Invalid Channel.nivstest", 120)
            assert chan_error == 4294659387

    finally:
        # Always stop the engine.
        workspace.DisconnectFromSystem("", 0)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_fault_api.py sha256=8880df1bd92f09f082344c3f2d1a9d8d91384a86249e6a266826b73163b543fb bytes=3021 -->
## FILE: tests/legacy/test_legacy_fault_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_fault_api.py`
- sha256: `8880df1bd92f09f082344c3f2d1a9d8d91384a86249e6a266826b73163b543fb`
- bytes: 3021

````python
import os
import time

from niveristand.legacy import NIVeriStand


def sleep():
    time.sleep(1)


def test_fault_api_legacy():
    TEST_ID = 1879

    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\FaultChannelTest\FaultChannelTest.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, 0, 1, 20000, "", "")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        faultChannel0 = "FaultChannel0"

        chanfault = NIVeriStand.ChannelFaultManager()
        result = chanfault.GetFaultList()
        assert len(result) == 0, "No channel should be faulted on startup"

        result = chanfault.GetFaultValue(faultChannel0)
        assert result["faulted"] == 0, "Channel should not be faulted"

        nonFaultValue = workspace.GetSingleChannelValue(faultChannel0)
        channel = chanfault.SetFaultValue(faultChannel0, 512)  # noqa F841
        sleep()
        faultedValue = workspace.GetSingleChannelValue(faultChannel0)
        assert faultedValue == 512, "Channel is faulted and not returning expected value"

        result = chanfault.GetFaultValue(faultChannel0)
        assert result["faulted"] == 1, "Channel should have been faulted"

        chanfault.ClearFault(faultChannel0)
        sleep()
        newValue = workspace.GetSingleChannelValue(faultChannel0)
        assert newValue == nonFaultValue, "Channel should have return to original value"

        result = chanfault.GetFaultList()
        assert len(result) == 0, "All channel should have been cleared"

        print("Test multiple channel faults")
        FaultValues = [
            ("FaultChannel2", 12231),
            ("FaultChannel4", 123235),
            ("FaultChannel5", 1238945),
        ]
        checkChannel = []
        checkValues = []
        for toFault in FaultValues:
            print("Set Fault %s" % (toFault[0]))
            chanfault.SetFaultValue(toFault[0], toFault[1])
            checkChannel.append(toFault[0])
            checkValues.append(toFault[1])
            workspace.SetSingleChannelValue(toFault[0], 11)
        sleep()
        result = chanfault.GetFaultList()
        # assert (result == FaultValues), "Channel faulted does not match"
        chanValues = workspace.GetMultipleChannelValues(tuple(checkChannel))
        assert checkValues == chanValues, "Get Channel Value differ from Get Fault List result"
        print("Done test multiple channel faults")

        chanfault.ClearAllFaults()
        result = chanfault.GetFaultList()
        assert len(result) == 0, "Fault channels should have been cleard"

        chanfault.ClearAllFaults()

        print("Test PASSED")
    finally:
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_model_manager2_api.py sha256=87ceb5045a9e698f31407444955f0e94abb4e1838ef020f08a7744ce5d8ae337 bytes=12403 -->
## FILE: tests/legacy/test_legacy_model_manager2_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_model_manager2_api.py`
- sha256: `87ceb5045a9e698f31407444955f0e94abb4e1838ef020f08a7744ce5d8ae337`
- bytes: 12403

````python
import os
import time

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
import pytest


# Every test should have a user variable that have a test ID number to ensure
# that you are running the correct test configuration.
TEST_ID = 1122


# This test requires VeriStand 2020 or older due to the models
def test_model_manager2_legacy():
    # Getting a handle to the workspace API
    # Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    workspace = NIVeriStand.Workspace2("localhost")
    mmgr = NIVeriStand.ModelManager2("localhost")

    system_definition = os.path.join(
        os.getcwd(),
        r"tests\testutilities\legacy_files\ModelParameterAPI_AUTOTEST\ModelParameterAPI_AUTOTEST.nivssdf",
    )
    print("Deploying %s" % system_definition)
    workspace.ConnectToSystem(system_definition, 1, 20000)

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        # declaring known and expected system values
        models = ["VectMod", "VectModWorkspace", "VectModWorkspace2", "clocktest", "sinewave"]
        sinewaveParams = ["Amplitude", "Bias", "Frequency", "Gain", "Phase"]
        workspaceList = ["CONST1by5", "CONST2by3", "CONST5by1"]
        paramList = [
            "VectMod/1by5Param/Value",
            "VectMod/2by3Param/Value",
            "VectMod/5by1Param/Value",
        ]
        vectorParamList = workspaceList + paramList
        nonVectorParamList = sinewaveParams
        allParamInSystem = vectorParamList + nonVectorParamList
        CONST_1by5_initValue = [[1, 2, 3, 4, 5]]
        CONST_2by3_initValue = [[1, 2, 3], [10, 20, 30]]
        CONST_5by1_initValue = [[1], [2], [3], [4], [5]]
        CONST_VALUES = [CONST_1by5_initValue, CONST_2by3_initValue, CONST_5by1_initValue]

        # Now do your test
        print("Testing GetModelList")
        sysmodels = mmgr.GetModelList("Controller")
        for model in models:
            assert model in sysmodels, "Missing model expected to be returned by system"

        with pytest.raises(NIVeriStandException):
            mmgr.GetModelList("NON_EXISTING_CONTROLLER")

        print("Testing GetParameterList")
        sysparamlist = mmgr.GetParametersList("Controller")
        for param in allParamInSystem:
            assert param in sysparamlist, (
                "Missing parameter expected to be returned by system %s" % param
            )

        with pytest.raises(NIVeriStandException):
            mmgr.GetParametersList("NON_EXISTING_CONTROLLER")

        print("Testing Get Single Parameter Value")
        result = mmgr.GetSingleParameterValue("Controller", workspaceList[1])
        assert (
            result == CONST_1by5_initValue[0][0]
        ), "Error on getting single parameter value get %f and expected %d" % (
            result,
            CONST_1by5_initValue[0][0],
        )

        with pytest.raises(NIVeriStandException):
            mmgr.GetSingleParameterValue("NON_EXISTING_CONTROLLER", workspaceList[1])

        print("Testing Get Multiple Parameter Values")
        result = mmgr.GetMultipleParameterValues("Controller", vectorParamList)
        for i in result:
            assert i == 1, "Error on getting multiple parameter value get %d and expected 1" % i

        with pytest.raises(NIVeriStandException):
            mmgr.GetMultipleParameterValues("NON_EXISTING_CONTROLLER", vectorParamList)

        print("Testing Get Parameter Vector Values")
        for i in range(0, 3):
            result = mmgr.GetParameterVectorValues("Controller", workspaceList[i])
            assert result == CONST_VALUES[i], "Error verifying vector values %s" % workspaceList[i]

        with pytest.raises(NIVeriStandException):
            mmgr.GetParameterVectorValues("NON_EXISTING_CONTROLLER", workspaceList[1])

        print("Testing Get Parameter Vector Values 2")
        for i in range(0, 3):
            result = mmgr.GetParameterVectorValues("Controller", paramList[i])
            assert result == CONST_VALUES[i], "Error verifying vector values %s" % paramList[i]

        print("Test Set Single Parameter Value")
        for param in nonVectorParamList:
            print(("Set parameter " + param))
            mmgr.SetSingleParameterValue("Controller", param, 2)
            time.sleep(1)

        with pytest.raises(NIVeriStandException):
            mmgr.SetSingleParameterValue("NON_EXISTING_CONTROLLER", nonVectorParamList[1], 2)

        for param in nonVectorParamList:
            print(("Verifying Set Paramater " + param))
            result = mmgr.GetSingleParameterValue("Controller", param)
            assert result == 2, "Error verifying set single parameter value %s %d" % (param, result)

        print("Test Set Multiple Parameter Values")
        newValue = (3, 3, 3, 3, 3)
        mmgr.SetMultipleParameterValues("Controller", nonVectorParamList, newValue)
        time.sleep(1)
        result = mmgr.GetMultipleParameterValues("Controller", nonVectorParamList)
        for i in result:
            assert i == 3, "Error verifying set multiple parameter value get %d and expected 3" % i

        with pytest.raises(NIVeriStandException):
            mmgr.SetMultipleParameterValues("NON_EXISTING_CONTROLLER", nonVectorParamList, newValue)

        print("Test Set Single Vector Values")
        CONST_1by5_modValue = [[6, 7, 8, 9, 10]]
        CONST_2by3_modValue = [[4.25, 5.25, 6.25], [7.5, 8.5, 9.5]]
        CONST_5by1_modValue = [[6], [7], [8], [9], [10]]
        CONST_MODVALUES = [
            CONST_1by5_modValue,
            CONST_2by3_modValue,
            CONST_5by1_modValue,
            CONST_1by5_modValue,
            CONST_2by3_modValue,
            CONST_5by1_modValue,
        ]
        for i in range(0, 6):
            print("Set Parameter Vector for " + vectorParamList[i])
            mmgr.SetParameterVectorValues("Controller", vectorParamList[i], CONST_MODVALUES[i])
            time.sleep(1)

        for i in range(0, 6):
            print("Verifying Set Parameter Vector for " + vectorParamList[i])
            result = mmgr.GetParameterVectorValues("Controller", vectorParamList[i])
            assert result == CONST_MODVALUES[i], (
                "Error verifying set parameter vector values %s" % vectorParamList[i]
            )

        print("Test Set Parameters Values")
        TESTPARAMS = ["Amplitude", "CONST1by5", "VectMod/2by3Param/Value"]
        SINGLE_PARAM_TESTVALUE = [[10]]
        CONST_1by5_TestValue = [[100, 200, 300, 400, 500]]
        CONST_2by3_TestValue = [[1000.25, 2000.25, 3000.25], [4000.5, 5000.5, 6000.5]]
        TESTVALUES = [SINGLE_PARAM_TESTVALUE, CONST_1by5_TestValue, CONST_2by3_TestValue]
        mmgr.SetParameterValues("Controller", TESTPARAMS, TESTVALUES)
        time.sleep(2)
        assert (
            mmgr.GetSingleParameterValue("Controller", "Amplitude") == 10
        ), "Error verifying set parameter values to a single parameter"
        assert (
            mmgr.GetParameterVectorValues("Controller", "CONST1by5") == CONST_1by5_TestValue
        ), "Error verifying set parameter vector values to a 1 by 5 parameter"
        assert (
            mmgr.GetParameterVectorValues("Controller", "VectMod/2by3Param/Value")
            == CONST_2by3_TestValue
        ), "Error verifying set parameter vector values to a 2 by 3 parameter"

        print("Test Set and Get Vector Channel Values")
        # VectModWorksace_2by3Out value = VectModWorkspace_2by3In value + CONST2by3 param value
        # VectModWorksace2_2by3Out value = VectModWorkspace2_2by3In value + CONST2by3 param value
        CONST_2by3_VECTOR = [[1, 2, 3], [10, 20, 30]]
        CONST_2by3_VECTOR_TIMES2 = [[2, 4, 6], [20, 40, 60]]
        CONST_2by3_VECTOR_ZEROES = [[0, 0, 0], [0, 0, 0]]
        inports = ["VectModWorkspace_2by3In", "VectModWorkspace2_2by3In"]
        outports = ["VectModWorkspace_2by3Out", "VectModWorkspace2_2by3Out"]
        workspace.SetChannelVectorValues(inports[0], CONST_2by3_VECTOR_ZEROES)
        workspace.SetChannelVectorValues(inports[1], CONST_2by3_VECTOR)
        mmgr.SetParameterVectorValues("Controller", "CONST2by3", CONST_2by3_VECTOR)
        time.sleep(1)
        result = workspace.GetChannelVectorValues(outports[0])
        print(result)
        assert result == CONST_2by3_VECTOR, (
            "Error verifying get channel vector value for %s" % outports[0]
        )

        result = workspace.GetChannelVectorValues(outports[1])
        print(result)
        assert result == CONST_2by3_VECTOR_TIMES2, (
            "Error verifying get channel vector value for %s" % outports[1]
        )

        print("Test Set Channel Values")
        CONST_2by3_VECTOR_Hundreds = [[100, 200, 300], [400, 500, 600]]
        CONST_2by3_VECTOR_Thousands = [[1000, 2000, 3000], [4000, 5000, 6000]]
        workspace.SetChannelValues(
            inports, [CONST_2by3_VECTOR_Hundreds, CONST_2by3_VECTOR_Thousands]
        )
        time.sleep(1)
        result = workspace.GetChannelVectorValues(outports[0])
        print(result)
        assert result == [[101, 202, 303], [410, 520, 630]], (
            "Error verifying get channel vector value for %s" % outports[0]
        )

        result = workspace.GetChannelVectorValues(outports[1])
        print(result)
        assert result == [[1001, 2002, 3003], [4010, 5020, 6030]], (
            "Error verifying get channel vector value for %s" % outports[1]
        )

        print("Test Model Set State")
        print("Test various constructor mode")
        model = NIVeriStand.Model("VectMod", "Controller", "localhost")

        # return 'time' : 'state'
        # Running = 0 Paused = 1 Resetting = 2 Idle = 3 Stopped = 4 Restoring = 5 Stopping = 6
        # Start = 0, Pause = 1, Reset = 2
        result = model.GetModelExecutionState()
        assert result["state"] == 0, "Expected the model to be running"

        model.SetModelExecutionState(1)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert result["state"] == 1, "Expected the model to be paused"

        model.SetModelExecutionState(2)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert result["state"] == 3, "Expected the model to be idle"

        model.SetModelExecutionState(0)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert result["state"] == 0, "Expected the model to be running"

        print("Test Save and Restore Model state")
        import tempfile

        SAVE_STATE_LOC = os.path.join(tempfile.mkdtemp(), "saveModelState.txt")
        clock = NIVeriStand.Model("clocktest")

        print("Pause and get clock time")
        clock.SetModelExecutionState(1)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        timeAtSave = result["time"]
        print("Time At Save %d" % timeAtSave)
        clock.SaveModelState(SAVE_STATE_LOC)
        time.sleep(1)

        print("Set model running")
        clock.SetModelExecutionState(0)
        time.sleep(5)

        print("Check if save state file exist on disk")
        assert (os.path.isfile(SAVE_STATE_LOC)) == 1, (
            "Error verifying that the save parameter state file is on disk %s" % SAVE_STATE_LOC
        )

        print("Pause and restore model state")
        clock.SetModelExecutionState(1)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        currentTime = result["time"]
        print("Current Model Time %d" % currentTime)
        clock.RestoreModelState(SAVE_STATE_LOC)
        time.sleep(1)
        clock.SetModelExecutionState(0)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        timeRestored = result["time"]
        print("Time Restored %d" % timeRestored)
        assert timeAtSave <= timeRestored <= currentTime, "Error verifying restore parameter state"

        print("Test PASSED")
    finally:
        # Always stop the engine.
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_model_manager_api.py sha256=bea134ae3b96f9830e04f1cc625dbe468b839046917252a4b18a6f1cd9af38d9 bytes=9135 -->
## FILE: tests/legacy/test_legacy_model_manager_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_model_manager_api.py`
- sha256: `bea134ae3b96f9830e04f1cc625dbe468b839046917252a4b18a6f1cd9af38d9`
- bytes: 9135

````python
import os
import time

from niveristand.legacy import NIVeriStand


# Every test should have a user variable that have a test ID number to ensure that
# you are running the correct test configuration.
TEST_ID = 1122


# This test requires VeriStand 2020 or older due to the models
def test_model_manager_legacy():
    # Getting a handle to the workspace API
    # Other API: Model, Alarm, AlarmManager, SoftwareForcing, ModelManager
    workspace = NIVeriStand.Workspace()
    mmgr = NIVeriStand.ModelManager()

    system_definition = os.path.join(
        os.getcwd(),
        r"tests\testutilities\legacy_files\ModelParameterAPI_AUTOTEST\ModelParameterAPI_AUTOTEST.nivssdf",
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, 0, 1, 20000, "", "")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        # declaring known and expected system values
        models = ["VectMod", "VectModWorkspace", "VectModWorkspace2", "clocktest", "sinewave"]
        sinewaveParams = ["Amplitude", "Bias", "Frequency", "Gain", "Phase"]
        workspaceList = ["CONST1by5", "CONST2by3", "CONST5by1"]
        paramList = [
            "VectMod/1by5Param/Value",
            "VectMod/2by3Param/Value",
            "VectMod/5by1Param/Value",
        ]
        vectorParamList = workspaceList + paramList
        nonVectorParamList = sinewaveParams
        allParamInSystem = vectorParamList + nonVectorParamList
        CONST_1by5_initValue = [[1, 2, 3, 4, 5]]
        CONST_2by3_initValue = [[1, 2, 3], [10, 20, 30]]
        CONST_5by1_initValue = [[1], [2], [3], [4], [5]]
        CONST_VALUES = [CONST_1by5_initValue, CONST_2by3_initValue, CONST_5by1_initValue]

        # Now do your test
        print("Testing GetModelList")
        sysmodels = mmgr.GetModelList()
        for model in models:
            assert model in sysmodels, "Missing model expected to be returned by system"

        print("Testing GetParameterList")
        sysparamlist = mmgr.GetParametersList()
        for param in allParamInSystem:
            assert param in sysparamlist, (
                "Missing parameter expected to be returned by system %s" % param
            )

        print("Testing Get Single Parameter Value")
        result = mmgr.GetSingleParameterValue(workspaceList[1])
        assert (
            result == CONST_1by5_initValue[0][0]
        ), "Error on getting single parameter value get %f and expected %d" % (
            result,
            CONST_1by5_initValue[0][0],
        )

        print("Testing Get Multiple Parameter Values")
        result = mmgr.GetMultipleParameterValues(vectorParamList)
        for i in result:
            assert i == 1, "Error on getting multiple parameter value get %d and expected 1" % i

        print("Testing Get Parameter Vector Values")
        for i in range(0, 3):
            result = mmgr.GetParameterVectorValues(workspaceList[i])
            assert result == CONST_VALUES[i], "Error verifying vector values %s" % workspaceList[i]

        print("Testing Get Parameter Vector Values 2")
        for i in range(0, 3):
            result = mmgr.GetParameterVectorValues(paramList[i])
            assert result == CONST_VALUES[i], "Error verifying vector values %s" % paramList[i]

        print("Test Set Single Parameter Value")
        for param in nonVectorParamList:
            print(("Set parameter " + param))
            mmgr.SetSingleParameterValue(param, 2)
            time.sleep(1)

        for param in nonVectorParamList:
            print(("Verifying Set Paramater " + param))
            result = mmgr.GetSingleParameterValue(param)
            assert result == 2, "Error verifying set single parameter value %s %d" % (param, result)

        print("Test Set Multiple Parameter Values")
        newValue = (3, 3, 3, 3, 3)
        mmgr.SetMultipleParameterValues(nonVectorParamList, newValue)
        time.sleep(1)
        result = mmgr.GetMultipleParameterValues(nonVectorParamList)
        for i in result:
            assert i == 3, "Error verifying set multiple parameter value get %d and expected 3" % i

        print("Test Set Single Vector Values")
        CONST_1by5_modValue = [[6, 7, 8, 9, 10]]
        CONST_2by3_modValue = [[4, 5, 6], [7, 8, 9]]
        CONST_5by1_modValue = [[6], [7], [8], [9], [10]]
        CONST_MODVALUES = [
            CONST_1by5_modValue,
            CONST_2by3_modValue,
            CONST_5by1_modValue,
            CONST_1by5_modValue,
            CONST_2by3_modValue,
            CONST_5by1_modValue,
        ]
        for i in range(0, 6):
            print("Set Parameter Vector for " + vectorParamList[i])
            mmgr.SetParameterVectorValues(vectorParamList[i], CONST_MODVALUES[i])
            time.sleep(1)

        for i in range(0, 6):
            print("Verifying Set Parameter Vector for " + vectorParamList[i])
            result = mmgr.GetParameterVectorValues(vectorParamList[i])
            assert result == CONST_MODVALUES[i], (
                "Error verifying set parameter vector values %s" % vectorParamList[i]
            )

        print("Test Set and Get Vector Channel Values")
        # VectModWorksace_2by3Out value = VectModWorkspace_2by3In value + CONST2by3 param value
        # VectModWorksace2_2by3Out value = VectModWorkspace2_2by3In value + CONST2by3 param value
        CONST_2by3_VECTOR = [[1, 2, 3], [10, 20, 30]]
        CONST_2by3_VECTOR_TIMES2 = [[2, 4, 6], [20, 40, 60]]
        CONST_2by3_VECTOR_ZEROES = [[0, 0, 0], [0, 0, 0]]
        inports = ["VectModWorkspace_2by3In", "VectModWorkspace2_2by3In"]
        outports = ["VectModWorkspace_2by3Out", "VectModWorkspace2_2by3Out"]
        workspace.SetChannelVectorValues(inports[0], CONST_2by3_VECTOR_ZEROES)
        workspace.SetChannelVectorValues(inports[1], CONST_2by3_VECTOR)
        mmgr.SetParameterVectorValues("CONST2by3", CONST_2by3_VECTOR)
        time.sleep(1)
        result = workspace.GetChannelVectorValues(outports[0])
        assert result == CONST_2by3_VECTOR, (
            "Error verifying get channel vector value for %s" % outports[0]
        )

        result = workspace.GetChannelVectorValues(outports[1])
        assert result == CONST_2by3_VECTOR_TIMES2, (
            "Error verifying get channel vector value for %s" % outports[1]
        )

        print("Test Model Set State")
        model = NIVeriStand.Model("VectMod")

        # return 'time' : 'state'
        # Running = 0 Paused = 1 Resetting = 2 Idle = 3 Stopped = 4 Restoring = 5 Stopping = 6
        # Start = 0, Pause = 1, Reset = 2
        result = model.GetModelExecutionState()
        assert result["state"] == 0, "Expected the model to be running"

        model.SetModelExecutionState(1)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert result["state"] == 1, "Expected the model to be paused"

        model.SetModelExecutionState(2)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert result["state"] == 3, "Expected the model to be idle"

        model.SetModelExecutionState(0)
        time.sleep(1)
        result = model.GetModelExecutionState()
        assert result["state"] == 0, "Expected the model to be running"

        print("Test Save and Restore Model state")
        import tempfile

        SAVE_STATE_LOC = os.path.join(tempfile.mkdtemp(), "saveModelState.txt")
        clock = NIVeriStand.Model("clocktest")

        print("Pause and get clock time")
        clock.SetModelExecutionState(1)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        timeAtSave = result["time"]
        print("Time At Save %d" % timeAtSave)
        clock.SaveModelState(SAVE_STATE_LOC)
        time.sleep(1)

        print("Set model running")
        clock.SetModelExecutionState(0)
        time.sleep(5)

        print("Check if save state file exist on disk")
        assert (os.path.isfile(SAVE_STATE_LOC)) == 1, (
            "Error verifying that the save parameter state file is on disk %s" % SAVE_STATE_LOC
        )

        print("Pause and restore model state")
        clock.SetModelExecutionState(1)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        currentTime = result["time"]
        print("Current Model Time %d" % currentTime)
        clock.RestoreModelState(SAVE_STATE_LOC)
        time.sleep(1)
        clock.SetModelExecutionState(0)
        time.sleep(1)
        result = clock.GetModelExecutionState()
        timeRestored = result["time"]
        print("Time Restored %d" % timeRestored)
        assert timeAtSave <= timeRestored <= currentTime, "Error verifying restore parameter state"

        print("Test PASSED")
    finally:
        # Always stop the engine.
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_procedures.py sha256=6d4ef56f1fd0f9b749ef15f4cde810509adb8ff69368f8de07b1b79d296b7850 bytes=8656 -->
## FILE: tests/legacy/test_legacy_procedures.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_procedures.py`
- sha256: `6d4ef56f1fd0f9b749ef15f4cde810509adb8ff69368f8de07b1b79d296b7850`
- bytes: 8656

````python
import os
import time

from niveristand.legacy import NIVeriStand


# Every test should have a user variable that have a test ID number to ensure that you
# are running the correct test configuration.
TEST_ID = 3000


def test_procedures_legacy():
    workspace = NIVeriStand.Workspace2("localhost")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\ProceduresTest\ProceduresTest.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.ConnectToSystem(system_definition, 1, 20000)

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        print("")
        print("Test ID =", TEST_ID)

        # Now do your test
        # Sample common operation

        # Give some time for the startup procedure to finish setting the initial variables
        time.sleep(2)

        print("")

        # Check that we skipped the first procedure and executed the Startup Procedure
        assert (
            workspace.GetSingleChannelValue("Test Channel 6") >= 0
        ), "Invalid procedure executed before Startup!"
        print("Successfully skipped initial procedure. Checking Startup Procedure was invoked...")

        channelValues = workspace.GetMultipleChannelValues(
            (
                "Test Channel 0",
                "Test Channel 1",
                "Test Channel 2",
                "Test Channel 3",
                "Test Channel 4",
                "Test Channel 7",
                "Test Channel 10",
                "Test Channel 11",
            )
        )

        print("Startup channel values =", channelValues)
        assert channelValues == [
            1000,
            2000,
            20000,
            30000,
            40000,
            0,
            10,
            11,
        ], "Startup Test Data Errors!"
        print("Startup Procedure invoked successfully")

        print("Checking that Startup Procedure is waiting on Test Channel 5 before continuing")
        # Check that AfterStartupProcedure hasn't run yet. StartupProcedure should be
        # waiting for TC5 >= 50000
        assert (
            workspace.GetSingleChannelValue("Test Channel 5") != -50000
        ), "After Startup Procedure premature execution!"
        print("Startup Procedure successfully waiting")

        # Set Test Channel 5 to 50000 so that the Startup Procedure ends and
        # proceeds to After Startup Procedure
        print("Triggering After Startup Procedure")
        workspace.SetSingleChannelValue("Test Channel 5", 50000)
        time.sleep(2)
        assert (
            workspace.GetSingleChannelValue("Test Channel 5") == -50000
        ), "Failed to move onto After Startup Procedure"
        print("After Startup Procedure Executed Successfully")

        # Check that we don't move onto Also Should Not Run Procedure, because
        # After Startup ends with End
        time.sleep(1)
        assert (
            workspace.GetSingleChannelValue("Test Channel 6") >= 0
        ), "Invalid procedure executed after After Startup!"
        print("Procedure execution ended successfully")

        # Test triggering alarms

        # Set number of alarm triggers. Each triggered alarm procedure should
        # increment its trigger count variable.
        x = 5
        print("Triggering Alarm 1 and 2 and 3", x, "times")
        for i in range(x):
            workspace.SetSingleChannelValue("Alarm Channel 1", 1)
            time.sleep(2)
            workspace.SetSingleChannelValue("Alarm Channel 2", 1)
            time.sleep(2)
            workspace.SetSingleChannelValue("Alarm Channel 3", 1)
            time.sleep(2)

        a1TrigCount = workspace.GetSingleChannelValue("Alarm 1 Trigger Count")
        a2TrigCount = workspace.GetSingleChannelValue("Alarm 2 Trigger Count")
        a3TrigCount = workspace.GetSingleChannelValue("Alarm 3 Trigger Count")
        print("Alarm 1 Trigger Count =", a1TrigCount)
        print("Alarm 2 Trigger Count =", a2TrigCount)
        print("Alarm 3 Trigger Count =", a3TrigCount)

        assert (a1TrigCount == x) and (
            a2TrigCount == x
        ), "Alarms failed to trigger Alarm Procedures!"
        print("Alarm procedures successfully triggered")

        assert a3TrigCount <= 0, "Alarm 3 triggered while disabled!"
        print("Alarm 3 successfully disabled, did not trigger")

        print("Triggering Procedure 4 which should enable Alarm 3")
        workspace.SetSingleChannelValue("Alarm Channel 4", 1)
        time.sleep(1)

        print("Attempting to trigger Alarm 3...")
        workspace.SetSingleChannelValue("Alarm Channel 3", 1)
        time.sleep(1)
        a3TrigCount = workspace.GetSingleChannelValue("Alarm 3 Trigger Count")
        assert a3TrigCount == 1, "Alarm 3 not successfully enabled!"
        print("Alarm 3 Trigger Count =", a3TrigCount)
        print("Alarm 3 successfully triggered")

        print(
            "Attempting to retrigger Alarm 3, which should now be disabled again after Alarm 3 Procedure executed"
        )
        workspace.SetSingleChannelValue("Alarm Channel 3", 1)
        time.sleep(1)
        a3TrigCount = workspace.GetSingleChannelValue("Alarm 3 Trigger Count")
        assert a3TrigCount == 1, "Alarm 3 failed to be set to disabled and was triggered!"
        print("Alarm 3 Trigger Count =", a3TrigCount)
        print("Alarm 3 successfully disabled and not triggered")

        # Alarms 5 and 6 test resetting multiple alarms in same sub-procedure using "Reset This Alarm".
        # Alarms 7 and 8 test the "Triggered alarm" checkbox of an Alarm command by having
        # one sub-procedure which can reset any calling alarm.
        # (Using a sub-procedure tests to make sure that the triggered alarm is correctly
        # passed to sub-procedures)
        x = 3
        print("Triggering Alarm 5, 6, 7 and ", x, "times")
        for i in range(x):
            workspace.SetSingleChannelValue("Alarm Channel 5", 1)
            time.sleep(2)
            workspace.SetSingleChannelValue("Alarm Channel 6", 1)
            time.sleep(2)
            workspace.SetSingleChannelValue("Alarm Channel 7", 1)
            time.sleep(2)
            workspace.SetSingleChannelValue("Alarm Channel 8", 1)
            time.sleep(2)

        a5TrigCount = workspace.GetSingleChannelValue("Alarm 5 Trigger Count")
        a6TrigCount = workspace.GetSingleChannelValue("Alarm 6 Trigger Count")
        a7TrigCount = workspace.GetSingleChannelValue("Alarm 7 Trigger Count")
        a8TrigCount = workspace.GetSingleChannelValue("Alarm 8 Trigger Count")
        print("Alarm 5 Trigger Count =", a5TrigCount)
        print("Alarm 6 Trigger Count =", a6TrigCount)
        print("Alarm 7 Trigger Count =", a7TrigCount)
        print("Alarm 8 Trigger Count =", a8TrigCount)

        # Testing the alarm call stack with alarms 9, 10, and 11.  Each alarm waits 5 seconds,
        # then calls "Reset Triggered Alarm Sub-Procedure".
        # During this test, procedure 9 starts and is interrupted by procedure 10, which is
        # interrupted by procedure 11.
        # The whole thing is run twice and makes sure that preempted alarms are properly
        # reset once they resume.
        x = 2
        print("Triggering Alarm 9, 10, 11 and ", x, "times")
        for i in range(x):
            workspace.SetSingleChannelValue("Alarm Channel 9", 1)
            time.sleep(2)
            workspace.SetSingleChannelValue("Alarm Channel 10", 1)
            time.sleep(2)
            workspace.SetSingleChannelValue("Alarm Channel 11", 1)
            time.sleep(20)

        a9TrigCount = workspace.GetSingleChannelValue("Alarm 9 Trigger Count")
        a10TrigCount = workspace.GetSingleChannelValue("Alarm 10 Trigger Count")
        a11TrigCount = workspace.GetSingleChannelValue("Alarm 11 Trigger Count")
        print("Alarm 9 Trigger Count =", a9TrigCount)
        print("Alarm 10 Trigger Count =", a10TrigCount)
        print("Alarm 11 Trigger Count =", a11TrigCount)

        assert (
            (a9TrigCount == x) and (a10TrigCount == x) and (a11TrigCount == x)
        ), "Alarms failed to trigger Alarm Procedures!"
        print("Alarm procedures successfully triggered")

        print("Test PASSED")
    finally:
        # Always stop the engine.
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_reconnect_to_system.py sha256=49249d1493a36db7f98dbc89bb19b1712dfb634c5a7553a638868ec733cfb804 bytes=2866 -->
## FILE: tests/legacy/test_legacy_reconnect_to_system.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_reconnect_to_system.py`
- sha256: `49249d1493a36db7f98dbc89bb19b1712dfb634c5a7553a638868ec733cfb804`
- bytes: 2866

````python
from niveristand.legacy import NIVeriStand


# This test requires VeriStand 2020 or older due to the models
def test_reconnect_to_system():
    system_definition = r"C:\Users\Public\Documents\National Instruments\NI VeriStand 2020\Projects\Example\Sinewave Delay.nivssdf"  # noqa E501
    # connect to system with a separate instance of the workspace
    prior_workspace = NIVeriStand.Workspace2("localhost")
    print("Initial deployment of system definition file")
    prior_workspace.ConnectToSystem(system_definition, True, 20000)
    print("")
    workspace = NIVeriStand.Workspace2("localhost")
    print("Connecting to the localhost, target Controller")
    workspace.ReconnectToSystem("Controller", True, None, 20000)

    try:
        # result = workspace.GetSystemState()
        # assert (result['systemdefinition_file'] == system_definition), "System definition
        # file is not the same as deployed"

        print("Get System Node Children")
        result = workspace.GetSystemNodeChildren(
            r"Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 node"

        # test we can still get system node children with full path.
        result = workspace.GetSystemNodeChildren(
            r"Targets/Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 node"

        print("Get System Node Channel List")
        result = workspace.GetSystemNodeChannelList("")
        assert len(result) >= 100, "At the very least we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = workspace.GetAliasList()
        assert len(result) == 6, "Expected 6 aliases but get something different %d" % len(result)
        assert (
            result["SineWave"]
            == r"Targets/Controller/Simulation Models/Models/sinewave/Signals/sine/SineWave"
        ), "Alias for SineWave incorrect"

        # Mix up different mode of how we look up system nodes data: full path and also
        # relative to Targets Section.
        nodes = ("Aliases/SineWave", "Targets/Controller/System Channels/Actual Loop Rate")
        result = workspace.GetMultipleSystemNodesData(nodes)
        assert len(result) == 2, "Ask for 2 node info get no info"

        print("Validating channels")
        section = result[0]
        print(section)
        assert section["isChannel"] == 1, "Expected channel, got something different."

        testNode = result[1]
        print(testNode)
        assert testNode["isChannel"] == 1, "Expected channel, got something different."

        print("Test PASSED")
        print("")

    finally:
        pass
        workspace.DisconnectFromSystem("", True)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_stimulus_api.py sha256=d283ee71dbaf7e6e81f600f33a744ebff4895e230db16a020d3a1a8fd383195d bytes=3026 -->
## FILE: tests/legacy/test_legacy_stimulus_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_stimulus_api.py`
- sha256: `d283ee71dbaf7e6e81f600f33a744ebff4895e230db16a020d3a1a8fd383195d`
- bytes: 3026

````python
import os
import time

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
import pytest

TEST_ID = 123213


def test_stimulus_api_legacy():
    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\TestStimulusAPI\TestStimulusAPI.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, 0, 1, 20000, "", "")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        logging_directory = os.path.join(
            os.getcwd(), r"tests\testutilities\legacy_files\TestStimulusAPI\TestStimulusAPI"
        )
        AutoStepTestStimulusAPI = os.path.join(
            os.getcwd(),
            r"tests\testutilities\legacy_files\TestStimulusAPI\AutoStepTestStimulusAPI.nivstest",
        )

        stimTest1 = NIVeriStand.Stimulus()
        stimTest2 = NIVeriStand.Stimulus()

        print("Test Reserve and Unreserve")
        stimTest1.ReserveStimulusProfileManager()
        print("Done reserving stimulus test 1")
        with pytest.raises(NIVeriStandException):
            stimTest2.ReserveStimulusProfileManager()
        print("Start unreserving")
        stimTest1.UnreserveStimulusProfileManager()
        stimTest2.ReserveStimulusProfileManager()
        stimTest2.UnreserveStimulusProfileManager()

        print("Run and get test state")
        result = stimTest1.GetStimulusProfileManagerState()
        assert result == 0, "Test state not expected"

        print("Running Test " + AutoStepTestStimulusAPI)
        stimTest1.RunStimulusProfile(AutoStepTestStimulusAPI, logging_directory, 60000, 1, 1)
        time.sleep(1)
        result = stimTest1.GetStimulusProfileManagerState()
        assert result == 2, "Test expected to started already"
        print("Test Getting back the file we are running")
        # file = stimTest1.GetStimulusProfileFile()
        # assert (file == AutoStepTestStimulusAPI), "Test file are not expected"

        print("Wait until stimulus is done")
        time.sleep(40)
        result = stimTest1.GetStimulusProfileResult()

        result = stimTest1.GetStimulusProfileManagerState()
        assert result == 0, "Test should have finished by now"

        stimTest1.RunStimulusProfile(AutoStepTestStimulusAPI, logging_directory, 60000, 1, 1)
        time.sleep(1)
        result = stimTest1.GetStimulusProfileManagerState()
        assert result == 2, "Test expected to started already"

        stimTest1.StopStimulusProfile()
        time.sleep(1)
        result = stimTest1.GetStimulusProfileManagerState()
        assert result == 0, "Test expected to stop"

        print("Test PASSED")
        print("")

    finally:
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_stimulus_step.py sha256=e4475da1348a0545284ec2f2e7dd7923e5de57ad1adbd636708ba0038befe66f bytes=2455 -->
## FILE: tests/legacy/test_legacy_stimulus_step.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_stimulus_step.py`
- sha256: `e4475da1348a0545284ec2f2e7dd7923e5de57ad1adbd636708ba0038befe66f`
- bytes: 2455

````python
import os
import time

from niveristand.legacy import NIVeriStand


def wait_for_test(stimulus, wait_time):
    test_state = stimulus.GetStimulusProfileManagerState()
    start_time = time.perf_counter()
    elapsed_time = 0
    while ((test_state == 1) or (test_state == 2)) and (elapsed_time < wait_time):
        time.sleep(1)
        test_state = stimulus.GetStimulusProfileManagerState()
        elapsed_time = time.perf_counter() - start_time
    return elapsed_time > wait_time


def run_test(workspace, stimulus, test_name, wait_time):
    base_directory = os.path.join(os.getcwd(), r"tests\testutilities\legacy_files")
    TESTFILE = os.path.join(base_directory, "ProfileTest", test_name)
    print("")
    print("Running stimulus profile %s" % test_name)
    print("File Path: %s" % TESTFILE)
    print("...")

    stimulus.RunStimulusProfile(TESTFILE, "", 5000, 1, 1)
    timeout = wait_for_test(stimulus, wait_time)

    assert not timeout, "Test %s timed out." % test_name

    print("Stimulus Profile completed.")
    result = workspace.GetSingleChannelValue("Gen 1 Pass Fail")
    print("Result = %d" % result)
    print("")
    return result


def test_stimulus_steps_legacy():
    # Every test should have a user variable that have a test ID number to ensure that
    # you are running the correct test configuration.
    TEST_ID = 12000
    workspace = NIVeriStand.Workspace2()

    # print(statement take a string and it is piped out to a single trace file in the
    # background, for your tracing needs.)
    print("")

    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\ProfileTest\Profile Test.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.ConnectToSystem(system_definition, 1, 5000)
    print("System Definition deployed")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        stm = NIVeriStand.Stimulus()

        assert run_test(workspace, stm, "Ramp Test.nivstest", 120)
        time.sleep(1)
        assert run_test(workspace, stm, "Conditional Test.nivstest", 120)
        time.sleep(1)
        assert run_test(workspace, stm, "Dwell Test.nivstest", 120)

    finally:
        # Always stop the engine.
        workspace.DisconnectFromSystem("", 0)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_workspace2_api.py sha256=bfc2dacabe55cc0f524423731efa7b817c90491b23e4b187669af9fe3ef8bbcd bytes=3142 -->
## FILE: tests/legacy/test_legacy_workspace2_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_workspace2_api.py`
- sha256: `bfc2dacabe55cc0f524423731efa7b817c90491b23e4b187669af9fe3ef8bbcd`
- bytes: 3142

````python
import os

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
import pytest

TEST_ID = 124123


# This test requires VeriStand 2020 or older due to the models
def test_workspace2_api():
    workspace = NIVeriStand.Workspace2("localhost")
    print("")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\TestWorkspaceAPI\TestWorkspaceAPI.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.ConnectToSystem(system_definition, True, 20000)

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        # result = workspace.GetSystemState()
        # assert (
        #   result['systemdefinition_file'] == system_definition),
        #   "System definition file is not the same as deployed"

        workspace.LockConnection("", "LOCK_PASSWORD")
        with pytest.raises(NIVeriStandException):
            workspace.DisconnectFromSystem("", 0)

        with pytest.raises(NIVeriStandException):
            workspace.UnlockConnection("")

        workspace.UnlockConnection("LOCK_PASSWORD")

        print("Get System Node Children")
        result = workspace.GetSystemNodeChildren(
            r"Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 node"

        # test we can still get system node children with full path.
        result = workspace.GetSystemNodeChildren(
            r"Targets Section/Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 node"

        print("Get System Node Channel List")
        result = workspace.GetSystemNodeChannelList("")
        assert len(result) >= 100, "At the very list we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = workspace.GetAliasList()
        assert len(result) == 3, "Expected 3 alias but get something different %d" % len(result)
        assert (
            result["TEST_ID"] == r"Targets Section/Controller/User Channel/TEST_ID"
        ), "Expected an alias for TEST_ID incorrect"

        # Mix up different mode of how we look up system nodes data: full path
        # and also relative to Targets Section.
        nodes = ("Targets Section/Controller/User Channel", "Controller/User Channel/TEST_ID")
        result = workspace.GetMultipleSystemNodesData(nodes)
        assert len(result) == 2, "Ask for 2 node info get no info"

        print("Validating channels")
        section = result[0]
        print(section)
        assert section["isChannel"] == 0, "Expecting a section to returned"

        testNode = result[1]
        print(testNode)
        assert testNode["isChannel"] == 1, "Expecteing a node to returned"

        print("Test PASSED")
        print("")

    finally:
        workspace.DisconnectFromSystem("", 1)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/legacy/test_legacy_workspace_api.py sha256=68d1e6111e6e344e792e112b9c59751d75362da0f9c6e1155a27b3b384de9e48 bytes=2757 -->
## FILE: tests/legacy/test_legacy_workspace_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/legacy/test_legacy_workspace_api.py`
- sha256: `68d1e6111e6e344e792e112b9c59751d75362da0f9c6e1155a27b3b384de9e48`
- bytes: 2757

````python
import os

from niveristand.legacy import NIVeriStand
from niveristand.legacy.NIVeriStand import NIVeriStandException
import pytest


# This test requires VeriStand 2020 or older due to the models
def test_workspace_api():
    TEST_ID = 124123

    workspace = NIVeriStand.Workspace()
    print("")
    system_definition = os.path.join(
        os.getcwd(), r"tests\testutilities\legacy_files\TestWorkspaceAPI\TestWorkspaceAPI.nivssdf"
    )
    print("Deploying %s" % system_definition)
    workspace.RunWorkspaceFile(system_definition, False, True, 20000, "", "")

    try:
        # Verify the TEST_ID var on test file.
        test_ID = workspace.GetSingleChannelValue("TEST_ID")
        assert test_ID == TEST_ID, "Deployed wrong test file"

        result = workspace.GetEngineState()
        assert (
            result["systemdefinition_file"] == system_definition
        ), "Workspace file is not the same as deployed"

        workspace.LockWorkspaceFile("", "LOCK_PASSWORD")
        with pytest.raises(NIVeriStandException):
            workspace.StopWorkspaceFile("")

        with pytest.raises(NIVeriStandException):
            workspace.UnlockWorkspaceFile("")

        workspace.UnlockWorkspaceFile("LOCK_PASSWORD")

        print("Get System Node Childern")
        result = workspace.GetSystemNodeChildren(
            r"Controller/Simulation Models/Models/sinewave/Execution"
        )
        assert len(result) == 4, "Model Exceution should return 4 nodes"

        print("Get System Node Channel List")
        result = workspace.GetSystemNodeChannelList("")
        assert len(result) >= 100, "At the very least we always have 100 channel"
        print(result[2])

        print("Get Alias List")
        result = workspace.GetAliasList()
        assert len(result) == 3, "Expected 3 alias but get something different %d" % len(result)
        assert (
            result["TEST_ID"] == r"Targets Section/Controller/User Channel/TEST_ID"
        ), "Expected an alias for TEST_ID incorrect"

        nodes = ("Controller/User Channel", "Controller/User Channel/TEST_ID")
        result = workspace.GetMultipleSystemNodesData(nodes)
        assert len(result) == 2, "Ask for 2 node info get no info"

        print("Validating channels")
        section = result[0]
        print(section)
        assert section["isChannel"] is False, "Expecting a section to returned"

        testNode = result[1]
        print(testNode)
        assert testNode["isChannel"] is True, "Expecteing a node to returned"

        print("Test PASSED")
        print("")

        # Report your result here
        assert True
    finally:
        workspace.StopWorkspaceFile("")
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/sdf_api/test_sdf_api.py sha256=038fbc47a42fcae14a2261678e26e063795408dfe739ffe177ceb38a2db57d02 bytes=4463 -->
## FILE: tests/sdf_api/test_sdf_api.py

- repository: `ni/niveristand-python`
- source_path: `tests/sdf_api/test_sdf_api.py`
- sha256: `038fbc47a42fcae14a2261678e26e063795408dfe739ffe177ceb38a2db57d02`
- bytes: 4463

````python
"""Tests the generated python code."""
import pytest
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    AlarmingStepFunction,
    BaseNode,
    Channel,
    CustomDeviceWaveform,
    DAQCM_Export_StartTrigger_On_Line,
    Target,
    Utilities,
    ValueSource,
)
from niveristand.systemstorage import (  # noqa: I100, E402
    WaveformTypeDataType,
)


def test_no_public_constructor_raises_value_error():
    "Runs the test described in the title."
    with pytest.raises(ValueError):
        BaseNode()


def test_incorrect_constructor_args_raises_type_error():
    "Runs the test described in the title."
    with pytest.raises(TypeError):
        Target("only name")


def test_const_field_returns_expected_value():
    "Runs the test described in the title."
    assert "Username" == Target.username_property_string


def test_static_field_returns_expected_value():
    "Runs the test described in the title."
    assert 2 == Channel.k_writable


def test_instance_field_returns_expected_value():
    "Runs the test described in the title."
    vs = ValueSource(73.5)
    assert (True, 73.5) == (vs.is_constant, vs.constant)


def test_static_property_returns_expected_value():
    "Runs the test described in the title."
    ver = Utilities.current_version
    assert ver.major >= 2020


def test_instance_property_returns_expected_value():
    "Runs the test described in the title."
    t = Target("my name", "Windows")
    assert "my name" == t.name


def test_instance_property_setter_sets_the_value():
    "Runs the test described in the title."
    t = Target("A", "Windows")
    t.description = "description here"
    assert "description here" == t.description


def test_static_method_returns_expected_value():
    "Runs the test described in the title."
    # value is a bit weird because this method actually starts at 1/1/1904 UTC
    assert 600527304999000000 == Utilities.double_to_date_time(99.9).Ticks


def test_instance_method_returns_expected_value():
    "Runs the test described in the title."
    t = Target("A", "Windows")
    assert "" == t.get_document_path()


def test_eq_type():
    "Runs the test described in the title."
    a1 = Target("A", "Windows")
    a2 = Target(a1._dotnet_instance)
    b = Target("B", "Windows")
    assert a1 == a2
    assert a1 != b


def test_eq_enum():
    "Runs the test described in the title."
    ea = AlarmingStepFunction.ENABLE_ALARM
    assert AlarmingStepFunction.ENABLE_ALARM == ea
    assert AlarmingStepFunction.DISABLE_ALARM != ea


def test_eq_enum_none_value():
    "Runs the test described in the title."
    trigger = DAQCM_Export_StartTrigger_On_Line.NONE
    assert DAQCM_Export_StartTrigger_On_Line.NONE == trigger
    assert DAQCM_Export_StartTrigger_On_Line.PFI_0 != trigger


def test_repr_type():
    "Runs the test described in the title."
    t = Target("A", "Windows")
    assert repr(t).startswith(
        "<niveristand.systemdefinitionapi.Target(name=A, node_path=A) object at 0x"
    )


def test_str_type():
    "Runs the test described in the title."
    t = Target("A", "Windows")
    assert str(t).startswith(
        "<niveristand.systemdefinitionapi.Target(name=A, node_path=A) object at 0x"
    )


def test_repr_enum():
    "Runs the test described in the title."
    ea = AlarmingStepFunction.ENABLE_ALARM
    assert "<niveristand.systemdefinitionapi.AlarmingStepFunction.ENABLE_ALARM: 2>" == repr(ea)


def test_str_enum():
    "Runs the test described in the title."
    ea = AlarmingStepFunction.ENABLE_ALARM
    assert "AlarmingStepFunction.ENABLE_ALARM" == str(ea)


def test_int_enum():
    "Runs the test described in the title."
    ea = AlarmingStepFunction.ENABLE_ALARM
    assert 2 == int(ea)


def test_property_returns_python_enum_repr_does_not_raise_error():
    "Runs the test described in the title."
    c = CustomDeviceWaveform("name", "not-a-GUID", WaveformTypeDataType.COMPLEX_DOUBLE)
    str(c.data_type)  # should not raise an error


@pytest.mark.skip(reason="TODO: is this worth the trouble of implementing?")
def test_property_returns_python_enum_with_proper_repr():
    "Runs the test described in the title."
    c = CustomDeviceWaveform("name", "not-a-GUID", WaveformTypeDataType.COMPLEX_DOUBLE)
    assert str(WaveformTypeDataType.COMPLEX_DOUBLE) == str(c.data_type)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/sdf_api/test_sdf_api__out_param_types.py sha256=c6004345f4f247734865b7e5f5a8fa1e06bd0c4c6b0139f231a7968cffa57e4d bytes=5632 -->
## FILE: tests/sdf_api/test_sdf_api__out_param_types.py

- repository: `ni/niveristand-python`
- source_path: `tests/sdf_api/test_sdf_api__out_param_types.py`
- sha256: `c6004345f4f247734865b7e5f5a8fa1e06bd0c4c6b0139f231a7968cffa57e4d`
- bytes: 5632

````python
"""Tests the generated python code all different `out` types."""
from typing import Any, Sequence, Tuple

from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    Dictionary,
    Target,
    UserChannel,
    Utilities,
)


def test_out_bool_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_boolean("my_key", True)
    assert (True, True) == d.get_boolean("my_key")  # Does not throw Type Error


def test_out_double_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_double("my_key", 1.5)
    assert (True, 1.5) == d.get_double("my_key")  # Does not throw Type Error


def test_out_uint16_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_u16("my_key", 65535)
    assert (True, 65535) == d.get_u16("my_key")  # Does not throw Type Error


def test_out_uint32_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_u32("my_key", 4294967295)
    assert (True, 4294967295) == d.get_u32("my_key")  # Does not throw Type Error


def test_out_uint64_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_u64("my_key", 18446744073709551615)
    assert (True, 18446744073709551615) == d.get_u64("my_key")  # Does not throw Type Error


def test_out_int16_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_i16("my_key", -32768)
    assert (True, -32768) == d.get_i16("my_key")  # Does not throw Type Error


def test_out_int32_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_i32("my_key", -2147483648)
    assert (True, -2147483648) == d.get_i32("my_key")  # Does not throw Type Error


def test_out_int64_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_i64("my_key", -9223372036854775808)
    assert (True, -9223372036854775808) == d.get_i64("my_key")  # Does not throw Type Error


def test_out_str_param():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_string("my_key", "my_value")
    assert (True, "my_value") == d.get_string("my_key")  # Does not throw Type Error


def test_differs_only_by_out_str():
    "Runs the test described in the title."
    path = r"C:\dev\Some Project\my file.xml"
    expected = (r"C:\dev\Some Project", "my file.xml")
    assert expected == Utilities.strip_path(path)  # Does not throw Type Error


def _assert_dictionary_array(expected_array: Sequence[Any], actual_result: Tuple[bool, Any]):
    assert 2 == len(actual_result)
    assert actual_result[0]
    assert [type(x) for x in expected_array] == [type(x) for x in actual_result[1]]
    assert expected_array == [x for x in actual_result[1]]


def test_out_sequence_of_bool_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [True, True]
    d.add_boolean_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_boolean_array("my_key"))


def test_out_sequence_of_double_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [1.5, 1.5]
    d.add_double_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_double_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_uint16_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [65535, 65535]
    d.add_u16_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_u16_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_uint32_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [4294967295, 4294967295]
    d.add_u32_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_u32_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_uint64_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [18446744073709551615, 18446744073709551615]
    d.add_u64_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_u64_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_int16_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [-32768, -32768]
    d.add_i16_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_i16_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_int32_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [-2147483648, -2147483648]
    d.add_i32_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_i32_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_int64_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = [-9223372036854775808, -9223372036854775808]
    d.add_i64_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_i64_array("my_key"))  # Does not throw Type Error


def test_out_sequence_of_str_param():
    "Runs the test described in the title."
    d = Dictionary()
    vals = ["my_value", "my_value"]
    d.add_string_array("my_key", vals)
    _assert_dictionary_array(vals, d.get_string_array("my_key"))  # Does not throw Type Error


def test_out_BaseNode_param():  # noqa N802 (references class names)
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    u = UserChannel("uc1", "description", "volts", 3.3)
    ucs = t.get_user_channels()
    ucs.add_user_channel(u)
    assert (True, ucs) == u.get_parent()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/sdf_api/test_sdf_api__overloads.py sha256=dab96edb0799130ec831b26af0de7d98091c7bf6060e2fb3239b456b7542c6ad bytes=5037 -->
## FILE: tests/sdf_api/test_sdf_api__overloads.py

- repository: `ni/niveristand-python`
- source_path: `tests/sdf_api/test_sdf_api__overloads.py`
- sha256: `dab96edb0799130ec831b26af0de7d98091c7bf6060e2fb3239b456b7542c6ad`
- bytes: 5037

````python
"""Tests the generated python code for method overload resolution."""
import pytest
from niveristand import VeriStandSdfError  # noqa: I100, E402
from niveristand.systemstorage import ChannelType  # noqa: I100, E402
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    Alarm,
    AlarmMode,
    AlarmPriority,
    AlarmState,
    Dictionary,
    Procedure,
    Target,
    UserChannel,
    Utilities,
)


def test_out_empty_sequence_resolves():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_string_array("my_key", [])
    actual = d.get_string_array("my_key")  # Does not throw Type Error
    assert 2 == len(actual)
    assert actual[0]
    assert not len(actual[1])


def test_error_out_parameter_given_success_condition_does_not_throw():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    u = UserChannel("uc1", "description", "volts", 3.3)
    assert t.get_user_channels().add_user_channel(u)


def test_error_out_parameter_given_error_condition_throws_error():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    try:
        t.get_user_channels().add_user_channel(None)
        raise AssertionError("Did not throw")
    except Exception as e:
        assert VeriStandSdfError == type(e)  # noqa: E721 - we want to directly compare types
        assert "-307676 (InputParameterInvalid): Input UserChannel cannot be null." == str(e)


def _add_new_alarm(target: Target):
    return target.get_alarms().add_new_alarm(
        "MyAlarm",
        "desc",
        UserChannel("uc1", "description", "volts", 3.3),
        2.5,
        1,
        Procedure("name", "desc"),
        AlarmMode.NORMAL,
        AlarmState.ENABLED,
        AlarmPriority.LOW,
        0,
        "tripped!",
    )


def test_add_new_alarm_given_success_condition_does_not_throw():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    a = _add_new_alarm(t)
    # if we call the `out Error` overload we'll get back an Alarm and not a bool
    assert Alarm == type(a)  # noqa: E721 - we want to directly compare types


def test_add_new_alarm_given_error_condition_throws_error():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    try:
        _add_new_alarm(t)
        _add_new_alarm(t)
        raise AssertionError("Did not throw")
    except Exception as e:
        assert VeriStandSdfError == type(e)  # noqa: E721 - we want to directly compare types


def test_non_final_out_error_param():
    "Runs the test described in the title."
    try:
        Utilities.deserialize_slsc("does_not_exist", ChannelType("test", "test"))
        raise AssertionError("Did not throw")
    except Exception as e:
        assert VeriStandSdfError == type(e)  # noqa: E721 - we want to directly compare types


def test_get_node_errors_given_success_condition_returns_empty_list():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    # an empty list counts as `false` in if statements but isn't None in case folks expect a list
    assert [] == t.get_node_errors()


@pytest.mark.skip(reason="TODO: is it worth implementing this test?")
def test_get_node_errors_given_error_condition_throws_error():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    try:
        t.get_node_errors()
        raise AssertionError("Did not throw")
    except Exception as e:
        assert VeriStandSdfError == type(e)  # noqa: E721 - we want to directly compare types


def test_method_overload_only_differs_by_str_out_parameter_false_case():
    "Runs the test described in the title."
    c = ChannelType("test", "test")
    assert (False, "") == c.get_dependent_node_value_str("none")


def test_method_overload_only_differs_by_str_out_parameter_true_case():
    "Runs the test described in the title."
    c1 = ChannelType("base", "base")
    c2 = ChannelType("dependent", "dependent")
    c1.set_dependent_node_value("test", c2)
    assert (True, "dependent") == c1.get_dependent_node_value_str("test")


def test_method_overload_only_differs_by_BaseNode_out_parameter_false_case():  # noqa N802 (references class names)
    "Runs the test described in the title."
    c = ChannelType("test", "test")
    assert (False, None) == c.get_dependent_node_value_basenodetype("none")


def test_method_overload_only_differs_by_BaseNode_out_parameter_true_case():  # noqa N802 (references class names)
    "Runs the test described in the title."
    c1 = ChannelType("base", "base")
    c2 = ChannelType("dependent", "dependent")
    c1.set_dependent_node_value("test", c2)
    result_bool, result_node = c1.get_dependent_node_value_basenodetype("test")
    assert result_bool
    assert ChannelType == type(result_node)
    assert (c2.name, c2.node_path) == (result_node.name, result_node.node_path)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/sdf_api/test_sdf_api__overloads__save_sdf.py sha256=d870eb5902098af925ed9c3d8f4a06d6e572a89fb9e29bedda6df91fa7a54e2d bytes=1921 -->
## FILE: tests/sdf_api/test_sdf_api__overloads__save_sdf.py

- repository: `ni/niveristand-python`
- source_path: `tests/sdf_api/test_sdf_api__overloads__save_sdf.py`
- sha256: `d870eb5902098af925ed9c3d8f4a06d6e572a89fb9e29bedda6df91fa7a54e2d`
- bytes: 1921

````python
"""Tests the generated python code for method overload resolution."""
import os

import pytest
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    SystemDefinition,
)


def test_save_system_definition_file_same_filename():
    "Runs the test described in the title."
    try:
        sdf_path = os.path.join(os.path.dirname(__file__), "test-original.nivssdf")
        if os.path.exists(sdf_path):
            os.remove(sdf_path)

        sdf = SystemDefinition("name", "", "", "", "", "Windows", sdf_path)

        assert not os.path.exists(sdf_path)
        sdf.save_system_definition_file()
        assert os.path.exists(sdf_path)
    except Exception as e:
        if type(e).__name__ == "DllNotFoundException":
            pytest.skip("VeriStand installation or vsdev required for NIVeriStand_util.dll")
        else:
            raise


# AB#2583012: save_system_definition_file is not respecting file path argument
def test_save_system_definition_file_different_filename():
    "Runs the test described in the title."
    try:
        original_sdf_path = os.path.join(os.path.dirname(__file__), "test-original.nivssdf")
        alternate_sdf_path = os.path.join(os.path.dirname(__file__), "test-alternate.nivssdf")
        if os.path.exists(original_sdf_path):
            os.remove(original_sdf_path)
        if os.path.exists(alternate_sdf_path):
            os.remove(alternate_sdf_path)

        sdf = SystemDefinition("name", "", "", "", "", "Windows", original_sdf_path)

        sdf.save_system_definition_file(alternate_sdf_path)
        assert os.path.exists(alternate_sdf_path)
        assert not os.path.exists(original_sdf_path)
    except Exception as e:
        if type(e).__name__ == "DllNotFoundException":
            pytest.skip("VeriStand installation or vsdev required for NIVeriStand_util.dll")
        else:
            raise
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/sdf_api/test_sdf_api__unwrap.py sha256=de5e2dd36460cabd761cd06075aeae5ab51ffd9eb50ca01985f0de305058c763 bytes=6820 -->
## FILE: tests/sdf_api/test_sdf_api__unwrap.py

- repository: `ni/niveristand-python`
- source_path: `tests/sdf_api/test_sdf_api__unwrap.py`
- sha256: `de5e2dd36460cabd761cd06075aeae5ab51ffd9eb50ca01985f0de305058c763`
- bytes: 6820

````python
"""Tests the generated python code for AB#2359562: Unwrap wrapped types..."""
import pytest
from niveristand.systemstorage import (  # noqa: I100, E402
    ChannelType,
    OnNodeChangeEventArgs,
    WaveformTypeDataType,
)
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    Alias,
    CallProcedure,
    Channel,
    ConditionStepComparison,
    CustomDeviceChannel,
    CustomDeviceWaveform,
    LookupTable,
    LUTValue,
    PolynomialScale,
    Procedure,
    SetMultipleVariables,
    Target,
    UserChannel,
)
from niveristand.systemdefinitionapi.modelsupport import (
    VsModelFeatureSet,
    VsModelJsonFileDescriptor,
    VsModelParameter,
)

_random_guid = "1de25881-7f05-49de-90d2-ff0720ee77e2"


def test_property_settter_enum_passed():
    "Runs the test described in the title."
    c = CustomDeviceWaveform("name", _random_guid, WaveformTypeDataType.COMPLEX_DOUBLE)
    assert c.data_type == WaveformTypeDataType.COMPLEX_DOUBLE
    c.data_type = WaveformTypeDataType.DOUBLE
    assert c.data_type == WaveformTypeDataType.DOUBLE


def test_property_setter_does_not_unwrap_primitive_element():
    "Runs the test described in the title."
    c = CustomDeviceChannel("cdc", "775506CE-1485-13A6-56A13E7139081FC2")
    assert _random_guid != c.type_guid
    c.type_guid = _random_guid
    assert _random_guid == c.type_guid


def test_property_setter_unwraps_veristand_elements():
    "Runs the test described in the title."
    a = Alias("alias", "", "unset_path")
    uc = UserChannel("uc1", "", "V", 3.3)
    a.linked_channel = uc
    assert uc == a.linked_channel


@pytest.mark.skip(reason="somewhat difficult to support List<T>, only used in model support")
def test_property_setter_unwraps_to_dotnet_generic_list_of_veristand_elements():
    "Runs the test described in the title."
    v = VsModelJsonFileDescriptor()
    params = [VsModelParameter(), VsModelParameter()]
    v.parameters = params
    pass  # no type error


def test_property_setter_unwraps_sequence_of_veristand_elements():
    "Runs the test described in the title."
    scaled = [3.5, 9.0]
    values = [LUTValue(), LUTValue()]
    values[0].scaled = scaled[0]
    values[1].scaled = scaled[1]
    lt = LookupTable("name")
    lt.lookup_table_values = values
    # instances returned aren't the same as passed in, so we can't compare LUTValues directly
    assert scaled == [x.scaled for x in lt.lookup_table_values]


def test_property_setter_passes_empty_sequence_of_veristand_elements():
    "Runs the test described in the title."
    lt = LookupTable("name")
    lt.lookup_table_values = []
    assert 0 == len(lt.lookup_table_values)


@pytest.mark.skip(reason="TODO: implement test? Only matters for Inport and Outport")
def test_property_setter_passes_2d_dotnet_array():
    "Runs the test described in the title."
    raise NotImplementedError()


@pytest.mark.skip(reason="TODO: implement test? Only matters for Inport and Outport")
def test_property_setter_2d_array_given_sequence_raises_type_error():
    "Runs the test described in the title."
    raise NotImplementedError()


def test_method_enum_passed():
    "Runs the test described in the title."
    p = Procedure("name", "desc")
    cp = CallProcedure("cp1", "first", p)
    assert p.add_command(cp)
    assert p.add_new_condition("name", "", p, ConditionStepComparison.EQUAL, 3.5, cp)


def test_method_unwraps_only_veristand_elements():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    u = UserChannel("uc1", "description", "volts", 3.3)
    assert t.get_user_channels().add_user_channel(u)


def test_method_unwraps_sequence_of_veristand_elements():
    "Runs the test described in the title."
    p = Procedure("name", "desc")
    cps = [CallProcedure("cp1", "first", p), CallProcedure("cp2", "second", p)]
    for cp in reversed(cps):
        assert p.add_command(cp)
    assert p.reorder_command_list(cps)
    assert cps == p.get_command_list()


@pytest.mark.skip(reason="TODO: is this worth the trouble of implementing?")
def test_method_unwraps_ienumerable_of_veristand_elements():
    "Runs the test described in the title."
    # would use Model.import_parameters() or SystemDefinitionExtensions.get_descendant_channels()
    raise NotImplementedError()


def test_method_passes_empty_sequence_of_veristand_elements():
    "Runs the test described in the title."
    p = Procedure("name", "desc")
    assert 0 == len(p.get_command_list())
    assert p.reorder_command_list([])
    assert 0 == len(p.get_command_list())


def test_constructor_enum_passed():
    "Runs the test described in the title."
    CustomDeviceWaveform("name", _random_guid, WaveformTypeDataType.COMPLEX_DOUBLE)
    pass  # Should not raise TypeError


def test_constructor_mix_of_primitive_and_veristand_types_are_properly_passed():
    "Runs the test described in the title."
    uc = UserChannel("uc1", "", "V", 3.3)
    a = Alias("alias", "", uc)
    assert "alias" == a.node_path
    assert uc == a.linked_channel


def test_constructor_does_not_unwrap_primitive_element():
    "Runs the test described in the title."
    coeff = [1.5, 2.25, 3.5]
    reverse_coeff = [9.75, 7.5, -1.5]
    scale = PolynomialScale("name", coeff, reverse_coeff, "unit")
    assert coeff == list(scale.polynomial_coeff)
    assert reverse_coeff == list(scale.reverse_polynomial_coeff)


def test_constructor_unwraps_sequence_of_veristand_elements():
    "Runs the test described in the title."
    channels = [UserChannel("uc1", "", "V", 3.3), Channel(ChannelType("test", "test"))]
    values = [1.25, 2.5]
    vars = SetMultipleVariables("name", "desc", channels, values)
    assert channels == vars.channels
    assert values == [x for x in vars.values]


def test_constructor_passes_empty_sequence_of_veristand_elements():
    "Runs the test described in the title."
    vars = SetMultipleVariables("name", "desc", [], [])
    assert 0 == len(vars.channels)
    assert 0 == len(vars.values)


@pytest.mark.skip(reason="somewhat difficult, only used for one constructor we don't care about")
def test_constructor_unwraps_four_tuple_version():
    "Runs the test described in the title."
    # mostly testing that the constructor does not throw
    fs = VsModelFeatureSet((1, 2, 3, 4))
    assert fs.supports_non_virtual_bus
    assert not fs.generated_using_latest_addon_version


def test_constructor_does_not_unwrap_four_tuple_if_not_version():
    "Runs the test described in the title."
    non_version_tuple = (1, 2, 3, 4)
    args = OnNodeChangeEventArgs("action", non_version_tuple)
    assert non_version_tuple == tuple(args.m_data)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/sdf_api/test_sdf_api__wrap.py sha256=31ae0a7b3c283507c9f4fdb85dc4a97697c96631c348c2003bad78f587d72619 bytes=6781 -->
## FILE: tests/sdf_api/test_sdf_api__wrap.py

- repository: `ni/niveristand-python`
- source_path: `tests/sdf_api/test_sdf_api__wrap.py`
- sha256: `31ae0a7b3c283507c9f4fdb85dc4a97697c96631c348c2003bad78f587d72619`
- bytes: 6781

````python
"""Tests the generated python code for return value wrapping."""
import pytest
from niveristand.systemstorage import (  # noqa: I100, E402
    AliasType,
    ChannelType,
    VersionType,
    WaveformTypeDataType,
)
from niveristand.systemdefinitionapi import (  # noqa: I100, E402
    AlarmPriority,
    Alias,
    BaseNode,
    Channel,
    CustomDeviceChannel,
    CustomDeviceWaveform,
    Dictionary,
    DictionaryElement,
    NodeIDUtil,
    PolynomialScale,
    SetMultipleVariables,
    SLSCChassis,
    SystemDefinition,
    SystemDefinitionExtensions,
    Target,
    UserChannel,
    UserChannels,
    Utilities,
    ValueSource,
)

_random_guid = "1de25881-7f05-49de-90d2-ff0720ee77e2"
_alias_guid = "2c11e122-dad9-44da-989c-a66ff203fa31"


def test_enum_returns_its_value():
    "Runs the test described in the title."
    m = AlarmPriority.MEDIUM
    assert AlarmPriority == type(m)  # noqa: E721 - we want to directly compare types
    assert m == AlarmPriority.MEDIUM
    assert "<niveristand.systemdefinitionapi.AlarmPriority.MEDIUM: 1>" == repr(m)


def test_nested_enum_returns_its_value():
    "Runs the test described in the title."
    hia = SLSCChassis.SLSCChassisIDType.HOSTNAME_IP_ADDRESS
    ect = SLSCChassis.SLSCChassisType.E12001_CHASSIS_TYPE
    outer_type = "niveristand.systemdefinitionapi.SLSCChassis"
    assert f"<{outer_type}.SLSCChassisIDType.HOSTNAME_IP_ADDRESS: 1>" == repr(hia)
    assert f"<{outer_type}.SLSCChassisType.E12001_CHASSIS_TYPE: 0>" == repr(ect)


def test_property_base_type_return_value_returns_derived_type():
    "Runs the test described in the title."
    vs = ValueSource(UserChannel("uc1", "", "V", 3.3))
    assert UserChannel == type(vs.channel)  # noqa: E721 - we want to directly compare types


def test_property_sequence_of_base_type_return_value_returns_derived_types():
    "Runs the test described in the title."
    channels = [UserChannel("uc1", "", "V", 3.3), Channel(ChannelType("test", "test"))]
    vars = SetMultipleVariables("name", "desc", channels, [1.25, 2.5])
    assert [type(x) for x in channels] == [type(x) for x in vars.channels]


def test_property_return_of_primitive_element_is_not_wrapped():
    "Runs the test described in the title."
    u = UserChannel("uc1", "description", "volts", 3.3)
    assert "uc1" == u.name


def test_property_return_of_sequence_of_primitive_elements_none_are_wrapped():
    "Runs the test described in the title."
    coeff = [1.5, 2.25, 3.5]
    reverse_coeff = [9.75, 7.5, -1.5]
    scale = PolynomialScale("name", coeff, reverse_coeff, "unit")
    assert coeff == list(scale.polynomial_coeff)
    assert reverse_coeff == list(scale.reverse_polynomial_coeff)


def test_property_return_of_sequence_of_veristand_elements_all_are_wrapped():
    "Runs the test described in the title."
    d = Dictionary()
    d.add_boolean("a", True)
    d.add_i16("bb", 12345)
    d.add_double("ccc", 34.5)
    elements = d.elem
    assert 3 == len(elements)
    for e in elements:
        assert DictionaryElement == type(e)


def test_property_returns_python_enum():
    "Runs the test described in the title."
    c = CustomDeviceWaveform("name", _random_guid, WaveformTypeDataType.COMPLEX_DOUBLE)
    assert WaveformTypeDataType.COMPLEX_DOUBLE == c.data_type


def test_property_returns_version():
    "Runs the test described in the title."
    sdf = SystemDefinition(
        "name", "desc", "creator", "", "Controller", "Windows", r"C:\does_not_exist"
    )
    assert (2020, 0, 0, 0) == sdf.version
    assert "(2020, 0, 0, 0)" == str(sdf.version)


@pytest.mark.skip(reason="TODO: implement test? Only matters for Inport and Outport")
def test_property_returns_2d_array():
    "Runs the test described in the title."
    raise NotImplementedError()


def test_method_base_type_return_value_returns_derived_type():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    u = UserChannel("uc1", "description", "volts", 3.3)
    ucs = t.get_user_channels()
    ucs.add_user_channel(u)
    assert ucs == SystemDefinitionExtensions.get_parent(u)
    assert (True, ucs) == u.get_parent()


def test_method_sequence_of_base_type_return_value_returns_derived_types():
    "Runs the test described in the title."
    alias_core = AliasType("name", _alias_guid)
    alias = NodeIDUtil.id_to_base_node(alias_core.id)
    assert Alias == type(alias)


def test_method_return_of_primitive_element_is_not_wrapped():
    "Runs the test described in the title."
    u = UserChannel("uc1", "description", "volts", 3.3)
    assert "" == u.get_document_path()


def test_method_return_of_veristand_element_is_wrapped():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    uc = t.get_user_channels()
    assert UserChannels == type(uc)


def test_method_return_of_sequence_of_primitive_elements_none_are_wrapped():
    "Runs the test described in the title."
    b = [True, False, False, True]
    d = Dictionary()
    d.add_boolean_array("bools", b)
    actual_success, actual_array = d.get_boolean_array("bools")
    assert (True, b) == (actual_success, list(actual_array))


def test_method_return_of_sequence_of_veristand_elements_all_are_wrapped():
    "Runs the test described in the title."
    c = CustomDeviceChannel("cdc", "775506CE-1485-13A6-56A13E7139081FC2")
    d1, d2 = Dictionary(), Dictionary()
    d1.add_boolean("a", True)
    d2.add_i16("bb", 12345)
    c.set_dictionary_array_property("dict", [d1, d2])
    actual = c.get_dictionary_array_property("dict")
    assert 2 == len(actual)
    assert (True, [Dictionary, Dictionary]) == (actual[0], [type(x) for x in actual[1]])
    assert [("a", True), ("bb", 12345)] == [(de.key, de.item) for d in actual[1] for de in d.elem]


def test_method_void_return_primitive_out_only_out_returned():
    "Runs the test described in the title."
    a = AliasType("name", _alias_guid)
    assert ([], []) == a.get_node_properties()


def test_method_return_of_ienumerable_of_veristand_elements_all_are_wrapped():
    "Runs the test described in the title."
    t = Target("my target", "Windows")
    results = SystemDefinitionExtensions.get_descendant_channels(t)
    assert len(results)
    assert all(isinstance(result, BaseNode) for result in results)
    assert list == type(results)


def test_method_returns_version():
    "Runs the test described in the title."
    vt = VersionType()
    vt.major = 3
    vt.minor = 2
    vt.fix = 1
    vt.build = 456
    v = Utilities.version_type_to_version(vt)
    assert (3, 2, 1, 456) == v
    assert "(3, 2, 1, 456)" == str(v)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/setup/test_run_sequence.py sha256=e1d0760eaed69a9467cc70b08e2c4f917bdb72ab4430084410567afbae64e1b5 bytes=579 -->
## FILE: tests/setup/test_run_sequence.py

- repository: `ni/niveristand-python`
- source_path: `tests/setup/test_run_sequence.py`
- sha256: `e1d0760eaed69a9467cc70b08e2c4f917bdb72ab4430084410567afbae64e1b5`
- bytes: 579

````python
import tempfile
from niveristand import _decorators
from niveristand import realtimesequencetools
from testutilities import rtseqrunner


@_decorators.nivs_rt_sequence
def simple():
    return 1.0


def test_run_simple():
    tempfolder = tempfile.mkdtemp()
    filename = realtimesequencetools.save_py_as_rtseq(simple, tempfolder)
    rtseq_result = rtseqrunner.run_rtseq_local(filename, [], [])
    py_result = simple()
    assert rtseq_result.Value == py_result


def test_call_assert_helper():
    rtseqrunner.assert_run_python_equals_rtseq(simple, 1.0)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/setup/test_validatesetup.py sha256=94a8fcf3837c6cade87c126b00623fe7048ecc1dce5d0d8953f1f1939629cd84 bytes=864 -->
## FILE: tests/setup/test_validatesetup.py

- repository: `ni/niveristand-python`
- source_path: `tests/setup/test_validatesetup.py`
- sha256: `94a8fcf3837c6cade87c126b00623fe7048ecc1dce5d0d8953f1f1939629cd84`
- bytes: 864

````python
from os import path
from testutilities import configutilities

__vs_binaries__ = ["NationalInstruments.VeriStand.dll"]


def _inc(x):
    return x + 1


def test_pass():
    """Just make sure asserts work."""
    assert _inc(4) == 5


def test_pythonnetworks():
    import clr

    clr.AddReference("System")
    from System import String

    s = String("teststring")
    assert "teststring" == str(s)


def test_binariesfound():
    folder = configutilities.getbinariesfolder()
    assert path.isdir(folder)
    for binary in __vs_binaries__:
        assert path.isfile(path.join(folder, binary))


def test_getinstalledbinariespath():
    from niveristand._internal import _get_install_path

    try:
        bindir = _get_install_path()
        assert bindir is not None
    except (IOError, WindowsError):
        pass
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_arithmetic_shift_left.py sha256=f0727df45e510ce2a5bcd25e7fba10913c6b3c74920a3b3199284a161a854e2c bytes=12232 -->
## FILE: tests/test_arithmetic_shift_left.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_arithmetic_shift_left.py`
- sha256: `f0727df45e510ce2a5bcd25e7fba10913c6b3c74920a3b3199284a161a854e2c`
- bytes: 12232

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import (
    BooleanValue,
    ChannelReference,
    DoubleValue,
    I32Value,
    I64Value,
    RealTimeSequence,
)
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = I32Value(5)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 << 3
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 << DoubleValue(3)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) << DoubleValue(3)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) << I32Value(3)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = BooleanValue(1) << BooleanValue(3)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) << I32Value(3)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_multiple_types():
    a = I32Value(0)
    a.value = 1 << I32Value(3) << 5
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_multiple_types1():
    a = I64Value(1)
    a.value = 1 << I64Value(5) << 3 << I32Value(7)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 << _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() << 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_use_rtseq2():
    a = DoubleValue(0)
    a.value = I32Value(1) << _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() << I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(1) << _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() << I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_with_parentheses():
    a = I32Value(0)
    a.value = 1 << (2 << 1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_with_parentheses1():
    a = DoubleValue(0)
    a.value = 1 << (DoubleValue(2) << I32Value(1))
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) << (I32Value(2) << 1.0) << DoubleValue(4)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_variables():
    a = I32Value(5)
    b = I32Value(0)
    b.value = 1 << a
    return b.value


@nivs_rt_sequence
def arithmetic_shift_left_variables1():
    a = I64Value(5)
    b = I64Value(0)
    b.value = 1 << a.value
    return b.value


@nivs_rt_sequence
def arithmetic_shift_left_variable_variable():
    a = I32Value(1)
    b = I64Value(3)
    c = I32Value(0)
    c.value = a.value << b.value
    return c.value


@nivs_rt_sequence
def arithmetic_shift_left_variable_variable1():
    a = I32Value(1)
    b = I64Value(3)
    c = DoubleValue(0)
    c.value = a.value << b.value
    return c.value


@nivs_rt_sequence
def arithmetic_shift_left_variable_rtseq():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = a.value << _return_constant()
    return b.value


@nivs_rt_sequence
def arithmetic_shift_left_variable_rtseq1():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = _return_constant() << a.value
    return b.value


@nivs_rt_sequence
def arithmetic_shift_left_to_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 << b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_binary_unary():
    a = I32Value(0)
    a.value = 3 << -1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_number():
    a = I32Value(1)
    a.value <<= 2
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_nivsdatatype():
    a = I32Value(1)
    a.value <<= I32Value(2)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_nivsdatatype1():
    a = I64Value(1)
    a.value <<= I64Value(2)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_nivsdatatype2():
    a = I64Value(1)
    a.value <<= I32Value(2)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_nivsdatatype3():
    a = I32Value(1)
    a.value <<= I64Value(2)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_nivsdatatype4():
    a = I32Value(1)
    a.value <<= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_variable():
    a = I32Value(1)
    b = I32Value(2)
    a.value <<= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_variable1():
    a = I64Value(1)
    b = I64Value(2)
    a.value <<= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_variable2():
    a = I32Value(1)
    b = I64Value(2)
    a.value <<= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_variable3():
    a = I64Value(1)
    b = I32Value(2)
    a.value <<= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_variable4():
    a = I32Value(1)
    b = DoubleValue(2)
    a.value <<= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_rtseq():
    a = I32Value(1)
    a.value <<= _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_parentheses():
    a = I32Value(1)
    a.value <<= (2 + I32Value(1)) + I64Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value <<= b.value
    return a.value


# <editor-fold desc=Invalid tests>
@nivs_rt_sequence
def arithmetic_shift_left_invalid_variables():
    return a.value << b


@nivs_rt_sequence
def arithmetic_shift_left_invalid_variables1():
    return a.value << b.value


@nivs_rt_sequence
def arithmetic_shift_left_to_None():
    a = DoubleValue(0)
    a.value = None << 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant << 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_complex_expr():
    a = DoubleValue(0)
    a.value = 1 << (2 if 2 < 3 else 4)
    return a.value


# </editor-fold>


run_tests = [
    (arithmetic_shift_left_simple_numbers, (), 8),
    (arithmetic_shift_left_nivsdatatype_nivsdatatype1, (), 8),
    (arithmetic_shift_left_nivsdatatype_nivsdatatype3, (), 8),
    (arithmetic_shift_left_variables, (), 32),
    (arithmetic_shift_left_variables1, (), 32),
    (arithmetic_shift_left_multiple_types, (), 256),
    (arithmetic_shift_left_multiple_types1, (), 32768),
    (arithmetic_shift_left_with_parentheses, (), 16),
    (arithmetic_shift_left_variable_variable, (), 8),
    (arithmetic_shift_left_variable_variable1, (), 8),
    (arithmetic_shift_left_augassign_number, (), 4),
    (arithmetic_shift_left_augassign_nivsdatatype, (), 4),
    (arithmetic_shift_left_augassign_nivsdatatype1, (), 4),
    (arithmetic_shift_left_augassign_nivsdatatype2, (), 4),
    (arithmetic_shift_left_augassign_nivsdatatype3, (), 4),
    (arithmetic_shift_left_augassign_variable, (), 4),
    (arithmetic_shift_left_augassign_variable1, (), 4),
    (arithmetic_shift_left_augassign_variable2, (), 4),
    (arithmetic_shift_left_augassign_variable3, (), 4),
    (arithmetic_shift_left_augassign_parentheses, (), 16),
    (arithmetic_shift_left_use_rtseq, (), 32),
    (arithmetic_shift_left_use_rtseq1, (), 10),
    (arithmetic_shift_left_use_rtseq2, (), 32),
    (arithmetic_shift_left_use_rtseq3, (), 10),
    (arithmetic_shift_left_use_rtseq4, (), 32),
    (arithmetic_shift_left_use_rtseq5, (), 10),
    (arithmetic_shift_left_variable_rtseq, (), 32),
    (arithmetic_shift_left_variable_rtseq1, (), 10),
    (arithmetic_shift_left_complex_expr, (), 4),
    (arithmetic_shift_left_augassign_rtseq, (), 32),
]

fail_transform_tests = [
    (arithmetic_shift_left_invalid_variables, (), TranslateError),
    (arithmetic_shift_left_invalid_variables1, (), TranslateError),
    (arithmetic_shift_left_num_nivsdatatype, (), VeristandError),  # cannot do shift left on Double
    (
        arithmetic_shift_left_nivsdatatype_nivsdatatype,
        (),
        VeristandError,
    ),  # cannot do shift left on Double
    (
        arithmetic_shift_left_nivsdatatype_nivsdatatype2,
        (),
        VeristandError,
    ),  # cannot do shift left on Boolean
    (arithmetic_shift_left_with_parentheses1, (), VeristandError),  # cannot do shift left on Double
    (arithmetic_shift_left_with_parentheses2, (), VeristandError),  # cannot do shift left on Double
    (
        arithmetic_shift_left_augassign_nivsdatatype4,
        (),
        VeristandError,
    ),  # cannot do shift left on Double
    (
        arithmetic_shift_left_augassign_variable4,
        (),
        VeristandError,
    ),  # cannot do shift left on Double
    (arithmetic_shift_left_to_channel_ref, (), VeristandError),  # cannot do shift left on Double
    (
        arithmetic_shift_left_augassign_channel_ref,
        (),
        VeristandError,
    ),  # cannot do shift left on Double
    (arithmetic_shift_left_to_None, (), TranslateError),
    (arithmetic_shift_left_invalid_rtseq_call, (), VeristandError),
    (arithmetic_shift_left_binary_unary, (), TranslateError),
]

py_only_errs = [
    (arithmetic_shift_left_nivsdatatype_nivsdatatype1, (), 8),  # cannot do shift left on float
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize(
    "func_name, params, expected_result", list(set(run_tests) - set(py_only_errs)), ids=idfunc
)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_arithmetic_shift_right.py sha256=957781e109f95e7c4522c01cf527299024e28cfabf02befc1e8da27c5dd78ea5 bytes=12404 -->
## FILE: tests/test_arithmetic_shift_right.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_arithmetic_shift_right.py`
- sha256: `957781e109f95e7c4522c01cf527299024e28cfabf02befc1e8da27c5dd78ea5`
- bytes: 12404

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import (
    BooleanValue,
    ChannelReference,
    DoubleValue,
    I32Value,
    I64Value,
    RealTimeSequence,
)
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = I32Value(5)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_simple_numbers():
    a = DoubleValue(0)
    a.value = 3 >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 3 >> DoubleValue(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(3) >> DoubleValue(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(3) >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = BooleanValue(3) >> BooleanValue(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(3) >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_multiple_types():
    a = I32Value(0)
    a.value = 15 >> I32Value(3) >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_multiple_types1():
    a = I64Value(0)
    a.value = 127 >> I64Value(2) >> 3 >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq():
    a = DoubleValue(1)
    a.value = 64 >> _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq2():
    a = DoubleValue(0)
    a.value = I32Value(64) >> _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(64) >> _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() >> I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_with_parentheses():
    a = I32Value(0)
    a.value = 1 >> (2 >> 1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_with_parentheses1():
    a = DoubleValue(0)
    a.value = 1 >> (DoubleValue(2) >> I32Value(1))
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) >> (I32Value(2) >> 1.0) >> DoubleValue(4)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_variables():
    a = I32Value(5)
    b = I32Value(0)
    b.value = 128 >> a
    return b.value


@nivs_rt_sequence
def arithmetic_shift_right_variables1():
    a = I64Value(5)
    b = I64Value(0)
    b.value = 128 >> a.value
    return b.value


@nivs_rt_sequence
def arithmetic_shift_right_variable_variable():
    a = I32Value(3)
    b = I64Value(1)
    c = I32Value(0)
    c.value = a.value >> b.value
    return c.value


@nivs_rt_sequence
def arithmetic_shift_right_variable_variable1():
    a = I32Value(3)
    b = I64Value(1)
    c = DoubleValue(0)
    c.value = a.value >> b.value
    return c.value


@nivs_rt_sequence
def arithmetic_shift_right_variable_rtseq():
    a = I32Value(64)
    b = DoubleValue(0)
    b.value = a.value >> _return_constant()
    return b.value


@nivs_rt_sequence
def arithmetic_shift_right_variable_rtseq1():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = _return_constant() >> a.value
    return b.value


@nivs_rt_sequence
def arithmetic_shift_right_to_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 >> b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_binary_unary():
    a = I32Value(0)
    a.value = 3 >> -1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_number():
    a = I32Value(2)
    a.value >>= 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype():
    a = I32Value(2)
    a.value >>= I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype1():
    a = I64Value(2)
    a.value >>= I64Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype2():
    a = I64Value(2)
    a.value >>= I32Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype3():
    a = I32Value(2)
    a.value >>= I64Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_nivsdatatype4():
    a = I32Value(2)
    a.value >>= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable():
    a = I32Value(2)
    b = I32Value(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable1():
    a = I64Value(2)
    b = I64Value(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable2():
    a = I32Value(2)
    b = I64Value(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable3():
    a = I64Value(2)
    b = I32Value(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_variable4():
    a = I32Value(2)
    b = DoubleValue(1)
    a.value >>= b.value
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_rtseq():
    a = I32Value(32987)
    a.value >>= _return_constant()
    return a.value


@nivs_rt_sequence
def arithmetic_shift_left_augassign_parentheses():
    a = I32Value(1024)
    a.value >>= (2 + I32Value(1)) + I64Value(1)
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_augassign_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value >>= b.value
    return a.value


# <editor-fold desc=Invalid tests>
@nivs_rt_sequence
def arithmetic_shift_right_invalid_variables():
    return a.value >> b


@nivs_rt_sequence
def arithmetic_shift_right_invalid_variables1():
    return a.value >> b.value


@nivs_rt_sequence
def arithmetic_shift_right_to_None():
    a = DoubleValue(0)
    a.value = None >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant >> 1
    return a.value


@nivs_rt_sequence
def arithmetic_shift_right_complex_expr():
    a = DoubleValue(0)
    a.value = 15 >> (2 if 2 < 3 else 4)
    return a.value


# </editor-fold>


run_tests = [
    (arithmetic_shift_right_simple_numbers, (), 1),
    (arithmetic_shift_right_nivsdatatype_nivsdatatype1, (), 1),
    (arithmetic_shift_right_nivsdatatype_nivsdatatype3, (), 1),
    (arithmetic_shift_right_variables, (), 4),
    (arithmetic_shift_right_variables1, (), 4),
    (arithmetic_shift_right_multiple_types, (), 0),
    (arithmetic_shift_right_multiple_types1, (), 1),
    (arithmetic_shift_right_with_parentheses, (), 0),
    (arithmetic_shift_right_variable_variable, (), 1),
    (arithmetic_shift_right_variable_variable1, (), 1),
    (arithmetic_shift_right_augassign_number, (), 1),
    (arithmetic_shift_right_augassign_nivsdatatype, (), 1),
    (arithmetic_shift_right_augassign_nivsdatatype1, (), 1),
    (arithmetic_shift_right_augassign_nivsdatatype2, (), 1),
    (arithmetic_shift_right_augassign_nivsdatatype3, (), 1),
    (arithmetic_shift_right_augassign_variable, (), 1),
    (arithmetic_shift_right_augassign_variable1, (), 1),
    (arithmetic_shift_right_augassign_variable2, (), 1),
    (arithmetic_shift_right_augassign_variable3, (), 1),
    (arithmetic_shift_left_augassign_parentheses, (), 64),
    (arithmetic_shift_right_use_rtseq, (), 2),
    (arithmetic_shift_right_use_rtseq1, (), 2),
    (arithmetic_shift_right_use_rtseq2, (), 2),
    (arithmetic_shift_right_use_rtseq3, (), 2),
    (arithmetic_shift_right_use_rtseq4, (), 2),
    (arithmetic_shift_right_use_rtseq5, (), 2),
    (arithmetic_shift_right_variable_rtseq, (), 2),
    (arithmetic_shift_right_variable_rtseq1, (), 2),
    (arithmetic_shift_right_complex_expr, (), 3),
    (arithmetic_shift_right_augassign_rtseq, (), 1030),
]

fail_transform_tests = [
    (arithmetic_shift_right_invalid_variables, (), TranslateError),
    (arithmetic_shift_right_invalid_variables1, (), TranslateError),
    (
        arithmetic_shift_right_num_nivsdatatype,
        (),
        VeristandError,
    ),  # cannot do shift right on Double
    (
        arithmetic_shift_right_nivsdatatype_nivsdatatype,
        (),
        VeristandError,
    ),  # cannot do shift right on Double
    (
        arithmetic_shift_right_nivsdatatype_nivsdatatype2,
        (),
        VeristandError,
    ),  # cannot do shift right on Boolean
    (
        arithmetic_shift_right_with_parentheses1,
        (),
        VeristandError,
    ),  # cannot do shift right on Double
    (
        arithmetic_shift_right_with_parentheses2,
        (),
        VeristandError,
    ),  # cannot do shift right on Double
    (
        arithmetic_shift_right_augassign_nivsdatatype4,
        (),
        VeristandError,
    ),  # cannot do shift right on Double
    (
        arithmetic_shift_right_augassign_variable4,
        (),
        VeristandError,
    ),  # cannot do shift right on Double
    (arithmetic_shift_right_to_channel_ref, (), VeristandError),  # cannot do shift right on Double
    (
        arithmetic_shift_right_augassign_channel_ref,
        (),
        VeristandError,
    ),  # cannot do shift right on Double
    (arithmetic_shift_right_to_None, (), TranslateError),
    (arithmetic_shift_right_invalid_rtseq_call, (), VeristandError),
    (arithmetic_shift_right_binary_unary, (), TranslateError),
]

py_only_errs = [
    (arithmetic_shift_right_nivsdatatype_nivsdatatype1, (), 1),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize(
    "func_name, params, expected_result", list(set(run_tests) - set(py_only_errs)), ids=idfunc
)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_binaryop_add.py sha256=1ee49cfe51f74b014b01cf2703a7f9e38a0b6572769b373c898a66b5d2861957 bytes=9321 -->
## FILE: tests/test_binaryop_add.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_binaryop_add.py`
- sha256: `1ee49cfe51f74b014b01cf2703a7f9e38a0b6572769b373c898a66b5d2861957`
- bytes: 9321

````python
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def add_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 + 2
    return a.value


@nivs_rt_sequence
def add_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 + DoubleValue(2)
    return a.value


@nivs_rt_sequence
def add_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) + DoubleValue(2)
    return a.value


@nivs_rt_sequence
def add_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) + I32Value(2)
    return a.value


@nivs_rt_sequence
def add_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(1) + DoubleValue(2)
    return a.value


@nivs_rt_sequence
def add_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) + I32Value(2)
    return a.value


@nivs_rt_sequence
def add_multiple_types():
    a = DoubleValue(0)
    a.value = 1 + DoubleValue(2) + 3.0
    return a.value


@nivs_rt_sequence
def add_multiple_types1():
    a = I32Value(0)
    a.value = 1 + I32Value(2) + 3.0 + DoubleValue(4)
    return a.value


@nivs_rt_sequence
def add_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 + _return_constant()
    return a.value


@nivs_rt_sequence
def add_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() + 1
    return a.value


@nivs_rt_sequence
def add_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) + _return_constant()
    return a.value


@nivs_rt_sequence
def add_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() + DoubleValue(1)
    return a.value


@nivs_rt_sequence
def add_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(1) + _return_constant()
    return a.value


@nivs_rt_sequence
def add_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() + I32Value(1)
    return a.value


@nivs_rt_sequence
def add_with_parentheses():
    a = DoubleValue(0)
    a.value = 1 + (2 + 3)
    return a.value


@nivs_rt_sequence
def add_with_parentheses1():
    a = DoubleValue(0)
    a.value = 1 + (DoubleValue(2) + I32Value(5))
    return a.value


@nivs_rt_sequence
def add_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) + (I32Value(2) + 3.0) + DoubleValue(4)
    return a.value


@nivs_rt_sequence
def add_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 + a
    return b.value


@nivs_rt_sequence
def add_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 + a.value
    return b.value


@nivs_rt_sequence
def add_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value + b.value
    return c.value


@nivs_rt_sequence
def add_variable_variable1():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value + b.value
    return c.value


@nivs_rt_sequence
def add_variable_rtseq():
    a = DoubleValue(1)
    b = DoubleValue(0)
    b.value = a.value + _return_constant()
    return b.value


@nivs_rt_sequence
def add_variable_rtseq1():
    a = DoubleValue(1)
    b = DoubleValue(0)
    b.value = _return_constant() + a.value
    return b.value


@nivs_rt_sequence
def add_to_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 + b.value
    return a.value


@nivs_rt_sequence
def add_binary_unary():
    a = DoubleValue(0)
    a.value = 2 + -1
    return a.value


@nivs_rt_sequence
def add_with_multiple_plus():
    a = DoubleValue(0)
    a.value = 1 + +2  # noqa: E225 it's ok to test this
    return a.value


@nivs_rt_sequence
def add_with_multiple_plus1():
    a = DoubleValue(0)
    a.value = 1 + ++2  # noqa: E225 it's ok to test this
    return a.value


@nivs_rt_sequence
def add_binary_unary_sequence():
    a = DoubleValue(0)
    a.value = 1 + -----2  # noqa: E225 it's ok to test this
    return a.value


@nivs_rt_sequence
def add_complex_expr():
    a = DoubleValue(0)
    a.value = 1 + (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_add_simple_numbers():
    a = DoubleValue(1)
    a.value += 2
    return a.value


@nivs_rt_sequence
def aug_add_num_nivsdatatype():
    a = DoubleValue(1)
    a.value += DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_add_use_rtseq():
    a = DoubleValue(1)
    a.value += _return_constant()
    return a.value


@nivs_rt_sequence
def aug_add_with_parentheses():
    a = DoubleValue(1)
    a.value += (I32Value(2) + 3.0) + DoubleValue(4)
    return a.value


@nivs_rt_sequence
def aug_add_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value += a.value
    return b.value


@nivs_rt_sequence
def aug_add_to_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value += b.value
    return a.value


@nivs_rt_sequence
def aug_add_unary():
    a = DoubleValue(1)
    a.value += -1
    return a.value


# </editor-fold>


# <editor-fold desc=Invalid tests>
@nivs_rt_sequence
def add_invalid_variables():
    return a.value + b


@nivs_rt_sequence
def add_invalid_variables1():
    return a.value + b.value


@nivs_rt_sequence
def add_to_None():
    a = DoubleValue(0)
    a.value = None + 1
    return a.value


@nivs_rt_sequence
def add_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant + 1
    return a.value


# </editor-fold>


run_tests = [
    (add_simple_numbers, (), 3),
    (add_num_nivsdatatype, (), 3),
    (add_nivsdatatype_nivsdatatype, (), 3),
    (add_nivsdatatype_nivsdatatype1, (), 3),
    (add_nivsdatatype_nivsdatatype2, (), 3),
    (add_nivsdatatype_nivsdatatype3, (), 3),
    (add_multiple_types, (), 6),
    (add_multiple_types1, (), 10),
    (add_with_parentheses, (), 6),
    (add_with_parentheses1, (), 8),
    (add_with_parentheses2, (), 10),
    (add_variables, (), 6),
    (add_variables1, (), 6),
    (add_variable_variable, (), 3),
    (add_variable_variable1, (), 3),
    (add_binary_unary, (), 1),
    (aug_add_simple_numbers, (), 3),
    (aug_add_variables, (), 6),
    (aug_add_num_nivsdatatype, (), 3),
    (aug_add_with_parentheses, (), 10),
    (aug_add_unary, (), 0),
    (add_complex_expr, (), 3),
    (add_use_rtseq, (), 6),
    (add_use_rtseq1, (), 6),
    (add_use_rtseq2, (), 6),
    (add_use_rtseq3, (), 6),
    (add_use_rtseq4, (), 6),
    (add_use_rtseq5, (), 6),
    (add_variable_rtseq, (), 6),
    (add_variable_rtseq1, (), 6),
    (aug_add_use_rtseq, (), 6),
    (add_to_channel_ref, (), 6),
    (aug_add_to_channel_ref, (), 6),
    (add_binary_unary_sequence, (), -1),
]

fail_transform_tests = [
    (add_invalid_variables, (), TranslateError),
    (add_invalid_variables1, (), TranslateError),
    (add_with_multiple_plus, (), VeristandError),  # "UnaryAdd not supported by SPE"
    (add_with_multiple_plus1, (), VeristandError),  # "UnaryAdd not supported by SPE"
    (add_to_None, (), TranslateError),
    (add_invalid_rtseq_call, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_binaryop_div.py sha256=b5494c2e3339173557d9ffb0a721932d709c43ee9d35b22c9b7036240adc268b bytes=8674 -->
## FILE: tests/test_binaryop_div.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_binaryop_div.py`
- sha256: `b5494c2e3339173557d9ffb0a721932d709c43ee9d35b22c9b7036240adc268b`
- bytes: 8674

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, I32Value, RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 0
b = 1


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def div_simple_numbers():
    a = DoubleValue(0)
    a.value = 1.0 / 2
    return a.value


@nivs_rt_sequence
def div_num_nivsdatatype():
    a = DoubleValue(0)
    b = DoubleValue(2)
    a.value = 1.0 / b.value
    return a.value


@nivs_rt_sequence
def div_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1.0) / DoubleValue(2)
    return a.value


@nivs_rt_sequence
def div_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) / I32Value(2)
    return a.value


@nivs_rt_sequence
def div_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(1) / DoubleValue(2)
    return a.value


@nivs_rt_sequence
def div_nivsdatatype_nivsdatatype3():
    a = I32Value(0)
    a.value = I32Value(2) / I32Value(1)
    return a.value


@nivs_rt_sequence
def div_multiple_types():
    a = DoubleValue(0)
    a.value = 1 / DoubleValue(2) / 3.0
    return a.value


@nivs_rt_sequence
def div_multiple_types1():
    a = I32Value(0)
    a.value = 8 / I32Value(2) / 2.0 / DoubleValue(2)
    return a.value


@nivs_rt_sequence
def div_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 / _return_constant()
    return a.value


@nivs_rt_sequence
def div_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() / 1
    return a.value


@nivs_rt_sequence
def div_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) / _return_constant()
    return a.value


@nivs_rt_sequence
def div_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() / DoubleValue(1)
    return a.value


@nivs_rt_sequence
def div_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(1) / _return_constant()
    return a.value


@nivs_rt_sequence
def div_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() / I32Value(1)
    return a.value


@nivs_rt_sequence
def div_with_parentheses():
    a = DoubleValue(0)
    a.value = 1.0 / (2.0 / 3)
    return a.value


@nivs_rt_sequence
def div_with_parentheses1():
    a = DoubleValue(1)
    a.value = 1 / (DoubleValue(2) / I32Value(5))
    return a.value


@nivs_rt_sequence
def div_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) / (I32Value(2) / 3.0) / DoubleValue(4)
    return a.value


@nivs_rt_sequence
def div_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 / a
    return b.value


@nivs_rt_sequence
def div_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 / a.value
    return b.value


@nivs_rt_sequence
def div_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value / b.value
    return c.value


@nivs_rt_sequence
def div_variable_variable1():
    a = DoubleValue(1)
    b = I32Value(2)
    c = DoubleValue(0)
    c.value = a.value / b.value
    return c.value


@nivs_rt_sequence
def div_variable_rtseq():
    a = DoubleValue(1)
    b = DoubleValue(0)
    b.value = a.value / _return_constant()
    return b.value


@nivs_rt_sequence
def div_variable_rtseq1():
    a = DoubleValue(1)
    b = DoubleValue(0)
    b.value = _return_constant() / a.value
    return b.value


@nivs_rt_sequence
def div_with_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 / b.value
    return a.value


@nivs_rt_sequence
def div_binary_unary():
    a = DoubleValue(0)
    a.value = 2 / -1
    return a.value


@nivs_rt_sequence
def div_complex_expr():
    a = DoubleValue(0)
    a.value = 1.0 / (2.0 if 2 < 3 else 4.0)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_div_simple_numbers():
    a = DoubleValue(1)
    a.value /= 2
    return a.value


@nivs_rt_sequence
def aug_div_num_nivsdatatype():
    a = DoubleValue(1)
    a.value /= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_div_use_rtseq():
    a = DoubleValue(1)
    a.value /= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_div_with_parentheses():
    a = DoubleValue(1)
    a.value /= (I32Value(2) / 3.0) / DoubleValue(4)
    return a.value


@nivs_rt_sequence
def aug_div_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value /= a.value
    return b.value


@nivs_rt_sequence
def aug_div_to_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value /= b.value
    return a.value


@nivs_rt_sequence
def aug_div_unary():
    a = DoubleValue(1)
    a.value /= -1
    return a.value


# </editor-fold>


# <editor-fold desc=Invalid tests>
@nivs_rt_sequence
def div_invalid_variables():
    return a / b


@nivs_rt_sequence
def div_invalid_variables1():
    return a.value / b.value


@nivs_rt_sequence
def div_with_None():
    a = DoubleValue(0)
    a.value = None / 1
    return a


@nivs_rt_sequence
def div_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant / 1
    return a


# </editor-fold>


run_tests = [
    (div_simple_numbers, (), 0.5),
    (div_num_nivsdatatype, (), 0.5),
    (div_nivsdatatype_nivsdatatype, (), 0.5),
    (div_nivsdatatype_nivsdatatype1, (), 0.5),
    (div_nivsdatatype_nivsdatatype2, (), 0.5),
    (div_nivsdatatype_nivsdatatype3, (), 2),
    (div_multiple_types, (), 0.5 / 3),
    (div_multiple_types1, (), 1),
    (div_with_parentheses, (), 1.5),
    (div_with_parentheses1, (), 2.5),
    (div_with_parentheses2, (), 3.0 / 8),
    (div_variables, (), 0.2),
    (div_variables1, (), 0.2),
    (div_variable_variable, (), 0.5),
    (div_variable_variable1, (), 0.5),
    (div_binary_unary, (), -2),
    (aug_div_simple_numbers, (), 0.5),
    (aug_div_variables, (), 0.2),
    (aug_div_num_nivsdatatype, (), 0.5),
    (aug_div_with_parentheses, (), 6.0),
    (aug_div_unary, (), -1),
    (div_complex_expr, (), 0.5),
    (div_use_rtseq, (), 0.2),
    (div_use_rtseq1, (), 5),
    (div_use_rtseq2, (), 0.2),
    (div_use_rtseq3, (), 5),
    (div_use_rtseq4, (), 0.2),
    (div_use_rtseq5, (), 5),
    (div_variable_rtseq, (), 0.2),
    (div_variable_rtseq1, (), 5),
    (aug_div_use_rtseq, (), 0.2),
    (div_with_channel_ref, (), 0.2),
    (aug_div_to_channel_ref, (), 0.2),
]

fail_transform_tests = [
    (div_invalid_variables, (), TranslateError),
    (div_invalid_variables1, (), TranslateError),
    (div_with_None, (), TranslateError),
    (div_invalid_rtseq_call, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_binaryop_modulo.py sha256=528c48ecaac3ff2f47ed2d879956a354e13e154b02907306915145c3edd7a253 bytes=10116 -->
## FILE: tests/test_binaryop_modulo.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_binaryop_modulo.py`
- sha256: `528c48ecaac3ff2f47ed2d879956a354e13e154b02907306915145c3edd7a253`
- bytes: 10116

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import (
    ChannelReference,
    DoubleValue,
    I32Value,
    I64Value,
    RealTimeSequence,
)
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 0
b = 1


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def modulo_simple_numbers():
    a = DoubleValue(0)
    a.value = 3 % 2
    return a.value


@nivs_rt_sequence
def modulo_num_nivsdatatype():
    a = DoubleValue(0)
    b = DoubleValue(2)
    a.value = 3 % b.value
    return a.value


@nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(5) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(5) % I32Value(2)
    return a.value


@nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(7) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_nivsdatatype_nivsdatatype3():
    a = I32Value(0)
    a.value = I32Value(7) % I32Value(2)
    return a.value


@nivs_rt_sequence
def modulo_multiple_types():
    a = DoubleValue(0)
    a.value = 7 % DoubleValue(4) % 2
    return a.value


@nivs_rt_sequence
def modulo_multiple_types1():
    a = I32Value(0)
    a.value = 12 % I32Value(7) % 3
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq():
    a = DoubleValue(0)
    a.value = 6 % _return_constant()
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() % 2
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(7) % _return_constant()
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(7) % _return_constant()
    return a.value


@nivs_rt_sequence
def modulo_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() % I32Value(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses():
    a = DoubleValue(0)
    a.value = 5 % (5 % 3)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses1():
    a = DoubleValue(1)
    a.value = 5 % (DoubleValue(5) % I32Value(3))
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses2():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % I64Value(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses3():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % I32Value(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses4():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % I32Value(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses5():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % I64Value(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses6():
    a = DoubleValue(0)
    a.value = I64Value(11) % (I32Value(11) % DoubleValue(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_with_parentheses7():
    a = DoubleValue(0)
    a.value = I32Value(11) % (I64Value(11) % DoubleValue(7)) % DoubleValue(2)
    return a.value


@nivs_rt_sequence
def modulo_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 7 % a
    return b.value


@nivs_rt_sequence
def modulo_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 7 % a.value
    return b.value


@nivs_rt_sequence
def modulo_variable_variable():
    a = DoubleValue(5)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value % b.value
    return c.value


@nivs_rt_sequence
def modulo_variable_variable1():
    a = DoubleValue(5)
    b = I32Value(2)
    c = DoubleValue(0)
    c.value = a.value % b.value
    return c.value


@nivs_rt_sequence
def modulo_variable_rtseq():
    a = DoubleValue(6)
    b = DoubleValue(0)
    b.value = a.value % _return_constant()
    return b.value


@nivs_rt_sequence
def modulo_variable_rtseq1():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = _return_constant() % a.value
    return b.value


@nivs_rt_sequence
def modulo_with_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 2.0
    localhost_wait()
    a.value = 3 % b.value
    return a.value


@nivs_rt_sequence
def modulo_binary_unary():
    a = DoubleValue(0)
    a.value = 5 % -2
    return a.value


@nivs_rt_sequence
def modulo_complex_expr():
    a = DoubleValue(0)
    a.value = 1 % (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_modulo_simple_numbers():
    a = DoubleValue(1)
    a.value %= 2
    return a.value


@nivs_rt_sequence
def aug_modulo_num_nivsdatatype():
    a = DoubleValue(1)
    a.value %= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_modulo_use_rtseq():
    a = DoubleValue(6)
    a.value %= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_modulo_with_parentheses():
    a = DoubleValue(5)
    a.value %= (I32Value(2) % 3.0) % DoubleValue(4)
    return a.value


@nivs_rt_sequence
def aug_modulo_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value %= a.value
    return b.value


@nivs_rt_sequence
def aug_modulo_to_channel_ref():
    a = DoubleValue(3)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 2.0
    localhost_wait()
    a.value %= b.value
    return a.value


@nivs_rt_sequence
def aug_modulo_unary():
    a = DoubleValue(5)
    a.value %= -2
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def modulo_invalid_variables():
    return a % b


@nivs_rt_sequence
def modulo_invalid_variables1():
    return a.value % b.value


@nivs_rt_sequence
def modulo_with_None():
    a = DoubleValue(0)
    a.value = None % 1
    return a


@nivs_rt_sequence
def modulo_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant % 1
    return a


# </editor-fold>


run_tests = [
    (modulo_simple_numbers, (), 1),
    (modulo_num_nivsdatatype, (), 1),
    (modulo_nivsdatatype_nivsdatatype, (), 1),
    (modulo_nivsdatatype_nivsdatatype1, (), 1),
    (modulo_nivsdatatype_nivsdatatype2, (), 1),
    (modulo_nivsdatatype_nivsdatatype3, (), 1),
    (modulo_multiple_types, (), 1),
    (modulo_multiple_types1, (), 2),
    (modulo_with_parentheses, (), 1),
    (modulo_with_parentheses1, (), 1),
    (modulo_with_parentheses2, (), 1),
    (modulo_with_parentheses3, (), 1),
    (modulo_with_parentheses4, (), 1),
    (modulo_with_parentheses5, (), 1),
    (modulo_with_parentheses6, (), 1),
    (modulo_with_parentheses7, (), 1),
    (modulo_variables, (), 2),
    (modulo_variables1, (), 2),
    (modulo_variable_variable, (), 1),
    (modulo_variable_variable1, (), 1),
    (aug_modulo_simple_numbers, (), 1),
    (aug_modulo_variables, (), 1),
    (aug_modulo_num_nivsdatatype, (), 1),
    (aug_modulo_with_parentheses, (), 1),
    (modulo_complex_expr, (), 1),
    (modulo_variable_rtseq, (), 1),
    (modulo_variable_rtseq1, (), 1),
    (modulo_use_rtseq, (), 1),
    (modulo_use_rtseq1, (), 1),
    (modulo_use_rtseq2, (), 2),
    (modulo_use_rtseq3, (), 1),
    (modulo_use_rtseq4, (), 2),
    (modulo_use_rtseq5, (), 1),
    (aug_modulo_use_rtseq, (), 1),
    (modulo_with_channel_ref, (), 1),
    (aug_modulo_to_channel_ref, (), 1),
    (modulo_binary_unary, (), 1),
    (aug_modulo_unary, (), 1),
]

py_only_different_behavior_tests = [
    (modulo_binary_unary, (), 1),
    (aug_modulo_unary, (), 1),
]

fail_transform_tests = [
    (modulo_invalid_variables, (), TranslateError),
    (modulo_invalid_variables1, (), TranslateError),
    (modulo_with_None, (), TranslateError),
    (modulo_invalid_rtseq_call, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize(
    "func_name, params, expected_result",
    list(set(run_tests) - set(py_only_different_behavior_tests)),
    ids=idfunc,
)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_binaryop_mult.py sha256=3be6c81968abe612295071fa63032991a19b570afcad816b3bdbe0f9d625717e bytes=8678 -->
## FILE: tests/test_binaryop_mult.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_binaryop_mult.py`
- sha256: `3be6c81968abe612295071fa63032991a19b570afcad816b3bdbe0f9d625717e`
- bytes: 8678

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, I32Value, RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 0
b = 1


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def mult_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 * 2
    return a.value


@nivs_rt_sequence
def mult_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 * DoubleValue(2)
    return a.value


@nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) * DoubleValue(2)
    return a.value


@nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) * I32Value(2)
    return a.value


@nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(1) * DoubleValue(2)
    return a.value


@nivs_rt_sequence
def mult_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) * I32Value(2)
    return a.value


@nivs_rt_sequence
def mult_multiple_types():
    a = DoubleValue(0)
    a.value = 1 * DoubleValue(2) * 3.0
    return a.value


@nivs_rt_sequence
def mult_multiple_types1():
    a = I32Value(0)
    a.value = 1 * I32Value(2) * 3.0 * DoubleValue(4)
    return a.value


@nivs_rt_sequence
def mult_use_rtseq():
    a = DoubleValue(0)
    a.value = 2 * _return_constant()
    return a.value


@nivs_rt_sequence
def mult_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() * 2
    return a.value


@nivs_rt_sequence
def mult_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(2) * _return_constant()
    return a.value


@nivs_rt_sequence
def mult_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() * DoubleValue(2)
    return a.value


@nivs_rt_sequence
def mult_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(2) * _return_constant()
    return a.value


@nivs_rt_sequence
def mult_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() * I32Value(2)
    return a.value


@nivs_rt_sequence
def mult_with_parentheses():
    a = DoubleValue(0)
    a.value = 1 * (2 * 3)
    return a.value


@nivs_rt_sequence
def mult_with_parentheses1():
    a = DoubleValue(1)
    a.value = 1 * (DoubleValue(2) * I32Value(5))
    return a.value


@nivs_rt_sequence
def mult_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) * (I32Value(2) * 3.0) * DoubleValue(4)
    return a.value


@nivs_rt_sequence
def mult_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 * a
    return b.value


@nivs_rt_sequence
def mult_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 * a.value
    return b.value


@nivs_rt_sequence
def mult_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value * b.value
    return c.value


@nivs_rt_sequence
def mult_variable_variable1():
    a = DoubleValue(1)
    b = I32Value(2)
    c = DoubleValue(0)
    c.value = a.value * b.value
    return c.value


@nivs_rt_sequence
def mult_variable_rtseq():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = a.value * _return_constant()
    return b.value


@nivs_rt_sequence
def mult_variable_rtseq1():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = _return_constant() * a.value
    return b.value


@nivs_rt_sequence
def mult_with_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 * b.value
    return a.value


@nivs_rt_sequence
def mult_binary_unary():
    a = DoubleValue(0)
    a.value = 2 * -1
    return a.value


@nivs_rt_sequence
def mult_complex_expr():
    a = DoubleValue(0)
    a.value = 1 * (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_mult_simple_numbers():
    a = DoubleValue(1)
    a.value *= 2
    return a.value


@nivs_rt_sequence
def aug_mult_num_nivsdatatype():
    a = DoubleValue(1)
    a.value *= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_mult_use_rtseq():
    a = DoubleValue(2)
    a.value *= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_mult_with_parentheses():
    a = DoubleValue(2)
    a.value *= (I32Value(1) * 3.0) * DoubleValue(4)
    return a.value


@nivs_rt_sequence
def aug_mult_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value *= a.value
    return b.value


@nivs_rt_sequence
def aug_mult_to_channel_ref():
    a = DoubleValue(2)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value *= b.value
    return a.value


@nivs_rt_sequence
def aug_mult_unary():
    a = DoubleValue(1)
    a.value *= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def mult_invalid_variables():
    return a * b


@nivs_rt_sequence
def mult_invalid_variables1():
    return a.value * b.value


@nivs_rt_sequence
def mult_with_None():
    a = DoubleValue(0)
    a.value = None * 1
    return a


@nivs_rt_sequence
def mult_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant * 1
    return a


# </editor-fold>


run_tests = [
    (mult_simple_numbers, (), 2),
    (mult_num_nivsdatatype, (), 2),
    (mult_nivsdatatype_nivsdatatype, (), 2),
    (mult_nivsdatatype_nivsdatatype1, (), 2),
    (mult_nivsdatatype_nivsdatatype2, (), 2),
    (mult_nivsdatatype_nivsdatatype3, (), 2),
    (mult_multiple_types, (), 6),
    (mult_multiple_types1, (), 24),
    (mult_with_parentheses, (), 6),
    (mult_with_parentheses1, (), 10),
    (mult_with_parentheses2, (), 24),
    (mult_variables, (), 5),
    (mult_variables1, (), 5),
    (mult_variable_variable, (), 2),
    (mult_variable_variable1, (), 2),
    (mult_binary_unary, (), -2),
    (aug_mult_simple_numbers, (), 2),
    (aug_mult_variables, (), 5),
    (aug_mult_num_nivsdatatype, (), 2),
    (aug_mult_with_parentheses, (), 24),
    (aug_mult_unary, (), -1),
    (mult_complex_expr, (), 2),
    (mult_variable_rtseq, (), 10),
    (mult_variable_rtseq1, (), 10),
    (mult_use_rtseq, (), 10),
    (mult_use_rtseq1, (), 10),
    (mult_use_rtseq2, (), 10),
    (mult_use_rtseq3, (), 10),
    (mult_use_rtseq4, (), 10),
    (mult_use_rtseq5, (), 10),
    (aug_mult_use_rtseq, (), 10),
    (mult_with_channel_ref, (), 5),
    (aug_mult_to_channel_ref, (), 10),
]

fail_transform_tests = [
    (mult_invalid_variables, (), TranslateError),
    (mult_invalid_variables1, (), TranslateError),
    (mult_with_None, (), TranslateError),
    (mult_invalid_rtseq_call, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_binaryop_pow.py sha256=441da93bf41fe5e297cc6ef296daee7c96c5adb1e728a69fe11245e8d28274cd bytes=8282 -->
## FILE: tests/test_binaryop_pow.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_binaryop_pow.py`
- sha256: `441da93bf41fe5e297cc6ef296daee7c96c5adb1e728a69fe11245e8d28274cd`
- bytes: 8282

````python
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, I32Value, RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 0
b = 1


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def exp_simple_numbers():
    a = DoubleValue(0)
    a.value = 2**2
    return a.value


@nivs_rt_sequence
def exp_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 2 ** DoubleValue(2)
    return a.value


@nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(2) ** DoubleValue(3)
    return a.value


@nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(2) ** I32Value(3)
    return a.value


@nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(2) ** DoubleValue(3)
    return a.value


@nivs_rt_sequence
def exp_nivsdatatype_nivsdatatype3():
    a = I32Value(0)
    a.value = I32Value(2) ** I32Value(3)
    return a.value


@nivs_rt_sequence
def exp_use_rtseq():
    a = DoubleValue(0)
    a.value = 2 ** _return_constant()
    return a.value


@nivs_rt_sequence
def exp_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() ** 2
    return a.value


@nivs_rt_sequence
def exp_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(2) ** _return_constant()
    return a.value


@nivs_rt_sequence
def exp_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() ** DoubleValue(2)
    return a.value


@nivs_rt_sequence
def exp_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(2) ** _return_constant()
    return a.value


@nivs_rt_sequence
def exp_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() ** I32Value(3)
    return a.value


@nivs_rt_sequence
def exp_with_parentheses():
    a = DoubleValue(0)
    a.value = 2 ** (2 + 3)
    return a.value


@nivs_rt_sequence
def exp_with_parentheses1():
    a = DoubleValue(1)
    a.value = 2 ** (DoubleValue(2) ** I32Value(2))
    return a.value


@nivs_rt_sequence
def exp_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) * (I32Value(2) ** 3.0) ** DoubleValue(2)
    return a.value


@nivs_rt_sequence
def exp_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 2**a
    return b.value


@nivs_rt_sequence
def exp_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 2**a.value
    return b.value


@nivs_rt_sequence
def exp_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(3)
    c = DoubleValue(0)
    c.value = a.value**b.value
    return c.value


@nivs_rt_sequence
def exp_variable_variable1():
    a = DoubleValue(2)
    b = I32Value(3)
    c = DoubleValue(0)
    c.value = a.value**b.value
    return c.value


@nivs_rt_sequence
def exp_variable_rtseq():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = a.value ** _return_constant()
    return b.value


@nivs_rt_sequence
def exp_variable_rtseq1():
    a = DoubleValue(2)
    b = DoubleValue(0)
    b.value = _return_constant() ** a.value
    return b.value


@nivs_rt_sequence
def exp_with_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 2**b.value
    return a.value


@nivs_rt_sequence
def exp_binary_unary():
    a = DoubleValue(0)
    a.value = 2**-1
    return a.value


@nivs_rt_sequence
def exp_complex_expr():
    a = DoubleValue(0)
    a.value = 3 ** (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_exp_simple_numbers():
    a = DoubleValue(2)
    a.value **= 2
    return a.value


@nivs_rt_sequence
def aug_exp_num_nivsdatatype():
    a = DoubleValue(3)
    a.value **= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_exp_use_rtseq():
    a = DoubleValue(2)
    a.value **= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_exp_with_parentheses():
    a = DoubleValue(2)
    a.value **= (I32Value(2) ** 3.0) ** DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_exp_variables():
    a = DoubleValue(5)
    b = DoubleValue(2)
    b.value **= a.value
    return b.value


@nivs_rt_sequence
def aug_exp_to_channel_ref():
    a = DoubleValue(2)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value **= b.value
    return a.value


@nivs_rt_sequence
def aug_exp_unary():
    a = DoubleValue(2)
    a.value **= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def exp_invalid_variables():
    return a**b


@nivs_rt_sequence
def exp_invalid_variables1():
    return a.value**b.value


@nivs_rt_sequence
def exp_with_None():
    a = DoubleValue(0)
    a.value = None**1
    return a


@nivs_rt_sequence
def exp_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant**1
    return a


# </editor-fold>


run_tests = [
    (exp_simple_numbers, (), 4),
    (exp_num_nivsdatatype, (), 4),
    (exp_nivsdatatype_nivsdatatype, (), 8),
    (exp_nivsdatatype_nivsdatatype1, (), 8),
    (exp_nivsdatatype_nivsdatatype2, (), 8),
    (exp_nivsdatatype_nivsdatatype3, (), 8),
    (exp_with_parentheses, (), 32),
    (exp_with_parentheses1, (), 16),
    (exp_with_parentheses2, (), 64),
    (exp_variables, (), 32),
    (exp_variables1, (), 32),
    (exp_variable_variable, (), 8),
    (exp_variable_variable1, (), 8),
    (exp_binary_unary, (), 0.5),
    (aug_exp_simple_numbers, (), 4),
    (aug_exp_variables, (), 32),
    (aug_exp_num_nivsdatatype, (), 9),
    (aug_exp_with_parentheses, (), float(2**64)),
    (aug_exp_unary, (), 0.5),
    (exp_complex_expr, (), 9),
    (exp_variable_rtseq, (), 32),
    (exp_variable_rtseq1, (), 25),
    (exp_use_rtseq, (), 32),
    (exp_use_rtseq1, (), 25),
    (exp_use_rtseq2, (), 32),
    (exp_use_rtseq3, (), 25),
    (exp_use_rtseq4, (), 32),
    (exp_use_rtseq5, (), 125),
    (aug_exp_use_rtseq, (), 32),
    (exp_with_channel_ref, (), 32),
    (aug_exp_to_channel_ref, (), 32),
]

fail_transform_tests = [
    (exp_invalid_variables, (), TranslateError),
    (exp_invalid_variables1, (), TranslateError),
    (exp_with_None, (), TranslateError),
    (exp_invalid_rtseq_call, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_binaryop_sub.py sha256=e751adacd9c221141c350825d1dd70531e6b049ffaca107f12a2840ecc9e7cad bytes=8906 -->
## FILE: tests/test_binaryop_sub.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_binaryop_sub.py`
- sha256: `e751adacd9c221141c350825d1dd70531e6b049ffaca107f12a2840ecc9e7cad`
- bytes: 8906

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, I32Value, RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def sub_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 - 2
    return a.value


def test_sub_simple_numbers():
    RealTimeSequence(sub_simple_numbers)


@nivs_rt_sequence
def sub_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 - DoubleValue(2)
    return a.value


@nivs_rt_sequence
def sub_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) - DoubleValue(2)
    return a.value


@nivs_rt_sequence
def sub_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) - I32Value(2)
    return a.value


@nivs_rt_sequence
def sub_nivsdatatype_nivsdatatype2():
    a = DoubleValue(0)
    a.value = I32Value(1) - DoubleValue(2)
    return a.value


@nivs_rt_sequence
def sub_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) - I32Value(2)
    return a.value


@nivs_rt_sequence
def sub_multiple_types():
    a = DoubleValue(0)
    a.value = 1 - DoubleValue(2) - 3.0
    return a.value


@nivs_rt_sequence
def sub_multiple_types1():
    a = I32Value(0)
    a.value = 1 - I32Value(2) - 3.0 - DoubleValue(4)
    return a.value


@nivs_rt_sequence
def sub_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 - _return_constant()
    return a.value


@nivs_rt_sequence
def sub_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() - 1
    return a.value


@nivs_rt_sequence
def sub_use_rtseq2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) - _return_constant()
    return a.value


@nivs_rt_sequence
def sub_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() - DoubleValue(1)
    return a.value


@nivs_rt_sequence
def sub_use_rtseq4():
    a = DoubleValue(0)
    a.value = I32Value(1) - _return_constant()
    return a.value


@nivs_rt_sequence
def sub_use_rtseq5():
    a = DoubleValue(0)
    a.value = _return_constant() - I32Value(1)
    return a.value


@nivs_rt_sequence
def sub_with_parentheses():
    a = DoubleValue(0)
    a.value = 1 - (2 - 3)
    return a.value


@nivs_rt_sequence
def sub_with_parentheses1():
    a = DoubleValue(0)
    a.value = 1 - (DoubleValue(2) - I32Value(5))
    return a.value


@nivs_rt_sequence
def sub_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(5) - (I32Value(2) - 3.0) - DoubleValue(4)
    return a.value


@nivs_rt_sequence
def sub_variables():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 - a
    return b.value


@nivs_rt_sequence
def sub_variables1():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = 1 - a.value
    return b.value


@nivs_rt_sequence
def sub_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value - b.value
    return c.value


@nivs_rt_sequence
def sub_variable_variable1():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(0)
    c.value = a.value - b.value
    return c.value


@nivs_rt_sequence
def sub_variable_rtseq():
    a = DoubleValue(1)
    b = DoubleValue(0)
    b.value = a.value - _return_constant()
    return b.value


@nivs_rt_sequence
def sub_variable_rtseq1():
    a = DoubleValue(1)
    b = DoubleValue(0)
    b.value = _return_constant() - a.value
    return b.value


@nivs_rt_sequence
def sub_to_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 - b.value
    return a.value


@nivs_rt_sequence
def sub_binary_unary():
    a = DoubleValue(0)
    a.value = 2 - -1
    return a.value


@nivs_rt_sequence
def sub_binary_unary_sequence():
    a = DoubleValue(0)
    a.value = 1 - -----2  # noqa: E225 it's ok to test this
    return a.value


@nivs_rt_sequence
def sub_complex_expr():
    a = DoubleValue(0)
    a.value = 1 - (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_sub_simple_numbers():
    a = DoubleValue(1)
    a.value -= 2
    return a.value


@nivs_rt_sequence
def aug_sub_num_nivsdatatype():
    a = DoubleValue(1)
    a.value -= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def aug_sub_use_rtseq():
    a = DoubleValue(1)
    a.value -= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_sub_with_parentheses():
    a = DoubleValue(1)
    a.value -= (I32Value(2) + 3.0) + DoubleValue(4)
    return a.value


@nivs_rt_sequence
def aug_sub_variables():
    a = DoubleValue(5)
    b = DoubleValue(1)
    b.value -= a.value
    return b.value


@nivs_rt_sequence
def aug_sub_to_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value -= b.value
    return a.value


@nivs_rt_sequence
def aug_sub_unary():
    a = DoubleValue(1)
    a.value -= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def sub_invalid_variables():
    return a - b


@nivs_rt_sequence
def sub_invalid_variables1():
    return a.value - b.value


@nivs_rt_sequence
def sub_from_None():
    a = DoubleValue(0)
    a.value = None - 1
    return a.value


@nivs_rt_sequence
def sub_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant - 1
    return a.value


# </editor-fold>


run_tests = [
    (sub_simple_numbers, (), -1),
    (sub_num_nivsdatatype, (), -1),
    (sub_nivsdatatype_nivsdatatype, (), -1),
    (sub_nivsdatatype_nivsdatatype1, (), -1),
    (sub_nivsdatatype_nivsdatatype2, (), -1),
    (sub_nivsdatatype_nivsdatatype3, (), -1),
    (sub_multiple_types, (), -4),
    (sub_multiple_types1, (), -8),
    (sub_with_parentheses, (), 2),
    (sub_with_parentheses1, (), 4),
    (sub_with_parentheses2, (), 2),
    (sub_variables, (), -4),
    (sub_variables1, (), -4),
    (sub_variable_variable, (), -1),
    (sub_variable_variable1, (), -1),
    (sub_binary_unary, (), 3),
    (sub_binary_unary_sequence, (), 3),
    (aug_sub_simple_numbers, (), -1),
    (aug_sub_num_nivsdatatype, (), -1),
    (aug_sub_with_parentheses, (), -8),
    (aug_sub_variables, (), -4),
    (aug_sub_unary, (), 2),
    (sub_complex_expr, (), -1),
    (sub_use_rtseq, (), -4),
    (sub_use_rtseq1, (), 4),
    (sub_use_rtseq2, (), -4),
    (sub_use_rtseq3, (), 4),
    (sub_use_rtseq4, (), -4),
    (sub_use_rtseq5, (), 4),
    (sub_variable_rtseq, (), -4),
    (sub_variable_rtseq1, (), 4),
    (aug_sub_use_rtseq, (), -4),
    (sub_to_channel_ref, (), -4.0),
    (aug_sub_to_channel_ref, (), -4.0),
]

fail_transform_tests = [
    (sub_invalid_variables, (), TranslateError),
    (sub_invalid_variables1, (), TranslateError),
    (sub_from_None, (), TranslateError),
    (sub_invalid_rtseq_call, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_bitwise_and.py sha256=d9dbbf907a37562d09a9e7b98ab2b52eb96be25110718cfa845bc175366319ce bytes=9530 -->
## FILE: tests/test_bitwise_and.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_bitwise_and.py`
- sha256: `d9dbbf907a37562d09a9e7b98ab2b52eb96be25110718cfa845bc175366319ce`
- bytes: 9530

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = I32Value(5)
    return a.value


@nivs_rt_sequence
def bitwise_and_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 & 3
    return a.value


@nivs_rt_sequence
def bitwise_and_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 & DoubleValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_and_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) & DoubleValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_and_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) & I32Value(3)
    return a.value


@nivs_rt_sequence
def bitwise_and_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = BooleanValue(1) & BooleanValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_and_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) & I32Value(3)
    return a.value


@nivs_rt_sequence
def bitwise_and_multiple_types():
    a = I32Value(0)
    a.value = 1 & I32Value(3) & 5
    return a.value


@nivs_rt_sequence
def bitwise_and_multiple_types1():
    a = I64Value(1)
    a.value = 1 & I64Value(5) & 3 & I32Value(7)
    return a.value


@nivs_rt_sequence
def bitwise_and_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 & _return_constant()
    return a.value


@nivs_rt_sequence
def bitwise_and_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() & 1
    return a.value


@nivs_rt_sequence
def bitwise_and_use_rtseq2():
    a = DoubleValue(0)
    a.value = I32Value(1) & _return_constant()
    return a.value


@nivs_rt_sequence
def bitwise_and_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() & I32Value(1)
    return a.value


@nivs_rt_sequence
def bitwise_and_with_parentheses():
    a = I32Value(0)
    a.value = 1 & (5 & 3)
    return a.value


@nivs_rt_sequence
def bitwise_and_with_parentheses1():
    a = DoubleValue(0)
    a.value = 1 & (DoubleValue(3) & I32Value(5))
    return a.value


@nivs_rt_sequence
def bitwise_and_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) & (I32Value(2) & 3.0) & DoubleValue(4)
    return a.value


@nivs_rt_sequence
def bitwise_and_variables():
    a = I32Value(5)
    b = I32Value(0)
    b.value = 1 & a
    return b.value


@nivs_rt_sequence
def bitwise_and_variables1():
    a = I64Value(5)
    b = I64Value(0)
    b.value = 1 & a.value
    return b.value


@nivs_rt_sequence
def bitwise_and_variable_variable():
    a = I32Value(1)
    b = I64Value(3)
    c = I32Value(0)
    c.value = a.value & b.value
    return c.value


@nivs_rt_sequence
def bitwise_and_variable_variable1():
    a = I32Value(1)
    b = I64Value(3)
    c = DoubleValue(0)
    c.value = a.value & b.value
    return c.value


@nivs_rt_sequence
def bitwise_and_variable_rtseq():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = a.value & _return_constant()
    return b.value


@nivs_rt_sequence
def bitwise_and_variable_rtseq1():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = _return_constant() & a.value
    return b.value


@nivs_rt_sequence
def bitwise_and_to_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 & b.value
    return a.value


@nivs_rt_sequence
def bitwise_and_binary_unary():
    a = I32Value(0)
    a.value = 3 & -1
    return a.value


@nivs_rt_sequence
def bitwise_and_complex_expr():
    a = DoubleValue(0)
    a.value = 1 & (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_bitwise_and_simple_numbers():
    a = I32Value(7)
    a.value &= 3
    return a.value


@nivs_rt_sequence
def aug_bitwise_and_num_nivsdatatype():
    a = I32Value(1)
    a.value &= I32Value(3)
    return a.value


@nivs_rt_sequence
def aug_bitwise_and_use_rtseq():
    a = I32Value(1)
    a.value &= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_bitwise_and_with_parentheses():
    a = I32Value(7)
    a.value &= 1 & (5 & 3)
    return a.value


@nivs_rt_sequence
def aug_bitwise_and_variables():
    a = I32Value(7)
    b = I32Value(3)
    b.value &= a.value
    return b.value


@nivs_rt_sequence
def aug_bitwise_and_to_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value &= b.value
    return a.value


@nivs_rt_sequence
def aug_bitwise_and_unary():
    a = I32Value(3)
    a.value &= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def bitwise_and_invalid_variables():
    return a.value & b


@nivs_rt_sequence
def bitwise_and_invalid_variables1():
    return a.value & b.value


@nivs_rt_sequence
def bitwise_and_to_None():
    a = DoubleValue(0)
    a.value = None & 1
    return a.value


@nivs_rt_sequence
def bitwise_and_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant & 1
    return a.value


# </editor-fold>


run_tests = [
    (bitwise_and_simple_numbers, (), 1),
    (bitwise_and_nivsdatatype_nivsdatatype3, (), 1),
    (bitwise_and_variables, (), 1),
    (bitwise_and_variables1, (), 1),
    (bitwise_and_multiple_types, (), 1),
    (bitwise_and_multiple_types1, (), 1),
    (bitwise_and_with_parentheses, (), 1),
    (bitwise_and_variable_variable, (), 1),
    (bitwise_and_variable_variable1, (), 1),
    (bitwise_and_binary_unary, (), 3),
    (aug_bitwise_and_simple_numbers, (), 3),
    (aug_bitwise_and_variables, (), 3),
    (aug_bitwise_and_num_nivsdatatype, (), 1),
    (aug_bitwise_and_with_parentheses, (), 1),
    (aug_bitwise_and_unary, (), 3),
    (bitwise_and_complex_expr, (), 0),
    (bitwise_and_use_rtseq, (), 1),
    (bitwise_and_use_rtseq1, (), 1),
    (bitwise_and_use_rtseq2, (), 1),
    (bitwise_and_use_rtseq3, (), 1),
    (bitwise_and_variable_rtseq, (), 1),
    (bitwise_and_variable_rtseq1, (), 1),
    (aug_bitwise_and_use_rtseq, (), 1),
    (bitwise_and_num_nivsdatatype, (), 1.0),
    (bitwise_and_nivsdatatype_nivsdatatype, (), 1.0),
    (bitwise_and_nivsdatatype_nivsdatatype1, (), 1.0),
    (bitwise_and_nivsdatatype_nivsdatatype2, (), True),
    (bitwise_and_with_parentheses1, (), 1.0),
    (bitwise_and_with_parentheses2, (), 0.0),
    (bitwise_and_to_channel_ref, (), 1.0),
    (aug_bitwise_and_to_channel_ref, (), 1.0),
]

fail_transform_tests = [
    (bitwise_and_invalid_variables, (), TranslateError),
    (bitwise_and_invalid_variables1, (), TranslateError),
    (bitwise_and_to_None, (), TranslateError),
    (bitwise_and_invalid_rtseq_call, (), VeristandError),
]

py_only_errs = [
    (bitwise_and_num_nivsdatatype, (), 1.0),  # cannot do bitwise and on float
    (bitwise_and_nivsdatatype_nivsdatatype, (), 1.0),  # cannot do bitwise and on float
    (bitwise_and_nivsdatatype_nivsdatatype1, (), 1.0),  # cannot do bitwise and on float
    (bitwise_and_nivsdatatype_nivsdatatype2, (), True),  # cannot do bitwise and on Boolean
    (bitwise_and_with_parentheses1, (), 1.0),  # cannot do bitwise and on float
    (bitwise_and_with_parentheses2, (), 0.0),  # cannot do bitwise and on float
    (bitwise_and_to_channel_ref, (), 1.0),  # cannot do bitwise and on float
    (aug_bitwise_and_to_channel_ref, (), 1.0),  # cannot do bitwise and on float
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize(
    "func_name, params, expected_result", list(set(run_tests) - set(py_only_errs)), ids=idfunc
)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_bitwise_or.py sha256=bb4063249a72ed1cb2f7d237a48ff53998125cb7665bc22513a9a3db3841382e bytes=9418 -->
## FILE: tests/test_bitwise_or.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_bitwise_or.py`
- sha256: `bb4063249a72ed1cb2f7d237a48ff53998125cb7665bc22513a9a3db3841382e`
- bytes: 9418

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = I32Value(5)
    return a.value


@nivs_rt_sequence
def bitwise_or_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 | 3
    return a.value


@nivs_rt_sequence
def bitwise_or_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 | DoubleValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_or_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) | DoubleValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_or_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) | I32Value(3)
    return a.value


@nivs_rt_sequence
def bitwise_or_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = BooleanValue(1) | BooleanValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_or_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) | I32Value(3)
    return a.value


@nivs_rt_sequence
def bitwise_or_multiple_types():
    a = I32Value(0)
    a.value = 1 | I32Value(3) | 5
    return a.value


@nivs_rt_sequence
def bitwise_or_multiple_types1():
    a = I64Value(1)
    a.value = 1 | I64Value(5) | 3 | I32Value(7)
    return a.value


@nivs_rt_sequence
def bitwise_or_use_rtseq():
    a = DoubleValue(0)
    a.value = 2 | _return_constant()
    return a.value


@nivs_rt_sequence
def bitwise_or_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() | 2
    return a.value


@nivs_rt_sequence
def bitwise_or_use_rtseq2():
    a = DoubleValue(0)
    a.value = I32Value(2) | _return_constant()
    return a.value


@nivs_rt_sequence
def bitwise_or_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() | I32Value(2)
    return a.value


@nivs_rt_sequence
def bitwise_or_with_parentheses():
    a = I32Value(0)
    a.value = 1 | (5 | 3)
    return a.value


@nivs_rt_sequence
def bitwise_or_with_parentheses1():
    a = DoubleValue(0)
    a.value = 1 | (DoubleValue(3) | I32Value(5))
    return a.value


@nivs_rt_sequence
def bitwise_or_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) | (I32Value(2) | 3.0) | DoubleValue(4)
    return a.value


@nivs_rt_sequence
def bitwise_or_variables():
    a = I32Value(5)
    b = I32Value(0)
    b.value = 1 | a
    return b.value


@nivs_rt_sequence
def bitwise_or_variables1():
    a = I64Value(5)
    b = I64Value(0)
    b.value = 1 | a.value
    return b.value


@nivs_rt_sequence
def bitwise_or_variable_variable():
    a = I32Value(1)
    b = I64Value(3)
    c = I32Value(0)
    c.value = a.value | b.value
    return c.value


@nivs_rt_sequence
def bitwise_or_variable_variable1():
    a = I32Value(1)
    b = I64Value(3)
    c = DoubleValue(0)
    c.value = a.value | b.value
    return c.value


@nivs_rt_sequence
def bitwise_or_variable_rtseq():
    a = I32Value(2)
    b = DoubleValue(0)
    b.value = a.value | _return_constant()
    return b.value


@nivs_rt_sequence
def bitwise_or_variable_rtseq1():
    a = I32Value(2)
    b = DoubleValue(0)
    b.value = _return_constant() | a.value
    return b.value


@nivs_rt_sequence
def bitwise_or_to_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 | b.value
    return a.value


@nivs_rt_sequence
def bitwise_or_binary_unary():
    a = I32Value(0)
    a.value = 3 | -1
    return a.value


@nivs_rt_sequence
def bitwise_or_complex_expr():
    a = DoubleValue(0)
    a.value = 1 | (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_bitwise_or_simple_numbers():
    a = I32Value(3)
    a.value |= 7
    return a.value


@nivs_rt_sequence
def aug_bitwise_or_num_nivsdatatype():
    a = I32Value(1)
    a.value |= I32Value(3)
    return a.value


@nivs_rt_sequence
def aug_bitwise_or_use_rtseq():
    a = I32Value(2)
    a.value |= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_bitwise_or_with_parentheses():
    a = I32Value(1)
    a.value |= 7 | (5 | 3)
    return a.value


@nivs_rt_sequence
def aug_bitwise_or_variables():
    a = I32Value(7)
    b = I32Value(3)
    b.value |= a.value
    return b.value


@nivs_rt_sequence
def aug_bitwise_or_to_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value |= b.value
    return a.value


@nivs_rt_sequence
def aug_bitwise_or_unary():
    a = I32Value(3)
    a.value |= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def bitwise_or_invalid_variables():
    return a.value | b


@nivs_rt_sequence
def bitwise_or_invalid_variables1():
    return a.value | b.value


@nivs_rt_sequence
def bitwise_or_to_None():
    a = DoubleValue(0)
    a.value = None | 1
    return a.value


@nivs_rt_sequence
def bitwise_or_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant | 1
    return a.value


# </editor-fold>


run_tests = [
    (bitwise_or_simple_numbers, (), 3),
    (bitwise_or_nivsdatatype_nivsdatatype3, (), 3),
    (bitwise_or_variables, (), 5),
    (bitwise_or_variables1, (), 5),
    (bitwise_or_multiple_types, (), 7),
    (bitwise_or_multiple_types1, (), 7),
    (bitwise_or_with_parentheses, (), 7),
    (bitwise_or_variable_variable, (), 3),
    (bitwise_or_variable_variable1, (), 3),
    (bitwise_or_binary_unary, (), -1),
    (aug_bitwise_or_simple_numbers, (), 7),
    (aug_bitwise_or_variables, (), 7),
    (aug_bitwise_or_num_nivsdatatype, (), 3),
    (aug_bitwise_or_with_parentheses, (), 7),
    (aug_bitwise_or_unary, (), -1),
    (bitwise_or_complex_expr, (), 3),
    (bitwise_or_use_rtseq, (), 7),
    (bitwise_or_use_rtseq1, (), 7),
    (bitwise_or_use_rtseq2, (), 7),
    (bitwise_or_use_rtseq3, (), 7),
    (bitwise_or_variable_rtseq, (), 7),
    (bitwise_or_variable_rtseq1, (), 7),
    (aug_bitwise_or_use_rtseq, (), 7),
    (bitwise_or_num_nivsdatatype, (), 3),
    (bitwise_or_nivsdatatype_nivsdatatype, (), 3),
    (bitwise_or_nivsdatatype_nivsdatatype1, (), 3),
    (bitwise_or_nivsdatatype_nivsdatatype2, (), True),
    (bitwise_or_with_parentheses1, (), 7),
    (bitwise_or_with_parentheses2, (), 7),
    (bitwise_or_to_channel_ref, (), 5),
    (aug_bitwise_or_to_channel_ref, (), 5),
]

fail_transform_tests = [
    (bitwise_or_invalid_variables, (), TranslateError),
    (bitwise_or_invalid_variables1, (), TranslateError),
    (bitwise_or_to_None, (), TranslateError),
    (bitwise_or_invalid_rtseq_call, (), VeristandError),
]

py_only_errs = [
    (bitwise_or_num_nivsdatatype, (), 3),  # cannot do bitwise or on float
    (bitwise_or_nivsdatatype_nivsdatatype, (), 3),  # cannot do bitwise or on float
    (bitwise_or_nivsdatatype_nivsdatatype1, (), 3),  # cannot do bitwise or on float
    (bitwise_or_nivsdatatype_nivsdatatype2, (), True),  # cannot do bitwise or on Boolean
    (bitwise_or_with_parentheses1, (), 7),  # cannot do bitwise or on float
    (bitwise_or_with_parentheses2, (), 7),  # cannot do bitwise or on float
    (bitwise_or_to_channel_ref, (), 5),  # cannot do bitwise or on float
    (aug_bitwise_or_to_channel_ref, (), 5),  # cannot do bitwise or on float
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize(
    "func_name, params, expected_result", list(set(run_tests) - set(py_only_errs)), ids=idfunc
)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_bitwise_xor.py sha256=9edb7efb9cd3d0a412779b167aac8b48740cbfef56d8869a7a326ddf5c1f51b7 bytes=9506 -->
## FILE: tests/test_bitwise_xor.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_bitwise_xor.py`
- sha256: `9edb7efb9cd3d0a412779b167aac8b48740cbfef56d8869a7a326ddf5c1f51b7`
- bytes: 9506

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = I32Value(5)
    return a.value


@nivs_rt_sequence
def bitwise_xor_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 ^ 3
    return a.value


@nivs_rt_sequence
def bitwise_xor_num_nivsdatatype():
    a = DoubleValue(0)
    a.value = 1 ^ DoubleValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype():
    a = DoubleValue(0)
    a.value = DoubleValue(1) ^ DoubleValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype1():
    a = DoubleValue(0)
    a.value = DoubleValue(1) ^ I32Value(3)
    return a.value


@nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = BooleanValue(1) ^ BooleanValue(3)
    return a.value


@nivs_rt_sequence
def bitwise_xor_nivsdatatype_nivsdatatype3():
    a = DoubleValue(0)
    a.value = I32Value(1) ^ I32Value(3)
    return a.value


@nivs_rt_sequence
def bitwise_xor_multiple_types():
    a = I32Value(0)
    a.value = 1 ^ I32Value(3) ^ 5
    return a.value


@nivs_rt_sequence
def bitwise_xor_multiple_types1():
    a = I64Value(1)
    a.value = 1 ^ I64Value(5) ^ 3 ^ I32Value(7)
    return a.value


@nivs_rt_sequence
def bitwise_xor_use_rtseq():
    a = DoubleValue(0)
    a.value = 1 ^ _return_constant()
    return a.value


@nivs_rt_sequence
def bitwise_xor_use_rtseq1():
    a = DoubleValue(0)
    a.value = _return_constant() ^ 1
    return a.value


@nivs_rt_sequence
def bitwise_xor_use_rtseq2():
    a = DoubleValue(0)
    a.value = I32Value(1) ^ _return_constant()
    return a.value


@nivs_rt_sequence
def bitwise_xor_use_rtseq3():
    a = DoubleValue(0)
    a.value = _return_constant() ^ I32Value(1)
    return a.value


@nivs_rt_sequence
def bitwise_xor_with_parentheses():
    a = I32Value(0)
    a.value = 1 ^ (5 ^ 3)
    return a.value


@nivs_rt_sequence
def bitwise_xor_with_parentheses1():
    a = DoubleValue(0)
    a.value = 1 ^ (DoubleValue(3) ^ I32Value(5))
    return a.value


@nivs_rt_sequence
def bitwise_xor_with_parentheses2():
    a = DoubleValue(0)
    a.value = DoubleValue(1) ^ (I32Value(2) ^ 3.0) ^ DoubleValue(4)
    return a.value


@nivs_rt_sequence
def bitwise_xor_variables():
    a = I32Value(5)
    b = I32Value(0)
    b.value = 1 ^ a
    return b.value


@nivs_rt_sequence
def bitwise_xor_variables1():
    a = I64Value(5)
    b = I64Value(0)
    b.value = 1 ^ a.value
    return b.value


@nivs_rt_sequence
def bitwise_xor_variable_variable():
    a = I32Value(1)
    b = I64Value(3)
    c = I32Value(0)
    c.value = a.value ^ b.value
    return c.value


@nivs_rt_sequence
def bitwise_xor_variable_variable1():
    a = I32Value(1)
    b = I64Value(3)
    c = DoubleValue(0)
    c.value = a.value ^ b.value
    return c.value


@nivs_rt_sequence
def bitwise_xor_variable_rtseq():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = a.value ^ _return_constant()
    return b.value


@nivs_rt_sequence
def bitwise_xor_variable_rtseq1():
    a = I32Value(1)
    b = DoubleValue(0)
    b.value = _return_constant() ^ a.value
    return b.value


@nivs_rt_sequence
def bitwise_xor_to_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 ^ b.value
    return a.value


@nivs_rt_sequence
def bitwise_xor_binary_unary():
    a = I32Value(0)
    a.value = 3 ^ -1
    return a.value


@nivs_rt_sequence
def bitwise_xor_complex_expr():
    a = DoubleValue(0)
    a.value = 1 ^ (2 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Augassign tests>


@nivs_rt_sequence
def aug_bitwise_xor_simple_numbers():
    a = I32Value(3)
    a.value ^= 7
    return a.value


@nivs_rt_sequence
def aug_bitwise_xor_num_nivsdatatype():
    a = I32Value(1)
    a.value ^= I32Value(3)
    return a.value


@nivs_rt_sequence
def aug_bitwise_xor_use_rtseq():
    a = I32Value(1)
    a.value ^= _return_constant()
    return a.value


@nivs_rt_sequence
def aug_bitwise_xor_with_parentheses():
    a = I32Value(1)
    a.value ^= 7 ^ (5 ^ 3)
    return a.value


@nivs_rt_sequence
def aug_bitwise_xor_variables():
    a = I32Value(7)
    b = I32Value(3)
    b.value ^= a.value
    return b.value


@nivs_rt_sequence
def aug_bitwise_xor_to_channel_ref():
    a = DoubleValue(1)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value ^= b.value
    return a.value


@nivs_rt_sequence
def aug_bitwise_xor_unary():
    a = I32Value(3)
    a.value ^= -1
    return a.value


# </editor-fold>

# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def bitwise_xor_invalid_variables():
    return a.value ^ b


@nivs_rt_sequence
def bitwise_xor_invalid_variables1():
    return a.value ^ b.value


@nivs_rt_sequence
def bitwise_xor_to_None():
    a = DoubleValue(0)
    a.value = None ^ 1
    return a.value


@nivs_rt_sequence
def bitwise_xor_invalid_rtseq_call():
    a = DoubleValue(0)
    a.value = _return_constant ^ 1
    return a.value


# </editor-fold>


run_tests = [
    (bitwise_xor_simple_numbers, (), 2),
    (bitwise_xor_nivsdatatype_nivsdatatype3, (), 2),
    (bitwise_xor_variables, (), 4),
    (bitwise_xor_variables1, (), 4),
    (bitwise_xor_multiple_types, (), 7),
    (bitwise_xor_multiple_types1, (), 0),
    (bitwise_xor_with_parentheses, (), 7),
    (bitwise_xor_variable_variable, (), 2),
    (bitwise_xor_variable_variable1, (), 2),
    (bitwise_xor_binary_unary, (), -4),
    (aug_bitwise_xor_simple_numbers, (), 4),
    (aug_bitwise_xor_variables, (), 4),
    (aug_bitwise_xor_num_nivsdatatype, (), 2),
    (aug_bitwise_xor_with_parentheses, (), 0),
    (aug_bitwise_xor_unary, (), -4),
    (bitwise_xor_complex_expr, (), 3),
    (bitwise_xor_use_rtseq, (), 4),
    (bitwise_xor_use_rtseq1, (), 4),
    (bitwise_xor_use_rtseq2, (), 4),
    (bitwise_xor_use_rtseq3, (), 4),
    (bitwise_xor_variable_rtseq, (), 4),
    (bitwise_xor_variable_rtseq1, (), 4),
    (aug_bitwise_xor_use_rtseq, (), 4),
    (bitwise_xor_num_nivsdatatype, (), 2),
    (bitwise_xor_nivsdatatype_nivsdatatype, (), 2),
    (bitwise_xor_nivsdatatype_nivsdatatype1, (), 2),
    (bitwise_xor_nivsdatatype_nivsdatatype2, (), False),
    (bitwise_xor_with_parentheses1, (), 7),
    (bitwise_xor_with_parentheses2, (), 4),
    (bitwise_xor_to_channel_ref, (), 4),
    (aug_bitwise_xor_to_channel_ref, (), 4),
]

fail_transform_tests = [
    (bitwise_xor_invalid_variables, (), TranslateError),
    (bitwise_xor_invalid_variables1, (), TranslateError),
    (bitwise_xor_to_None, (), TranslateError),
    (bitwise_xor_invalid_rtseq_call, (), VeristandError),
]

py_only_errs = [
    (bitwise_xor_num_nivsdatatype, (), 2),  # cannot do bitwise xor on float
    (bitwise_xor_nivsdatatype_nivsdatatype, (), 2),  # cannot do bitwise xor on float
    (bitwise_xor_nivsdatatype_nivsdatatype1, (), 2),  # cannot do bitwise xor on float
    (bitwise_xor_nivsdatatype_nivsdatatype2, (), False),  # cannot do bitwise xor on Boolean
    (bitwise_xor_with_parentheses1, (), 7),  # cannot do bitwise xor on float
    (bitwise_xor_with_parentheses2, (), 4),  # cannot do bitwise xor on float
    (bitwise_xor_to_channel_ref, (), 4),  # cannot do bitwise xor on float
    (aug_bitwise_xor_to_channel_ref, (), 4),  # cannot do bitwise xor on float
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize(
    "func_name, params, expected_result", list(set(run_tests) - set(py_only_errs)), ids=idfunc
)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_builtin_math_functions.py sha256=5129d72178af52c53acd220f4c3df9fe76dbc770a7eb631feecf45ab6c2f73d9 bytes=10896 -->
## FILE: tests/test_builtin_math_functions.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_builtin_math_functions.py`
- sha256: `5129d72178af52c53acd220f4c3df9fe76dbc770a7eb631feecf45ab6c2f73d9`
- bytes: 10896

````python
from math import (
    acos,
    acosh,
    asin,
    asinh,
    atan,
    atan2,
    atanh,
    ceil,
    cos,
    cosh,
    exp,
    expm1,
    floor,
    fmod,
    hypot,
    isnan,
    log,
    log10,
    log1p,
    log2,
    pi,
    sin,
    sinh,
    sqrt,
    tan,
    tanh,
)
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import (
    BooleanValue,
    ChannelReference,
    DoubleValue,
    I32Value,
    I64Value,
    U32Value,
    U64Value,
)
from niveristand.clientapi import RealTimeSequence
from niveristand.library.primitives import localhost_wait
import numpy
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(-5)
    return a.value


# <editor-fold desc=Abs tests>


@nivs_rt_sequence
def abs_simple_number():
    a = DoubleValue(0)
    a.value = abs(-5)
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype_value():
    a = DoubleValue(0)
    a.value = abs(DoubleValue(-5).value)
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype():
    a = DoubleValue(0)
    a.value = abs(DoubleValue(-5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype1():
    a = I32Value(0)
    a.value = abs(I32Value(-5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype2():
    a = DoubleValue(0)
    a.value = abs(I64Value(-5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype3():
    a = DoubleValue(0)
    a.value = abs(U32Value(5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype4():
    a = DoubleValue(0)
    a.value = abs(U64Value(5))
    return a.value


@nivs_rt_sequence
def abs_nivsdatatype5():
    a = DoubleValue(0)
    a.value = abs(BooleanValue(5))
    return a.value


@nivs_rt_sequence
def abs_variable_double():
    a = DoubleValue(0)
    b = DoubleValue(-5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_i32():
    a = I32Value(0)
    b = I32Value(-5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_i64():
    a = I64Value(0)
    b = I64Value(-5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_u32():
    a = U32Value(0)
    b = U32Value(5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_u64():
    a = U64Value(0)
    b = U64Value(5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_variable_boolean():
    a = BooleanValue(0)
    b = BooleanValue(-5)
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = -5.0
    localhost_wait()
    a.value = abs(b.value)
    return a.value


@nivs_rt_sequence
def abs_call_rtseq():
    a = DoubleValue(0)
    a.value = abs(_return_constant())
    return a.value


@nivs_rt_sequence
def abs_expr():
    a = DoubleValue(0)
    a.value = abs(1 - 2)
    return a.value


@nivs_rt_sequence
def abs_expr_parentheses():
    a = DoubleValue(0)
    a.value = abs(2 * (2 - 3))
    return a.value


@nivs_rt_sequence
def abs_ifexpr():
    a = DoubleValue(0)
    a.value = abs(1 if True else 2)
    return a.value


@nivs_rt_sequence
def abs_builtin():
    a = DoubleValue(0)
    a.value = abs(abs(-5))
    return a.value


# </editor-fold>


@nivs_rt_sequence
def acos_double():
    a = DoubleValue(0)
    b = DoubleValue(0)
    a.value = acos(b.value)
    return a.value


@nivs_rt_sequence
def acosh_double():
    a = DoubleValue(1)
    b = DoubleValue(1)
    a.value = acosh(b.value)
    return a.value


@nivs_rt_sequence
def asin_double():
    a = DoubleValue(1)
    b = DoubleValue(1)
    a.value = asin(b.value)
    return a.value


@nivs_rt_sequence
def asinh_double():
    a = DoubleValue(1)
    b = DoubleValue(0)
    a.value = asinh(b.value)
    return a.value


@nivs_rt_sequence
def atan_double():
    a = DoubleValue(1)
    b = DoubleValue(0)
    a.value = atan(b.value)
    return a.value


@nivs_rt_sequence
def atan2_double():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = DoubleValue(-2)
    a.value = atan2(c.value, b.value)
    return a.value


@nivs_rt_sequence
def atanh_double():
    a = DoubleValue(1)
    b = DoubleValue(0)
    a.value = atanh(b.value)
    return a.value


@nivs_rt_sequence
def ceil_double():
    a = DoubleValue(0)
    b = DoubleValue(1.2)
    a.value = ceil(b.value)
    return a.value


@nivs_rt_sequence
def ceil_double_negative():
    a = DoubleValue(0)
    b = DoubleValue(-1.2)
    a.value = ceil(b.value)
    return a.value


@nivs_rt_sequence
def cos_double():
    a = DoubleValue(0)
    b = DoubleValue(0)
    a.value = cos(b.value)
    return a.value


@nivs_rt_sequence
def cosh_double():
    a = DoubleValue(0)
    b = DoubleValue(0)
    a.value = cosh(b.value)
    return a.value


@nivs_rt_sequence
def exp_double():
    a = DoubleValue(0)
    b = DoubleValue(0)
    a.value = exp(b.value)
    return a.value


@nivs_rt_sequence
def expm1_double():
    a = DoubleValue(1)
    b = DoubleValue(0)
    a.value = expm1(b.value)
    return a.value


@nivs_rt_sequence
def floor_double():
    a = DoubleValue(5.7)
    a.value = floor(a.value)
    return a.value


@nivs_rt_sequence
def hypot_double():
    a = DoubleValue(4)
    b = DoubleValue(3)
    a.value = hypot(a.value, b.value)
    return a.value


@nivs_rt_sequence
def isnan_double():
    a = DoubleValue(0)
    b = BooleanValue(False)
    b.value = isnan(a.value)
    return b.value


@nivs_rt_sequence
def ln_double():
    a = DoubleValue(1)
    a.value = log(exp(a.value))
    return a.value


@nivs_rt_sequence
def lnp1_double():
    a = DoubleValue(0)
    a.value = expm1(10)
    a.value = log1p(a.value)
    return a.value


@nivs_rt_sequence
def log_double():
    a = DoubleValue(27.0)
    b = DoubleValue(3)
    a.value = log(a.value, b.value)
    return a.value


@nivs_rt_sequence
def log10_double():
    a = DoubleValue(1000)
    a.value = log10(a.value)
    return a.value


@nivs_rt_sequence
def log2_double():
    a = DoubleValue(1024)
    a.value = log2(a.value)
    return a.value


@nivs_rt_sequence
def max_double():
    a = DoubleValue(1024)
    b = DoubleValue(2048)
    a.value = max(b.value, a.value)
    return a.value


@nivs_rt_sequence
def min_double():
    a = DoubleValue(1024)
    b = DoubleValue(2048)
    a.value = min(b.value, a.value)
    return a.value


@nivs_rt_sequence
def mod_double():
    a = DoubleValue(3)
    b = DoubleValue(-2048)
    a.value = fmod(b.value, a.value)
    return a.value


@nivs_rt_sequence
def pow_double():
    a = DoubleValue(3.0)
    b = DoubleValue(3)
    a.value = pow(a.value, b.value)
    return a.value


@nivs_rt_sequence
def round_double():
    a = DoubleValue(3.7)
    a.value = round(a.value)
    return a.value


@nivs_rt_sequence
def sin_double():
    a = DoubleValue(0)
    a.value = pi / 2
    a.value = sin(a.value)
    return a.value


@nivs_rt_sequence
def sinh_double():
    a = DoubleValue(0)
    a.value = pi
    a.value = sinh(a.value)
    return a.value


@nivs_rt_sequence
def sqrt_double():
    a = DoubleValue(25)
    a.value = sqrt(a.value)
    return a.value


@nivs_rt_sequence
def tan_double():
    a = DoubleValue(0)
    a.value = pi / 2
    a.value = tan(a.value)
    return a.value


@nivs_rt_sequence
def tanh_double():
    a = DoubleValue(0)
    a.value = pi
    a.value = tanh(a.value)
    return a.value


run_tests = [
    (abs_nivsdatatype_value, (), 5),
    (abs_simple_number, (), 5),
    (abs_variable_double, (), 5.0),
    (abs_variable_i32, (), numpy.int32(5)),
    (abs_variable_i64, (), numpy.int64(5)),
    (abs_variable_u32, (), numpy.uint32(5)),
    (abs_variable_u64, (), numpy.uint64(5)),
    (abs_call_rtseq, (), 5),
    (abs_expr, (), 1.0),
    (abs_expr_parentheses, (), 2.0),
    (abs_ifexpr, (), 1.0),
    (abs_builtin, (), 5.0),
    (acos_double, (), pi / 2),
    (acosh_double, (), 0.0),
    (asin_double, (), pi / 2),
    (asinh_double, (), 0.0),
    (atan_double, (), 0.0),
    (atan2_double, (), -pi / 4),
    (atanh_double, (), 0.0),
    (ceil_double, (), 2.0),
    (ceil_double_negative, (), -1.0),
    (cos_double, (), 1.0),
    (cosh_double, (), 1),
    (exp_double, (), 1),
    (expm1_double, (), 0),
    (floor_double, (), 5.0),
    (hypot_double, (), 5.0),
    (isnan_double, (), False),
    (log10_double, (), 3),
    (ln_double, (), log(exp(1))),
    (lnp1_double, (), 10),
    (log_double, (), 3),
    (log2_double, (), 10),
    (max_double, (), 2048),
    (min_double, (), 1024),
    (mod_double, (), 1.0),
    (pow_double, (), 27),
    (round_double, (), 4),
    (sin_double, (), 1),
    (sinh_double, (), sinh(pi)),
    (sqrt_double, (), 5),
    (tan_double, (), tan(pi / 2)),
    (tanh_double, (), tanh(pi)),
    (abs_channel_ref, (), 5.0),
    (abs_variable_boolean, (), False),
]

transform_tests = run_tests + [
    (abs_nivsdatatype, (), 5),
    (abs_nivsdatatype1, (), 5),
    (abs_nivsdatatype2, (), 5),
    (abs_nivsdatatype3, (), 5),
    (abs_nivsdatatype4, (), 5),
    (abs_nivsdatatype5, (), 5),
]

py_only_different_behavior_tests = [
    (abs_variable_boolean, (), False),
    (mod_double, (), 1.0),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", transform_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize(
    "func_name, params, expected_result",
    list(set(run_tests) - set(py_only_different_behavior_tests)),
    ids=idfunc,
)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_builtin_veristand_functions.py sha256=91c3b7e66585f856b513f935bb188b79fd69a5f6e3a2ea2a4b043a5664297885 bytes=7130 -->
## FILE: tests/test_builtin_veristand_functions.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_builtin_veristand_functions.py`
- sha256: `91c3b7e66585f856b513f935bb188b79fd69a5f6e3a2ea2a4b043a5664297885`
- bytes: 7130

````python
import inspect
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import (
    BooleanValue,
    ChannelReference,
    DoubleValue,
    DoubleValueArray,
    I64Value,
)
from niveristand.clientapi import ErrorAction
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import RunFailedError, VeristandError
from niveristand.library.primitives import (
    abstime,
    arraysize,
    clearfault,
    clearlasterror,
    deltat,
    deltatus,
    fault,
    fix,
    generate_error,
    getlasterror,
    iteration,
    quotient,
    recip,
    rem,
    seqtime,
    seqtimeus,
    tickcountms,
    tickcountus,
)
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def call_abstime():
    a = DoubleValue(0)
    a.value = abstime()
    return a.value


@nivs_rt_sequence
def call_arraysize():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3])
    a.value = arraysize(b.value)
    return a.value


@nivs_rt_sequence
def call_clearfault():
    a = ChannelReference("Aliases/DesiredRPM")
    b = DoubleValue(0)
    c = BooleanValue(False)
    # Store initial channel value
    b.value = a.value
    fault(a, 1001)
    clearfault(a)
    # Try to assign back to the channel the initial value
    a.value = b.value
    # If everything went well the initial value and the current value should now be equal
    c.value = b.value == a.value
    return c.value


@nivs_rt_sequence
def call_clearlasterror():
    generate_error(1, "Continue1", ErrorAction.ContinueSequenceExecution)
    generate_error(2, "Continue2", ErrorAction.ContinueSequenceExecution)
    a = BooleanValue(False)
    b = I64Value(5)
    clearlasterror()
    b.value = getlasterror()
    if b.value == 0:
        a.value = True
    return a.value


@nivs_rt_sequence
def call_deltat():
    a = DoubleValue(0)
    a.value = deltat()
    return a.value


@nivs_rt_sequence
def call_deltatus():
    a = DoubleValue(0)
    a.value = deltatus()
    return a.value


@nivs_rt_sequence
def call_fault():
    a = ChannelReference("Aliases/DesiredRPM")
    b = DoubleValue(0)
    fault(a, 1001)
    b.value = a.value
    # cleanup the fault so that other tests are still able to use this channel
    clearfault(a)
    return b.value


@nivs_rt_sequence
def call_fix():
    a = DoubleValue(4.9)
    a.value = fix(a.value)
    return a.value


@nivs_rt_sequence
def call_getlasterror():
    generate_error(1, "Continue1", ErrorAction.ContinueSequenceExecution)
    generate_error(2, "Continue2", ErrorAction.ContinueSequenceExecution)
    a = BooleanValue(False)
    b = I64Value(0)
    b.value = getlasterror()
    if b.value == 2:
        a.value = True
    return a.value


@nivs_rt_sequence
def call_iteration():
    a = I64Value(0)
    a.value = iteration()
    return a.value


@nivs_rt_sequence
def call_quotient():
    a = I64Value(1440)
    b = DoubleValue(12)
    b.value = quotient(a, b)
    return b.value


@nivs_rt_sequence
def call_recip():
    a = DoubleValue(1024)
    a.value = recip(a)
    return a.value


@nivs_rt_sequence
def call_rem():
    a = I64Value(1439)
    b = DoubleValue(12)
    b.value = rem(a, b)
    return b.value


@nivs_rt_sequence
def call_seqtime():
    a = DoubleValue(0)
    a.value = seqtime()
    a.value = seqtime() - a.value
    return a.value


@nivs_rt_sequence
def call_seqtimeus():
    a = DoubleValue(0)
    a.value = seqtimeus()
    a.value = seqtimeus() - a.value
    return a.value


@nivs_rt_sequence
def call_tickcountms():
    a = I64Value(0)
    a.value = tickcountms()
    a.value = tickcountms() - a.value
    return a.value


@nivs_rt_sequence
def call_tickcountus():
    a = I64Value(0)
    a.value = tickcountus()
    a.value = tickcountus() - a.value
    return a.value


run_everywhere_tests = [
    (call_abstime, (), None),
    (call_arraysize, (), 3),
    (call_clearfault, (), True),
    (call_clearlasterror, (), True),
    (call_deltat, (), 0.01),  # it is 0.01 for engine demo
    (call_deltatus, (), 10**4),  # 0.01 seconds in microseconds
    (call_fault, (), 1001),
    (call_fix, (), 4),
    (call_iteration, (), 0),
    (call_quotient, (), 120),
    (call_recip, (), 1.0 / 1024),
    (call_rem, (), 11),
    (call_seqtime, (), None),
    (call_seqtimeus, (), None),
    (call_tickcountms, (), None),
    (call_tickcountus, (), None),
]

run_tests = run_everywhere_tests + [
    (call_getlasterror, (), True),
]

py_only_errs = [
    (call_abstime, (), None),
    (call_clearfault, (), True),
    (call_clearlasterror, (), True),
    (call_deltat, (), 0.01),  # it is 0.01 for engine demo
    (call_deltatus, (), 10**4),  # 0.01 seconds in microseconds
    (call_fault, (), 1001),
    (call_fix, (), 4),
    (call_getlasterror, (), True),
    (call_recip, (), 1.0 / 1024),
    (call_rem, (), 11),
]

run_as_rts_tests = run_everywhere_tests + [
    (call_getlasterror, (), RunFailedError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize(
    "func_name, params, expected_result", list(set(run_tests) - set(py_only_errs)), ids=idfunc
)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    if expected_result is None:
        assert actual >= 0
    else:
        assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_as_rts_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    if inspect.isclass(expected_result) and issubclass(expected_result, VeristandError):
        with pytest.raises(expected_result):
            realtimesequencetools.run_py_as_rtseq(func_name)
    else:
        actual = realtimesequencetools.run_py_as_rtseq(func_name)
        # some of these functions are time sensitive so we can't know what to expect
        # so if the expected result is None we just check that a non-zero value got returned
        if expected_result is None:
            assert actual >= 0
        else:
            assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name, 0.01)
    # some of these functions are time sensitive so we can't know what to expect
    # so if the expected result is None we just check that a non-zero value got returned
    if expected_result is None:
        assert actual >= 0
    else:
        assert actual == expected_result


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_call_nested_rtsequence.py sha256=58a1b15b45550c564079fbf662ee374a60f43e7f13b044d260d738235cf3ee0d bytes=1311 -->
## FILE: tests/test_call_nested_rtsequence.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_call_nested_rtsequence.py`
- sha256: `58a1b15b45550c564079fbf662ee374a60f43e7f13b044d260d738235cf3ee0d`
- bytes: 1311

````python
from niveristand import nivs_rt_sequence, realtimesequencetools
from niveristand.clientapi import DoubleValue
from niveristand.library import wait
import pytest


@nivs_rt_sequence
def nested_sequence():
    wait(DoubleValue(1))


@nivs_rt_sequence
def call_nested_sequence_after():
    param = DoubleValue(1)
    wait(param)
    nested_sequence()


@nivs_rt_sequence
def call_nested_sequence_before():
    param = DoubleValue(1)
    nested_sequence()
    wait(param)


@nivs_rt_sequence
def call_nested_sequence_twice():
    param = DoubleValue(1)
    wait(param)
    nested_sequence()
    nested_sequence()
    wait(param)
    wait(param)


@nivs_rt_sequence
def call_complex_nested_sequences():
    param = DoubleValue(1)
    wait(param)
    call_nested_sequence_after()
    wait(param)
    call_nested_sequence_before()
    wait(param)


run_tests = [
    call_nested_sequence_after,
    call_nested_sequence_before,
    call_nested_sequence_twice,
    call_complex_nested_sequences,
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name):
    realtimesequencetools.run_py_as_rtseq(func_name)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_channel_refs.py sha256=eecea17de30ddbdfe154fdbcbd12d690f149fb4e8331138ba83ba00e3c96bfea bytes=3777 -->
## FILE: tests/test_channel_refs.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_channel_refs.py`
- sha256: `eecea17de30ddbdfe154fdbcbd12d690f149fb4e8331138ba83ba00e3c96bfea`
- bytes: 3777

````python
from niveristand import errors, realtimesequencetools
from niveristand.clientapi import RealTimeSequence
import pytest
from testutilities import rtseqrunner, testfunctions
from NationalInstruments.VeriStand.RealTimeSequenceDefinitionApi import (  # noqa: I100 .NET imports out of order
    Expression,
)


def test_channel_ref_type_string():
    rtseq = RealTimeSequence(testfunctions.channel_ref_type_string)
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length == 0
    assert rtseq._rtseq.Variables.ChannelReferences.Channels.Length == 1
    assert (
        rtseq._rtseq.Variables.ChannelReferences.Channels[0].Channel.Channel == "Aliases/DesiredRPM"
    )


def test_channel_ref_setter():
    rtseq = RealTimeSequence(testfunctions.channel_ref_setter)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 1
    expression = Expression("ch_a = 5")
    assert rtseq._rtseq.Code.Main.Body.Statements[0].Equals(expression)


def test_channel_ref_return():
    testfunc = testfunctions.channel_ref_return
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)


def test_channel_ref_run():
    result = rtseqrunner.run_rtseq_in_VM(testfunctions.channel_ref_validate_getter)
    assert result == 5


def test_channel_ref_run_python():
    result = testfunctions.channel_ref_validate_getter()
    assert result == 5


def test_channel_ref_invalid_channel_set():
    with pytest.raises(errors.VeristandError):
        testfunctions.channel_ref_invalid_channel_set()


def test_channel_ref_invalid_channel_get():
    with pytest.raises(errors.VeristandError):
        testfunctions.channel_ref_invalid_channel_get()


def test_channel_ref_invalid_channel_transform():
    # Transforming sequences with invalid channels should work, because they are not validated. This is, because users
    # need to be able to transform without a deployed system definition and therefore we are not checking through the
    # C# API the validity of a channel. This will be improved in the future to differentiate between the two cases.
    rtseq = RealTimeSequence(testfunctions.channel_ref_invalid_channel_transform)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 0
    assert rtseq._rtseq.Variables.ChannelReferences.Channels.Length == 1


def test_channel_ref_array_type_string():
    rtseq = RealTimeSequence(testfunctions.channel_ref_array_type_string)
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length == 0
    assert rtseq._rtseq.Variables.ChannelReferences.Channels.Length == 1
    assert (
        rtseq._rtseq.Variables.ChannelReferences.Channels[0].Channel.Channel
        == "Targets/Controller/Simulation Models/Models/Engine Demo/Parameters/a"
    )


def test_channel_ref_array_setter():
    rtseq = RealTimeSequence(testfunctions.channel_ref_array_setter)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 1
    expression = Expression("ch_a[0] = 5")
    assert rtseq._rtseq.Code.Main.Body.Statements[0].Equals(expression)


def test_channel_ref_array_return():
    testfunc = testfunctions.channel_ref_array_return
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)


def test_channel_ref_for_vector_channel():
    with pytest.raises(errors.VeristandError):
        realtimesequencetools.run_py_as_rtseq(testfunctions.channel_ref_for_vector_channel)


@pytest.mark.skip
def test_channel_ref_array_run():
    result = rtseqrunner.run_rtseq_in_VM(testfunctions.channel_ref_array_validate_getter)
    assert result == 5


@pytest.mark.skip
def test_channel_ref_array_run_python():
    result = testfunctions.channel_ref_array_validate_getter()
    assert result == 5
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_compare_equal.py sha256=7fc28920468f3edda3df8879d3a0ed2d658907bc0fa2262e21e3d982aeb4426d bytes=9117 -->
## FILE: tests/test_compare_equal.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_compare_equal.py`
- sha256: `7fc28920468f3edda3df8879d3a0ed2d658907bc0fa2262e21e3d982aeb4426d`
- bytes: 9117

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation


a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def equal_bool_builtins():
    a = BooleanValue(False)
    a.value = True == True  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_bool_builtins1():
    a = BooleanValue(False)
    a.value = False == False  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_bool_builtins2():
    a = BooleanValue(False)
    a.value = False == a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_bool_builtins3():
    a = BooleanValue(False)
    a.value = True == a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_simple_numbers():
    a = BooleanValue(False)
    a.value = 1 == 1
    return a.value


@nivs_rt_sequence
def equal_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = 1 == DoubleValue(2)
    return a.value


@nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(1) == DoubleValue(1)
    return a.value


@nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(0)
    a.value = DoubleValue(1) == I32Value(1)
    return a.value


@nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = I32Value(1) == DoubleValue(1)
    return a.value


@nivs_rt_sequence
def equal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(0)
    a.value = I32Value(1) == I32Value(2)
    return a.value


@nivs_rt_sequence
def equal_multiple_types():
    a = BooleanValue(0)
    a.value = 1 == DoubleValue(1) == 1.0
    return a.value


@nivs_rt_sequence
def equal_multiple_types1():
    a = BooleanValue(0)
    a.value = 1 == I32Value(2) == 3.0 == DoubleValue(4)
    return a.value


@nivs_rt_sequence
def equal_use_rtseq():
    a = BooleanValue(0)
    a.value = 5 == _return_constant()
    return a.value


@nivs_rt_sequence
def equal_use_rtseq1():
    a = BooleanValue(0)
    a.value = _return_constant() == 5
    return a.value


@nivs_rt_sequence
def equal_use_rtseq2():
    a = BooleanValue(0)
    a.value = DoubleValue(5) == _return_constant()
    return a.value


@nivs_rt_sequence
def equal_use_rtseq3():
    a = BooleanValue(0)
    a.value = _return_constant() == DoubleValue(5)
    return a.value


@nivs_rt_sequence
def equal_use_rtseq4():
    a = BooleanValue(0)
    a.value = I32Value(5) == _return_constant()
    return a.value


@nivs_rt_sequence
def equal_use_rtseq5():
    a = BooleanValue(0)
    a.value = _return_constant() == I32Value(5)
    return a.value


@nivs_rt_sequence
def equal_with_parentheses():
    a = BooleanValue(True)
    a.value = 1 == (2 == 3)
    return a.value


@nivs_rt_sequence
def equal_with_parentheses1():
    a = BooleanValue(True)
    a.value = 1 == (DoubleValue(2) == I32Value(5))
    return a.value


@nivs_rt_sequence
def equal_with_parentheses2():
    a = BooleanValue(True)
    a.value = DoubleValue(1) == (I32Value(2) == 3.0) == DoubleValue(4)
    return a.value


@nivs_rt_sequence
def equal_variables():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = 1 == a
    return b.value


@nivs_rt_sequence
def equal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = 1 == a.value
    return b.value


@nivs_rt_sequence
def equal_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a.value == b.value
    return c.value


@nivs_rt_sequence
def equal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value == b.value
    return c.value


@nivs_rt_sequence
def equal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a == b
    return c.value


@nivs_rt_sequence
def equal_variable_rtseq():
    a = DoubleValue(5)
    b = BooleanValue(0)
    b.value = a.value == _return_constant()
    return b.value


@nivs_rt_sequence
def equal_variable_rtseq1():
    a = DoubleValue(5)
    b = BooleanValue(0)
    b.value = _return_constant() == a.value
    return b.value


@nivs_rt_sequence
def equal_to_channel_ref():
    a = BooleanValue(True)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 == b.value
    return a.value


@nivs_rt_sequence
def equal_binary_unary():
    a = BooleanValue(0)
    a.value = -1 == -1
    return a.value


@nivs_rt_sequence
def equal_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 1 == 2 == 3 == 4
    return a.value


@nivs_rt_sequence
def equal_complex_expr():
    a = BooleanValue(0)
    a.value = 1 == (1 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def equal_invalid_variables():
    return a.value == b


@nivs_rt_sequence
def equal_invalid_variables1():
    return a.value == b.value


@nivs_rt_sequence
def equal_to_None():
    a = BooleanValue(0)
    a.value = None == 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def equal_invalid_rtseq_call():
    a = BooleanValue(0)
    a.value = _return_constant == 1
    return a.value


# </editor-fold>


run_tests = [
    (equal_bool_builtins, (), True),
    (equal_bool_builtins1, (), True),
    (equal_bool_builtins2, (), True),
    (equal_bool_builtins3, (), False),
    (equal_simple_numbers, (), True),
    (equal_num_nivsdatatype, (), False),
    (equal_nivsdatatype_nivsdatatype, (), True),
    (equal_nivsdatatype_nivsdatatype1, (), True),
    (equal_nivsdatatype_nivsdatatype2, (), True),
    (equal_nivsdatatype_nivsdatatype3, (), False),
    (equal_with_parentheses, (), False),
    (equal_with_parentheses1, (), False),
    (equal_variables, (), True),
    (equal_variables1, (), True),
    (equal_variable_variable, (), False),
    (equal_variable_variable1, (), True),
    (equal_variable_variable2, (), True),
    (equal_binary_unary, (), True),
    (equal_complex_expr, (), True),
    (equal_use_rtseq, (), True),
    (equal_use_rtseq1, (), True),
    (equal_use_rtseq2, (), True),
    (equal_use_rtseq3, (), True),
    (equal_use_rtseq4, (), True),
    (equal_use_rtseq5, (), True),
    (equal_variable_rtseq, (), True),
    (equal_variable_rtseq1, (), True),
    (equal_to_channel_ref, (), False),
]

fail_transform_tests = [
    (equal_invalid_variables, (), TranslateError),
    (equal_invalid_variables1, (), TranslateError),
    (equal_to_None, (), TranslateError),
    (equal_invalid_rtseq_call, (), VeristandError),
    (equal_multiple_types, (), TranslateError),
    (equal_multiple_types1, (), TranslateError),
    (equal_with_parentheses2, (), TranslateError),
    (equal_with_multiple_comparators, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_compare_greater.py sha256=35ca7b9537b08fd6adabcdd75c7ba9992927dda71fe9e2c30fb366bb86698b25 bytes=7785 -->
## FILE: tests/test_compare_greater.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_compare_greater.py`
- sha256: `35ca7b9537b08fd6adabcdd75c7ba9992927dda71fe9e2c30fb366bb86698b25`
- bytes: 7785

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def greater_simple_numbers():
    a = BooleanValue(False)
    a.value = 5 > 1
    return a.value


@nivs_rt_sequence
def greater_nivsdatatype_num():
    a = BooleanValue(False)
    a.value = DoubleValue(5) > 2
    return a.value


@nivs_rt_sequence
def greater_num_nivsdatatype():
    a = BooleanValue(False)
    a.value = 5 > DoubleValue(2)
    return a.value


@nivs_rt_sequence
def greater_nivsdatatype_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(5) > DoubleValue(1)
    return a.value


@nivs_rt_sequence
def greater_nivsdatatype_nivsdatatype1():
    a = BooleanValue(False)
    a.value = DoubleValue(5) > I32Value(1)
    return a.value


@nivs_rt_sequence
def greater_nivsdatatype_nivsdatatype2():
    a = BooleanValue(False)
    a.value = I32Value(5) > DoubleValue(1)
    return a.value


@nivs_rt_sequence
def greater_nivsdatatype_nivsdatatype3():
    a = BooleanValue(False)
    a.value = I32Value(5) > I32Value(2)
    return a.value


@nivs_rt_sequence
def greater_multiple_types():
    a = BooleanValue(False)
    a.value = DoubleValue(5) > 2 > 1.0
    return a.value


@nivs_rt_sequence
def greater_multiple_types1():
    a = BooleanValue(False)
    a.value = I32Value(5) > DoubleValue(4) > 3 > 2.0
    return a.value


@nivs_rt_sequence
def greater_use_rtseq():
    a = BooleanValue(False)
    a.value = 6 > _return_constant()
    return a.value


@nivs_rt_sequence
def greater_use_rtseq1():
    a = BooleanValue(False)
    a.value = _return_constant() > 4
    return a.value


@nivs_rt_sequence
def greater_use_rtseq2():
    a = BooleanValue(False)
    a.value = DoubleValue(6) > _return_constant()
    return a.value


@nivs_rt_sequence
def greater_use_rtseq3():
    a = BooleanValue(False)
    a.value = _return_constant() > DoubleValue(4)
    return a.value


@nivs_rt_sequence
def greater_use_rtseq4():
    a = BooleanValue(False)
    a.value = I32Value(6) > _return_constant()
    return a.value


@nivs_rt_sequence
def greater_use_rtseq5():
    a = BooleanValue(False)
    a.value = _return_constant() > I32Value(1)
    return a.value


@nivs_rt_sequence
def greater_with_parentheses():
    a = BooleanValue(False)
    a.value = 5 > (3 > 2)
    return a.value


@nivs_rt_sequence
def greater_variables():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a > 1
    return b.value


@nivs_rt_sequence
def greater_variables1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = 5 > a.value
    return b.value


@nivs_rt_sequence
def greater_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a.value > b.value
    return c.value


@nivs_rt_sequence
def greater_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a > b
    return c.value


@nivs_rt_sequence
def greater_variable_rtseq():
    a = DoubleValue(6.0)
    b = BooleanValue(False)
    b.value = a.value > _return_constant()
    return b.value


@nivs_rt_sequence
def greater_variable_rtseq1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = _return_constant() > a.value
    return b.value


@nivs_rt_sequence
def greater_to_channel_ref():
    a = BooleanValue(True)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 > b.value
    return a.value


@nivs_rt_sequence
def greater_binary_unary():
    a = BooleanValue(False)
    a.value = 2 > -1
    return a.value


@nivs_rt_sequence
def greater_with_multiple_comparators():
    a = BooleanValue(False)
    a.value = 5 > 4 > 3 > 2
    return a.value


@nivs_rt_sequence
def greater_complex_expr():
    a = BooleanValue(False)
    a.value = 2 > (1 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def greater_invalid_variables():
    return a.value > b


@nivs_rt_sequence
def greater_invalid_variables1():
    return a.value > b.value


@nivs_rt_sequence
def greater_to_None():
    a = BooleanValue(False)
    a.value = None > 1
    return a.value


@nivs_rt_sequence
def greater_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = _return_constant > 1
    return a.value


# </editor-fold>


run_tests = [
    (greater_simple_numbers, (), True),
    (greater_nivsdatatype_num, (), True),
    (greater_nivsdatatype_nivsdatatype, (), True),
    (greater_nivsdatatype_nivsdatatype1, (), True),
    (greater_nivsdatatype_nivsdatatype2, (), True),
    (greater_nivsdatatype_nivsdatatype3, (), True),
    (greater_with_parentheses, (), True),
    (greater_variables, (), True),
    (greater_variables1, (), True),
    (greater_variable_variable, (), True),
    (greater_variable_variable1, (), True),
    (greater_complex_expr, (), True),
    (greater_use_rtseq, (), True),
    (greater_use_rtseq1, (), True),
    (greater_use_rtseq2, (), True),
    (greater_use_rtseq3, (), True),
    (greater_use_rtseq4, (), True),
    (greater_use_rtseq5, (), True),
    (greater_variable_rtseq, (), True),
    (greater_variable_rtseq1, (), True),
    (greater_binary_unary, (), True),
    (greater_to_channel_ref, (), False),
    (greater_num_nivsdatatype, (), True),
]

fail_transform_tests = [
    (greater_invalid_variables, (), TranslateError),
    (greater_invalid_variables1, (), TranslateError),
    (greater_to_None, (), TranslateError),
    (greater_invalid_rtseq_call, (), VeristandError),
    (greater_multiple_types, (), TranslateError),
    (greater_multiple_types1, (), TranslateError),
    (greater_with_multiple_comparators, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_compare_greater_equal.py sha256=cb5d5f2708900228109975c9f216f22ddada2e12d9e1b30d71ace3b6bfc029ae bytes=14145 -->
## FILE: tests/test_compare_greater_equal.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_compare_greater_equal.py`
- sha256: `cb5d5f2708900228109975c9f216f22ddada2e12d9e1b30d71ace3b6bfc029ae`
- bytes: 14145

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def greater_eq_simple_numbers():
    a = BooleanValue(False)
    a.value = 5 >= 1
    return a.value


@nivs_rt_sequence
def greater_eq_nivsdatatype_num():
    a = BooleanValue(False)
    a.value = DoubleValue(5) >= 2
    return a.value


@nivs_rt_sequence
def greater_eq_num_nivsdatatype():
    a = BooleanValue(False)
    a.value = 5 >= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(5) >= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype1():
    a = BooleanValue(False)
    a.value = DoubleValue(5) >= I32Value(1)
    return a.value


@nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype2():
    a = BooleanValue(False)
    a.value = I32Value(5) >= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def greater_eq_nivsdatatype_nivsdatatype3():
    a = BooleanValue(False)
    a.value = I32Value(5) >= I32Value(2)
    return a.value


@nivs_rt_sequence
def greater_eq_multiple_types():
    a = BooleanValue(False)
    a.value = DoubleValue(5) >= 2 >= 1.0
    return a.value


@nivs_rt_sequence
def greater_eq_multiple_types1():
    a = BooleanValue(False)
    a.value = I32Value(5) >= DoubleValue(4) >= 3 >= 2.0
    return a.value


@nivs_rt_sequence
def greater_eq_use_rtseq():
    a = BooleanValue(False)
    a.value = 6 >= _return_constant()
    return a.value


@nivs_rt_sequence
def greater_eq_use_rtseq1():
    a = BooleanValue(False)
    a.value = _return_constant() >= 4
    return a.value


@nivs_rt_sequence
def greater_eq_use_rtseq2():
    a = BooleanValue(False)
    a.value = DoubleValue(6) >= _return_constant()
    return a.value


@nivs_rt_sequence
def greater_eq_use_rtseq3():
    a = BooleanValue(False)
    a.value = _return_constant() >= DoubleValue(4)
    return a.value


@nivs_rt_sequence
def greater_eq_use_rtseq4():
    a = BooleanValue(False)
    a.value = I32Value(6) >= _return_constant()
    return a.value


@nivs_rt_sequence
def greater_eq_use_rtseq5():
    a = BooleanValue(False)
    a.value = _return_constant() >= I32Value(1)
    return a.value


@nivs_rt_sequence
def greater_eq_with_parentheses():
    a = BooleanValue(False)
    a.value = 5 >= (3 >= 2)
    return a.value


@nivs_rt_sequence
def greater_eq_variables():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a >= 1
    return b.value


@nivs_rt_sequence
def greater_eq_variables1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = 5 >= a.value
    return b.value


@nivs_rt_sequence
def greater_eq_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a.value >= b.value
    return c.value


@nivs_rt_sequence
def greater_eq_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a >= b
    return c.value


@nivs_rt_sequence
def greater_eq_variable_rtseq():
    a = DoubleValue(6.0)
    b = BooleanValue(False)
    b.value = a.value >= _return_constant()
    return b.value


@nivs_rt_sequence
def greater_eq_variable_rtseq1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = _return_constant() >= a.value
    return b.value


@nivs_rt_sequence
def greater_eq_to_channel_ref():
    a = BooleanValue(True)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 >= b.value
    return a.value


@nivs_rt_sequence
def greater_eq_binary_unary():
    a = BooleanValue(False)
    a.value = 2 >= -1
    return a.value


@nivs_rt_sequence
def greater_eq_with_multiple_comparators():
    a = BooleanValue(False)
    a.value = 5 >= 4 >= 3 >= 2
    return a.value


@nivs_rt_sequence
def greater_eq_complex_expr():
    a = BooleanValue(False)
    a.value = 2 >= (1 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def greater_eq_invalid_variables():
    return a.value >= b


@nivs_rt_sequence
def greater_eq_invalid_variables1():
    return a.value >= b.value


@nivs_rt_sequence
def greater_eq_to_None():
    a = BooleanValue(False)
    a.value = None >= 1
    return a.value


@nivs_rt_sequence
def greater_eq_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = _return_constant >= 1
    return a.value


# </editor-fold>


@nivs_rt_sequence
def gt_equal_simple_numbers():
    a = BooleanValue(False)
    a.value = 1 >= 1
    return a.value


@nivs_rt_sequence
def gt_equal_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(1) >= 2
    return a.value


@nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(1) >= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(0)
    a.value = DoubleValue(1) >= I32Value(1)
    return a.value


@nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(0)
    a.value = I32Value(1) >= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def gt_equal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(0)
    a.value = I32Value(1) >= I32Value(2)
    return a.value


@nivs_rt_sequence
def gt_equal_multiple_types():
    a = BooleanValue(0)
    a.value = DoubleValue(1) >= 1 >= 1.0
    return a.value


@nivs_rt_sequence
def gt_equal_multiple_types1():
    a = BooleanValue(0)
    a.value = I32Value(1) >= DoubleValue(2) >= 3.0 >= 4
    return a.value


@nivs_rt_sequence
def gt_equal_use_rtseq():
    a = BooleanValue(0)
    a.value = 5 >= _return_constant()
    return a.value


@nivs_rt_sequence
def gt_equal_use_rtseq1():
    a = BooleanValue(0)
    a.value = _return_constant() >= 5
    return a.value


@nivs_rt_sequence
def gt_equal_use_rtseq2():
    a = BooleanValue(0)
    a.value = DoubleValue(5) >= _return_constant()
    return a.value


@nivs_rt_sequence
def gt_equal_use_rtseq3():
    a = BooleanValue(0)
    a.value = _return_constant() >= DoubleValue(5)
    return a.value


@nivs_rt_sequence
def gt_equal_use_rtseq4():
    a = BooleanValue(0)
    a.value = I32Value(5) >= _return_constant()
    return a.value


@nivs_rt_sequence
def gt_equal_use_rtseq5():
    a = BooleanValue(0)
    a.value = _return_constant() >= I32Value(5)
    return a.value


@nivs_rt_sequence
def gt_equal_with_parentheses():
    a = BooleanValue(True)
    a.value = 1 >= (2 >= 3)
    return a.value


@nivs_rt_sequence
def gt_equal_with_parentheses1():
    a = BooleanValue(True)
    a.value = 0 >= (DoubleValue(2) >= I32Value(2))
    return a.value


@nivs_rt_sequence
def gt_equal_variables():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = a >= 1
    return b.value


@nivs_rt_sequence
def gt_equal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = a.value >= 1
    return b.value


@nivs_rt_sequence
def gt_equal_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a.value >= b.value
    return c.value


@nivs_rt_sequence
def gt_equal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value >= b.value
    return c.value


@nivs_rt_sequence
def gt_equal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a >= b
    return c.value


@nivs_rt_sequence
def gt_equal_variable_rtseq():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a.value >= _return_constant()
    return b.value


@nivs_rt_sequence
def gt_equal_variable_rtseq1():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = _return_constant() >= a.value
    return b.value


@nivs_rt_sequence
def gt_equal_to_channel_ref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 1.0
    localhost_wait()
    a.value = 1 >= b.value
    return a.value


@nivs_rt_sequence
def gt_equal_binary_unary():
    a = BooleanValue(0)
    a.value = -1 >= -1
    return a.value


@nivs_rt_sequence
def gt_equal_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 1 >= 2 >= 3 >= 4
    return a.value


@nivs_rt_sequence
def gt_equal_complex_expr():
    a = BooleanValue(0)
    a.value = 1 >= (1 if 2 < 3 else 4)
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def gt_equal_invalid_variables():
    return a.value >= b


@nivs_rt_sequence
def gt_equal_invalid_variables1():
    return a.value >= b.value


@nivs_rt_sequence
def gt_equal_to_None():
    a = BooleanValue(0)
    a.value = None >= 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def gt_equal_invalid_rtseq_call():
    a = BooleanValue(0)
    a.value = _return_constant >= 1
    return a.value


# </editor-fold>


run_tests = [
    (greater_eq_simple_numbers, (), True),
    (greater_eq_nivsdatatype_num, (), True),
    (greater_eq_nivsdatatype_nivsdatatype, (), True),
    (greater_eq_nivsdatatype_nivsdatatype1, (), True),
    (greater_eq_nivsdatatype_nivsdatatype2, (), True),
    (greater_eq_nivsdatatype_nivsdatatype3, (), True),
    (greater_eq_with_parentheses, (), True),
    (greater_eq_variables, (), True),
    (greater_eq_variables1, (), True),
    (greater_eq_variable_variable, (), True),
    (greater_eq_variable_variable1, (), True),
    (greater_eq_complex_expr, (), True),
    (greater_eq_binary_unary, (), True),
    (gt_equal_simple_numbers, (), True),
    (gt_equal_num_nivsdatatype, (), False),
    (gt_equal_nivsdatatype_nivsdatatype, (), True),
    (gt_equal_nivsdatatype_nivsdatatype1, (), True),
    (gt_equal_nivsdatatype_nivsdatatype2, (), True),
    (gt_equal_nivsdatatype_nivsdatatype3, (), False),
    (gt_equal_with_parentheses, (), True),
    (gt_equal_with_parentheses1, (), False),
    (gt_equal_variables, (), True),
    (gt_equal_variables1, (), True),
    (gt_equal_variable_variable, (), False),
    (gt_equal_variable_variable1, (), True),
    (gt_equal_variable_variable2, (), True),
    (gt_equal_complex_expr, (), True),
    (gt_equal_binary_unary, (), True),
    (greater_eq_use_rtseq, (), True),
    (greater_eq_use_rtseq1, (), True),
    (greater_eq_use_rtseq2, (), True),
    (greater_eq_use_rtseq3, (), True),
    (greater_eq_use_rtseq4, (), True),
    (greater_eq_use_rtseq5, (), True),
    (greater_eq_variable_rtseq, (), True),
    (greater_eq_variable_rtseq1, (), True),
    (gt_equal_use_rtseq, (), True),
    (gt_equal_use_rtseq1, (), True),
    (gt_equal_use_rtseq2, (), True),
    (gt_equal_use_rtseq3, (), True),
    (gt_equal_use_rtseq4, (), True),
    (gt_equal_use_rtseq5, (), True),
    (gt_equal_variable_rtseq, (), True),
    (gt_equal_variable_rtseq1, (), True),
    (greater_eq_to_channel_ref, (), False),
    (gt_equal_to_channel_ref, (), True),
    (greater_eq_num_nivsdatatype, (), True),
]

fail_transform_tests = [
    (greater_eq_invalid_variables, (), TranslateError),
    (greater_eq_invalid_variables1, (), TranslateError),
    (gt_equal_invalid_variables, (), TranslateError),
    (gt_equal_invalid_variables1, (), TranslateError),
    (greater_eq_to_None, (), TranslateError),
    (gt_equal_to_None, (), TranslateError),
    (greater_eq_invalid_rtseq_call, (), VeristandError),
    (gt_equal_invalid_rtseq_call, (), VeristandError),
    (greater_eq_multiple_types, (), TranslateError),
    (greater_eq_multiple_types1, (), TranslateError),
    (greater_eq_with_multiple_comparators, (), TranslateError),
    (gt_equal_multiple_types, (), TranslateError),
    (gt_equal_multiple_types1, (), TranslateError),
    (gt_equal_with_multiple_comparators, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_compare_inequality.py sha256=d89cd5fc86693010b1465dc6615b2e2163ef5f01de80b975b3069a63ad734e1d bytes=9400 -->
## FILE: tests/test_compare_inequality.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_compare_inequality.py`
- sha256: `d89cd5fc86693010b1465dc6615b2e2163ef5f01de80b975b3069a63ad734e1d`
- bytes: 9400

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def notequal_bool_builtins():
    a = BooleanValue(True)
    a.value = True != True  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def notequal_bool_builtins1():
    a = BooleanValue(True)
    a.value = False != False  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def notequal_bool_builtins2():
    a = BooleanValue(False)
    a.value = False != a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def notequal_bool_builtins3():
    a = BooleanValue(False)
    a.value = True != a.value  # noqa: E712 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def notequal_simple_numbers():
    a = BooleanValue(True)
    a.value = 1 != 1
    return a.value


@nivs_rt_sequence
def notequal_num_nivsdatatype():
    a = BooleanValue(False)
    a.value = 1 != DoubleValue(2)
    return a.value


@nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(1) != DoubleValue(1)
    return a.value


@nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(True)
    a.value = DoubleValue(1) != I32Value(1)
    return a.value


@nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(True)
    a.value = I32Value(1) != DoubleValue(1)
    return a.value


@nivs_rt_sequence
def notequal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(False)
    a.value = I32Value(1) != I32Value(2)
    return a.value


@nivs_rt_sequence
def notequal_multiple_types():
    a = BooleanValue(True)
    a.value = 1 != DoubleValue(1) != 1.0
    return a.value


@nivs_rt_sequence
def notequal_multiple_types1():
    a = BooleanValue(False)
    a.value = 1 != I32Value(2) != 3.0 != DoubleValue(4)
    return a.value


@nivs_rt_sequence
def notequal_use_rtseq():
    a = BooleanValue(True)
    a.value = 5 != _return_constant()
    return a.value


@nivs_rt_sequence
def notequal_use_rtseq1():
    a = BooleanValue(True)
    a.value = _return_constant() != 5
    return a.value


@nivs_rt_sequence
def notequal_use_rtseq2():
    a = BooleanValue(True)
    a.value = DoubleValue(5) != _return_constant()
    return a.value


@nivs_rt_sequence
def notequal_use_rtseq3():
    a = BooleanValue(True)
    a.value = _return_constant() != DoubleValue(5)
    return a.value


@nivs_rt_sequence
def notequal_use_rtseq4():
    a = BooleanValue(False)
    a.value = I32Value(5) != _return_constant()
    return a.value


@nivs_rt_sequence
def notequal_use_rtseq5():
    a = BooleanValue(False)
    a.value = _return_constant() != I32Value(1)
    return a.value


@nivs_rt_sequence
def notequal_with_parentheses():
    a = BooleanValue(False)
    a.value = 0 != (2 != 3)
    return a.value


@nivs_rt_sequence
def notequal_with_parentheses1():
    a = BooleanValue(False)
    a.value = 0 != (DoubleValue(2) != I32Value(5))
    return a.value


@nivs_rt_sequence
def notequal_with_parentheses2():
    a = BooleanValue(False)
    a.value = DoubleValue(0) != (I32Value(2) != 3.0) != DoubleValue(4)
    return a.value


@nivs_rt_sequence
def notequal_variables():
    a = DoubleValue(1)
    b = BooleanValue(True)
    b.value = 1 != a
    return b.value


@nivs_rt_sequence
def notequal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(True)
    b.value = 1 != a.value
    return b.value


@nivs_rt_sequence
def notequal_variable_variable():
    a = DoubleValue(1)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value != b.value
    return c.value


@nivs_rt_sequence
def notequal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a.value != b.value
    return c.value


@nivs_rt_sequence
def notequal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(True)
    c.value = a != b
    return c.value


@nivs_rt_sequence
def notequal_variable_rtseq():
    a = BooleanValue(False)
    b = DoubleValue(0)
    a.value = b.value != _return_constant()
    return a.value


@nivs_rt_sequence
def notequal_variable_rtseq1():
    a = BooleanValue(False)
    b = DoubleValue(0)
    a.value = _return_constant() != b.value
    return a.value


@nivs_rt_sequence
def notequal_to_channel_ref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 != b.value
    return a.value


@nivs_rt_sequence
def notequal_binary_unary():
    a = BooleanValue(True)
    a.value = -1 != -1
    return a.value


@nivs_rt_sequence
def notequal_with_multiple_comparators():
    a = BooleanValue(False)
    a.value = 1 != 2 != 3 != 4
    return a.value


@nivs_rt_sequence
def notequal_complex_expr():
    a = BooleanValue(False)
    a.value = 1 != (2 if 2 < 3 else 1)
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def notequal_invalid_variables():
    return a.value != b


@nivs_rt_sequence
def notequal_invalid_variables1():
    return a.value != b.value


@nivs_rt_sequence
def notequal_to_None():
    a = BooleanValue(0)
    a.value = None != 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def notequal_invalid_rtseq_call():
    a = BooleanValue(0)
    a.value = _return_constant != 1
    return a.value


# </editor-fold>


run_tests = [
    (notequal_bool_builtins, (), False),
    (notequal_bool_builtins1, (), False),
    (notequal_bool_builtins2, (), False),
    (notequal_bool_builtins3, (), True),
    (notequal_simple_numbers, (), False),
    (notequal_num_nivsdatatype, (), True),
    (notequal_nivsdatatype_nivsdatatype, (), False),
    (notequal_nivsdatatype_nivsdatatype1, (), False),
    (notequal_nivsdatatype_nivsdatatype2, (), False),
    (notequal_nivsdatatype_nivsdatatype3, (), True),
    (notequal_with_parentheses, (), True),
    (notequal_with_parentheses1, (), True),
    (notequal_variables, (), False),
    (notequal_variables1, (), False),
    (notequal_variable_variable, (), True),
    (notequal_variable_variable1, (), False),
    (notequal_variable_variable2, (), False),
    (notequal_binary_unary, (), False),
    (notequal_complex_expr, (), True),
    (notequal_use_rtseq, (), False),
    (notequal_use_rtseq1, (), False),
    (notequal_use_rtseq2, (), False),
    (notequal_use_rtseq3, (), False),
    (notequal_use_rtseq4, (), False),
    (notequal_use_rtseq5, (), True),
    (notequal_variable_rtseq, (), True),
    (notequal_variable_rtseq1, (), True),
    (notequal_to_channel_ref, (), True),
]

fail_transform_tests = [
    (notequal_invalid_variables, (), TranslateError),
    (notequal_invalid_variables1, (), TranslateError),
    (notequal_to_None, (), TranslateError),
    (notequal_invalid_rtseq_call, (), VeristandError),
    (notequal_with_parentheses2, (), TranslateError),
    (notequal_with_multiple_comparators, (), TranslateError),
    (notequal_multiple_types, (), TranslateError),
    (notequal_multiple_types1, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_compare_less.py sha256=d4fdf0fc7be8892451c2af70e686fbc49767ef36e6733b884ebb6a1bb9cf85db bytes=7599 -->
## FILE: tests/test_compare_less.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_compare_less.py`
- sha256: `d4fdf0fc7be8892451c2af70e686fbc49767ef36e6733b884ebb6a1bb9cf85db`
- bytes: 7599

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def less_simple_numbers():
    a = BooleanValue(True)
    a.value = 5 < 1
    return a.value


@nivs_rt_sequence
def less_nivsdatatype_num():
    a = BooleanValue(True)
    a.value = DoubleValue(5) < 2
    return a.value


@nivs_rt_sequence
def less_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = 5 < DoubleValue(2)
    return a.value


@nivs_rt_sequence
def less_nivsdatatype_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(5) < DoubleValue(1)
    return a.value


@nivs_rt_sequence
def less_nivsdatatype_nivsdatatype1():
    a = BooleanValue(True)
    a.value = DoubleValue(5) < I32Value(1)
    return a.value


@nivs_rt_sequence
def less_nivsdatatype_nivsdatatype2():
    a = BooleanValue(True)
    a.value = I32Value(5) < DoubleValue(1)
    return a.value


@nivs_rt_sequence
def less_nivsdatatype_nivsdatatype3():
    a = BooleanValue(True)
    a.value = I32Value(5) < I32Value(2)
    return a.value


@nivs_rt_sequence
def less_multiple_types():
    a = BooleanValue(True)
    a.value = DoubleValue(5) < 2 < 1.0
    return a.value


@nivs_rt_sequence
def less_multiple_types1():
    a = BooleanValue(True)
    a.value = I32Value(5) < DoubleValue(4) < 3 < 2.0
    return a.value


@nivs_rt_sequence
def less_use_rtseq():
    a = BooleanValue(True)
    a.value = 5 < _return_constant()
    return a.value


@nivs_rt_sequence
def less_use_rtseq1():
    a = BooleanValue(True)
    a.value = _return_constant() < 4
    return a.value


@nivs_rt_sequence
def less_use_rtseq2():
    a = BooleanValue(True)
    a.value = DoubleValue(6) < _return_constant()
    return a.value


@nivs_rt_sequence
def less_use_rtseq3():
    a = BooleanValue(True)
    a.value = _return_constant() < DoubleValue(4)
    return a.value


@nivs_rt_sequence
def less_use_rtseq4():
    a = BooleanValue(True)
    a.value = I32Value(6) < _return_constant()
    return a.value


@nivs_rt_sequence
def less_use_rtseq5():
    a = BooleanValue(True)
    a.value = _return_constant() < I32Value(6)
    return a.value


@nivs_rt_sequence
def less_with_parentheses():
    a = BooleanValue(True)
    a.value = 5 < (3 < 2)
    return a.value


@nivs_rt_sequence
def less_variables():
    a = DoubleValue(5)
    b = BooleanValue(True)
    b.value = a < 1
    return b.value


@nivs_rt_sequence
def less_variables1():
    a = DoubleValue(1)
    b = BooleanValue(True)
    b.value = 5 < a.value
    return b.value


@nivs_rt_sequence
def less_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(True)
    c.value = a.value < b.value
    return c.value


@nivs_rt_sequence
def less_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(True)
    c.value = a < b
    return c.value


@nivs_rt_sequence
def less_variable_rtseq():
    a = DoubleValue(6.0)
    b = BooleanValue(True)
    b.value = a.value < _return_constant()
    return b.value


@nivs_rt_sequence
def less_variable_rtseq1():
    a = DoubleValue(1)
    b = BooleanValue(True)
    b.value = _return_constant() < a.value
    return b.value


@nivs_rt_sequence
def less_to_channel_ref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 < b.value
    return a.value


@nivs_rt_sequence
def less_binary_unary():
    a = BooleanValue(True)
    a.value = 2 < -1
    return a.value


@nivs_rt_sequence
def less_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 5 < 4 < 3 < 2
    return a.value


@nivs_rt_sequence
def less_complex_expr():
    a = BooleanValue(False)
    a.value = 1 < (2 if 2 < 3 else 1)
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def less_invalid_variables():
    return a.value < b


@nivs_rt_sequence
def less_invalid_variables1():
    return a.value < b.value


@nivs_rt_sequence
def less_to_None():
    a = BooleanValue(True)
    a.value = None < 1
    return a.value


@nivs_rt_sequence
def less_invalid_rtseq_call():
    a = BooleanValue(True)
    a.value = _return_constant < 1
    return a.value


# </editor-fold>


run_tests = [
    (less_simple_numbers, (), False),
    (less_nivsdatatype_num, (), False),
    (less_nivsdatatype_nivsdatatype, (), False),
    (less_nivsdatatype_nivsdatatype1, (), False),
    (less_nivsdatatype_nivsdatatype2, (), False),
    (less_nivsdatatype_nivsdatatype3, (), False),
    (less_with_parentheses, (), False),
    (less_variables, (), False),
    (less_variables1, (), False),
    (less_variable_variable, (), False),
    (less_variable_variable1, (), False),
    (less_complex_expr, (), True),
    (less_binary_unary, (), False),
    (less_use_rtseq, (), False),
    (less_use_rtseq1, (), False),
    (less_use_rtseq2, (), False),
    (less_use_rtseq3, (), False),
    (less_use_rtseq4, (), False),
    (less_use_rtseq5, (), True),
    (less_variable_rtseq, (), False),
    (less_variable_rtseq1, (), False),
    (less_to_channel_ref, (), True),
    (less_num_nivsdatatype, (), False),
]

fail_transform_tests = [
    (less_invalid_variables, (), TranslateError),
    (less_invalid_variables1, (), TranslateError),
    (less_to_None, (), TranslateError),
    (less_invalid_rtseq_call, (), VeristandError),
    (less_multiple_types, (), TranslateError),
    (less_multiple_types1, (), TranslateError),
    (less_with_multiple_comparators, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_compare_less_equal.py sha256=38c84e1760ab4406bec0ab3d76c6ba6248494bd0035bd7d46f2e61cfdfb1b161 bytes=14021 -->
## FILE: tests/test_compare_less_equal.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_compare_less_equal.py`
- sha256: `38c84e1760ab4406bec0ab3d76c6ba6248494bd0035bd7d46f2e61cfdfb1b161`
- bytes: 14021

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, ChannelReference, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def less_eq_simple_numbers():
    a = BooleanValue(True)
    a.value = 5 <= 1
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_num():
    a = BooleanValue(True)
    a.value = DoubleValue(5) <= 2
    return a.value


@nivs_rt_sequence
def less_eq_num_nivsdatatype():
    a = BooleanValue(True)
    a.value = 5 <= DoubleValue(2)
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(5) <= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_nivsdatatype1():
    a = BooleanValue(True)
    a.value = DoubleValue(5) <= I32Value(1)
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_nivsdatatype2():
    a = BooleanValue(True)
    a.value = I32Value(5) <= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def less_eq_nivsdatatype_nivsdatatype3():
    a = BooleanValue(True)
    a.value = I32Value(5) <= I32Value(2)
    return a.value


@nivs_rt_sequence
def less_eq_multiple_types():
    a = BooleanValue(True)
    a.value = DoubleValue(5) <= 2 <= 1.0
    return a.value


@nivs_rt_sequence
def less_eq_multiple_types1():
    a = BooleanValue(True)
    a.value = I32Value(2.0) <= DoubleValue(3) <= 4 <= 5.0
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq():
    a = BooleanValue(True)
    a.value = 6 <= _return_constant()
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq1():
    a = BooleanValue(True)
    a.value = _return_constant() <= 4
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq2():
    a = BooleanValue(True)
    a.value = DoubleValue(6) <= _return_constant()
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq3():
    a = BooleanValue(True)
    a.value = _return_constant() <= DoubleValue(4)
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq4():
    a = BooleanValue(True)
    a.value = I32Value(6) <= _return_constant()
    return a.value


@nivs_rt_sequence
def less_eq_use_rtseq5():
    a = BooleanValue(True)
    a.value = _return_constant() <= I32Value(1)
    return a.value


@nivs_rt_sequence
def less_eq_with_parentheses():
    a = BooleanValue(True)
    a.value = 5 <= (3 <= 2)
    return a.value


@nivs_rt_sequence
def less_eq_variables():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a <= 1
    return b.value


@nivs_rt_sequence
def less_eq_variables1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = 5 <= a.value
    return b.value


@nivs_rt_sequence
def less_eq_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a.value <= b.value
    return c.value


@nivs_rt_sequence
def less_eq_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(False)
    c.value = a <= b
    return c.value


@nivs_rt_sequence
def less_eq_variable_rtseq():
    a = DoubleValue(6.0)
    b = BooleanValue(False)
    b.value = a.value <= _return_constant()
    return b.value


@nivs_rt_sequence
def less_eq_variable_rtseq1():
    a = DoubleValue(1)
    b = BooleanValue(False)
    b.value = _return_constant() <= a.value
    return b.value


@nivs_rt_sequence
def less_eq_to_channel_ref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 5.0
    localhost_wait()
    a.value = 1 <= b.value
    return a.value


@nivs_rt_sequence
def less_eq_binary_unary():
    a = BooleanValue(True)
    a.value = 2 <= -1
    return a.value


@nivs_rt_sequence
def less_eq_with_multiple_comparators():
    a = BooleanValue(True)
    a.value = 5 <= 4 <= 3 <= 2
    return a.value


@nivs_rt_sequence
def less_eq_complex_expr():
    a = BooleanValue(False)
    a.value = 1 <= (2 if 2 < 3 else 1)
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def less_eq_invalid_variables():
    return a.value <= b


@nivs_rt_sequence
def less_eq_invalid_variables1():
    return a.value <= b.value


@nivs_rt_sequence
def less_eq_to_None():
    a = BooleanValue(True)
    a.value = None <= 1
    return a.value


@nivs_rt_sequence
def less_eq_invalid_rtseq_call():
    a = BooleanValue(True)
    a.value = _return_constant <= 1
    return a.value


# </editor-fold>


@nivs_rt_sequence
def lt_equal_simple_numbers():
    a = BooleanValue(True)
    a.value = 1 <= 1
    return a.value


@nivs_rt_sequence
def lt_equal_num_nivsdatatype():
    a = BooleanValue(False)
    a.value = DoubleValue(1) <= 2
    return a.value


@nivs_rt_sequence
def lt_equal_nivsdatatype_nivsdatatype():
    a = BooleanValue(True)
    a.value = DoubleValue(1) <= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def lt_equal_nivsdatatype_nivsdatatype1():
    a = BooleanValue(True)
    a.value = DoubleValue(1) <= I32Value(1)
    return a.value


@nivs_rt_sequence
def lt_equal_nivsdatatype_nivsdatatype2():
    a = BooleanValue(True)
    a.value = I32Value(1) <= DoubleValue(1)
    return a.value


@nivs_rt_sequence
def lt_equal_nivsdatatype_nivsdatatype3():
    a = BooleanValue(True)
    a.value = I32Value(2) <= I32Value(1)
    return a.value


@nivs_rt_sequence
def lt_equal_multiple_types():
    a = BooleanValue(True)
    a.value = DoubleValue(1) <= 1 <= 1.0
    return a.value


@nivs_rt_sequence
def lt_equal_multiple_types1():
    a = BooleanValue(True)
    a.value = I32Value(4) <= DoubleValue(3) <= 2.0 <= 1
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq():
    a = BooleanValue(False)
    a.value = 5 <= _return_constant()
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq1():
    a = BooleanValue(False)
    a.value = _return_constant() <= 5
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq2():
    a = BooleanValue(False)
    a.value = DoubleValue(5) <= _return_constant()
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq3():
    a = BooleanValue(False)
    a.value = _return_constant() <= DoubleValue(5)
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq4():
    a = BooleanValue(False)
    a.value = I32Value(5) <= _return_constant()
    return a.value


@nivs_rt_sequence
def lt_equal_use_rtseq5():
    a = BooleanValue(True)
    a.value = _return_constant() <= I32Value(1)
    return a.value


@nivs_rt_sequence
def lt_equal_with_parentheses():
    a = BooleanValue(False)
    a.value = 1 <= (2 <= 3)
    return a.value


@nivs_rt_sequence
def lt_equal_with_parentheses1():
    a = BooleanValue(False)
    a.value = 3 <= (DoubleValue(2) <= I32Value(2))
    return a.value


@nivs_rt_sequence
def lt_equal_variables():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = a <= 1
    return b.value


@nivs_rt_sequence
def lt_equal_variables1():
    a = DoubleValue(1)
    b = BooleanValue(0)
    b.value = a.value <= 1
    return b.value


@nivs_rt_sequence
def lt_equal_variable_variable():
    a = DoubleValue(2)
    b = DoubleValue(1)
    c = BooleanValue(True)
    c.value = a.value <= b.value
    return c.value


@nivs_rt_sequence
def lt_equal_variable_variable1():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a.value <= b.value
    return c.value


@nivs_rt_sequence
def lt_equal_variable_variable2():
    a = DoubleValue(2)
    b = DoubleValue(2)
    c = BooleanValue(False)
    c.value = a <= b
    return c.value


@nivs_rt_sequence
def lt_equal_variable_rtseq():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = a.value <= _return_constant()
    return b.value


@nivs_rt_sequence
def lt_equal_variable_rtseq1():
    a = DoubleValue(5)
    b = BooleanValue(False)
    b.value = _return_constant() <= a.value
    return b.value


@nivs_rt_sequence
def lt_equal_to_channel_ref():
    a = BooleanValue(False)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 1.0
    localhost_wait()
    a.value = 1 <= b.value
    return a.value


@nivs_rt_sequence
def lt_equal_binary_unary():
    a = BooleanValue(True)
    a.value = -1 <= -1
    return a.value


@nivs_rt_sequence
def lt_equal_with_multiple_comparators():
    a = BooleanValue(False)
    a.value = 4 <= 3 <= 2 <= 1
    return a.value


@nivs_rt_sequence
def lt_equal_complex_expr():
    a = BooleanValue(False)
    a.value = 1 <= (1 if 2 < 3 else 0)
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def lt_equal_invalid_variables():
    return a.value <= b


@nivs_rt_sequence
def lt_equal_invalid_variables1():
    return a.value <= b.value


@nivs_rt_sequence
def lt_equal_to_None():
    a = BooleanValue(True)
    a.value = None <= 1  # noqa: E711 the identity operator "is" is not being tested here.
    return a.value


@nivs_rt_sequence
def lt_equal_invalid_rtseq_call():
    a = BooleanValue(True)
    a.value = _return_constant <= 1
    return a.value


# </editor-fold>


run_tests = [
    (less_eq_simple_numbers, (), False),
    (less_eq_nivsdatatype_num, (), False),
    (less_eq_nivsdatatype_nivsdatatype, (), False),
    (less_eq_nivsdatatype_nivsdatatype1, (), False),
    (less_eq_nivsdatatype_nivsdatatype2, (), False),
    (less_eq_nivsdatatype_nivsdatatype3, (), False),
    (less_eq_with_parentheses, (), False),
    (less_eq_variables, (), False),
    (less_eq_variables1, (), False),
    (less_eq_variable_variable, (), False),
    (less_eq_variable_variable1, (), False),
    (less_eq_binary_unary, (), False),
    (less_eq_complex_expr, (), True),
    (lt_equal_simple_numbers, (), True),
    (lt_equal_num_nivsdatatype, (), True),
    (lt_equal_nivsdatatype_nivsdatatype, (), True),
    (lt_equal_nivsdatatype_nivsdatatype1, (), True),
    (lt_equal_nivsdatatype_nivsdatatype2, (), True),
    (lt_equal_nivsdatatype_nivsdatatype3, (), False),
    (lt_equal_with_parentheses, (), True),
    (lt_equal_with_parentheses1, (), False),
    (lt_equal_variables, (), True),
    (lt_equal_variables1, (), True),
    (lt_equal_variable_variable, (), False),
    (lt_equal_variable_variable1, (), True),
    (lt_equal_variable_variable2, (), True),
    (lt_equal_binary_unary, (), True),
    (lt_equal_complex_expr, (), True),
    (less_eq_use_rtseq, (), False),
    (less_eq_use_rtseq1, (), False),
    (less_eq_use_rtseq2, (), False),
    (less_eq_use_rtseq3, (), False),
    (less_eq_use_rtseq4, (), False),
    (less_eq_use_rtseq5, (), False),
    (less_eq_variable_rtseq, (), False),
    (less_eq_variable_rtseq1, (), False),
    (lt_equal_use_rtseq, (), True),
    (lt_equal_use_rtseq1, (), True),
    (lt_equal_use_rtseq2, (), True),
    (lt_equal_use_rtseq3, (), True),
    (lt_equal_use_rtseq4, (), True),
    (lt_equal_use_rtseq5, (), False),
    (lt_equal_variable_rtseq, (), True),
    (lt_equal_variable_rtseq1, (), True),
    (less_eq_to_channel_ref, (), True),
    (lt_equal_to_channel_ref, (), True),
    (less_eq_num_nivsdatatype, (), False),
]

fail_transform_tests = [
    (less_eq_invalid_variables, (), TranslateError),
    (less_eq_invalid_variables1, (), TranslateError),
    (lt_equal_invalid_variables, (), TranslateError),
    (lt_equal_invalid_variables1, (), TranslateError),
    (less_eq_to_None, (), TranslateError),
    (lt_equal_to_None, (), TranslateError),
    (less_eq_invalid_rtseq_call, (), VeristandError),
    (lt_equal_invalid_rtseq_call, (), VeristandError),
    (less_eq_multiple_types, (), TranslateError),
    (less_eq_multiple_types1, (), TranslateError),
    (less_eq_with_multiple_comparators, (), TranslateError),
    (lt_equal_multiple_types, (), TranslateError),
    (lt_equal_multiple_types1, (), TranslateError),
    (lt_equal_with_multiple_comparators, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_conditional.py sha256=93ae27e34e36d58afe463ef368f5e788f0bb1e3f3382a3f7a256f3ac0a9c0a06 bytes=7335 -->
## FILE: tests/test_conditional.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_conditional.py`
- sha256: `93ae27e34e36d58afe463ef368f5e788f0bb1e3f3382a3f7a256f3ac0a9c0a06`
- bytes: 7335

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def if_pass():
    if True:
        pass


@nivs_rt_sequence
def if_else_pass():
    if True:
        pass
    else:
        pass


@nivs_rt_sequence
def if_invalid_boolean():
    if 1:
        pass


@nivs_rt_sequence
def if_invalid_boolean_const():
    if I32Value(0):
        pass


@nivs_rt_sequence
def if_invalid_boolean_var():
    a = I32Value(1)
    if a.value:
        pass


@nivs_rt_sequence
def if_elif_pass():
    if True:
        pass
    elif True:
        pass
    else:
        pass


@nivs_rt_sequence
def if_nested():
    if True:
        if True:
            if True:
                pass
            else:
                if True:
                    pass
                else:
                    pass
        elif True:
            pass
        else:
            pass
    else:
        pass


@nivs_rt_sequence
def if_one_statement():
    ret_var = I32Value(0)
    if True:
        ret_var.value = 1
    else:
        ret_var.value = 2
    return ret_var.value


@nivs_rt_sequence
def if_multiple_statements():
    ret_var = I32Value(0)
    if True:
        ret_var.value = 1
        ret_var.value = 2
        ret_var.value = 3
    elif False:
        ret_var.value = 4
        ret_var.value = 5
    else:
        ret_var.value = 6
        ret_var.value = 7
        ret_var.value = 8

    return ret_var.value


@nivs_rt_sequence
def if_condition_variable():
    var = BooleanValue(0)
    if var.value:
        var.value = True
    else:
        var.value = False
    return var.value


@nivs_rt_sequence
def if_condition_equal_operator():
    var = I32Value(1)
    if var.value == 1:
        var.value = 2
    else:
        var.value = 3
    return var.value


@nivs_rt_sequence
def if_condition_identity_operator():
    var = BooleanValue(True)
    ret = I32Value(0)
    if var.value is True:
        ret.value = 1
    return ret.value


@nivs_rt_sequence
def if_condition_identity_not_operator():
    var = BooleanValue(True)
    ret = I32Value(0)
    if var is not False:
        ret.value = 1
    return ret.value


@nivs_rt_sequence
def _returns_true():
    a = BooleanValue(True)
    return a.value


@nivs_rt_sequence
def if_condition_function_call():
    ret = I32Value(0)
    if _returns_true():
        ret.value = 1
    return ret.value


@nivs_rt_sequence
def if_condition_complex_expression():
    a = I32Value(0)
    if (True and False) is not _returns_true() or a.value < 10:
        a.value = 1
    return a.value


@nivs_rt_sequence
def if_elif_condition_complex_expression():
    a = I32Value(0)
    if False:
        a.value = 1
    elif (True and False) is not _returns_true() or a.value < 10:
        a.value = 2
    return a.value


@nivs_rt_sequence
def if_try_catch_fails():
    if True:
        try:
            pass
        except Exception:
            pass
        finally:
            pass


@nivs_rt_sequence
def if_try_finally_fails():
    if True:
        try:
            pass
        finally:
            pass


@nivs_rt_sequence
def if_else_try_finally_fails():
    if True:
        pass
    else:
        try:
            pass
        finally:
            pass


@nivs_rt_sequence
def if_elif_try_finally_fails():
    if True:
        pass
    elif True:
        try:
            pass
        finally:
            pass
    else:
        pass


@nivs_rt_sequence
def if_return_fails():
    a = BooleanValue(True)
    if True:
        return a.value


@nivs_rt_sequence
def if_else_return_fails():
    a = BooleanValue(True)
    if True:
        pass
    else:
        return a.value


@nivs_rt_sequence
def if_elif_return_fails():
    a = BooleanValue(True)
    if False:
        pass
    elif True:
        return a.value
    else:
        pass


@nivs_rt_sequence
def if_funcdef_fails():
    if True:

        def func():
            pass


@nivs_rt_sequence
def if_else_funcdef_fails():
    if False:
        pass
    else:

        def func():
            pass


@nivs_rt_sequence
def if_elif_funcdef_fails():
    if False:
        pass
    elif True:

        def func():
            pass

    else:
        pass


run_tests = [
    (if_one_statement, (), 1),
    (if_multiple_statements, (), 3),
    (if_condition_variable, (), False),
    (if_condition_equal_operator, (), 2),
    (if_condition_function_call, (), 1),
    (if_condition_identity_operator, (), 1),
    (if_condition_identity_not_operator, (), 1),
    (if_condition_complex_expression, (), 1),
    (if_elif_condition_complex_expression, (), 2),
]


transform_tests = run_tests + [
    (if_pass, (), 0),
    (if_else_pass, (), 0),
    (if_elif_pass, (), 0),
    (if_nested, (), 0),
]


fail_transform_tests = [
    (if_invalid_boolean, (), VeristandError),
    (if_invalid_boolean_const, (), VeristandError),
    (if_invalid_boolean_var, (), VeristandError),
    (if_return_fails, (), TranslateError),
    (if_elif_return_fails, (), TranslateError),
    (if_else_return_fails, (), TranslateError),
    (if_try_catch_fails, (), TranslateError),
    (if_try_finally_fails, (), TranslateError),
    (if_elif_try_finally_fails, (), TranslateError),
    (if_else_try_finally_fails, (), TranslateError),
    (if_funcdef_fails, (), TranslateError),
    (if_elif_funcdef_fails, (), TranslateError),
    (if_else_funcdef_fails, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", transform_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_datatypes.py sha256=ca3217cea0d08745a10f258abac4c9a76f96c6380dc8bfb4d0674d76bd00af7e bytes=32182 -->
## FILE: tests/test_datatypes.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_datatypes.py`
- sha256: `ca3217cea0d08745a10f258abac4c9a76f96c6380dc8bfb4d0674d76bd00af7e`
- bytes: 32182

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue
from niveristand.clientapi import BooleanValueArray
from niveristand.clientapi import DoubleValue
from niveristand.clientapi import DoubleValueArray
from niveristand.clientapi import I32Value
from niveristand.clientapi import I32ValueArray
from niveristand.clientapi import I64Value
from niveristand.clientapi import I64ValueArray
from niveristand.clientapi import RealTimeSequence
from niveristand.clientapi import U32Value
from niveristand.clientapi import U32ValueArray
from niveristand.clientapi import U64Value
from niveristand.clientapi import U64ValueArray
from niveristand.errors import TranslateError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def boolean_type():
    a = BooleanValue(True)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type1():
    a = BooleanValue(False)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type2():
    a = BooleanValue(1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type3():
    a = BooleanValue(0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type_run():
    a = BooleanValue(True)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@nivs_rt_sequence
def boolean_type1_run():
    a = BooleanValue(False)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@nivs_rt_sequence
def boolean_type2_run():
    a = BooleanValue(1)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@nivs_rt_sequence
def boolean_type3_run():
    a = BooleanValue(0)  # noqa: F841 it's ok for this variable to never be used
    return a.value


@nivs_rt_sequence
def illegal_boolean_type():
    a = BooleanValue("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_type():
    a = DoubleValue(5)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_type1():
    a = DoubleValue(5.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_type_run():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def double_type1_run():
    a = DoubleValue(5.0)
    return a.value


@nivs_rt_sequence
def illegal_double_type():
    a = DoubleValue("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_type():
    a = I32Value(2)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_type1():
    a = I32Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_type_run():
    a = I32Value(2)
    return a.value


@nivs_rt_sequence
def int32_type1_run():
    a = I32Value(1.0)
    return a.value


@nivs_rt_sequence
def illegal_int32_type():
    a = I32Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_overflow_error():
    a = I32Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_type():
    a = I64Value(2)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_type1():
    a = I64Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_type_run():
    a = I64Value(2)
    return a.value


@nivs_rt_sequence
def int64_type1_run():
    a = I64Value(1.0)
    return a.value


@nivs_rt_sequence
def illegal_int64_type():
    a = I64Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_overflow_error():
    a = I64Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_type():
    a = U32Value(2)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_type1():
    a = U32Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_type_run():
    a = U32Value(2)
    return a.value


@nivs_rt_sequence
def uint32_type1_run():
    a = U32Value(1.0)
    return a.value


@nivs_rt_sequence
def illegal_uint32_type():
    a = U32Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_overflow_error():
    a = U32Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_type():
    a = U64Value(2)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_type1():
    a = U64Value(1.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_type_run():
    a = U64Value(2)
    return a.value


@nivs_rt_sequence
def uint64_type1_run():
    a = U64Value(1.0)
    return a.value


@nivs_rt_sequence
def illegal_uint64_type():
    a = U64Value("Some string")  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_overflow_error():
    a = U64Value(100000000000000000000)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type_negative():
    a = BooleanValue(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_type_negative():
    a = DoubleValue(-5.0)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_type_negative():
    a = I32Value(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_type_negative():
    a = I64Value(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_type_negative():
    a = U32Value(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_type_negative():
    a = U64Value(-1)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_type_negative_run():
    a = BooleanValue(-1)
    return a.value


@nivs_rt_sequence
def double_type_negative_run():
    a = DoubleValue(-5.0)
    return a.value


@nivs_rt_sequence
def int32_type_negative_run():
    a = I32Value(-1)
    return a.value


@nivs_rt_sequence
def int64_type_negative_run():
    a = I64Value(-1)
    return a.value


@nivs_rt_sequence
def uint32_type_negative_run():
    a = U32Value(-1)
    return a.value


@nivs_rt_sequence
def uint64_type_negative_run():
    a = U64Value(-1)
    return a.value


@nivs_rt_sequence
def boolean_array_one_element():
    a = BooleanValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_array_type():
    a = BooleanValueArray(  # noqa: F841 it's ok for this variable to never be used
        [True, False, 1, 0]
    )


@nivs_rt_sequence
def boolean_array_empty():
    a = BooleanValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def boolean_array_one_element_run():
    a = BooleanValueArray([1])
    return a[0].value


@nivs_rt_sequence
def boolean_array_type_run():
    a = BooleanValueArray([True, False, 1, 0])
    return a[3].value


@nivs_rt_sequence
def boolean_array_invalid_type():
    a = BooleanValueArray(  # noqa: F841 it's ok for this variable to never be used
        [True, "something"]
    )


@nivs_rt_sequence
def boolean_array_invalid_type1():
    a = BooleanValueArray([True, "False"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_one_element():
    a = DoubleValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_type():
    a = DoubleValueArray([0, 1.0, 5.5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_empty():
    a = DoubleValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def double_array_one_element_run():
    a = DoubleValueArray([1])
    return a[0].value


@nivs_rt_sequence
def double_array_type_run():
    a = DoubleValueArray([0, 1.0, 5.5])
    return a[2].value


@nivs_rt_sequence
def double_array_invalid_type():
    a = DoubleValueArray(  # noqa: F841 it's ok for this variable to never be used
        [5.5, "something"]
    )


@nivs_rt_sequence
def double_array_invalid_type1():
    a = DoubleValueArray([5.5, "5.5"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_one_element():
    a = I32ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_type():
    a = I32ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_empty():
    a = I32ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_one_element_run():
    a = I32ValueArray([1])
    return a[0].value


@nivs_rt_sequence
def int32_array_type_run():
    a = I32ValueArray([0, 1, 5])
    return a[2].value


@nivs_rt_sequence
def int32_array_invalid_type():
    a = I32ValueArray([5, "something"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int32_array_invalid_type1():
    a = I32ValueArray([5, "-5"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_one_element():
    a = I64ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_type():
    a = I64ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_empty():
    a = I64ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_one_element_run():
    a = I64ValueArray([1])
    return a[0].value


@nivs_rt_sequence
def int64_array_type_run():
    a = I64ValueArray([0, 1, 5])
    return a[2].value


@nivs_rt_sequence
def int64_array_invalid_type():
    a = I64ValueArray([5, "something"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def int64_array_invalid_type1():
    a = I64ValueArray([5, "-5"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_one_element():
    a = U32ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_type():
    a = U32ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_empty():
    a = U32ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_one_element_run():
    a = U32ValueArray([1])
    return a[0].value


@nivs_rt_sequence
def uint32_array_type_run():
    a = U32ValueArray([0, 1, 5])
    return a[2].value


@nivs_rt_sequence
def uint32_array_invalid_type():
    a = U32ValueArray([5, "something"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_invalid_type1():
    a = U32ValueArray([5, "5"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint32_array_negative_values():
    a = U32ValueArray([-5, -1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_one_element():
    a = U64ValueArray([1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_type():
    a = U64ValueArray([0, 1, 5])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_one_element_run():
    a = U64ValueArray([1])
    return a[0].value


@nivs_rt_sequence
def uint64_array_type_run():
    a = U64ValueArray([0, 1, 5])
    return a[2].value


@nivs_rt_sequence
def uint64_array_empty():
    a = U64ValueArray([])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_invalid_type():
    a = U64ValueArray([5, "something"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_invalid_type1():
    a = U64ValueArray([5, "5"])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def uint64_array_negative_values():
    a = U64ValueArray([-5, -1])  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def invalid_return_type():
    return DoubleValueArray([5.0, 1])


@nivs_rt_sequence
def int32_max_value():
    a = I32Value(0x7FFFFFFF)
    return a.value


@nivs_rt_sequence
def int32_max_value_overflow():
    a = I32Value(0x800000001)
    return a.value


@nivs_rt_sequence
def int64_max_value():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    return a.value


@nivs_rt_sequence
def int64_max_value_overflow():
    a = I64Value(0x80000000000000001)
    return a.value


@nivs_rt_sequence
def uint32_max_value():
    a = U32Value(0xFFFFFFFF)
    return a.value


@nivs_rt_sequence
def uint32_max_value_overflow():
    a = U32Value(0x800000001)
    return a.value


@nivs_rt_sequence
def uint64_max_value():
    a = U64Value(0xFFFFFFFFFFFFFFFF)
    return a.value


@nivs_rt_sequence
def uint64_max_value_overflow():
    a = U64Value(0x80000000000000001)
    return a.value


@nivs_rt_sequence
def int32_array_overflow():
    a = I32ValueArray([0x80000000, 0x80000000])
    return a.value


@nivs_rt_sequence
def int64_array_overflow():
    a = I64ValueArray([0x80000000000000001, 0x8000000000000000])
    return a.value


@nivs_rt_sequence
def uint32_array_overflow():
    a = U32ValueArray([0x800000001, 0x80000000])
    return a.value


@nivs_rt_sequence
def uint64_array_overflow():
    a = U64ValueArray([0x80000000000000001, 0x8000000000000000])
    return a.value


transform_tests = [
    (boolean_type, ()),
    (boolean_type1, ()),
    (boolean_type2, ()),
    (boolean_type3, ()),
    (double_type, ()),
    (double_type1, ()),
    (int32_type, ()),
    (int32_type1, ()),
    (int64_type, ()),
    (int64_type1, ()),
    (uint32_type, ()),
    (uint32_type1, ()),
    (uint64_type, ()),
    (uint64_type1, ()),
    (boolean_array_type, ()),
    (double_array_type, ()),
    (int32_array_type, ()),
    (int64_array_type, ()),
    (uint32_array_type, ()),
    (uint64_array_type, ()),
    (boolean_array_empty, ()),
    (double_array_empty, ()),
    (int32_array_empty, ()),
    (int64_array_empty, ()),
    (uint32_array_empty, ()),
    (uint64_array_empty, ()),
    (boolean_array_one_element, ()),
    (double_array_one_element, ()),
    (int32_array_one_element, ()),
    (int64_array_one_element, ()),
    (uint32_array_one_element, ()),
    (uint64_array_one_element, ()),
    (boolean_type_negative, ()),
    (double_type_negative, ()),
    (int32_type_negative, ()),
    (int64_type_negative, ()),
]

run_tests = [
    (boolean_type_run, (), True),
    (boolean_type1_run, (), False),
    (boolean_type2_run, (), True),
    (boolean_type3_run, (), False),
    (double_type_run, (), 5.0),
    (double_type1_run, (), 5.0),
    (int32_type_run, (), 2),
    (int32_type1_run, (), 1),
    (int64_type_run, (), 2),
    (int64_type1_run, (), 1),
    (uint32_type_run, (), 2),
    (uint32_type1_run, (), 1),
    (uint64_type_run, (), 2),
    (uint64_type1_run, (), 1),
    (boolean_type_negative_run, (), True),
    (double_type_negative_run, (), -5.0),
    (int32_type_negative_run, (), -1),
    (int64_type_negative_run, (), -1),
    (int32_max_value, (), 0x7FFFFFFF),
    (int64_max_value, (), 0x7FFFFFFFFFFFFFFF),
    (uint32_max_value, (), 0xFFFFFFFF),
    (uint64_max_value, (), 0xFFFFFFFFFFFFFFFF),
    (boolean_array_type_run, (), False),
    (double_array_type_run, (), 5.5),
    (int32_array_type_run, (), 5),
    (int64_array_type_run, (), 5),
    (uint32_array_type_run, (), 5),
    (uint64_array_type_run, (), 5),
    (boolean_array_one_element_run, (), 1),
    (double_array_one_element_run, (), 1),
    (int32_array_one_element_run, (), 1),
    (int64_array_one_element_run, (), 1),
    (uint32_array_one_element_run, (), 1),
    (uint64_array_one_element_run, (), 1),
]

fail_transform_tests = [
    (illegal_boolean_type, TranslateError),
    (illegal_double_type, TranslateError),
    (illegal_int32_type, TranslateError),
    (int32_overflow_error, OverflowError),
    (illegal_int64_type, TranslateError),
    (int64_overflow_error, OverflowError),
    (illegal_uint32_type, TranslateError),
    (uint32_overflow_error, OverflowError),
    (illegal_uint64_type, TranslateError),
    (uint64_overflow_error, OverflowError),
    (boolean_array_invalid_type, TranslateError),
    (boolean_array_invalid_type1, TranslateError),
    (double_array_invalid_type, TranslateError),
    (double_array_invalid_type1, TranslateError),
    (int32_array_invalid_type, TranslateError),
    (int32_array_invalid_type1, TranslateError),
    (int64_array_invalid_type, TranslateError),
    (int64_array_invalid_type1, TranslateError),
    (uint32_array_invalid_type, TranslateError),
    (uint32_array_invalid_type1, TranslateError),
    (uint64_array_invalid_type, TranslateError),
    (uint64_array_invalid_type1, TranslateError),
    (invalid_return_type, TranslateError),
    (uint32_type_negative, OverflowError),
    (uint64_type_negative, OverflowError),
    (uint32_array_negative_values, OverflowError),
    (uint64_array_negative_values, OverflowError),
    (uint32_type_negative_run, OverflowError),
    (uint64_type_negative_run, OverflowError),
    (int32_max_value_overflow, OverflowError),
    (int64_max_value_overflow, OverflowError),
    (uint32_max_value_overflow, OverflowError),
    (uint64_max_value_overflow, OverflowError),
    (int32_array_overflow, OverflowError),
    (int64_array_overflow, OverflowError),
    (uint32_array_overflow, OverflowError),
    (uint64_array_overflow, OverflowError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params", transform_tests, ids=idfunc)
def test_transform(func_name, params):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])


def test_python_only_boolean():
    def return_true():
        return True

    def return_false():
        return False

    def return_one():
        return 1

    def return_string():
        return "string"

    # Boolean datatype creation from other boolean forms
    assert BooleanValue(True).value
    assert BooleanValue(return_true()).value
    assert BooleanValue(not return_false()).value
    assert BooleanValue(BooleanValue(True)).value
    assert BooleanValue(BooleanValue(True).value).value
    assert BooleanValue(BooleanValue(return_true())).value
    assert not BooleanValue(False).value
    assert not BooleanValue(return_false()).value
    assert not BooleanValue(not return_true()).value
    assert not BooleanValue(BooleanValue(False)).value
    assert not BooleanValue(BooleanValue(False).value).value
    assert not BooleanValue(BooleanValue(return_false())).value

    # Boolean datatype creation from numeric forms
    assert BooleanValue(1).value
    assert BooleanValue(return_one()).value
    assert BooleanValue(DoubleValue(1)).value
    assert BooleanValue(DoubleValue(1).value).value

    assert not BooleanValue(0).value
    assert not BooleanValue(DoubleValue(0).value).value
    assert not BooleanValue(DoubleValue(0)).value

    # Boolean datatype creation from expression
    assert BooleanValue(True and True).value
    assert not BooleanValue(False and True).value
    assert BooleanValue(5 < 10).value
    assert not BooleanValue(return_one() > 1).value

    # Boolean datatype creation from array
    assert BooleanValue(BooleanValueArray([True, False])[0]).value
    assert not BooleanValue(([True, False])[1]).value
    assert BooleanValue(BooleanValueArray([True, False])[0].value).value
    assert not BooleanValue(([True, False])[1]).value

    # Boolean datatype creation from strings
    assert BooleanValue("True").value
    assert not BooleanValue("False").value
    assert BooleanValue("true").value
    assert not BooleanValue("false").value

    # Boolean datatype creation that should fail
    with pytest.raises(TypeError):
        BooleanValue("string")
    with pytest.raises(TypeError):
        BooleanValue(object())
    with pytest.raises(TypeError):
        BooleanValue([])
    with pytest.raises(TypeError):
        BooleanValue(BooleanValueArray([True]))


def test_python_only_double():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3.14

    def return_string():
        return "string"

    # Double datatype creation from boolean forms
    assert DoubleValue(True).value == 1.0
    assert DoubleValue(return_true()).value == 1.0
    assert DoubleValue(not return_false()).value == 1.0
    assert DoubleValue(DoubleValue(True)).value == 1.0
    assert DoubleValue(DoubleValue(True).value).value == 1.0
    assert DoubleValue(DoubleValue(return_true())).value == 1.0
    assert DoubleValue(False).value == 0.0
    assert DoubleValue(return_false()).value == 0.0
    assert DoubleValue(not return_true()).value == 0.0
    assert DoubleValue(DoubleValue(False)).value == 0.0
    assert DoubleValue(DoubleValue(False).value).value == 0.0
    assert DoubleValue(DoubleValue(return_false())).value == 0.0

    # Double datatype creation from numeric forms
    assert DoubleValue(3.14).value == 3.14
    assert DoubleValue(return_non_zero()).value == return_non_zero()
    assert DoubleValue(DoubleValue(3.14)).value == 3.14
    assert DoubleValue(DoubleValue(3.14).value).value == 3.14

    # Double datatype creation from expression
    assert DoubleValue(2.04 + 1.1).value == 3.14
    assert DoubleValue(False and True).value == 0.0
    assert DoubleValue(5 < 10).value == 1.0
    assert DoubleValue(return_non_zero() > 1).value == 1.0

    # Double datatype creation from array
    assert DoubleValue(DoubleValueArray([1.0, 3.14])[0]).value == 1.0
    assert DoubleValue([1.0, 3.14][1]).value == 3.14

    # Double datatype creation that should fail
    with pytest.raises(TypeError):
        DoubleValue("3.14")
    with pytest.raises(TypeError):
        DoubleValue("string")
    with pytest.raises(TypeError):
        DoubleValue(object())
    with pytest.raises(TypeError):
        DoubleValue([])
    with pytest.raises(TypeError):
        DoubleValue(DoubleValueArray([True]))


def test_python_only_i32():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3

    def return_string():
        return "string"

    # I32 datatype creation from boolean forms
    assert I32Value(True).value == 1
    assert I32Value(return_true()).value == 1
    assert I32Value(not return_false()).value == 1
    assert I32Value(I32Value(True)).value == 1
    assert I32Value(I32Value(True).value).value == 1
    assert I32Value(I32Value(return_true())).value == 1
    assert I32Value(False).value == 0
    assert I32Value(return_false()).value == 0
    assert I32Value(not return_true()).value == 0
    assert I32Value(I32Value(False)).value == 0
    assert I32Value(I32Value(False).value).value == 0
    assert I32Value(I32Value(return_false())).value == 0

    # I32 datatype creation from numeric forms
    assert I32Value(3).value == 3
    assert I32Value(3.3).value == 3
    assert I32Value(DoubleValue(3.3)).value == 3
    assert I32Value(return_non_zero()).value == return_non_zero()
    assert I32Value(I32Value(3)).value == 3
    assert I32Value(I32Value(3).value).value == 3

    # I32 datatype creation from expression
    assert I32Value(2 + 1).value == 3
    assert I32Value(False and True).value == 0
    assert I32Value(5 < 10).value == 1
    assert I32Value(return_non_zero() > 1).value == 1

    # I32 datatype creation from array
    assert I32Value(I32ValueArray([1, 3])[0]).value == 1
    assert I32Value([1, 3][1]).value == 3

    # I32 datatype creation that should fail
    with pytest.raises(TypeError):
        I32Value("3")
    with pytest.raises(TypeError):
        I32Value("string")
    with pytest.raises(TypeError):
        I32Value(object())
    with pytest.raises(TypeError):
        I32Value([])
    with pytest.raises(TypeError):
        I32Value(I32ValueArray([True]))


def test_python_only_i64():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3

    def return_string():
        return "string"

    # I64 datatype creation from boolean forms
    assert I64Value(True).value == 1
    assert I64Value(return_true()).value == 1
    assert I64Value(not return_false()).value == 1
    assert I64Value(I64Value(True)).value == 1
    assert I64Value(I64Value(True).value).value == 1
    assert I64Value(I64Value(return_true())).value == 1
    assert I64Value(False).value == 0
    assert I64Value(return_false()).value == 0
    assert I64Value(not return_true()).value == 0
    assert I64Value(I64Value(False)).value == 0
    assert I64Value(I64Value(False).value).value == 0
    assert I64Value(I64Value(return_false())).value == 0

    # I64 datatype creation from numeric forms
    assert I64Value(3).value == 3
    assert I64Value(3.3).value == 3
    assert I64Value(DoubleValue(3.3)).value == 3
    assert I64Value(return_non_zero()).value == return_non_zero()
    assert I64Value(I64Value(3)).value == 3
    assert I64Value(I64Value(3).value).value == 3

    # I64 datatype creation from expression
    assert I64Value(2 + 1).value == 3
    assert I64Value(False and True).value == 0
    assert I64Value(5 < 10).value == 1
    assert I64Value(return_non_zero() > 1).value == 1

    # I64 datatype creation from array
    assert I64Value(I64ValueArray([1, 3])[0]).value == 1
    assert I64Value([1, 3][1]).value == 3

    # I64 datatype creation that should fail
    with pytest.raises(TypeError):
        I64Value("3")
    with pytest.raises(TypeError):
        I64Value("string")
    with pytest.raises(TypeError):
        I64Value(object())
    with pytest.raises(TypeError):
        I64Value([])
    with pytest.raises(TypeError):
        I64Value(I64ValueArray([1]))


def test_python_only_u32():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3

    def return_string():
        return "string"

    # U32 datatype creation from boolean forms
    assert U32Value(True).value == 1
    assert U32Value(return_true()).value == 1
    assert U32Value(not return_false()).value == 1
    assert U32Value(U32Value(True)).value == 1
    assert U32Value(U32Value(True).value).value == 1
    assert U32Value(U32Value(return_true())).value == 1
    assert U32Value(False).value == 0
    assert U32Value(return_false()).value == 0
    assert U32Value(not return_true()).value == 0
    assert U32Value(U32Value(False)).value == 0
    assert U32Value(U32Value(False).value).value == 0
    assert U32Value(U32Value(return_false())).value == 0

    # U32 datatype creation from numeric forms
    assert U32Value(3).value == 3
    assert U32Value(3.3).value == 3
    assert U32Value(DoubleValue(3.3)).value == 3
    assert U32Value(return_non_zero()).value == return_non_zero()
    assert U32Value(U32Value(3)).value == 3
    assert U32Value(U32Value(3).value).value == 3

    # U32 datatype creation from expression
    assert U32Value(2 + 1).value == 3
    assert U32Value(False and True).value == 0
    assert U32Value(5 < 10).value == 1
    assert U32Value(return_non_zero() > 1).value == 1

    # U32 datatype creation from array
    assert U32Value(U32ValueArray([1, 3])[0]).value == 1
    assert U32Value([1, 3][1]).value == 3

    # U32 datatype creation that should fail
    with pytest.raises(TypeError):
        U32Value("3")
    with pytest.raises(TypeError):
        U32Value("string")
    with pytest.raises(TypeError):
        U32Value(object())
    with pytest.raises(TypeError):
        U32Value([])
    with pytest.raises(TypeError):
        U32Value(U32ValueArray([1]))


def test_python_only_u64():
    def return_true():
        return True

    def return_false():
        return False

    def return_non_zero():
        return 3

    def return_string():
        return "string"

    # U64 datatype creation from boolean forms
    assert U64Value(True).value == 1
    assert U64Value(return_true()).value == 1
    assert U64Value(not return_false()).value == 1
    assert U64Value(U64Value(True)).value == 1
    assert U64Value(U64Value(True).value).value == 1
    assert U64Value(U64Value(return_true())).value == 1
    assert U64Value(False).value == 0
    assert U64Value(return_false()).value == 0
    assert U64Value(not return_true()).value == 0
    assert U64Value(U64Value(False)).value == 0
    assert U64Value(U64Value(False).value).value == 0
    assert U64Value(U64Value(return_false())).value == 0

    # U64 datatype creation from numeric forms
    assert U64Value(3).value == 3
    assert U64Value(3.3).value == 3
    assert U64Value(DoubleValue(3.3)).value == 3
    assert U64Value(return_non_zero()).value == return_non_zero()
    assert U64Value(U64Value(3)).value == 3
    assert U64Value(U64Value(3).value).value == 3

    # U64 datatype creation from expression
    assert U64Value(2 + 1).value == 3
    assert U64Value(False and True).value == 0
    assert U64Value(5 < 10).value == 1
    assert U64Value(return_non_zero() > 1).value == 1

    # U64 datatype creation from array
    assert U64Value(U64ValueArray([1, 3])[0]).value == 1
    assert U64Value([1, 3][1]).value == 3

    # U64 datatype creation that should fail
    with pytest.raises(TypeError):
        U64Value("3")
    with pytest.raises(TypeError):
        U64Value("string")
    with pytest.raises(TypeError):
        U64Value(object())
    with pytest.raises(TypeError):
        U64Value([])
    with pytest.raises(TypeError):
        U64Value(U64ValueArray([1]))
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_docstrings.py sha256=40370c2f593a52163c6f906ecd386bb1d26f77d8f34ae76dd0cfff6f3b7adcf8 bytes=2336 -->
## FILE: tests/test_docstrings.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_docstrings.py`
- sha256: `40370c2f593a52163c6f906ecd386bb1d26f77d8f34ae76dd0cfff6f3b7adcf8`
- bytes: 2336

````python
import sys
from niveristand import nivs_rt_sequence
from niveristand.clientapi import RealTimeSequence
from niveristand.library import multitask, task
import pytest
from testutilities import validation


@nivs_rt_sequence
def docstring_func_single_line():
    """Single-line doc."""
    pass


@nivs_rt_sequence
def docstring_func_parameters(arg1, arg2):
    """Test parameters docstring.

    :param arg1: first argument
    :param arg2: second argument
    """
    pass


@nivs_rt_sequence
def docstring_func_multi_line():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    pass


@nivs_rt_sequence
def docstring_func_in_code():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    pass
    """ More doc strings"""
    pass


@nivs_rt_sequence
def docstring_try():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    try:
        pass
    finally:
        pass


@nivs_rt_sequence
def docstring_multitask():
    """Test multitask docstring."""
    with multitask() as mt:

        @task(mt)
        def func1():
            """Test task docstring in func1."""
            pass

        @task(mt)
        def func2():
            """Test task docstring in func2.

            Multi-line comment here.
            """
            pass

    pass


@nivs_rt_sequence
def docstring_try_inside():
    """Begin doc.

    This is more doc
    that is in multiple strings.
    """
    try:
        """More docs"""
        pass
    finally:
        pass


transform_tests = [
    (docstring_func_in_code, (), None),
    (docstring_func_multi_line, (), None),
    (docstring_func_parameters, (), None),
    (docstring_func_single_line, (), None),
    (docstring_multitask, (), None),
    (docstring_try, (), None),
    (docstring_try_inside, (), None),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", transform_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_for_loop.py sha256=f46de0171d7f70d927d4f341393e4fe1084d7cdf47f3c9b8f106dea3c008bef5 bytes=6788 -->
## FILE: tests/test_for_loop.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_for_loop.py`
- sha256: `f46de0171d7f70d927d4f341393e4fe1084d7cdf47f3c9b8f106dea3c008bef5`
- bytes: 6788

````python
import sys
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, DoubleValueArray, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import arraysize, localhost_wait
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def _return_constant():
    return 10


@nivs_rt_sequence
def _increment_param_by_ref(param):
    param.value = param.value + 1


@nivs_rt_sequence
def for_loop_variable_array():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b:
        a.value += x.value
    return a.value


@nivs_rt_sequence
def for_loop_variable_array1():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b.value:
        a.value += x.value
    return a.value


@nivs_rt_sequence
def for_loop_modify_collection():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    for x in a.value:
        x.value += 1
    return a[0].value


@nivs_rt_sequence
def for_loop_modify_elements():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    for x in a.value:
        _increment_param_by_ref(x)
    return a[0].value


@nivs_rt_sequence
def for_loop_constant_array():
    a = DoubleValue(0)
    for x in [1, 2, 3, 4, 5]:
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range():
    a = DoubleValue(0)
    for x in range(10):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range_with_start():
    a = DoubleValue(0)
    for x in range(2, 10):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range_with_step():
    a = DoubleValue(0)
    for x in range(2, 10, 2):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range_with_variable():
    a = DoubleValue(0)
    b = I32Value(10)
    for x in range(b.value):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_range_with_channel_ref():
    a = DoubleValue(0)
    b = ChannelReference("Aliases/DesiredRPM")
    b.value = 10.0
    localhost_wait(0.2)
    for x in range(b.value):
        a.value += x
    return a


@nivs_rt_sequence
def for_loop_range_with_call():
    a = DoubleValue(0)
    for x in range(_return_constant()):
        a.value += x
    return a.value


@nivs_rt_sequence
def for_loop_iterate_on_array():
    a = DoubleValueArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    for i in range(10):
        a[0].value += a[i].value
    return a[0].value


@nivs_rt_sequence
def for_loop_else():
    a = DoubleValue(0)
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for x in b.value:
        a.value += x
    else:
        a.value = -1
    return a.value


@nivs_rt_sequence
def nested_for_loop():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for i in range(5):
        for j in b.value:
            a[i].value += j.value
    return a[3].value


@nivs_rt_sequence
def nested_for_loop_body():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    b = DoubleValueArray([1, 2, 3, 4, 5])
    for i in range(5):
        for j in b.value:
            if j.value % 2 == 0:
                a[i].value += j.value
            else:
                a[i].value -= j.value
    return a[3].value


@nivs_rt_sequence
def looping_over_invalid_var():
    a = DoubleValue(0)
    for x in a.value:
        a.value += x
    return a.value


@nivs_rt_sequence
def for_return_in_body():
    for i in range(5):
        return i


@nivs_rt_sequence
def for_try_in_body():
    for i in range(5):
        try:
            pass
        finally:
            pass


@nivs_rt_sequence
def for_funcdef_in_body():
    for i in range(5):

        def func():
            pass

        pass


@nivs_rt_sequence
@NivsParam("array", DoubleValueArray([0]), NivsParam.BY_REF)
def _average(array):
    average_var = DoubleValue(0)
    for x in array:
        average_var.value += x.value
    average_var.value /= arraysize(array.value)
    return average_var.value


@nivs_rt_sequence
def call_average():
    a = DoubleValueArray([1, 2, 3, 4, 5])
    res = DoubleValue(0)
    res.value = _average(a)
    return res.value


run_tests = [
    (for_loop_variable_array, (), 15),
    (for_loop_variable_array1, (), 15),
    (for_loop_modify_collection, (), 2),
    (for_loop_modify_elements, (), 2),
    (for_loop_range, (), 45),
    (for_loop_range_with_variable, (), 45),
    (for_loop_range_with_call, (), 45),
    (for_loop_iterate_on_array, (), 45),
    (nested_for_loop, (), 19),
    (nested_for_loop_body, (), 1),
    (call_average, (), 3),
]

fail_transform_tests = [
    (for_loop_else, (), TranslateError),
    (for_loop_range_with_start, (), TranslateError),
    (for_loop_range_with_step, (), TranslateError),
    (looping_over_invalid_var, (), TranslateError),
    (for_return_in_body, (), TranslateError),
    (for_try_in_body, (), TranslateError),
    (for_funcdef_in_body, (), TranslateError),
    (for_loop_range_with_channel_ref, (), VeristandError),
    (for_loop_constant_array, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_generate_error.py sha256=36a7c6167b18eb3fc610305ec05355f2049b13c2fb065eeb7e93f67c019c8980 bytes=9065 -->
## FILE: tests/test_generate_error.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_generate_error.py`
- sha256: `36a7c6167b18eb3fc610305ec05355f2049b13c2fb065eeb7e93f67c019c8980`
- bytes: 9065

````python
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, I32Value
from niveristand.clientapi import ErrorAction, RealTimeSequence
from niveristand.errors import (
    RunAbortedError,
    RunError,
    RunFailedError,
    SequenceError,
    TranslateError,
)
from niveristand.library import multitask, nivs_yield, task
from niveristand.library.primitives import generate_error
import pytest
from testutilities import rtseqrunner, validation

_stop_err = SequenceError(-100, "Stop", ErrorAction.StopSequence)
_abort_err = SequenceError(-200, "Abort", ErrorAction.AbortSequence)
_cont_err = SequenceError(1, "Continue", ErrorAction.ContinueSequenceExecution)
_cont_err_no_fail = SequenceError(0, "Continue", ErrorAction.ContinueSequenceExecution)


@nivs_rt_sequence
def _gen_stop():
    generate_error(-100, "Stop", ErrorAction.StopSequence)


@nivs_rt_sequence
def _gen_abort():
    generate_error(-200, "Abort", ErrorAction.AbortSequence)


@nivs_rt_sequence
def _gen_continue():
    generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)


@nivs_rt_sequence
def generate_error_simple():
    generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)


@nivs_rt_sequence
def generate_continue():
    try:
        a = DoubleValue(0)
        generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def _generate_continue_no_fail():
    try:
        a = DoubleValue(0)
        generate_error(0, "Continue", ErrorAction.ContinueSequenceExecution)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_stop():
    try:
        a = DoubleValue(0)
        generate_error(-100, "Stop", ErrorAction.StopSequence)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_abort():
    try:
        a = DoubleValue(0)
        generate_error(-200, "Abort", ErrorAction.AbortSequence)
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_continue_mt():
    a = DoubleValue(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)

        @task(mt)
        def f2():
            nivs_yield()
            a.value = 1

    return a.value


@nivs_rt_sequence
def generate_stop_mt():
    a = DoubleValue(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            generate_error(-100, "Stop", ErrorAction.StopSequence)

        @task(mt)
        def f2():
            nivs_yield()
            a.value = 1

    return a.value


@nivs_rt_sequence
def generate_abort_mt():
    a = DoubleValue(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            generate_error(-200, "Abort", ErrorAction.AbortSequence)

        @task(mt)
        def f2():
            nivs_yield()
            a.value = 1

    return a.value


@nivs_rt_sequence
def generate_continue_subroutine():
    a = DoubleValue(1)
    _gen_continue()
    a.value = 5
    return a.value


@nivs_rt_sequence
def generate_continue_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_continue()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_stop_subroutine():
    a = DoubleValue(1)
    _gen_stop()
    a.value = 5
    return a.value


@nivs_rt_sequence
def generate_stop_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_stop()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def generate_abort_subroutine():
    a = DoubleValue(1)
    _gen_abort()
    a.value = 5
    return a.value


@nivs_rt_sequence
def generate_abort_subroutine1():
    try:
        a = DoubleValue(0)
        _gen_abort()
        a.value += 1
    finally:
        a.value += 1
    return a.value


@nivs_rt_sequence
def invalid_error_code():
    a = I32Value(-1)
    generate_error(a.value, "Message", ErrorAction.AbortSequence)


@nivs_rt_sequence
def invalid_error_message():
    generate_error(-1, 22, ErrorAction.AbortSequence)


@nivs_rt_sequence
def invalid_error_action():
    generate_error(1, "Message", 1)


@nivs_rt_sequence
def generate_multiple_errors():
    _gen_continue()
    _gen_continue()
    _gen_continue()
    _gen_stop()


@nivs_rt_sequence
def generate_multiple_errors1():
    try:
        _gen_continue()
        _gen_stop()
        _gen_continue()
    finally:
        _gen_continue()


@nivs_rt_sequence
def generate_multiple_errors2():
    _gen_continue()
    _gen_abort()
    _gen_continue()
    _gen_continue()


run_tests = [
    (generate_error_simple, (), (None, (_cont_err,))),
    (generate_continue, (), (2, (_cont_err,))),
    (generate_stop, (), (1, (_stop_err,))),
    (generate_abort, (), (0, (_abort_err,))),
    (generate_continue_mt, (), (1, (_cont_err,))),
    (generate_stop_mt, (), (0, (_stop_err,))),
    (generate_abort_mt, (), (0, (_abort_err,))),
    (generate_continue_subroutine, (), (5, (_cont_err,))),
    (generate_continue_subroutine1, (), (2, (_cont_err,))),
    (generate_stop_subroutine, (), (1, (_stop_err,))),
    (generate_stop_subroutine1, (), (1, (_stop_err,))),
    (generate_abort_subroutine, (), (1, (_abort_err,))),
    (generate_abort_subroutine1, (), (0, (_abort_err,))),
    (generate_multiple_errors, (), (None, (_stop_err, _cont_err, _cont_err, _cont_err))),
    (generate_multiple_errors1, (), (None, (_cont_err, _stop_err, _cont_err))),
    (generate_multiple_errors2, (), (None, (_abort_err, _cont_err))),
]

fail_transform_tests = [
    (invalid_error_code, (), TranslateError),
    (invalid_error_message, (), TranslateError),
    (invalid_error_action, (), TranslateError),
]

run_as_rts_tests = [
    (generate_error_simple, (), RunFailedError),
    (generate_continue, (), RunFailedError),
    (generate_stop, (), RunAbortedError),
    (generate_abort, (), RunAbortedError),
    (generate_continue_mt, (), RunFailedError),
    (generate_stop_mt, (), RunAbortedError),
    (generate_abort_mt, (), RunAbortedError),
    (generate_continue_subroutine, (), RunFailedError),
    (generate_continue_subroutine1, (), RunFailedError),
    (generate_stop_subroutine, (), RunAbortedError),
    (generate_stop_subroutine1, (), RunAbortedError),
    (generate_abort_subroutine, (), RunAbortedError),
    (generate_abort_subroutine1, (), RunAbortedError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


def test_gen_continue_no_fail():
    assert _generate_continue_no_fail() == 2
    assert rtseqrunner.run_rtseq_in_VM(_generate_continue_no_fail) == 2
    assert realtimesequencetools.run_py_as_rtseq(_generate_continue_no_fail) == 2


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    expected_value, expected_errors = expected_result
    with pytest.raises(RunError) as e:
        func_name(*params)
    if e.value.error.error_action in (ErrorAction.AbortSequence, ErrorAction.StopSequence):
        assert isinstance(e.value, RunAbortedError)
    else:
        assert isinstance(e.value, RunFailedError)
    all_errors = list(e.value.get_all_errors())
    for error, expected_error in zip(all_errors, expected_errors):
        assert error.error_code == expected_error.error_code
        assert error.error_action == expected_error.error_action
        assert error.message == expected_error.message


@pytest.mark.parametrize("func_name, params, expected_result", run_as_rts_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    with pytest.raises(expected_result):
        realtimesequencetools.run_py_as_rtseq(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result[0]


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_ifexpression.py sha256=93793ab3d2993c13cd3fa31105e2603575903d4e83ebf399c5f754cee07ecdcc bytes=5834 -->
## FILE: tests/test_ifexpression.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_ifexpression.py`
- sha256: `93793ab3d2993c13cd3fa31105e2603575903d4e83ebf399c5f754cee07ecdcc`
- bytes: 5834

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def _returns_true():
    a = BooleanValue(True)
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_bool_assign():
    a = BooleanValue(False)
    a.value = True if True else False
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_int_assign():
    a = I32Value(0)
    a.value = 1 if True else 0
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_int_assign1():
    a = I32Value(0)
    a.value = 0 if not True else 1
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_nivstype_assign():
    a = I32Value(0)
    b = I32Value(1)
    c = I32Value(0)
    a.value = b.value if True else c.value
    return a.value


@nivs_rt_sequence
def ifexp_nivsbool_test_nivstype_assign():
    a = I32Value(0)
    b = I32Value(1)
    c = I32Value(2)
    a.value = b.value if BooleanValue(False) else c.value
    return a.value


@nivs_rt_sequence
def ifexp_nivsbool_test_nivstype_assign1():
    a = I32Value(0)
    b = I32Value(1)
    c = I32Value(0)
    a.value = b.value if not BooleanValue(False) else c.value
    return a.value


@nivs_rt_sequence
def ifexp_nivsboolvar_test_int_assign():
    a = I32Value(0)
    b = BooleanValue(True)
    c = I32Value(1)
    d = I32Value(0)
    a.value = c.value if b.value else d.value
    return a.value


@nivs_rt_sequence
def ifexp_nivsboolvar_test_int_assign1():
    a = I32Value(0)
    b = BooleanValue(False)
    c = I32Value(1)
    d = I32Value(0)
    a.value = c.value if not b.value else d.value
    return a.value


@nivs_rt_sequence
def ifexp_expression_test_int_assign():
    a = I32Value(5)
    a.value = 1 if a <= 5 else 0
    return a.value


@nivs_rt_sequence
def ifexp_expression_test_int_assign1():
    a = I32Value(5)
    a.value = 1 if (a < 5) or True else 0
    return a.value


@nivs_rt_sequence
def ifexp_nested_ifexp():
    a = I32Value(5)
    a.value = 2 if (a < 5) else 1 if a <= 5 else 0
    return a.value


@nivs_rt_sequence
def ifexp_rtseq_test():
    a = I32Value(0)
    a.value = 1 if _returns_true() else 0
    return a.value


@nivs_rt_sequence
def ifexp_rtseq_test_rtseq_assign():
    a = BooleanValue(False)
    a.value = _returns_true() if _returns_true() else False
    return a.value


@nivs_rt_sequence
def ifexp_rtseq_test_rtseq_assign1():
    a = BooleanValue(False)
    a.value = _returns_true() if not _returns_true() else _returns_true()
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_expression_assign():
    a = I32Value(0)
    a.value = (1 * 2) - 1 & 7 | a if True else 0
    return a.value


@nivs_rt_sequence
def ifexp_bool_test_expression_assign1():
    a = I32Value(0)
    a.value = 0 if not True else (1 * 2) - 1 & 7 | a
    return a.value


@nivs_rt_sequence
def aug_ifexp_bool_test_expression_assign():
    a = I32Value(0)
    a.value += 0 if not True else (1 * 2) - 1 & 7 | a
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def ifexp_invalid_int_test():
    a = I32Value(0)
    a = I32Value(1) if 1 else I32Value(0)
    return a.value


# </editor-fold>


run_tests = [
    (ifexp_bool_test_bool_assign, (), True),
    (ifexp_bool_test_int_assign, (), 1),
    (ifexp_bool_test_int_assign1, (), 1),
    (ifexp_bool_test_nivstype_assign, (), 1),
    (ifexp_nivsboolvar_test_int_assign, (), 1),
    (ifexp_nivsboolvar_test_int_assign1, (), 1),
    (ifexp_expression_test_int_assign, (), 1),
    (ifexp_expression_test_int_assign1, (), 1),
    (ifexp_nested_ifexp, (), 1),
    (ifexp_bool_test_expression_assign, (), 1),
    (ifexp_bool_test_expression_assign1, (), 1),
    (aug_ifexp_bool_test_expression_assign, (), 1),
    (ifexp_rtseq_test, (), 1),
    (ifexp_rtseq_test_rtseq_assign, (), True),
    (ifexp_rtseq_test_rtseq_assign1, (), True),
]

fail_transform_tests = [
    (ifexp_invalid_int_test, (), VeristandError),
    (ifexp_nivsbool_test_nivstype_assign, (), TranslateError),
    (ifexp_nivsbool_test_nivstype_assign1, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_logical_and.py sha256=76b7efed8c76fcb97d7f8d535b97b94296c5b247e1232c42460ebb6eae2278fc bytes=5480 -->
## FILE: tests/test_logical_and.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_logical_and.py`
- sha256: `76b7efed8c76fcb97d7f8d535b97b94296c5b247e1232c42460ebb6eae2278fc`
- bytes: 5480

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_true():
    a = BooleanValue(True)
    return a.value


@nivs_rt_sequence
def logical_and_simple_numbers():
    a = DoubleValue(0)
    a.value = 2 and 1
    return a.value


@nivs_rt_sequence
def logical_and_simple_numbers1():
    a = BooleanValue(0)
    a.value = 1 and 2
    return a.value


@nivs_rt_sequence
def logical_and_nivsdatatype_double():
    a = BooleanValue(0)
    a = DoubleValue(3) and DoubleValue(1)
    return a.value


@nivs_rt_sequence
def logical_and_nivsdatatype_int32():
    a = BooleanValue(0)
    a = I32Value(2) and I32Value(1)
    return a.value


@nivs_rt_sequence
def logical_and_nivsdatatype_int64():
    a = BooleanValue(0)
    a = I64Value(2) and I64Value(1)
    return a.value


@nivs_rt_sequence
def logical_and_nivsdatatype_bool():
    a = BooleanValue(True)
    a.value = True and False
    return a.value


@nivs_rt_sequence
def logical_and_multiple_types():
    a = BooleanValue(False)
    a.value = True and I32Value(2) and DoubleValue(3) and True
    return a.value


@nivs_rt_sequence
def logical_and_multiple_types1():
    a = BooleanValue(True)
    a.value = True and BooleanValue(True) and False
    return a.value


@nivs_rt_sequence
def logical_and_variables_redefined():
    a = BooleanValue(True)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a = b and c
    return a.value


@nivs_rt_sequence
def logical_and_variables1():
    a = BooleanValue(True)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a.value = b.value and c.value
    return a.value


@nivs_rt_sequence
def logical_and_rtseq():
    a = BooleanValue(False)
    a.value = _return_true() and True
    return a.value


@nivs_rt_sequence
def logical_and_rtseq1():
    a = BooleanValue(False)
    a.value = True and _return_true()
    return a.value


@nivs_rt_sequence
def logical_and_parentheses():
    a = BooleanValue(True)
    a.value = True and (BooleanValue(True) and BooleanValue(True)) and False
    return a.value


@nivs_rt_sequence
def logical_and_unary():
    a = BooleanValue(True)
    a.value = -2 and 1
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def logical_and_invalid_variables():
    return a.value and b


@nivs_rt_sequence
def logical_and_invalid_variables1():
    return a.value and b.value


@nivs_rt_sequence
def logical_and_None():
    a = BooleanValue(True)
    a.value = True and None
    return a.value


@nivs_rt_sequence
def logical_and_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = True and _return_true
    return a.value


# </editor-fold>


run_tests = [
    (logical_and_nivsdatatype_bool, (), False),
    (logical_and_variables1, (), False),
    (logical_and_parentheses, (), False),
    (logical_and_rtseq, (), True),
    (logical_and_rtseq1, (), True),
    (logical_and_multiple_types1, (), False),
]

fail_transform_tests = [
    (logical_and_invalid_variables, (), TranslateError),
    (logical_and_invalid_variables1, (), TranslateError),
    (logical_and_None, (), TranslateError),
    (logical_and_invalid_rtseq_call, (), VeristandError),
    (logical_and_simple_numbers, (), TranslateError),
    (logical_and_simple_numbers1, (), TranslateError),
    (logical_and_nivsdatatype_double, (), TranslateError),
    (logical_and_nivsdatatype_int32, (), TranslateError),
    (logical_and_nivsdatatype_int64, (), TranslateError),
    (logical_and_unary, (), TranslateError),
    (logical_and_multiple_types, (), TranslateError),
    (logical_and_variables_redefined, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_logical_not.py sha256=7f3eafbb00c21e1ede3e0c3fc2902e5be7908edd586ae4417db2198d69356d63 bytes=4942 -->
## FILE: tests/test_logical_not.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_logical_not.py`
- sha256: `7f3eafbb00c21e1ede3e0c3fc2902e5be7908edd586ae4417db2198d69356d63`
- bytes: 4942

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_true():
    a = BooleanValue(True)
    return a.value


@nivs_rt_sequence
def logical_not_simple_numbers():
    a = BooleanValue(0)
    a.value = not 2
    return a.value


@nivs_rt_sequence
def logical_not_simple_numbers1():
    a = BooleanValue(0)
    a.value = not 0
    return a.value


@nivs_rt_sequence
def logical_not_nivsdatatype_double():
    a = BooleanValue(0)
    a.value = not DoubleValue(3)
    return a.value


@nivs_rt_sequence
def logical_not_nivsdatatype_double1():
    a = BooleanValue(0)
    a.value = not DoubleValue(0)
    return a.value


@nivs_rt_sequence
def logical_not_nivsdatatype_int32():
    a = BooleanValue(0)
    a.value = not I32Value(0)
    return a.value


@nivs_rt_sequence
def logical_not_nivsdatatype_int64():
    a = BooleanValue(0)
    a.value = not I64Value(0)
    return a.value


@nivs_rt_sequence
def logical_not_bool():
    a = BooleanValue(True)
    a.value = not True
    return a.value


@nivs_rt_sequence
def logical_not_bool1():
    a = BooleanValue(False)
    a.value = not False
    return a.value


@nivs_rt_sequence
def logical_not_variables():
    a = BooleanValue(False)
    b = BooleanValue(False)
    a.value = not b.value
    return a.value


@nivs_rt_sequence
def logical_not_rtseq():
    a = BooleanValue(True)
    a.value = not _return_true()
    return a.value


@nivs_rt_sequence
def logical_not_parentheses():
    a = BooleanValue(True)
    a.value = not (True and (BooleanValue(True) and BooleanValue(True)) and False)
    return a.value


@nivs_rt_sequence
def logical_not_unary():
    a = BooleanValue(True)
    a.value = not -1
    return a.value


@nivs_rt_sequence
def logical_not_sequence():
    a = BooleanValue(False)
    a.value = not not not False
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def logical_not_invalid_variables():
    return not a.value


@nivs_rt_sequence
def logical_not_None():
    a = BooleanValue(False)
    a.value = not None
    return a.value


@nivs_rt_sequence
def logical_not_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = not _return_true
    return a.value


# </editor-fold>


run_tests = [
    (logical_not_bool, (), False),
    (logical_not_bool1, (), True),
    (logical_not_variables, (), True),
    (logical_not_parentheses, (), True),
    (logical_not_sequence, (), True),
    (logical_not_sequence, (), True),
    (logical_not_rtseq, (), False),
]

fail_transform_tests = [
    (logical_not_invalid_variables, (), TranslateError),
    (logical_not_None, (), TranslateError),
    (logical_not_invalid_rtseq_call, (), VeristandError),
    (logical_not_simple_numbers, (), TranslateError),
    (logical_not_simple_numbers1, (), TranslateError),
    (logical_not_nivsdatatype_double, (), TranslateError),
    (logical_not_nivsdatatype_double1, (), TranslateError),
    (logical_not_nivsdatatype_int32, (), TranslateError),
    (logical_not_nivsdatatype_int64, (), TranslateError),
    (logical_not_unary, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_logical_or.py sha256=a311e3de0bb72ceec95c82ec4efe476f9bd2844ca1be2608dea37317662c1f5e bytes=5241 -->
## FILE: tests/test_logical_or.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_logical_or.py`
- sha256: `a311e3de0bb72ceec95c82ec4efe476f9bd2844ca1be2608dea37317662c1f5e`
- bytes: 5241

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_true():
    a = BooleanValue(True)
    return a.value


@nivs_rt_sequence
def logical_or_simple_numbers():
    a = DoubleValue(0)
    a.value = 1 or 2
    return a.value


@nivs_rt_sequence
def logical_or_nivsdatatype_double():
    a = BooleanValue(0)
    a = DoubleValue(3) or DoubleValue(0)
    return a.value


@nivs_rt_sequence
def logical_or_nivsdatatype_int32():
    a = BooleanValue(0)
    a = I32Value(2) or I32Value(0)
    return a.value


@nivs_rt_sequence
def logical_or_nivsdatatype_int64():
    a = BooleanValue(0)
    a = I64Value(2) or I64Value(0)
    return a.value


@nivs_rt_sequence
def logical_or_nivsdatatype_bool():
    a = BooleanValue(True)
    a.value = True or False
    return a.value


@nivs_rt_sequence
def logical_or_multiple_types():
    a = BooleanValue(False)
    a.value = True or I32Value(2) or DoubleValue(3) or True
    return a.value


@nivs_rt_sequence
def logical_or_multiple_types1():
    a = BooleanValue(False)
    a.value = True or BooleanValue(False) or False
    return a.value


@nivs_rt_sequence
def logical_or_variables_redefined():
    a = BooleanValue(False)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a = b or c
    return a.value


@nivs_rt_sequence
def logical_or_variables1():
    a = BooleanValue(True)
    b = BooleanValue(True)
    c = BooleanValue(False)
    a.value = b.value or c.value
    return a.value


@nivs_rt_sequence
def logical_or_rtseq():
    a = BooleanValue(False)
    a.value = _return_true() or True
    return a.value


@nivs_rt_sequence
def logical_or_rtseq1():
    a = BooleanValue(False)
    a.value = True or _return_true()
    return a.value


@nivs_rt_sequence
def logical_or_parentheses():
    a = BooleanValue(True)
    a.value = True or (BooleanValue(False) or BooleanValue(True)) or False
    return a.value


@nivs_rt_sequence
def logical_or_unary():
    a = BooleanValue(True)
    a.value = 1 or -2
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def logical_or_invalid_variables():
    return a.value or b


@nivs_rt_sequence
def logical_or_invalid_variables1():
    return a.value or b.value


@nivs_rt_sequence
def logical_or_None():
    a = BooleanValue(True)
    a.value = True or None
    return a.value


@nivs_rt_sequence
def logical_or_invalid_rtseq_call():
    a = BooleanValue(False)
    a.value = True or _return_true
    return a.value


# </editor-fold>


run_tests = [
    (logical_or_nivsdatatype_bool, (), True),
    (logical_or_multiple_types1, (), True),
    (logical_or_variables1, (), True),
    (logical_or_parentheses, (), True),
    (logical_or_rtseq, (), True),
    (logical_or_rtseq1, (), True),
]

fail_transform_tests = [
    (logical_or_simple_numbers, (), TranslateError),
    (logical_or_multiple_types, (), TranslateError),
    (logical_or_invalid_variables, (), TranslateError),
    (logical_or_invalid_variables1, (), TranslateError),
    (logical_or_None, (), TranslateError),
    (logical_or_invalid_rtseq_call, (), VeristandError),
    (logical_or_unary, (), TranslateError),
    (logical_or_nivsdatatype_double, (), TranslateError),
    (logical_or_nivsdatatype_int32, (), TranslateError),
    (logical_or_nivsdatatype_int64, (), TranslateError),
    (logical_or_variables_redefined, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_multitask.py sha256=22309671029bfbf6fd9ffcbecaedcd8a3bf40af96ed0ebb1d21b1187ec18f02f bytes=13277 -->
## FILE: tests/test_multitask.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_multitask.py`
- sha256: `22309671029bfbf6fd9ffcbecaedcd8a3bf40af96ed0ebb1d21b1187ec18f02f`
- bytes: 13277

````python
import sys
import threading
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library import multitask, nivs_yield, task
from niveristand.library._tasks import get_scheduler
import pytest
from testutilities import rtseqrunner, validation


@NivsParam("param", I32Value(0), NivsParam.BY_REF)
@nivs_rt_sequence
def _increase_param_by_ref(param):
    param.value += 1


@NivsParam("param", I32Value(0), NivsParam.BY_REF)
@nivs_rt_sequence
def _subseq_with_multitask(param):
    with multitask() as mt:

        @task(mt)
        def fa():
            nivs_yield()
            if param.value == 2:
                param.value = 3

        @task(mt)
        def fb():
            if param.value == 0:
                param.value = 1


@nivs_rt_sequence
def multitask_pass():
    a = I32Value(1)
    with multitask() as mt:

        @task(mt)
        def f1():
            pass

        @task(mt)
        def f2():
            pass

    return a.value


@nivs_rt_sequence
def multitask_access_local():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            a.value = 5

        @task(mt)
        def f2():
            a.value *= 7

    return a.value


@nivs_rt_sequence
def multitask_blocks_until_done():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            nivs_yield()
            a.value = 1

        @task(mt)
        def f2():
            a.value = 2
            nivs_yield()

    if a.value != 1:
        a.value = -1
    return a.value


@nivs_rt_sequence
def multitask_nested():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            with multitask() as mt_inside:

                @task(mt_inside)
                def fa():
                    a.value = 5

                @task(mt_inside)
                def fb():
                    a.value *= 7

        @task(mt)
        def f2():
            a.value *= 13

    return a.value


@nivs_rt_sequence
def multitask_task_with_yield():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            nivs_yield()
            a.value = 1

        @task(mt)
        def f2():
            a.value = 2
            nivs_yield()

    return a.value


@nivs_rt_sequence
def multitask_tasks_with_different_iter_count():
    a = I32Value(0)
    ret = I32Value(1)
    with multitask() as mt:

        @task(mt)
        def f1():
            while a.value < 15:
                a.value += 1
                if a.value % 2 != 1 and a.value < 10:
                    ret.value = a.value * -1
                nivs_yield()

        @task(mt)
        def f2():
            while a.value < 10:
                a.value += 1
                if a.value % 2 != 0:
                    ret.value = a.value * -1
                if a.value > 10:
                    ret.value -= 100
                nivs_yield()

    ret.value *= a.value
    return ret.value


@nivs_rt_sequence
def multitask_nested_validate_order():
    a = I32Value(0)
    counter = I32Value(1000)
    ret = I32Value(0)
    with multitask() as mt_top:

        @task(mt_top)
        def fa():
            with multitask() as mt_nested:

                @task(mt_nested)
                def f0():
                    with multitask() as mt_bottom:

                        @task(mt_bottom)
                        def fx():
                            if a.value != 0:
                                ret.value = -1000
                            while counter.value > 0:
                                counter.value -= 1
                                nivs_yield()

                @task(mt_nested)
                def f1():
                    if a.value > 3 and ret.value == 0:
                        ret.value = -1
                    a.value += 1
                    nivs_yield()
                    if a.value > 303 and ret.value == 0:
                        ret.value = -100
                    a.value += 100
                    nivs_yield()

                @task(mt_nested)
                def f2():
                    if a.value > 3 and ret.value == 0:
                        ret.value = -2
                    a.value += 1
                    nivs_yield()
                    if a.value > 303 and ret.value == 0:
                        ret.value = -200
                    a.value += 100
                    nivs_yield()

        @task(mt_top)
        def fb():
            if a.value > 3 and ret.value == 0:
                ret.value = -3
            a.value += 1
            nivs_yield()
            if a.value > 303 and ret.value == 0:
                ret.value = -300
            a.value += 100
            nivs_yield()

        @task(mt_top)
        def fc():
            while counter.value > 0:
                counter.value -= 1
                nivs_yield()

    if counter.value != 0:
        ret.value -= 10000
    return ret.value


@nivs_rt_sequence
def multitask_multiple_in_sequence_validate_order():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            nivs_yield()
            if a.value == 1:
                a.value = 2

        @task(mt)
        def f2():
            if a.value == 0:
                a.value = 1
            nivs_yield()

    with multitask() as mt2:

        @task(mt2)
        def fa():
            nivs_yield()
            if a.value == 3:
                a.value = 4

        @task(mt2)
        def fb():
            if a.value == 2:
                a.value = 3
            nivs_yield()

    return a.value


@nivs_rt_sequence
def multitask_call_subroutine_params_by_ref():
    a = I32Value(0)
    b = I32Value(1)
    with multitask() as mt:

        @task(mt)
        def f1():
            _increase_param_by_ref(a)

        @task(mt)
        def f2():
            _increase_param_by_ref(b)

        @task(mt)
        def f3():
            a.value += b.value

    return a.value


@nivs_rt_sequence
def multitask_call_subroutine_with_multitask():
    a = I32Value(0)

    with multitask() as mt:

        @task(mt)
        def f1():
            _subseq_with_multitask(a)
            nivs_yield()
            if a.value == 3:
                a.value = 4

        @task(mt)
        def f2():
            if a.value == 1:
                a.value = 2
            nivs_yield()
            nivs_yield()
            nivs_yield()
            if a.value == 4:
                a.value = 5

    return a.value


@nivs_rt_sequence
def multitask_duplicate_name_fails():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            a.value = 1

        @task(mt)  # noqa: F811 redefinition is exactly what we're testing here.
        def f1():  # noqa: F811 redefinition is exactly what we're testing here.
            a.value = 2

    return a.value


@nivs_rt_sequence
def multitask_redefine_var_fails():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            a = I32Value(1)
            a.value = 2

    return a.value


@nivs_rt_sequence
def multitask_return_fails():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            a = I32Value(1)
            a.value = 2

        return a.value


@nivs_rt_sequence
def multitask_stmt_fails():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            a = I32Value(1)
            a.value = 2

        return a.value


@nivs_rt_sequence
def multitask_with_param_fails():
    a = I32Value(1)
    with multitask(a) as mt:

        @task(mt)
        def f1():
            pass

        @task(mt)
        def f2():
            pass

    return a.value


@nivs_rt_sequence
def multitask_task_with_param_fails():
    a = I32Value(1)
    with multitask(a) as mt:

        @task(mt)
        def f1(x):
            pass

        @task(mt)
        def f2():
            pass

    return a.value


@nivs_rt_sequence
def multitask_return_in_task_fails():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            a = I32Value(1)
            return a.value

    return a.value


@nivs_rt_sequence
def multitask_funcdef_in_task_fails():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            def func():
                pass

    return a.value


@nivs_rt_sequence
def multitask_no_var_name_fails():
    a = I32Value(0)
    with multitask():

        @task()
        def f1():
            pass

    return a.value


@nivs_rt_sequence
def multitask_wrong_var_name_fails():
    a = I32Value(0)
    with multitask():

        @task(a)
        def f1():
            pass

    return a.value


@nivs_rt_sequence
def multitask_task_multi_dec_fails():
    a = I32Value(0)
    with multitask() as mt:

        @task(mt)
        @task(mt)
        def f1():
            pass

    return a.value


run_tests = [
    (multitask_pass, (), 1),
    (multitask_nested, (), 455),
    (multitask_access_local, (), 35),
    (multitask_blocks_until_done, (), 1),
    (multitask_task_with_yield, (), 1),
    (multitask_call_subroutine_params_by_ref, (), 3),
    (multitask_tasks_with_different_iter_count, (), 15),
    (multitask_nested_validate_order, (), 0),
    (multitask_multiple_in_sequence_validate_order, (), 4),
    (multitask_call_subroutine_with_multitask, (), 5),
]

fail_transform_tests = [
    (multitask_duplicate_name_fails, (), VeristandError),
    (multitask_return_fails, (), TranslateError),
    (multitask_stmt_fails, (), TranslateError),
    (multitask_with_param_fails, (), TranslateError),
    (multitask_task_with_param_fails, (), TranslateError),
    (multitask_return_in_task_fails, (), TranslateError),
    (multitask_funcdef_in_task_fails, (), TranslateError),
    (multitask_no_var_name_fails, (), TranslateError),
    (multitask_wrong_var_name_fails, (), TranslateError),
    (multitask_task_multi_dec_fails, (), TranslateError),
    (multitask_redefine_var_fails, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


def test_run_multiple_top_level_seqs():
    assert len(get_scheduler()._task_dict) == 0
    for func, params, expected in run_tests:
        actual = func(*params)
        assert actual == expected
        # check that there are no tasks left to run
        assert len(get_scheduler()._task_dict) == 0


def test_run_multiple_top_level_seqs_in_parallel():
    assert len(get_scheduler()._task_dict) == 0
    threads = list()
    thread_results = dict()
    for func, params, expected in run_tests:
        thread_results[func] = expected

        def run_func_helper(func):
            actual = func()
            thread_results[func] = (thread_results[func], actual)

        thread = threading.Thread(target=run_func_helper, name=func.__name__, args=(func,))
        threads.append(thread)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for func, results in thread_results.items():
        # results[1] is actual, results[0] is expected
        assert results[1] == results[0], "Func: %s failed assert" % func.__name__
    assert len(get_scheduler()._task_dict) == 0


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_rtseqpkg.py sha256=b76ae24f9cea9aa2a56bac85e8b8b03573d12f30881464c3952c00f0365f4b26 bytes=3270 -->
## FILE: tests/test_rtseqpkg.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_rtseqpkg.py`
- sha256: `b76ae24f9cea9aa2a56bac85e8b8b03573d12f30881464c3952c00f0365f4b26`
- bytes: 3270

````python
import os
import sys
import tempfile
from niveristand import nivs_rt_sequence
from niveristand.clientapi import I32Value, RealTimeSequence
from niveristand.clientapi.realtimesequencepkg import RealTimeSequencePkg

__num_of_valid_rtseqs__ = 4


@nivs_rt_sequence
def empty_func():
    pass


@nivs_rt_sequence
def returns_one():
    return 1


@nivs_rt_sequence
def calls_another():
    a = I32Value(0)
    a.value = returns_one()
    return a.value


@nivs_rt_sequence
def two_levels_deep():
    a = I32Value(0)
    a.value = calls_another()
    a.value += returns_one()
    empty_func()
    return a.value


def test_rtseqpkg_create_empty():
    pkg = RealTimeSequencePkg()
    assert len(pkg) == 0


def test_rtseqpkg_append_module():
    mod = sys.modules[__name__]
    pkg = RealTimeSequencePkg()
    pkg.append(mod)
    assert len(pkg) == __num_of_valid_rtseqs__


def test_rtseqpkg_append_func():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    assert len(pkg) == 1


def test_rtseqpkg_index_returns_RealTimeSequence():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    assert isinstance(pkg[empty_func], RealTimeSequence)


def test_rtseqpkg_can_iterate():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    pkg.append(returns_one)
    assert isinstance(pkg[empty_func], RealTimeSequence)
    assert isinstance(pkg[returns_one], RealTimeSequence)


def test_rtseqpkg_append_dup_doesnt_append():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    pkg.append(empty_func)
    assert len(pkg) == 1


def test_rtseqpkg_contains():
    pkg = RealTimeSequencePkg()
    pkg.append(empty_func)
    assert empty_func in pkg
    assert returns_one not in pkg
    pkg.append(returns_one)
    assert returns_one in pkg


def test_save_all_module():
    pkg = RealTimeSequencePkg()
    folder = tempfile.mkdtemp()
    pkg.append(sys.modules[__name__])
    pkg.save_all(folder)
    _, _, files = next(os.walk(folder))
    assert len(pkg) == __num_of_valid_rtseqs__
    assert len(files) == len(pkg)


def test_rtseq_with_deps():
    seq = RealTimeSequence(calls_another)
    folder = tempfile.mkdtemp()
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 2


def test_rtseq_with_deps_multiple_times():
    seq = RealTimeSequence(calls_another)
    folder = tempfile.mkdtemp()
    seq.save(folder)
    root, _, files = next(os.walk(folder))
    assert len(files) == 2
    for file in files:
        os.remove(os.path.join(root, file))
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 2


def test_rtseq_with_deps_multiple_times_diff_folder():
    seq = RealTimeSequence(calls_another)
    folder = tempfile.mkdtemp()
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 2
    folder = tempfile.mkdtemp()
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 2


def test_rtseq_several_calls():
    seq = RealTimeSequence(two_levels_deep)
    folder = tempfile.mkdtemp()
    seq.save(folder)
    _, _, files = next(os.walk(folder))
    assert len(files) == 4
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_runpyasrtseq.py sha256=6bdc2f3f8ee33263f284c25b1ac3231715b608b82e73815f8ea24c8c8d917d1c bytes=3643 -->
## FILE: tests/test_runpyasrtseq.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_runpyasrtseq.py`
- sha256: `6bdc2f3f8ee33263f284c25b1ac3231715b608b82e73815f8ea24c8c8d917d1c`
- bytes: 3643

````python
import sys
import threading
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, ErrorAction, RealTimeSequence
from niveristand.errors import RunAbortedError, RunFailedError, TranslateError
from niveristand.library import generate_error
from niveristand.library._tasks import get_scheduler
import pytest
from testutilities import validation


@nivs_rt_sequence
def return_var():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def _increment(a):
    a.value += 1
    return a.value


@nivs_rt_sequence
def sub_routine_caller():
    a = DoubleValue(5)
    _increment(a)
    return a.value


@nivs_rt_sequence
def invalid_sequence():
    a = DoubleValue(5)
    a += 1
    return a


@nivs_rt_sequence
def return_void():
    a = DoubleValue(5)  # noqa: F841 it's ok for this variable to never be used


@nivs_rt_sequence
def generate_error_continue():
    generate_error(1, "Continue", ErrorAction.ContinueSequenceExecution)


@nivs_rt_sequence
def generate_error_stop():
    generate_error(2, "Stop", ErrorAction.StopSequence)


@nivs_rt_sequence
def generate_error_abort():
    generate_error(3, "Abort", ErrorAction.AbortSequence)


run_tests = [
    (return_var, (), 5),
    (sub_routine_caller, (), 6),
    (return_void, (), None),
]


fail_transform_tests = [
    (invalid_sequence, (), TranslateError),
    (generate_error_continue, (), RunFailedError),
    (generate_error_stop, (), RunAbortedError),
    (generate_error_abort, (), RunAbortedError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


def test_not_wait_to_complete():
    seq = RealTimeSequence(return_var)
    result_state = seq.run()
    assert result_state.ret_val is None
    result_state.wait_for_result()
    assert result_state.ret_val == 5


def test_run_multiple_top_level_seqs():
    assert len(get_scheduler()._task_dict) == 0
    for func, params, expected in run_tests:
        actual = realtimesequencetools.run_py_as_rtseq(func)
        assert actual == expected
        # check that the scheduler is empty after every run.
        assert len(get_scheduler()._task_dict) == 0


def test_run_multiple_top_level_seqs_in_parallel():
    threads = list()
    thread_results = dict()
    for func, params, expected in run_tests:
        thread_results[func] = expected

        def run_func_helper(func):
            actual = realtimesequencetools.run_py_as_rtseq(func)
            thread_results[func] = (thread_results[func], actual)

        thread = threading.Thread(target=run_func_helper, name=func.__name__, args=(func,))
        threads.append(thread)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    for func, results in thread_results.items():
        assert results[0] == results[1], "Func: %s failed assert" % func.__name__


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        realtimesequencetools.run_py_as_rtseq(func_name)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_saveasrtseq.py sha256=8bd6ba0e234987a439ed066aa2c75e615fc6db292baed58630eff97c67344af4 bytes=1031 -->
## FILE: tests/test_saveasrtseq.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_saveasrtseq.py`
- sha256: `8bd6ba0e234987a439ed066aa2c75e615fc6db292baed58630eff97c67344af4`
- bytes: 1031

````python
import os
import shutil
import tempfile
from niveristand import realtimesequencetools as rtseq
import pytest
import testutilities.testfunctions as testfuncs


def test_save_creates_file():
    try:
        tempfolder = tempfile.mkdtemp()
        rtseq.save_py_as_rtseq(testfuncs.empty_func, tempfolder)
        exp_path = os.path.join(tempfolder, testfuncs.empty_func.__name__ + ".nivsseq")
        assert os.path.isfile(exp_path)
    finally:
        shutil.rmtree(tempfolder, ignore_errors=True)


def test_save_invalid_folder_throws():
    tempfolder = tempfile.mkdtemp()
    shutil.rmtree(tempfolder, ignore_errors=True)
    with pytest.raises(IOError):
        rtseq.save_py_as_rtseq(testfuncs.empty_func, tempfolder)


def _save_debug_helper(func):
    """Save a sequence so it can be inspected manually."""
    tempfolder = tempfile.mkdtemp()
    print(tempfolder)
    rtseq.save_py_as_rtseq(func, tempfolder)


if __name__ == "__main__":
    _save_debug_helper(testfuncs.simple_assign_pi)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_stop_taks.py sha256=8446174197c3a07a5863e6b2dc54ce0204f30df1b070576a23e0ed55d293b328 bytes=4863 -->
## FILE: tests/test_stop_taks.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_stop_taks.py`
- sha256: `8446174197c3a07a5863e6b2dc54ce0204f30df1b070576a23e0ed55d293b328`
- bytes: 4863

````python
import sys
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library import multitask, nivs_yield, stop_task, task
import pytest
from testutilities import rtseqrunner, validation


def _invalid():
    pass


@NivsParam("param", DoubleValue(0), False)
@nivs_rt_sequence
def _return_param_plus_1(param):
    a = DoubleValue(0)
    a.value = param.value + 1
    return a.value


@nivs_rt_sequence
def stop_task_simple():
    a = I32Value(1)
    with multitask() as mt:

        @task(mt)
        def f1():
            nivs_yield()
            pass

        @task(mt)
        def f2():
            stop_task(f1)

    return a.value


@nivs_rt_sequence
def stop_task_invalid_task_name():
    a = I32Value(1)
    with multitask() as mt:

        @task(mt)
        def f1():
            pass

        @task(mt)
        def f2():
            stop_task(_invalid)

    return a.value


@nivs_rt_sequence
def stop_task_invalid_task_name1():
    a = I32Value(1)
    with multitask() as mt:

        @task(mt)
        def f1():
            pass

        @task(mt)
        def f2():
            stop_task("whatever")

    return a.value


@nivs_rt_sequence
def stop_task_in_try():
    try:
        a = I32Value(1)
        with multitask() as mt:

            @task(mt)
            def f1():
                pass

            @task(mt)
            def f2():
                pass

        stop_task(f1)
    finally:
        a.value = 2
    return a.value


@nivs_rt_sequence
def stop_task_complex():
    a = I32Value(1)
    with multitask() as mt:

        @task(mt)
        def f1():
            nivs_yield()
            a.value = 10

        @task(mt)
        def f2():
            a.value = 2
            stop_task(f1)

    return a.value


@nivs_rt_sequence
def stop_task_call_subroutine():
    a = DoubleValue(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            nivs_yield()
            a.value = 10

        @task(mt)
        def f2():
            a.value = _return_param_plus_1(a)
            stop_task(f1)

    return a.value


@nivs_rt_sequence
def stop_task_call_subroutine1():
    a = DoubleValue(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            nivs_yield()
            a.value = _return_param_plus_1(a)

        @task(mt)
        def f2():
            stop_task(f1)

    return a.value


@nivs_rt_sequence
def stop_task_call_subroutine2():
    a = DoubleValue(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            a.value = _return_param_plus_1(a)
            nivs_yield()
            a.value = _return_param_plus_1(a)

        @task(mt)
        def f2():
            stop_task(f1)

    return a.value


run_tests = [
    (stop_task_simple, (), 1),
    (stop_task_in_try, (), 2),
    (stop_task_complex, (), 2),
    (stop_task_call_subroutine, (), 1),
    (stop_task_call_subroutine1, (), 0),
    (stop_task_call_subroutine2, (), 1),
]

fail_transform_tests = [
    (stop_task_invalid_task_name, (), VeristandError),
    (stop_task_invalid_task_name1, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_subroutine_call.py sha256=3676a6c74353bd4b07d7f6464daa13b14babc7d5031ead0753583892b76a1d6d bytes=11432 -->
## FILE: tests/test_subroutine_call.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_subroutine_call.py`
- sha256: `3676a6c74353bd4b07d7f6464daa13b14babc7d5031ead0753583892b76a1d6d`
- bytes: 11432

````python
from math import sqrt
import sys
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import (
    BooleanValue,
    ChannelReference,
    DoubleValue,
    DoubleValueArray,
    I32Value,
)
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
from niveristand.library.primitives import localhost_wait
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _return_constant():
    a = DoubleValue(5)
    return a.value


@nivs_rt_sequence
def finite_recursion(x):
    res = BooleanValue(False)
    if x < 0:
        res.value = True
    else:
        finite_recursion(x - 1)
    return res.value


@nivs_rt_sequence
def circular_call_a():
    circular_call_b()


@nivs_rt_sequence
def circular_call_b():
    circular_call_a()


@NivsParam("param", DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def _return_parameter(param):
    return param.value


class FunkyDecorator:
    def __init__(self, a, b):
        pass

    def __call__(self, f):
        return f


@nivs_rt_sequence
@FunkyDecorator(1, 2)
def return_parameter_invalid_decorator(param):
    return param


@NivsParam("no_param", DoubleValue(0), NivsParam.BY_VALUE)
def _return_param_wrong_param_name_pure_python(param):
    return param


@NivsParam("wrong", I32Value(5), NivsParam.BY_VALUE)
@nivs_rt_sequence
def return_parameter_with_decorator_wrong_name(param):
    return param.value


@NivsParam("param", I32Value(5), NivsParam.BY_VALUE)
@nivs_rt_sequence
def _return_parameter_with_decorator(param):
    return param.value


@NivsParam("param", I32Value(5), NivsParam.BY_REF)
@nivs_rt_sequence
def _return_parameter_with_decorator_by_ref(param):
    return param.value


@nivs_rt_sequence
@NivsParam("param", I32Value(5), NivsParam.BY_VALUE)
def _return_parameter_with_decorator_inverted(param):
    return param.value


@NivsParam("x", I32Value(5), NivsParam.BY_VALUE)
@NivsParam("y", I32Value(5), NivsParam.BY_VALUE)
@NivsParam("z", I32Value(5), NivsParam.BY_REF)
@nivs_rt_sequence
def _return_by_ref_in_z_sqrt_of_square_x_plus_square_y(x, y, z):
    z.value = sqrt(x.value**2 + y.value**2)


@NivsParam("param", DoubleValueArray([0]), NivsParam.BY_REF)
@nivs_rt_sequence
def _return_arr_element(param):
    return param[0].value


@nivs_rt_sequence
def _return_arr_element_plus1_by_ref(param):
    param[0].value += 1


@nivs_rt_sequence
def _return_parameter_plus1_by_ref(param):
    param.value += 1
    return param.value


@NivsParam("param", DoubleValue(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def _return_parameter_plus1_by_value(param):
    param.value += 1
    return param.value


@NivsParam("param", DoubleValue(0), False)
@nivs_rt_sequence
def _return_parameter_plus1_by_ref_bool(param):
    param.value += 1
    return param.value


@NivsParam("param", DoubleValue(0), True)
@nivs_rt_sequence
def _return_parameter_plus1_by_value_bool(param):
    param.value += 1
    return param.value


@NivsParam("param", DoubleValue(0), NivsParam.BY_REF)
@nivs_rt_sequence
def _increment_constant_passed_by_ref(param):
    param.value += 1
    return param.value


@NivsParam("mod", DoubleValue(0), NivsParam.BY_VALUE)
@nivs_rt_sequence
def _return_parameter_with_built_in_function_name(mod):
    return mod.value


@nivs_rt_sequence
def call_increment_constant_passed_by_ref():
    a = DoubleValue(0)
    a.value = _increment_constant_passed_by_ref(5)
    return a.value


@nivs_rt_sequence
def call_return_constant_as_assignment():
    a = DoubleValue(0)
    a.value = _return_constant()
    return a.value


@nivs_rt_sequence
def call_return_constant_as_expr():
    a = BooleanValue(0)
    _return_constant()
    a.value = True
    return a.value


@nivs_rt_sequence
def call_return_parameter():
    a = DoubleValue(0)
    a.value = _return_parameter(DoubleValue(5))
    return a.value


@nivs_rt_sequence
def call_parameter_nivsdatatype():
    a = DoubleValue(5)
    _return_parameter_plus1_by_ref(a)
    return a.value


@nivs_rt_sequence
def call_parameter_nivsdatatype_by_value():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = _return_parameter_plus1_by_value(a)
    return b.value


@nivs_rt_sequence
def call_parameter_nivsdatatype_by_value_untouched_orig():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = _return_parameter_plus1_by_value(a) + a.value
    return b.value


@nivs_rt_sequence
def call_parameter_nivsdatatype_by_ref_bool_ref():
    a = DoubleValue(5)
    _return_parameter_plus1_by_ref_bool(a)
    return a.value


@nivs_rt_sequence
def call_parameter_nivsdatatype_by_value_bool_ref():
    a = DoubleValue(5)
    b = DoubleValue(0)
    b.value = _return_parameter_plus1_by_value_bool(a) + a.value
    return b.value


@nivs_rt_sequence
def call_parameter_builtin_math():
    a = DoubleValue(-5)
    a.value = _return_parameter(abs(a.value))
    return a.value


@nivs_rt_sequence
def call_parameter_array_elem():
    a = DoubleValueArray([1, 2, 3])
    b = DoubleValue(0)
    b.value = _return_arr_element(a)
    return b.value


@nivs_rt_sequence
def call_parameter_array_elem_by_ref():
    a = DoubleValueArray([1, 2, 3])
    return a[1].value


@nivs_rt_sequence
def call_parameter_with_decorator_diff_param_type_by_value():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = _return_parameter_with_decorator(a.value)
    return b.value


@nivs_rt_sequence
def call_parameter_with_decorator_diff_param_type_by_ref():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = _return_parameter_with_decorator_by_ref(a.value)
    return b.value


@nivs_rt_sequence
def call_parameter_with_decorator():
    a = I32Value(1)
    b = I32Value(0)
    b.value = _return_parameter_with_decorator(a.value)
    return b.value


@nivs_rt_sequence
def call_parameter_with_decorator_inverted():
    a = DoubleValue(1.2)
    b = DoubleValue(0)
    b.value = _return_parameter_with_decorator_inverted(a.value)
    return b.value


@nivs_rt_sequence
def call_parameter_with_many_decorators():
    a = DoubleValue(3.1)
    b = DoubleValue(4.999)
    c = I32Value(0)
    _return_by_ref_in_z_sqrt_of_square_x_plus_square_y(a, b, c)
    return c.value


@nivs_rt_sequence
def call_parameter_send_channel_ref_by_value():
    a = ChannelReference("Aliases/DesiredRPM")
    ret = DoubleValue(0)
    a.value = 67
    localhost_wait(0.5)
    _return_parameter_plus1_by_value(a)
    ret.value = a.value
    return ret.value


@nivs_rt_sequence
def call_parameter_send_channel_ref_by_ref():
    a = ChannelReference("Aliases/DesiredRPM")
    ret = DoubleValue(0)
    a.value = 101.2
    localhost_wait(0.5)
    _return_parameter_plus1_by_ref(a)
    localhost_wait(0.5)
    ret.value = a.value
    return ret.value


@nivs_rt_sequence
def recursive_call():
    recursive_call()


@nivs_rt_sequence
def invalid_call():
    fake_call()  # noqa: F821 this is supposed to be an undefined call.


@nivs_rt_sequence
def call_return_parameter_with_built_in_function_name():
    a = DoubleValue(1)
    a.value = _return_parameter_with_built_in_function_name(a.value)
    return a.value


def test_param_wrong_name_python():
    from niveristand import _errormessages

    with pytest.raises(VeristandError) as e:
        _return_param_wrong_param_name_pure_python(True)
    assert str(e.value) is _errormessages.param_description_no_param


@nivs_rt_sequence
def constant_passed_by_ref_is_not_actually_by_ref():
    a = DoubleValue(5)
    _increment_constant_passed_by_ref(a.value)
    return a.value


@NivsParam("param", DoubleValue(0), NivsParam.BY_REF)
def _increment_constant_passed_by_ref_without_rt_decorator(param):
    param.value += 1
    return param.value


def test_constant_passed_by_ref_without_rt_decorator():
    a = DoubleValue(5)
    _increment_constant_passed_by_ref_without_rt_decorator(a.value)
    assert a.value == 5


def test_object_passed_by_ref_without_rt_decorator():
    a = DoubleValue(5)
    _increment_constant_passed_by_ref_without_rt_decorator(a)
    assert a.value == 6


run_tests = [
    (call_return_constant_as_assignment, (), _return_constant()),
    (call_return_constant_as_expr, (), True),
    (call_return_parameter, (), 5),
    (call_parameter_nivsdatatype, (), 6),
    (call_parameter_nivsdatatype_by_value, (), 6),
    (call_parameter_nivsdatatype_by_value_untouched_orig, (), 11),
    (call_parameter_nivsdatatype_by_ref_bool_ref, (), 6),
    (call_parameter_nivsdatatype_by_value_bool_ref, (), 11),
    (call_parameter_builtin_math, (), 5),
    (call_parameter_with_decorator, (), 1),
    (call_parameter_with_decorator_diff_param_type_by_value, (), 1),
    (call_parameter_with_many_decorators, (), 5),
    (call_parameter_with_decorator_inverted, (), 1),
    (call_parameter_array_elem, (), 1),
    (call_parameter_array_elem_by_ref, (), 2),
    (call_parameter_send_channel_ref_by_ref, (), 102.2),
    (call_parameter_send_channel_ref_by_value, (), 67),
    (call_increment_constant_passed_by_ref, (), 6),
    (call_return_parameter_with_built_in_function_name, (), 1),
]

python_tests = run_tests + [(constant_passed_by_ref_is_not_actually_by_ref, (), 5)]

fail_transform_tests = [
    (recursive_call, (), RuntimeError),
    (circular_call_a, (), RuntimeError),
    (circular_call_b, (), RuntimeError),
    (finite_recursion, (), RuntimeError),
    (invalid_call, (), TranslateError),
    (return_parameter_with_decorator_wrong_name, [5], VeristandError),
    (return_parameter_invalid_decorator, [1], TranslateError),
    (call_parameter_with_decorator_diff_param_type_by_ref, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", python_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_subscript.py sha256=089380bb5c9c9d88eb24d0927a89e4a329e14f7332e89184b575cb805d396471 bytes=3977 -->
## FILE: tests/test_subscript.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_subscript.py`
- sha256: `089380bb5c9c9d88eb24d0927a89e4a329e14f7332e89184b575cb805d396471`
- bytes: 3977

````python
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, DoubleValueArray, I32Value, I32ValueArray
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def _return_constant():
    return 2


@nivs_rt_sequence
def _return_param_plus_one(param):
    param.value = param.value + 1
    return param.value


@nivs_rt_sequence
def _modify_param(param):
    param.value = param.value + 1


@nivs_rt_sequence
def number_subscript():
    a = DoubleValueArray([0, 1, 2])
    return a[1].value


@nivs_rt_sequence
def rtseq_call_subscript():
    a = DoubleValueArray([0, 1, 2])
    return a[_return_constant()].value


@nivs_rt_sequence
def subscript_in_subscript():
    a = I32ValueArray([1, 2, 3])
    return a[a[1].value].value


@nivs_rt_sequence
def operator_in_subscript():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    return a[1 + 2].value


@nivs_rt_sequence
def operator_in_subscript1():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    b = I32Value(1)
    c = I32Value(2)
    return a[b.value + c.value].value


@nivs_rt_sequence
def assign_subscript():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    b = DoubleValue(0)
    b.value = a[1].value
    return b.value


@nivs_rt_sequence
def assign_subscript1():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0] = DoubleValue(3)
    return a[0].value


@nivs_rt_sequence
def assign_subscript2():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0] = a[4]
    return a[0].value


@nivs_rt_sequence
def assign_subscript3():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0].value = 5
    return a[0].value


@nivs_rt_sequence
def assign_subroutine_return():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    a[0].value = _return_param_plus_one(a[0])
    return a[0].value


@nivs_rt_sequence
def modify_array():
    a = DoubleValueArray([0, 1, 2, 3, 4])
    _modify_param(a[0])
    return a[0].value


run_tests = [
    (number_subscript, (), 1),
    (rtseq_call_subscript, (), 2),
    (subscript_in_subscript, (), 3),
    (operator_in_subscript, (), 3),
    (operator_in_subscript1, (), 3),
    (assign_subscript, (), 1),
    (assign_subscript3, (), 5),
    (assign_subroutine_return, (), 1),
    (modify_array, (), 1),
]

fail_transform_tests = [
    (assign_subscript1, TranslateError),
    (assign_subscript2, TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name()


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_timing.py sha256=dc642546616ff105841e22e369590ca4b92ce66d3fdc644cca7ef0d23b50b761 bytes=7327 -->
## FILE: tests/test_timing.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_timing.py`
- sha256: `dc642546616ff105841e22e369590ca4b92ce66d3fdc644cca7ef0d23b50b761`
- bytes: 7327

````python
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import VeristandError
from niveristand.library import multitask, nivs_yield, seqtime, task, tickcountms, tickcountus
from niveristand.library.timing import (
    wait,
    wait_until_next_ms_multiple,
    wait_until_next_us_multiple,
    wait_until_settled,
)
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def wait_nivstype():
    init = DoubleValue(0)
    duration = DoubleValue(1)
    end = DoubleValue(0)
    ret = BooleanValue(False)

    init.value = seqtime()
    end.value = wait(duration) - init.value
    if end.value >= duration.value and end.value <= duration.value + 0.1:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_const():
    init = DoubleValue(0)
    end = DoubleValue(0)
    ret = BooleanValue(False)

    init.value = seqtime()
    end.value = wait(DoubleValue(1)) - init.value
    if end.value >= 1 and end.value <= 1.1:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_multitask():
    ret = BooleanValue(False)
    init1 = DoubleValue(0)
    end1 = DoubleValue(0)
    init2 = DoubleValue(0)
    end2 = DoubleValue(0)
    tot_init = DoubleValue(0)
    tot_end = DoubleValue(0)

    tot_init.value = seqtime()
    with multitask() as mt:

        @task(mt)
        def f1():
            init1.value = seqtime()
            nivs_yield()
            end1.value = wait(DoubleValue(1)) - init1.value

        @task(mt)
        def f2():
            init2.value = seqtime()
            end2.value = wait(DoubleValue(3)) - init2.value

    tot_end.value = seqtime() - tot_init.value
    ret.value = (
        tot_end.value >= 3
        and tot_end.value <= 4
        and end1.value >= 1
        and end1.value <= 2
        and end2.value >= 3
        and end2.value <= 4
    )
    return ret.value


@nivs_rt_sequence
def wait_const_negative():
    init = DoubleValue(0)
    end = DoubleValue(0)
    ret = BooleanValue(True)

    init.value = seqtime()
    end.value = wait(DoubleValue(-1)) - init.value
    if end.value >= 0.1 or end.value < 0:
        ret.value = False
    return ret.value


@nivs_rt_sequence
def _return_one():
    a = DoubleValue(1)
    return a.value


@nivs_rt_sequence
def wait_subseq_call():
    init = DoubleValue(0)
    end = DoubleValue(0)
    ret = BooleanValue(False)

    init.value = seqtime()
    end.value = wait(_return_one()) - init.value
    if end.value >= 1 and end.value <= 1.1:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_until_next_ms():
    init = I64Value(0)
    end = I64Value(0)
    ret = BooleanValue(False)

    init.value = tickcountms()
    end.value = wait_until_next_ms_multiple(DoubleValue(231)) - init.value
    if end.value <= 231 and end.value >= 0:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_until_next_us():
    init = I64Value(0)
    end = I64Value(0)
    ret = BooleanValue(False)

    init.value = tickcountus()
    end.value = wait_until_next_us_multiple(DoubleValue(17000)) - init.value
    # give this one a few us buffer because come on, no way python can do it all that fast
    if end.value <= 22000 and end.value >= 0:
        ret.value = True
    return ret.value


@nivs_rt_sequence
def wait_until_settled_multitask():
    a = DoubleValue(15000)
    timer = DoubleValue(0)
    ret = BooleanValue(False)
    timer.value = seqtime()
    with multitask() as mt:

        @task(mt)
        def monitor():
            ret.value = wait_until_settled(
                a, DoubleValue(1000), DoubleValue(500), DoubleValue(2), DoubleValue(-1)
            )

        @task(mt)
        def signal():
            a.value = 600
            wait(DoubleValue(1))
            a.value = 12000
            wait(DoubleValue(1))
            a.value = 300
            wait(DoubleValue(1))
            a.value = 750

    timer.value = seqtime() - timer.value
    ret.value = a.value == 750 and timer.value >= 4 and timer.value <= 6 and not ret.value
    return ret.value


@nivs_rt_sequence
def wait_until_settled_timeout():
    pass_test = BooleanValue(False)
    time = DoubleValue(0)
    time.value = seqtime()
    pass_test.value = wait_until_settled(
        DoubleValue(100), DoubleValue(90), DoubleValue(0), DoubleValue(2), DoubleValue(1)
    )
    time.value = seqtime() - time.value
    pass_test.value &= time.value > 1 and time.value < 1.1
    return pass_test.value


@nivs_rt_sequence
def wait_wrong_param_type():
    duration = I64Value(1)
    wait(duration)
    return duration.value


run_tests = [
    (wait_nivstype, (), True),
    (wait_const, (), True),
    (wait_const_negative, (), True),
    (wait_subseq_call, (), True),
    (wait_multitask, (), True),
    (wait_until_next_us, (), True),
    (wait_until_next_ms, (), True),
    (wait_until_settled_multitask, (), True),
    (wait_until_settled_timeout, (), True),
]

skip_tests = [
    (wait, (), "Imported RT sequence that we're trying to test."),
    (wait_until_next_ms_multiple, (), "Imported RT sequence that we're trying to test."),
    (wait_until_next_us_multiple, (), "Imported RT sequence that we're trying to test."),
    (wait_until_settled, (), "Imported RT sequence that we're trying to test."),
]

fail_transform_tests = [
    (wait_wrong_param_type, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name, deltat=0.01)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


@pytest.mark.parametrize("func_name, params, reason", skip_tests, ids=idfunc)
def test_skipped(func_name, params, reason):
    pytest.skip(func_name.__name__ + ": " + reason)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_top_level_rtseq_params.py sha256=d615c073fb9dd5b61fba55e084615c78e620e54263ba29cd6c422b5e5aba9267 bytes=2882 -->
## FILE: tests/test_top_level_rtseq_params.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_top_level_rtseq_params.py`
- sha256: `d615c073fb9dd5b61fba55e084615c78e620e54263ba29cd6c422b5e5aba9267`
- bytes: 2882

````python
from niveristand import nivs_rt_sequence
from niveristand import NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import ChannelReference, DoubleValue, DoubleValueArray, RealTimeSequence
from niveristand.errors import VeristandError
import pytest


@NivsParam("p", DoubleValue(1.2), NivsParam.BY_REF)
@nivs_rt_sequence
def func1(p):
    return p.value


@NivsParam("p", DoubleValueArray([1.2, 2.3]), NivsParam.BY_VALUE)
@nivs_rt_sequence
def func2(p):
    return p[0].value


def test_run_py_as_rtseq_numeric_param():
    actual = realtimesequencetools.run_py_as_rtseq(func1, {"p": DoubleValue(2.3)})
    assert actual == 2.3


def test_run_py_as_rtseq_channel_reference_param():
    desired_rpm = ChannelReference("Aliases/DesiredRPM")
    desired_rpm.value = 100.101
    actual = realtimesequencetools.run_py_as_rtseq(func1, {"p": desired_rpm})
    assert actual == 100.101


def test_run_py_as_rtseq_invalid_extra_parameter():
    with pytest.raises(VeristandError):
        realtimesequencetools.run_py_as_rtseq(
            func1, {"p": DoubleValue(2.3), "pp": DoubleValue(3.4)}
        )


def test_run_py_as_rtseq_missing_by_ref_parameter():
    with pytest.raises(VeristandError):
        realtimesequencetools.run_py_as_rtseq(func1, {})


def test_run_py_as_rtseq_missing_by_value_parameter():
    actual = realtimesequencetools.run_py_as_rtseq(func2, {})
    assert actual == 1.2


def test_run_py_as_rtseq_wrong_parameter_data_type():
    with pytest.raises(VeristandError):
        realtimesequencetools.run_py_as_rtseq(func2, {"p": DoubleValue(2.3)})


def test_realtimesequence_numeric_param():
    rtseq = RealTimeSequence(func1)
    actual = rtseq.run({"p": DoubleValue(2.3)})
    actual.wait_for_result()
    assert actual.ret_val == 2.3


def test_realtimesequence_channel_reference_param():
    desired_rpm = ChannelReference("Aliases/DesiredRPM")
    desired_rpm.value = 100.101
    rtseq = RealTimeSequence(func1)
    actual = rtseq.run({"p": desired_rpm})
    actual.wait_for_result()
    assert actual.ret_val == 100.101


def test_realtimesequence_invalid_extra_parameter():
    rtseq = RealTimeSequence(func1)
    with pytest.raises(VeristandError):
        rtseq.run({"p": DoubleValue(2.3), "pp": DoubleValue(3.4)})


def test_realtimesequence_missing_by_ref_parameter():
    rtseq = RealTimeSequence(func1)
    with pytest.raises(VeristandError):
        rtseq.run({})


def test_realtimesequence_missing_by_value_parameter():
    rtseq = RealTimeSequence(func2)
    actual = rtseq.run({})
    actual.wait_for_result()
    assert actual.ret_val == 1.2


def test_realtimesequence_wrong_parameter_data_type():
    rtseq = RealTimeSequence(func2)
    with pytest.raises(VeristandError):
        rtseq.run({"p": DoubleValue(2.3)})
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_transformpy2rtseq.py sha256=5dc69bd917e9d3bbfedd6c70125bc8e03edcff34e91a7892e5bff20776f6c936 bytes=4487 -->
## FILE: tests/test_transformpy2rtseq.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_transformpy2rtseq.py`
- sha256: `5dc69bd917e9d3bbfedd6c70125bc8e03edcff34e91a7892e5bff20776f6c936`
- bytes: 4487

````python
from niveristand import errors
from niveristand.clientapi import RealTimeSequence
import pytest
import testutilities.testfunctions as testfuncs


def test_transform_invalid_function_fails():
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfuncs)


def test_transform_func_without_decorator_fails():
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfuncs.func_without_decorator)


def test_transform_empty():
    rtseq = RealTimeSequence(testfuncs.empty_func)
    assert rtseq._rtseq is not None
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 0
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length == 0


def test_transform_empty_with_two_decorators():
    rtseq = RealTimeSequence(testfuncs.empty_func_with_double_decorator)
    assert rtseq._rtseq is not None
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 0
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length == 0


def test_transform_simple_local_assignment():
    testfunc = testfuncs.simple_local_assignment
    rtseq = RealTimeSequence(testfunc)
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length == 1


def test_transform_pi_assign_to_local():
    testfunc = testfuncs.simple_assign_pi
    rtseq = RealTimeSequence(testfunc)
    assert rtseq._rtseq.Variables.LocalVariables.Variables.Length == 1
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 3


def test_untyped_declarations_fail():
    testfunc = testfuncs.assign_untyped
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)


def test_return_var():
    testfunc = testfuncs.return_var
    rtseq = RealTimeSequence(testfunc)
    assert isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 2


def test_return_var_value():
    testfunc = testfuncs.return_var_value
    rtseq = RealTimeSequence(testfunc)
    assert isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 2


def test_undeclared_variable_fail():
    testfunc = testfuncs.return_var_invalid_value
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)


def test_return_named_type():
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfuncs.return_named_type)


def test_return_primitive_num():
    testfunc = testfuncs.return_primitive_num
    rtseq = RealTimeSequence(testfunc)
    assert isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 1


def test_return_var_pi():
    testfunc = testfuncs.return_var_pi
    rtseq = RealTimeSequence(testfunc)
    assert isinstance(rtseq._rtseq.Variables.ReturnType.DefaultValue.Value, float)
    assert rtseq._rtseq.Code.Main.Body.Statements.Length == 3


def test_return_untyped_symbol():
    testfunc = testfuncs.return_untyped_symbol
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)


def test_multiple_returns():
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfuncs.multiple_returns)


def test_return_not_last():
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfuncs.return_not_last)


def test_default_value_bool_true():
    testfunc = testfuncs.return_true
    rtseq = RealTimeSequence(testfunc)
    assert rtseq._rtseq.Variables.LocalVariables.Variables[0].DefaultValue.Value is True


def test_default_value_bool_false():
    testfunc = testfuncs.return_false
    rtseq = RealTimeSequence(testfunc)
    assert rtseq._rtseq.Variables.LocalVariables.Variables[0].DefaultValue.Value is False


def test_boolean_array_return_type():
    with pytest.raises(errors.TranslateError):
        testfuncs.return_boolean_array()


def test_double_array_return_type():
    with pytest.raises(errors.TranslateError):
        testfuncs.return_double_array()


def test_a_value_value_assignment():
    testfunc = testfuncs.a_value_value_assignment
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)


def test_a_value_value_assign_to():
    testfunc = testfuncs.a_value_value_assign_to
    with pytest.raises(errors.TranslateError):
        RealTimeSequence(testfunc)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_try_finally.py sha256=e6fc1e16c01bd7ff90a96eb1c0e9f499bcd1b16c11196266524f805dce504cca bytes=6228 -->
## FILE: tests/test_try_finally.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_try_finally.py`
- sha256: `e6fc1e16c01bd7ff90a96eb1c0e9f499bcd1b16c11196266524f805dce504cca`
- bytes: 6228

````python
import sys
from niveristand import nivs_rt_sequence, NivsParam
from niveristand import realtimesequencetools
from niveristand.clientapi import DoubleValue, DoubleValueArray
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError
from niveristand.library import multitask, nivs_yield, task
import pytest
from testutilities import rtseqrunner, validation


@NivsParam("param", DoubleValue(0), False)
@nivs_rt_sequence
def _sub_rt_seq(param):
    try:
        a = DoubleValue(1)
    finally:
        a.value = param.value
    return a.value


@nivs_rt_sequence
def try_simple():
    try:
        a = DoubleValue(1)
    finally:
        a.value = 5
    return a.value


@nivs_rt_sequence
def try_second_statement():
    a = DoubleValue(0)
    try:
        a.value = 5
    finally:
        a.value = 10
    return a.value


@nivs_rt_sequence
def return_in_try():
    try:
        a = DoubleValue(0)
        return a.value
    finally:
        a.value = 10


@nivs_rt_sequence
def return_in_finally():
    try:
        a = DoubleValue(0)
    finally:
        a.value = 10
        return a.value


@nivs_rt_sequence
def try_complex_body():
    try:
        a = DoubleValueArray([0, 1, 2, 3, 4])
        b = DoubleValue(0)
        for x in a.value:
            if x.value % 2 == 0:
                b.value += x.value
            else:
                b.value -= x.value
    finally:
        if b.value < 5:
            b.value = 1
    return b.value


@nivs_rt_sequence
def try_in_try():
    try:
        a = DoubleValue(0)
        try:
            a.value = 1
        finally:
            a.value = 3
    finally:
        a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_if():
    if True:
        try:
            a = DoubleValue(0)
        finally:
            a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_else():
    a = DoubleValue(0)
    if True:
        a.value = 1
    else:
        try:
            a.value = 3
        finally:
            a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_while():
    while True:
        try:
            a = DoubleValue(0)
        finally:
            a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_for():
    for i in range(5):
        try:
            a = DoubleValue(0)
        finally:
            a.value = 5
    return a.value


@nivs_rt_sequence
def call_subroutine_with_try():
    try:
        a = DoubleValue(0)
        b = DoubleValue(5)
        a.value = _sub_rt_seq(b)
    finally:
        b.value = 5
    return a.value


@nivs_rt_sequence
def try_with_except():
    try:
        a = DoubleValue(0)
    except Exception:
        a.value = 1
    finally:
        a.value = 3
    return a.value


@nivs_rt_sequence
def try_with_orelse():
    try:
        a = DoubleValue(0)
    except Exception:
        a.value = 3
    else:
        a.value = 5
    return a.value


@nivs_rt_sequence
def try_in_task():
    a = DoubleValue(0)
    with multitask() as mt:

        @task(mt)
        def f1():
            try:
                a.value += 1
            finally:
                a.value += 1

        @task(mt)
        def f2():
            nivs_yield()

    return a.value


@nivs_rt_sequence
def try_in_multitask():
    a = DoubleValue(0)
    with multitask() as mt:
        try:
            a.value = 5
        finally:
            a.value += 1

        @task(mt)
        def f1():
            try:
                a.value += 1
            finally:
                a.value += 1

        @task(mt)
        def f2():
            nivs_yield()

    return a.value


@nivs_rt_sequence
def try_in_multitask1():
    a = DoubleValue(0)
    with multitask() as mt:
        try:

            @task(mt)
            def f1():
                pass

        finally:
            a.value += 1

        @task(mt)
        def f2():
            nivs_yield()

    return a.value


run_tests = [
    (try_simple, (), 5),
    (try_complex_body, (), 1),
    (call_subroutine_with_try, (), 5),
]

fail_transform_tests = [
    (try_second_statement, (), TranslateError),
    (return_in_try, (), TranslateError),
    (return_in_finally, (), TranslateError),
    (try_in_try, (), TranslateError),
    (try_in_if, (), TranslateError),
    (try_in_else, (), TranslateError),
    (try_in_while, (), TranslateError),
    (try_in_for, (), TranslateError),
    (try_with_except, (), TranslateError),
    (try_with_orelse, (), TranslateError),
    (try_in_task, (), TranslateError),
    (try_in_multitask, (), TranslateError),
    (try_in_multitask1, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_unary_invert.py sha256=1e0947f4eaf513961af0cf45382b7d0e663b5c790ec2b0bb110e2cec26c02bd7 bytes=7615 -->
## FILE: tests/test_unary_invert.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_unary_invert.py`
- sha256: `1e0947f4eaf513961af0cf45382b7d0e663b5c790ec2b0bb110e2cec26c02bd7`
- bytes: 7615

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I32Value, I64Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import numpy
import pytest
from testutilities import rtseqrunner, validation

a = 1
b = 2


@nivs_rt_sequence
def _returns_zero():
    a = I32Value(0)
    return a.value


@nivs_rt_sequence
def invert_bool():
    a = I32Value(0)
    a.value = ~False
    return a.value


@nivs_rt_sequence
def invert_bool_var():
    a = BooleanValue(False)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32():
    a = I32Value(0)
    a.value = ~0
    return a.value


@nivs_rt_sequence
def invert_int32_1():
    a = I32Value(-1)
    a.value = ~-1
    return a.value


@nivs_rt_sequence
def invert_int32_2():
    a = I32Value(0x7FFFFFFF)
    a.value = ~0x7FFFFFFF
    return a.value


@nivs_rt_sequence
def invert_int32_limit():
    a = I32Value(-0x80000000)
    a.value = ~-0x80000000
    return a.value


@nivs_rt_sequence
def invert_int32_4():
    a = I32Value(-0x7FFFFFFF)
    a.value = ~-0x7FFFFFFF
    return a.value


@nivs_rt_sequence
def invert_int32_var():
    a = I32Value(0)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32_var_1():
    a = I32Value(-1)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32_var_2():
    a = I32Value(0x7FFFFFFF)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32_var_limit():
    a = I32Value(-0x80000000)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int32_var_4():
    a = I32Value(-0x7FFFFFFF)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64():
    a = I64Value(0)
    a.value = ~0
    return a.value


@nivs_rt_sequence
def invert_int64_1():
    a = I64Value(-1)
    a.value = ~-1
    return a.value


@nivs_rt_sequence
def invert_int64_2():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    a.value = ~0x7FFFFFFFFFFFFFFF
    return a.value


@nivs_rt_sequence
def invert_int64_out_of_spe_range():
    a = I64Value(-0x8000000000000000)
    a.value = ~-0x8000000000000000
    return a.value


@nivs_rt_sequence
def invert_int64_4():
    a = I64Value(-0x7FFFFFFFFFFFFFFF)
    a.value = ~-0x7FFFFFFFFFFFFFFF
    return a.value


@nivs_rt_sequence
def invert_int64_var():
    a = I64Value(0)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_var_1():
    a = I64Value(-1)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_var_2():
    a = I64Value(0x7FFFFFFFFFFFFFFF)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_var_out_of_spe_range():
    a = I64Value(-0x8000000000000000)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_var_4():
    a = I64Value(-0x7FFFFFFFFFFFFFFF)
    a.value = ~a
    return a.value


@nivs_rt_sequence
def invert_int64_multiple():
    a = I64Value(-1)
    a.value = ~~a
    return a.value


@nivs_rt_sequence
def invert_int64_multiple1():
    a = I64Value(-1)
    a.value = ~~~a
    return a.value


@nivs_rt_sequence
def invert_int32_multiple():
    a = I32Value(-1)
    a.value = ~~a
    return a.value


@nivs_rt_sequence
def invert_int32_multiple1():
    a = I32Value(-1)
    a.value = ~~~a
    return a.value


@nivs_rt_sequence
def invert_parentheses():
    a = I32Value(0)
    a.value = ~(a)
    return a.value


@nivs_rt_sequence
def invert_rtseq():
    a = I32Value(0)
    a.value = ~_returns_zero()
    return a.value


@nivs_rt_sequence
def invert_double():
    a = DoubleValue(0)
    a.value = ~1.2
    return a.value


@nivs_rt_sequence
def invert_double_var():
    a = DoubleValue(0)
    a.value = ~a
    return a.value


# <editor-fold desc=Invalid tests>


@nivs_rt_sequence
def invert_invalid_variables():
    return ~a


@nivs_rt_sequence
def invert_invalid_variables1():
    return ~a.value


@nivs_rt_sequence
def invert_with_None():
    a = I32Value(0)
    a.value = ~None
    return a


@nivs_rt_sequence
def invert_invalid_rtseq_call():
    a = I32Value(0)
    a.value = ~_returns_zero
    return a


# </editor-fold>


run_tests = [
    (invert_int32, (), -1),
    (invert_int32_1, (), 0),
    (invert_int32_2, (), numpy.int32(-0x80000000)),
    (invert_int32_4, (), numpy.int32(0x7FFFFFFE)),
    (invert_int32_var, (), -1),
    (invert_int32_var_1, (), 0),
    (invert_int32_var_2, (), numpy.int32(-0x80000000)),
    (invert_int32_var_4, (), numpy.int32(0x7FFFFFFE)),
    (invert_int64, (), -1),
    (invert_int64_1, (), 0),
    (invert_int64_2, (), numpy.int64(-0x8000000000000000)),
    (invert_int64_4, (), numpy.int64(0x7FFFFFFFFFFFFFFE)),
    (invert_int64_var, (), -1),
    (invert_int64_var_1, (), 0),
    (invert_int64_var_2, (), numpy.int64(-0x8000000000000000)),
    (invert_int64_var_4, (), numpy.int64(0x7FFFFFFFFFFFFFFE)),
    (invert_int32_multiple, (), -1),
    (invert_int32_multiple1, (), 0),
    (invert_int64_multiple, (), -1),
    (invert_int64_multiple1, (), 0),
    (invert_parentheses, (), -1),
    (invert_rtseq, (), numpy.int32(-1)),
    (invert_bool_var, (), False),  # For RTSeqs, negating a bool or double is always 0
    (invert_double_var, (), 0),  # For RTSeqs, negating a bool or double is always 0
    (invert_int32_limit, (), ~-0x80000000),
    (invert_int32_var_limit, (), ~-0x80000000),
]

fail_transform_tests = [
    (invert_invalid_variables, (), TranslateError),
    (invert_invalid_variables1, (), TranslateError),
    (invert_with_None, (), TranslateError),
    (invert_invalid_rtseq_call, (), VeristandError),
    (invert_bool, (), TranslateError),
    (invert_double, (), TranslateError),
    # SPE doesn't support initializing with the full int32/int64 range.
    (invert_int64_out_of_spe_range, (), VeristandError),
    (invert_int64_var_out_of_spe_range, (), VeristandError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_while.py sha256=650044dfc6005050f4b28e2ddda6fd00870459525ffcd845f97ef2fcdf1663d1 bytes=6036 -->
## FILE: tests/test_while.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_while.py`
- sha256: `650044dfc6005050f4b28e2ddda6fd00870459525ffcd845f97ef2fcdf1663d1`
- bytes: 6036

````python
import sys

from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import BooleanValue, DoubleValue, I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError, VeristandError
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def while_pass():
    while True:
        pass


@nivs_rt_sequence
def while_break():
    while True:
        break


@nivs_rt_sequence
def while_else_pass_fails():
    while True:
        pass
    else:
        pass


@nivs_rt_sequence
def while_invalid_boolean():
    while 1:
        pass


@nivs_rt_sequence
def while_invalid_boolean_const():
    while I32Value(0):
        pass


@nivs_rt_sequence
def while_invalid_boolean_var():
    a = I32Value(1)
    while a.value:
        pass


@nivs_rt_sequence
def while_nested():
    while True:
        while True:
            while True:
                pass


@nivs_rt_sequence
def while_one_statement():
    ret_var = I32Value(0)
    while ret_var.value == 0:
        ret_var.value = 1
    return ret_var.value


@nivs_rt_sequence
def while_multiple_statements():
    cond = BooleanValue(False)
    ret_var = I32Value(0)
    while cond.value is False:
        cond.value = True
        ret_var.value = 1
        ret_var.value = 2
        ret_var.value = 3
    return ret_var.value


@nivs_rt_sequence
def while_condition_variable():
    var = BooleanValue(True)
    while var.value:
        var.value = False
    return var.value


@nivs_rt_sequence
def while_condition_equal_operator():
    var = I32Value(1)
    while var.value == 1:
        var.value = 2
    return var.value


@nivs_rt_sequence
def while_condition_identity_operator():
    var = BooleanValue(True)
    ret = I32Value(0)
    while var.value is True:
        ret.value = 1
        var.value = False
    return ret.value


@nivs_rt_sequence
def while_condition_identity_not_operator():
    var = BooleanValue(True)
    ret = I32Value(0)
    while var.value is not False:
        ret.value = 1
        var.value = False
    return ret.value


@nivs_rt_sequence
def _returns_true_if_less_than_5(x):
    a = BooleanValue(True)
    if x >= 5:
        a.value = False
    return a.value


@nivs_rt_sequence
def while_condition_function_call():
    ret = DoubleValue(0)
    while _returns_true_if_less_than_5(ret.value):
        ret.value += 1
    return ret.value


@nivs_rt_sequence
def while_condition_complex_expression():
    a = DoubleValue(0)
    # the part before the or is true while a.value >= 6
    # the part after the or is true while a.value <6
    # so the last iteration should be a.value == 6
    while ((True and False) is ((a.value * 3) < 20)) or _returns_true_if_less_than_5(a.value - 1):
        a.value += 1
    return a.value


@nivs_rt_sequence
def while_try_catch_fail():
    while True:
        try:
            pass
        except Exception:
            pass
        finally:
            pass


@nivs_rt_sequence
def while_try_finally_fail():
    while True:
        try:
            pass
        finally:
            pass


@nivs_rt_sequence
def while_funcdef_fail():
    while True:

        def f1():
            pass

        f1()


@nivs_rt_sequence
def while_return_fail():
    a = BooleanValue(True)
    while True:
        return a.value


@nivs_rt_sequence
def while_false():
    a = I32Value(1)
    while False:
        a.value = 2
    return a.value


run_tests = [
    (while_one_statement, (), 1),
    (while_multiple_statements, (), 3),
    (while_condition_variable, (), False),
    (while_condition_equal_operator, (), 2),
    (while_condition_function_call, (), 5),
    (while_condition_identity_operator, (), 1),
    (while_condition_identity_not_operator, (), 1),
    (while_condition_complex_expression, (), 6),
    (while_false, (), 1),
]


transform_tests = run_tests + [
    (while_pass, (), 0),
    (while_nested, (), 0),
]


fail_transform_tests = [
    (while_invalid_boolean, (), VeristandError),
    (while_invalid_boolean_const, (), VeristandError),
    (while_invalid_boolean_var, (), VeristandError),
    (while_else_pass_fails, (), TranslateError),
    (while_break, (), TranslateError),
    (while_try_catch_fail, (), TranslateError),
    (while_try_finally_fail, (), TranslateError),
    (while_return_fail, (), TranslateError),
    (while_funcdef_fail, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", transform_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/test_yield.py sha256=c7b1e7c770617475504d4deef91479560fabff8bce3a8231a03ba4b9ce93f04a bytes=3443 -->
## FILE: tests/test_yield.py

- repository: `ni/niveristand-python`
- source_path: `tests/test_yield.py`
- sha256: `c7b1e7c770617475504d4deef91479560fabff8bce3a8231a03ba4b9ce93f04a`
- bytes: 3443

````python
import sys
from niveristand import nivs_rt_sequence
from niveristand import realtimesequencetools
from niveristand.clientapi import I32Value
from niveristand.clientapi import RealTimeSequence
from niveristand.errors import TranslateError
from niveristand.library import iteration, multitask, nivs_yield, task
import pytest
from testutilities import rtseqrunner, validation


@nivs_rt_sequence
def yield_single():
    a = I32Value(0)
    nivs_yield()
    a.value = iteration()
    return a.value


@nivs_rt_sequence
def yield_many():
    a = I32Value(0)
    nivs_yield()
    nivs_yield()
    nivs_yield()
    nivs_yield()
    nivs_yield()
    a.value = iteration()
    return a.value


@nivs_rt_sequence
def yield_in_while():
    a = I32Value(0)
    while a.value < 10:
        nivs_yield()
        a.value = iteration()
    return a.value


@nivs_rt_sequence
def yield_multitask():
    with multitask() as mt:

        @task(mt)
        def f1():
            for a in range(5):
                nivs_yield()

        @task(mt)
        def f2():
            with multitask() as mt_inner:

                @task(mt_inner)
                def fa():
                    for b in range(7):
                        nivs_yield()

                @task(mt_inner)
                def fb():
                    for c in range(13):
                        nivs_yield()

    a = I32Value(0)
    a.value = iteration()
    return a.value


@nivs_rt_sequence
def yield_as_parameter_fail():
    abs(nivs_yield())


@nivs_rt_sequence
def yield_as_operator_fails():
    a = I32Value(0)
    a.value = nivs_yield() + 1
    return a.value


run_tests = [
    (yield_single, (), 1),
    (yield_many, (), 5),
    (yield_in_while, (), 10),
    # multitask() has an implicit yield at the end of it. Keep that in mind!
    (yield_multitask, (), 15),
]

fail_transform_tests = [
    (yield_as_parameter_fail, (), TranslateError),
    (yield_as_operator_fails, (), TranslateError),
]


def idfunc(val):
    try:
        return val.__name__
    except AttributeError:
        return str(val)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_transform(func_name, params, expected_result):
    RealTimeSequence(func_name)


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_runpy(func_name, params, expected_result):
    actual = func_name(*params)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_py_as_rts(func_name, params, expected_result):
    actual = realtimesequencetools.run_py_as_rtseq(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", run_tests, ids=idfunc)
def test_run_in_VM(func_name, params, expected_result):
    actual = rtseqrunner.run_rtseq_in_VM(func_name)
    assert actual == expected_result


@pytest.mark.parametrize("func_name, params, expected_result", fail_transform_tests, ids=idfunc)
def test_failures(func_name, params, expected_result):
    with pytest.raises(expected_result):
        RealTimeSequence(func_name)
    with pytest.raises(expected_result):
        func_name(*params)


def test_check_all_tested():
    validation.test_validate(sys.modules[__name__])
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/__init__.py sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 bytes=0 -->
## FILE: tests/testutilities/__init__.py

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/__init__.py`
- sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- bytes: 0

````python

````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/astutils.py sha256=22f37a0a703750d3ccfa13103b26a8d906e98607e688b30b032696b0c57153ac bytes=2936 -->
## FILE: tests/testutilities/astutils.py

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/astutils.py`
- sha256: `22f37a0a703750d3ccfa13103b26a8d906e98607e688b30b032696b0c57153ac`
- bytes: 2936

````python
import ast
import inspect
import tkinter
from tkinter import ttk
import test_binaryop_add


def pretty_print_ast(obj, graphical=False):
    node = ast.parse(inspect.getsource(obj))
    if graphical:
        AstGUIPrinter(node).print_all()
    else:
        AstPrinter(node).print_all()


class AstPrinter(object):
    def __init__(self, topnode):
        self.__indent = 0
        self._topnode = topnode

    def print_all(self):
        self.print_node(self._topnode)

    def print_node(self, node):
        self.print_with_indentation("%s(" % node.__class__.__name__)
        self.increment_indent()
        for field, value in ast.iter_fields(node):
            if isinstance(value, str) or isinstance(value, int):
                self.print_with_indentation("%s = '%s'" % (field, value))
            elif isinstance(value, list):
                self.print_with_indentation("%s = [" % field)
                self.increment_indent()
                for item in value:
                    self.print_node(item)
                self.decrement_indent("] # %s" % field)
            elif value is None:
                self.print_with_indentation("%s = None" % field)
            elif isinstance(value, ast.AST):
                self.print_with_indentation("%s =" % field)
                self.increment_indent()
                self.print_node(value)
                self.decrement_indent()
            else:
                raise Exception("Unexpected field type %s" % field)
        self.decrement_indent(") # %s" % node.__class__.__name__)

    def print_with_indentation(self, msg):
        print((" " * self.__indent) + msg)

    def increment_indent(self):
        self.__indent += 4

    def decrement_indent(self, msg=None):
        self.__indent -= 4
        if msg is not None:
            self.print_with_indentation(msg)


class AstGUIPrinter(AstPrinter):
    def __init__(self, topnode):
        self._topwindow = tkinter.Tk()
        self._tree = ttk.Treeview(self._topwindow)
        self._curparent = ""
        self._prevparent = ""
        self._lastitem = ""
        super(AstGUIPrinter, self).__init__(topnode)

    def print_all(self):
        self.print_node(self._topnode)
        self._topwindow.geometry("300x900")
        self._tree.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=tkinter.YES)
        self._topwindow.mainloop()

    def print_with_indentation(self, msg):
        self._lastitem = self._tree.insert(self._curparent, "end", text=msg)

    def increment_indent(self):
        self._prevparent = self._curparent
        self._curparent = self._lastitem

    def decrement_indent(self, msg=None):
        self._curparent = self._prevparent
        self._prevparent = self._tree.parent(self._prevparent)


if __name__ == "__main__":
    pretty_print_ast(test_binaryop_add.add_simple_numbers, graphical=True)
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/configutilities.py sha256=6a9665fed25b5bed8ebabd88d222761e02d913ef201dc183ddac034ced6df73c bytes=110 -->
## FILE: tests/testutilities/configutilities.py

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/configutilities.py`
- sha256: `6a9665fed25b5bed8ebabd88d222761e02d913ef201dc183ddac034ced6df73c`
- bytes: 110

````python
def getbinariesfolder():
    from niveristand import _internal

    return _internal.base_assembly_path()
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivsproj sha256=e97f00fe167789c29fecf86f33182e29484b4d1c71b7cad8ae7f264768909d74 bytes=11167 -->
## FILE: tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivsproj`
- sha256: `e97f00fe167789c29fecf86f33182e29484b4d1c71b7cad8ae7f264768909d74`
- bytes: 11167

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="CalcChanFormulaTest" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CalcChanFormulaTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079547.9250941</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="CalcChanFormulaTest.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="CalcChanFormulaTest.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>89c477b2e9b9e1b98ff0aad0eb9aec91</MD5>
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Workspace" TypeGUID="bc98486f-7b49-4949-9504-949cbe254c85">
			<Description />
			<Properties>
				<Property Name="User Accounts">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAAzwkAgAAAAAAFAA5AMP////8ETmFtZQAAEkAw/////whQYXNzd29yZAAADkAw/////wVHcm91cABMAPEAAAAAAAAAAhhTZWMgQWRtaW5pc3RyYXRpb24ubHZsaWIMVXNlclR5cGUuY3RsAB5AUAADAAAAAQACDFVzZXIgQWNjb3VudAAAGkBAAAH/////AAMNVXNlciBBY2NvdW50cwABAAQAAAABAAAADUFkbWluaXN0cmF0b3IAAAAAAAAADkFkbWluaXN0cmF0aW9uAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Group Accounts">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAA7QkAgAAAAAAFAA5AMP////8ETmFtZQAADEAhB0Jvb2xlYW4AGEBAAAH/////AAELUGVybWlzc2lvbnMASwDxAAAAAAAAAAIYU2VjIEFkbWluaXN0cmF0aW9uLmx2bGliDUdyb3VwVHlwZS5jdGwAHEBQAAIAAAACDUdyb3VwIEFjY291bnQAHEBAAAH/////AAMOR3JvdXAgQWNjb3VudHMAAAEABAAAAAIAAAAOQWRtaW5pc3RyYXRpb24AAAANAQEBAQEBAQEBAQEBAQAAAAhPcGVyYXRvcgAAAA0BAAAAAQAAAQEAAAABAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Tools Menu Items">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAEsAkAgAAAAAAIAA5AMP////8ETmFtZQAAEkAw/////whGdW5jdGlvbgAAYQDxAAAAAAAAAAETVG9vbGJhciBCdXR0b25zLmN0bABFQBYAAwROb25lF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yC0RhdGEgVmlld2VyAAAOVG9vbGJhciBCdXR0b24AAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAYwDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZVG9vbHMgTWVudSBJdGVtcyBUeXBlLmN0bAAmQFAABgAAAAEAAgADAAQABQ9Ub29scyBNZW51IEl0ZW0AHkBAAAH/////AAYQVG9vbHMgTWVudSBJdGVtcwAAAQAHAAAACAAAABdNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlcgAAABpNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlci52aQAAAABQVEgwAAAABAAAAAAAAAAAAAEtAAAAAS0AAAAAUFRIMAAAAAQAAAAAAAAAAAATVGVzdCBQcm9maWxlIEVkaXRvcgAAABVUZXN0IEVkaXRvciAoU3RlcCkudmkAAQAAUFRIMAAAAAQAAAAAAAAAAAARQmF0Y2ggVGVzdCBFZGl0b3IAAAAWVGVzdCBFZGl0b3IgKEJhdGNoKS52aQAAAABQVEgwAAAABAAAAAAAAAAAABBURE1TIEZpbGUgVmlld2VyAAAAF3Njcl9URE1TIERhdGEgVmlld2VyLnZpAAIAAFBUSDAAAAAEAAAAAAAAAAAAAS0AAAABLQAAAABQVEgwAAAABAAAAAAAAAAAABNDaGFubmVsIERhdGEgVmlld2VyAAAAFkNoYW5uZWwgRGF0YSBWaWV3ZXIudmkAAAAAUFRIMAAAAAQAAAAAAAAAAAAOQ29uc29sZSBWaWV3ZXIAAAASVmlldyBSVCBDb25zb2xlLnZpAAAAAFBUSDAAAAAEAAAAAAAAAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Engine Components">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAACOQkAgAAAAAAIABJAMP////8IRnVuY3Rpb24AAA5AIQlTaG93SXRlbT8AL0AWAAMETm9uZQxXYWl0Q29tcGxldGUIV2FpdFN5bmMAAApMYXVuY2hUeXBlAAARQAMAC1N5bmNUaW1lb3V0ABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAaQDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZRW5naW5lIENvbXBvbmVudCBUeXBlLmN0bAAsQFAABgAAAAEAAgADAAQABRVFbmdpbmUgQ29tcG9uZW50IEl0ZW0AHkBAAAH/////AAYRRW5naW5lIENvbXBvbmVudHMAAQAHAAAABAAAABJzdWJfQ2FsaWJyYXRpb24udmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAVVGVzdCBFZGl0b3IgKFN0ZXApLnZpAAAAAAAAAFBUSDAAAAAEAAAAAAAAAAAAFlRlc3QgRWRpdG9yIChCYXRjaCkudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAaTW9kZWwgUGFyYW1ldGVyIE1hbmFnZXIudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAA</Data>
					</Variant>
				</Property>
				<Property Name="Hidden Channels">
					<StringArray />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Screens" TypeGUID="cdfadfe0-c84a-4268-a677-4f2f3525465e">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="CalcChanFormulaTest.nivsscreen">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Services" TypeGUID="736a951c-d9c8-457f-96a9-cd0ef16011a5">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Model Parameter Manager" TypeGUID="cc686646-9933-410d-a553-6308e6e06897">
				<Description />
				<Properties>
					<Property Name="Function">
						<String>Model Parameter Manager.vi</String>
					</Property>
					<Property Name="Path">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Sync Options">
						<String>WaitSync</String>
					</Property>
					<Property Name="Sync Timeout">
						<I32>10000</I32>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Profiles" TypeGUID="c3bd79ec-3336-4b06-868e-3217c640edd5">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Calibration" TypeGUID="38433223-24A0-4b32-9339-370EC5AA31B4">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Alarm Responses" TypeGUID="3b1ab560-d77a-41f2-adb4-0c0250b010b3">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Response High" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>true</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>10</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>0</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Response Med" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>true</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>21</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>11</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Response Low" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>31</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>22</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Custom Files" TypeGUID="9e2cb626-3583-4345-aeb6-b9fead6ec565">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Dependencies" TypeGUID="e5b093fa-a709-4df2-807e-a403422ba675">
			<Description />
			<Properties />
			<Errors />
			<Section Name="CalcChanFormulaTest.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanFormulaTest\CalcChanFormulaTest.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanFormulaTest\CalcChanFormulaTest.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="CalcChanFormulaTest.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanFormulaTest\CalcChanFormulaTest.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanFormulaTest\CalcChanFormulaTest.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivsscreen sha256=e779740d50dab2f96be481d8fadfd2bc9d01b9fc677cf42a7cf4faf98ff013e6 bytes=6903 -->
## FILE: tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivsscreen`
- sha256: `e779740d50dab2f96be481d8fadfd2bc9d01b9fc677cf42a7cf4faf98ff013e6`
- bytes: 6903

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="WorkspaceScreen" TypeGUID="2e39a440-e372-11de-8a39-0800200c9a66">
		<Properties>
			<Property Name="Screen Data">
				<Variant>
					<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
					<Data>AAAQuAkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAABgAAABtOdW1lcmljIENvbnRyb2wgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAlBgEAAAAAAAAF0AAAAAAAAVoAeAHqAUACJwAAAAAAAAkBAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwoAFXAQAAAAEAAAArVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvVXNlciBWYXJpYWJsZXMvWgkAgAAAAAABAAQAAAABAAAAAAAAAAAAG051bWVyaWMgQ29udHJvbCAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAACK8AQAAAAAAAAXQAAAAAAABWQB4AaQBQAHhAAAAAAAACQIAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADEAAQoBAAAAAQAAACtUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9Vc2VyIFZhcmlhYmxlcy9ZCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAbTnVtZXJpYyBDb250cm9sIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAFfwBAAAAAAAABdAAAAAAAAFYAHgBXgFAAZv//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMXABTQEAAAABAAAAK1RhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1VzZXIgVmFyaWFibGVzL1gJAIAAAAAAAQAEAAAAAQAAAAAAAAAAABtOdW1lcmljIENvbnRyb2wgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAi2QEAAAAAAAAF0AAAAAAAAVIAeAEYAUABVf//////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAx4ADQAQAAAAEAAAArVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvVXNlciBWYXJpYWJsZXMvUgkAgAAAAAABAAQAAAABAAAAAAAAAAAAG051bWVyaWMgQ29udHJvbCAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAAfPAQAAAAAAAAXQAAAAAAABUQB4ANIBQAEP//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADJQAUgBAAAAAQAAACtUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9Vc2VyIFZhcmlhYmxlcy9RCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAbTnVtZXJpYyBDb250cm9sIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAC28BAAAAAAAABdAAAAAAAAFQAHgAjAFAAMn//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMsABEAEAAAABAAAAK1RhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1VzZXIgVmFyaWFibGVzL1AJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAAxFbXB0eSBTY3JlZW4AAAAAAAAF0AAAAAAAAAAAAAAAAQAAAAAA</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>1488</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>281</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>39</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1228</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>701</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivssdf sha256=2bd5102c025d5ea567b8cbe5e35dd30c3ceeae0c1bf35ed104863e4a2331014a bytes=117426 -->
## FILE: tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivssdf

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanFormulaTest/CalcChanFormulaTest.nivssdf`
- sha256: `2bd5102c025d5ea567b8cbe5e35dd30c3ceeae0c1bf35ed104863e4a2331014a`
- bytes: 117426

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="9" />
	<Content>Definition</Content>
	<Root Name="CalcChanFormulaTest" TypeGUID="03D3BA22-1485-13A6-56BD17DA950CCD00">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CalcChanFormulaTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.98</String>
			</Property>
			<Property Name="Creator">
				<String>Administrator</String>
			</Property>
			<Property Name="Creation Date">
				<Double>3318358984.5011888</Double>
			</Property>
		</Properties>
		<Errors />
		<TargetSections Name="Targets Section" TypeGUID="eb379619-68d7-4d81-be90-c0bc511cdc10">
			<Description />
			<Properties />
			<Errors />
			<Target Name="Controller" TypeGUID="775504BB-1485-13A6-56755DBF2C326980">
				<Description />
				<Properties>
					<Property Name="IP Address">
						<String>localhost</String>
					</Property>
					<Property Name="Control Rate">
						<Double>0</Double>
					</Property>
					<Property Name="HS Port">
						<I32>2040</I32>
					</Property>
					<Property Name="LS Port">
						<I32>2050</I32>
					</Property>
					<Property Name="HS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="LS Port Timeout">
						<I32>1000</I32>
					</Property>
					<Property Name="Control Loop Processor">
						<I32>0</I32>
					</Property>
					<Property Name="Streamed Channels">
						<I32>512</I32>
					</Property>
					<Property Name="Stream Rate">
						<I32>1</I32>
					</Property>
					<Property Name="Secondary Control Loop Processor">
						<I32>-2</I32>
					</Property>
					<Property Name="OS">
						<String>Windows</String>
					</Property>
					<Property Name="Engine Rate">
						<Double>10</Double>
					</Property>
					<Property Name="Execution Mode">
						<U32>0</U32>
					</Property>
					<Property Name="TS_Custom_Dev">
						<String />
					</Property>
					<Property Name="ctr decimation">
						<U32>1</U32>
					</Property>
					<Property Name="custom loop time">
						<U32>1</U32>
					</Property>
					<Property Name="daq">
						<Variant>
							<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
							<Data>AAAAYwkAgAAAAAADABRAMP////8KREFRIERldmljZQAAJ0AHACBQcmltYXJ5IENvbnRyb2wgTG9vcCByYXRlICh1c2VjKQAAEEBQAAIAAAABBGRhdGEAAAEAAgAAAAAAACcQAAAAAA==</Data>
						</Variant>
					</Property>
					<Property Name="dio decimation">
						<U32>1</U32>
					</Property>
					<Property Name="loop time">
						<U32>100000</U32>
					</Property>
					<Property Name="name">
						<String />
					</Property>
					<Property Name="path">
						<Variant>
							<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
							<Data>AAAAuQkAgAAAAAADAB5AMv////8VU2ltdWxhdGlvbiBtb2RlbCBwYXRoAG0A8QAAAAAAAAACH1N5c3RlbSBFeHBsb3JlciBGcmFtZXdvcmsubHZsaWIdUGF0aCByZWxhdGl2ZSBvciBhYnNvbHV0ZS5jdGwAJ0AWAAIIQWJzb2x1dGUIUmVsYXRpdmUACVBhdGggdHlwZQAQQFAAAgAAAAEFVmFsdWUAAQACUFRIMAAAAAQAAAAAAAAAAAAA</Data>
						</Variant>
					</Property>
					<Property Name="ts">
						<U32>0</U32>
					</Property>
					<Property Name="Filter Watchdog Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Filter DAQ Errors">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="DIO Rate">
						<Double>10</Double>
					</Property>
				</Properties>
				<Errors />
				<Section Name="System Variables" TypeGUID="03D3B753-1485-13A6-56B10ED0820CF410">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Actual Loop Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="Hz" BitFields="1">
						<Description>The execution rate of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100000</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Index" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="index" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100001</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Command Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The decimation of the Data Processing Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100002</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The relative system time of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100003</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Alarm Rate" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100004</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="DAQ Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last reported error code from a DAQmx function call. The value zero indicates no error has occurred.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100005</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Delta T" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>The period in seconds of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100006</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Compiler Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100007</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 1" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100008</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 2" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100009</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 3" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100010</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Resume Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100011</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 4" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100012</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 5" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100013</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Stack Index 6" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100014</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>-1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100015</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100016</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Alarm" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ID" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100017</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Low Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100018</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped Medium Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100019</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tripped High Value" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="EUs" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100020</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RT Engine Build" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>A value representing the build number of the NI VeriStand Engine</Description>
						<Properties>
							<Property Name="ID">
								<I32>100021</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Primary Control Loop in nanoseconds</Description>
						<Properties>
							<Property Name="ID">
								<I32>100022</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Loop Duration" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="nsec" BitFields="1">
						<Description>The duration of the Data Processing Loop in nanoseconds</Description>
						<Properties>
							<Property Name="ID">
								<I32>100023</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Command" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Internally commands the RT system with the following numeric values:

0: None
1: Restart System
2: Reset System
3: Shut Down System
4: Reboot System</Description>
						<Properties>
							<Property Name="ID">
								<I32>100024</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Channel Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
						<Description />
						<Properties>
							<Property Name="ID">
								<I32>100025</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Max Streamed Channels" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="cycles" BitFields="1">
						<Description />
						<Properties>
							<Property Name="ID">
								<I32>100026</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Model Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>The number of times the models have not completed their execution in time</Description>
						<Properties>
							<Property Name="ID">
								<I32>100027</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Clients" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100028</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Maximum GENs" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of stimulus profile generators instantiated by the system</Description>
						<Properties>
							<Property Name="ID">
								<I32>100029</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Generator Engine State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>The current state of the stimulus profile generator engine

0: Idle
1: Running
2: Stopped
3: Paused</Description>
						<Properties>
							<Property Name="ID">
								<I32>100030</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Watchdog Timer" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The amount of time in nanoseconds since the Watchdog Timer Loop last executed. The Watchdog Timer Loop is set to execute at a rate of 10Hz.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100031</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HS TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the streaming data gets overwritten.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100032</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Host IP" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The 32-bit integer IP Address of the connected host. A zero value indicates no host is connected to the VeriStand Engine.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100033</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Enabled Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100034</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Detailed Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100035</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="VI Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100036</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Trace Buffer Size" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100037</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Thread Tracing Flag" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100038</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Absolute Time" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="sec" BitFields="1">
						<Description>Returns the current date and time in seconds relative to 12:00 a.m., Friday, January 1, 1904, Universal Time [01-01-1904 00:00:00]. This value is coerced from a 128-bit value to double precision, which may impact resolution.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100039</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Time - Microseconds" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="usec" BitFields="1">
						<Description>The relative system time in microseconds of the VeriStand Engine according to the iteration count and Delta T of the Primary Control Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100040</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 41" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100041</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 42" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100042</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 43" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100043</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 44" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100044</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Iterations" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100045</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Min Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ms" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100046</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PC Timing - Actual Wait" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="ms" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100047</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Failure Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>The failure count of current analysis settings</Description>
						<Properties>
							<Property Name="ID">
								<I32>100048</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Analysis State" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="3">
						<Description>The state of the analysis sub-system on the RT execution host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100049</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TCP Data Packet Loss" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the VeriStand Engine fails to send a data packet to the host. A non-zero number can indicate data loss in logged data. The value is reset every time a Workspace connects to the VeriStand Engine.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100050</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to a waveform read session within the NI VeriStand engine and timed out.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100051</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL TCP Overflow Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop attempted to write to the TCP loop (for a host waveform stream session) and timed out.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100052</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the waveform processing loop encountered an error.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100053</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="WPL Error Code" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The last error code encountered by the waveform processing loop.</Description>
						<Properties>
							<Property Name="ID">
								<I32>100054</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Streamed Waveform Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of waveforms that the VeriStand Engine is currently streaming to the host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100055</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 56" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100056</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 57" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100057</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 58" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100058</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 59" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100059</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 60" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100060</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 61" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100061</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 62" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100062</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 63" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100063</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 64" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100064</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 65" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100065</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 66" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100066</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 67" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100067</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 68" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100068</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 69" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100069</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 70" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100070</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 71" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100071</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 72" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100072</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 73" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100073</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 74" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100074</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 75" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100075</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 76" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100076</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 77" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100077</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 78" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100078</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 79" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100079</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 80" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100080</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 81" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100081</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 82" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100082</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 83" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100083</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 84" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100084</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 85" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100085</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 86" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100086</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 87" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100087</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 88" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100088</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 89" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100089</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 90" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100090</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="System Reserved 91" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100091</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AO1 Error" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100092</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Loop Wakeup Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The wakeup status of the Primary Control Loop.

0: Normal
1: Aborted
2: Asynchronous wakeup
3: Timing source error
4: Timed loop error
5: Timeout</Description>
						<Properties>
							<Property Name="ID">
								<I32>100093</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HD Free Space" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="KB" BitFields="3">
						<Description>Deprecated</Description>
						<Properties>
							<Property Name="ID">
								<I32>100094</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP-LP Overwrite" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop timed out writing channel data to the Data Processing Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100095</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Data Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop timed out writing channel data to the Communication Send Loop</Description>
						<Properties>
							<Property Name="ID">
								<I32>100096</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="HP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Primary Control Loop reported being late</Description>
						<Properties>
							<Property Name="ID">
								<I32>100097</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LP Count" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The number of times the Data Processing Loop reported being late</Description>
						<Properties>
							<Property Name="ID">
								<I32>100098</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Log Status" TypeGUID="03D3B762-1485-13A6-56F0D6D728909E23" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The state of the logging sub-system on the RT execution host</Description>
						<Properties>
							<Property Name="ID">
								<I32>100099</I32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Hardware" TypeGUID="775504AB-1485-13A6-560018C1F4E3EEE1">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Chassis" TypeGUID="03D3BACD-1485-13A6-56E99D97B7543BAF">
						<Description />
						<Properties>
							<Property Name="Chassis master active edge">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master clock source">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master export clock on line">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master export sample clock">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master slope">
								<I32>0</I32>
							</Property>
							<Property Name="Chassis master trigger line">
								<I32>0</I32>
							</Property>
						</Properties>
						<Errors />
						<Section Name="Timing and Sync" TypeGUID="03D3BAED-1485-13A6-56E20B50F6E06D94">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="DAQ" TypeGUID="77550612-1485-13A6-56570AB5032158E9">
							<Description />
							<Properties />
							<Errors />
							<Section Name="Waveform Tasks" TypeGUID="1D6B8779-A957-42D1-B074-82153DB7FF44">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
						<Section Name="FPGA" TypeGUID="03D3B659-1485-13A6-5652D8A07328ECB7">
							<Description />
							<Properties />
							<Errors />
						</Section>
						<Section Name="Data Sharing" TypeGUID="d56f3ac1-7b2c-422c-9d11-fd9cc7abf2a5">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="XNET" TypeGUID="6b693e6d-67b1-40b8-8108-4a4cc3147721">
							<Description />
							<Properties>
								<Property Name="CD Status">
									<U32>2</U32>
								</Property>
							</Properties>
							<Errors />
							<Section Name="LIN" TypeGUID="c9c30728-42cb-4dc3-b054-b80e7a54e833">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="FlexRay" TypeGUID="e33fae90-03f1-4f76-b2f1-6eb8fcac2676">
								<Description />
								<Properties />
								<Errors />
							</Section>
							<Section Name="CAN" TypeGUID="6c5bb91f-0da7-407d-aefc-acbe49c768df">
								<Description />
								<Properties />
								<Errors />
							</Section>
						</Section>
					</Section>
				</Section>
				<Section Name="Stimulus" TypeGUID="03D3B7FF-1485-13A6-56B2328F9511AC8B">
					<Description />
					<Properties>
						<Property Name="Aux Buffer Size">
							<I32>10000</I32>
						</Property>
						<Property Name="Max Gen Maps">
							<I32>256</I32>
						</Property>
						<Property Name="Max Steps">
							<I32>128</I32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Simulation Models" TypeGUID="03D3B937-1485-13A6-5600F2871E269F9A">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Models" TypeGUID="03D3B976-1485-13A6-5604255F981010CE">
						<Description />
						<Properties />
						<Errors />
					</Section>
					<Section Name="Execution Order" TypeGUID="03D3B966-1485-13A6-569CFF8A449BF90A">
						<Description />
						<Properties />
						<Errors />
					</Section>
				</Section>
				<Section Name="Alarms" TypeGUID="03D3B782-1485-13A6-56F58B35B6CBA484">
					<Description />
					<Properties>
						<Property Name="Alarm Rate">
							<U32>0</U32>
						</Property>
					</Properties>
					<Errors />
				</Section>
				<Section Name="Procedures" TypeGUID="03D3B7B1-1485-13A6-56649C7783203F22">
					<Description />
					<Properties />
					<Errors />
					<Section Name="Main" TypeGUID="03D3B7C0-1485-13A6-5652B22D1EEB1FA1">
						<Description />
						<Properties />
						<Errors />
						<Section Name="Dwell" TypeGUID="6dde8411-8c68-408b-8558-d18c0909c789">
							<Description />
							<Properties>
								<Property Name="Command.Value">
									<Double>1</Double>
								</Property>
								<Property Name="Command.Mode">
									<U32>0</U32>
								</Property>
							</Properties>
							<Errors />
						</Section>
						<Section Name="End of Main" TypeGUID="b485fef3-012c-4c9e-acdb-c204000d11e5">
							<Description />
							<Properties>
								<Property Name="Goto Label">
									<DependentNode Path="Targets Section/Controller/Procedures/Main/Dwell" />
								</Property>
							</Properties>
							<Errors />
						</Section>
					</Section>
				</Section>
				<Section Name="Custom Devices" TypeGUID="03D3BB79-1485-13A6-5605EB7AFD7405AC">
					<Description />
					<Properties />
					<Errors />
				</Section>
				<Section Name="User Variables" TypeGUID="03D3B6B7-1485-13A6-567BE1E1E0DF999A">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="P" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>3</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>12</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Q" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>4</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>6</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="R" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>9</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>3</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="X" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>10</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0.1</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Z" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>17</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>3</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Y" TypeGUID="03D3B6C6-1485-13A6-56609EA3AE19E356" RowDim="1" ColDim="1" Units="" BitFields="7">
						<Description />
						<Properties>
							<Property Name="ID">
								<U32>18</U32>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>2</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="Calculated Variables" TypeGUID="03D3B714-1485-13A6-56031C5F1CCB78A9">
					<Description />
					<Properties />
					<Errors />
					<Channel Name="Time" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Zero" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEtAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="MinusOne" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAlQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEtAAAAATEAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Zero" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>1</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Pi" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>This value should be accurate to all bits of the matissa.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABWFjb3MoAAAABltWYXIwXQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/MinusOne" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>acos(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PplusQtimesRsq" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Test precedence of operators: "P + Q*R^2" should be equal to "P + (Q * (R^2))"</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAswkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAHAAAABltWYXIwXQAAAAErAAAABltWYXIxXQAAAAEqAAAABltWYXIyXQAAAAFeAAAAATIAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>[Var2]</Elem>
									<Elem>^</Elem>
									<Elem>2</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PplusQtimesRsq_Exact" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAxwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAALAAAABltWYXIwXQAAAAErAAAAASgAAAAGW1ZhcjFdAAAAASoAAAABKAAAAAZbVmFyMl0AAAABXgAAAAEyAAAAASkAAAABKQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/User Variables/P" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/User Variables/Q" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/User Variables/R" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>(</Elem>
									<Elem>[Var2]</Elem>
									<Elem>^</Elem>
									<Elem>2</Elem>
									<Elem>)</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TmoduloPi" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAxQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAJAAAABltWYXIwXQAAAAEtAAAABltWYXIxXQAAAAEqAAAABGludCgAAAAGW1ZhcjJdAAAAAS8AAAAGW1ZhcjNdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Time" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Pi" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Time" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Pi" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>int(</Elem>
									<Elem>[Var2]</Elem>
									<Elem>/</Elem>
									<Elem>[Var3]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="CosTmoduloPi" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABGNvcygAAAAGW1ZhcjBdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/TmoduloPi" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>cos(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ZeroEqualsTMinusAcosCosT" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>T = acos(cos(T))  is true iff  T = (Time modulo Pi).</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAqAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAABltWYXIwXQAAAAEtAAAABWFjb3MoAAAABltWYXIxXQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/TmoduloPi" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/CosTmoduloPi" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>acos(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="TmoduloPiMinusPiOver2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAApAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAABltWYXIwXQAAAAEtAAAABltWYXIxXQAAAAEvAAAAATIAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/TmoduloPi" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Pi" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>[Var1]</Elem>
									<Elem>/</Elem>
									<Elem>2</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="SinTmoduloPiMinusPiOver2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABHNpbigAAAAGW1ZhcjBdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/TmoduloPiMinusPiOver2" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>sin(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ZeroEqualsTMinusAsinSinT" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>T = asin(sin(T))  is true iff  T = (Time modulo Pi) - Pi/2.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAqAkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAABltWYXIwXQAAAAEtAAAABWFzaW4oAAAABltWYXIxXQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/TmoduloPiMinusPiOver2" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/SinTmoduloPiMinusPiOver2" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>asin(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="SinSqT" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAogkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAABHNpbigAAAAGW1ZhcjBdAAAAASkAAAABXgAAAAEyAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>sin(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
									<Elem>^</Elem>
									<Elem>2</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="CosSqT" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAogkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAABGNvcygAAAAGW1ZhcjBdAAAAASkAAAABXgAAAAEyAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>cos(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
									<Elem>^</Elem>
									<Elem>2</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="OneEqualsSinSqTPlusCosSqT" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAErAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/SinSqT" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/CosSqT" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PiEquals4TimesAtan1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>This value should be accurate to all bits of the matissa.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAowkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAFAAAAATQAAAABKgAAAAVhdGFuKAAAAAZbVmFyMF0AAAABKQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/OneEqualsSinSqTPlusCosSqT" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>4</Elem>
									<Elem>*</Elem>
									<Elem>atan(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="AnotherFormulaForZero" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>N = int(T/Pi) is a count of the number of half cycles we have traversed.
(-1)^N should be equal to sign(sin(T)) except when T=0.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA6gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAQAAAAASgAAAABLQAAAAExAAAAASkAAAABXgAAAARpbnQoAAAABltWYXIwXQAAAAEvAAAABltWYXIxXQAAAAEpAAAAAS0AAAAFc2lnbigAAAAEc2luKAAAAAZbVmFyMl0AAAABKQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Pi" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>(</Elem>
									<Elem>-</Elem>
									<Elem>1</Elem>
									<Elem>)</Elem>
									<Elem>^</Elem>
									<Elem>int(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>/</Elem>
									<Elem>[Var1]</Elem>
									<Elem>)</Elem>
									<Elem>-</Elem>
									<Elem>sign(</Elem>
									<Elem>sin(</Elem>
									<Elem>[Var2]</Elem>
									<Elem>)</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Tshifted" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The value 4.55*(Delta T) accounts for the various phase shifts encountered while
processing the signal. These are:
                  (a) The first calculation is done at T=(Delta T) not T=0.
                  (b) The group delay through the lowpass Butterworth filter.
                  (c) The phase shift through Simpson's rule integration.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAswkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAIAAAABltWYXIwXQAAAAEtAAAABltWYXIxXQAAAAEqAAAAATQAAAABLgAAAAE1AAAAATUAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>(</Elem>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
									<Elem>)</Elem>
									<Elem>-</Elem>
									<Elem>[Var2]</Elem>
									<Elem>*</Elem>
									<Elem>4</Elem>
									<Elem>.</Elem>
									<Elem>5</Elem>
									<Elem>5</Elem>
								</StringArray>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="2Sin30TPlusPoint5CosTPlus4" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Two tone sinusoidal input waveform that we will process.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA5gkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAARAAAAATIAAAABKgAAAARzaW4oAAAAATMAAAABMAAAAAEqAAAABltWYXIwXQAAAAEpAAAAASsAAAABLgAAAAE1AAAAASoAAAAEY29zKAAAAAZbVmFyMV0AAAABKQAAAAErAAAAATQAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Tshifted" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Tshifted" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>2</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>3</Elem>
									<Elem>0</Elem>
									<Elem>*</Elem>
									<Elem>[Var0]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>.</Elem>
									<Elem>5</Elem>
									<Elem>*</Elem>
									<Elem>cos(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>)</Elem>
									<Elem>+</Elem>
									<Elem>4</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="LowPassFilterAt3Hz" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>This Butterworth filter will be applied to the input waveform to eliminate the high
frequency content. There will be a group delay through the third order low-pass
Butterworth filter. It is related to the cutoff frequency and order of the filter.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>3</U16>
							</Property>
							<Property Name="CC:Lowpass:Chan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/2Sin30TPlusPoint5CosTPlus4" />
							</Property>
							<Property Name="CC:Lowpass:CutFrequency">
								<Double>3</Double>
							</Property>
							<Property Name="CC:Lowpass:AnalysisOrder">
								<I32>3</I32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Zero" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="PeakAndValleyOfFilterOut" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>4</U16>
							</Property>
							<Property Name="CC:Peak:XChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/LowPassFilterAt3Hz" />
							</Property>
							<Property Name="CC:Peak:ValleyChan">
								<DependentNode Path="Targets Section/Controller/User Variables/Y" />
							</Property>
							<Property Name="CC:Peak:OffsetChan">
								<DependentNode Path="Targets Section/Controller/User Variables/Z" />
							</Property>
							<Property Name="CC:Peak:Hysteresis">
								<Double>0.2</Double>
							</Property>
							<Property Name="CC:Peak:Reset">
								<U32>100</U32>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FilterOutMinusFourKm2" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>23</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFourKm1" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FilterOutMinusFourKm1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="ID">
								<U32>14</U32>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFour" />
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FilterOutMinusFour" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The filter's output should be ".5*cos(T) + 4". Here we subtract off the offset of 4 leaving ".5*cos(T)".</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAlQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEtAAAAATQAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/LowPassFilterAt3Hz" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>4</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ErrorInFilterOutMinusFour" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAtgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAIAAAABltWYXIwXQAAAAEtAAAAAS4AAAABNQAAAAEqAAAABGNvcygAAAAGW1ZhcjFdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFour" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Tshifted" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>.</Elem>
									<Elem>5</Elem>
									<Elem>*</Elem>
									<Elem>cos(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="IntegralAtKm1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/IntegralOfFilterOutMinusFour" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="IntegralOfFilterOutMinusFour" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>Simpson's Rule for integrating an input waveform. It uses values at the previous two steps.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA5QkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAPAAAABltWYXIwXQAAAAErAAAABltWYXIxXQAAAAEqAAAAASgAAAAGW1ZhcjJdAAAAASsAAAABNAAAAAEqAAAABltWYXIzXQAAAAErAAAABltWYXI0XQAAAAEpAAAAAS8AAAABNgAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/IntegralAtKm1" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/System Variables/Delta T" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFourKm2" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFourKm1" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFour" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>[Var1]</Elem>
									<Elem>*</Elem>
									<Elem>(</Elem>
									<Elem>[Var2]</Elem>
									<Elem>+</Elem>
									<Elem>4</Elem>
									<Elem>*</Elem>
									<Elem>[Var3]</Elem>
									<Elem>+</Elem>
									<Elem>[Var4]</Elem>
									<Elem>)</Elem>
									<Elem>/</Elem>
									<Elem>6</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="ErrorInIntegral" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The integral should have produced: ".5*sin(T)"</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAtgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAIAAAABltWYXIwXQAAAAEtAAAAAS4AAAABNQAAAAEqAAAABHNpbigAAAAGW1ZhcjFdAAAAASkAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/IntegralOfFilterOutMinusFour" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Tshifted" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>.</Elem>
									<Elem>5</Elem>
									<Elem>*</Elem>
									<Elem>sin(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="Rand" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAAB3JhbmQoMSkAAAABKwAAAAZbVmFyMF0AAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Zero" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>rand(1)</Elem>
									<Elem>+</Elem>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandCount" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAlQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAErAAAAATEAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandCount" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>1</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandCountMinus1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAlQkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEtAAAAATEAAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandCount" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>1</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandSafeCountMinus1" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>1</U16>
							</Property>
							<Property Name="CC:Max:YConstant">
								<Boolean>false</Boolean>
							</Property>
							<Property Name="CC:Max:XConstant">
								<Boolean>true</Boolean>
							</Property>
							<Property Name="CC:Max:XConstValue">
								<Double>2</Double>
							</Property>
							<Property Name="CC:Max:YChan">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandCountMinus1" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray />
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandRunningMeanPrev" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningMean" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandRunningMean" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The average value for a set of uniform random numbers between 0 and 1 should be 1/2.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAwgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAJAAAABltWYXIwXQAAAAErAAAAASgAAAAGW1ZhcjFdAAAAAS0AAAAGW1ZhcjJdAAAAASkAAAABLwAAAAZbVmFyM10AAAAA</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningMeanPrev" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Rand" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningMeanPrev" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandCount" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>-</Elem>
									<Elem>[Var2]</Elem>
									<Elem>)</Elem>
									<Elem>/</Elem>
									<Elem>[Var3]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandRunningSquaresPrev" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningSquares" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandRunningSquares" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAA2wkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAANAAAABltWYXIwXQAAAAErAAAAASgAAAAGW1ZhcjFdAAAAAS0AAAAGW1ZhcjJdAAAAASkAAAABKgAAAAEoAAAABltWYXIzXQAAAAEtAAAABltWYXI0XQAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningSquaresPrev" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Rand" />
							</Property>
							<Property Name="Var2">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningMeanPrev" />
							</Property>
							<Property Name="Var3">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/Rand" />
							</Property>
							<Property Name="Var4">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningMean" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>+</Elem>
									<Elem>(</Elem>
									<Elem>[Var1]</Elem>
									<Elem>-</Elem>
									<Elem>[Var2]</Elem>
									<Elem>)</Elem>
									<Elem>*</Elem>
									<Elem>(</Elem>
									<Elem>[Var3]</Elem>
									<Elem>-</Elem>
									<Elem>[Var4]</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandRunningVariance" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAmgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAADAAAABltWYXIwXQAAAAEvAAAABltWYXIxXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningSquares" />
							</Property>
							<Property Name="Var1">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandSafeCountMinus1" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>/</Elem>
									<Elem>[Var1]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="RandErrorInVariance" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description>The variance of a set of uniform random numbers between 0 and 1 should be 1/12.</Description>
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAArgkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAAIAAAABltWYXIwXQAAAAEtAAAAASgAAAABMQAAAAEvAAAAATEAAAABMgAAAAEpAAAAAA==</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningVariance" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
									<Elem>-</Elem>
									<Elem>(</Elem>
									<Elem>1</Elem>
									<Elem>/</Elem>
									<Elem>1</Elem>
									<Elem>2</Elem>
									<Elem>)</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
					<Channel Name="FinalTime" TypeGUID="03D3B772-1485-13A6-56D8DB23F9C234C2" RowDim="1" ColDim="1" Units="" BitFields="1">
						<Description />
						<Properties>
							<Property Name="CalcCh:Type">
								<U16>0</U16>
							</Property>
							<Property Name="CalcCh:Formula:Formula">
								<Variant>
									<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
									<Data>AAAAiwkAgAAAAAADABBAMP////8GU3RyaW5nAAAUQEAAAf////8AAAdGb3JtdWxhAEkA8QAAAAAAAAACIENhbGN1bGF0ZWQgQ2hhbm5lbCBTdG9yYWdlLmx2bGliC0Zvcm11bGEuY3RsABRAUAABAAEHRm9ybXVsYQABAAIAAAABAAAABltWYXIwXQAAAAA=</Data>
								</Variant>
							</Property>
							<Property Name="Var0">
								<DependentNode Path="Targets Section/Controller/System Variables/System Time" />
							</Property>
							<Property Name="CalcCh:Formula:FormulaString">
								<StringArray>
									<Elem>[Var0]</Elem>
								</StringArray>
							</Property>
						</Properties>
						<Errors />
						<DefaultValue>
							<Elem>0</Elem>
						</DefaultValue>
					</Channel>
				</Section>
				<Section Name="XNET Databases" TypeGUID="def5630b-577f-4ae9-9682-5f8ee445ee21">
					<Description />
					<Properties />
					<Errors />
				</Section>
			</Target>
		</TargetSections>
		<Section Name="Aliases" TypeGUID="e11f4519-09e6-4fb0-99df-2967c4313d67">
			<Description />
			<Properties />
			<Errors />
			<Alias Name="P" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/P" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Q" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/Q" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="RandCount" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/RandCount" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="X" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/X" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Z" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/Z" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Y" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/Y" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Pi" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Pi" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="SinT" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/CosTmoduloPi" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="SinSqT" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/SinSqT" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ZeroEqualsTMinusAsinSinT" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ZeroEqualsTMinusAsinSinT" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="CosT" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/SinTmoduloPiMinusPiOver2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="CosSqT" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/CosSqT" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ZeroEqualsTMinusAcosCosT" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ZeroEqualsTMinusAcosCosT" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="OneEqualsSinSqTPlusCosSqT" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/OneEqualsSinSqTPlusCosSqT" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="PiEquals4TimesAtan1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/PiEquals4TimesAtan1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FilterOutMinusFourKm2" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFourKm2" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FilterOutMinusFourKm1" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFourKm1" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FilterOutMinusFour" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/FilterOutMinusFour" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Zero" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Zero" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="MinusOne" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/MinusOne" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="PplusQtimesRsq" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/PplusQtimesRsq" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="PplusQtimesRsq_Exact" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/PplusQtimesRsq_Exact" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="AnotherFormulaForZero" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/AnotherFormulaForZero" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="PeakAndValleyOfFilterOut" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/PeakAndValleyOfFilterOut" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ErrorInFilterOutMinusFour" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ErrorInFilterOutMinusFour" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="RandErrorInVariance" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/RandErrorInVariance" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="RandRunningMean" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningMean" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="RandRunningVariance" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/RandRunningVariance" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="Time" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/Time" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="R" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/User Variables/R" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="ErrorInIntegral" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/ErrorInIntegral" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
			<Alias Name="FinalTime" TypeGUID="2c11e122-dad9-44da-989c-a66ff203fa31">
				<Description />
				<Properties>
					<Property Name="Referenced Channel">
						<DependentNode Path="Targets Section/Controller/Calculated Variables/FinalTime" />
					</Property>
				</Properties>
				<Errors />
			</Alias>
		</Section>
		<Section Name="Data Sharing Network" TypeGUID="8288dbb9-8c87-4fda-9c66-acec90c46c03">
			<Description />
			<Properties>
				<Property Name="CD Status">
					<U32>2</U32>
				</Property>
			</Properties>
			<Errors />
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivsproj sha256=1168638528b04021527cdfdd7c14339eea51c9714898cd96cce7b7c52eea0a7c bytes=11137 -->
## FILE: tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivsproj

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivsproj`
- sha256: `1168638528b04021527cdfdd7c14339eea51c9714898cd96cce7b7c52eea0a7c`
- bytes: 11137

````xml
<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2012" Minor="0" Fix="0" Build="1" />
	<Content>Definition</Content>
	<Root Name="CalcChanLatchTest" TypeGUID="d9313aae-3554-45e5-93f3-86454275d4f2">
		<Description />
		<Properties>
			<Property Name="Name">
				<String>CalcChanLatchTest</String>
			</Property>
			<Property Name="Version">
				<String>1.0.0.0</String>
			</Property>
			<Property Name="Creator">
				<String />
			</Property>
			<Property Name="Creation Date">
				<Double>3351079547.9250941</Double>
			</Property>
		</Properties>
		<Errors />
		<Section Name="System Definition File" TypeGUID="b9227a5b-2770-4a62-8621-ac414d4124fb">
			<Description />
			<Properties />
			<Errors />
			<Section Name="CalcChanLatchTest.nivssdf" TypeGUID="3a41ca74-36ec-4aff-9219-9d05c8f91208">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="CalcChanLatchTest.nivssdf">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5>89c477b2e9b9e1b98ff0aad0eb9aec91</MD5>
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Workspace" TypeGUID="bc98486f-7b49-4949-9504-949cbe254c85">
			<Description />
			<Properties>
				<Property Name="User Accounts">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAAzwkAgAAAAAAFAA5AMP////8ETmFtZQAAEkAw/////whQYXNzd29yZAAADkAw/////wVHcm91cABMAPEAAAAAAAAAAhhTZWMgQWRtaW5pc3RyYXRpb24ubHZsaWIMVXNlclR5cGUuY3RsAB5AUAADAAAAAQACDFVzZXIgQWNjb3VudAAAGkBAAAH/////AAMNVXNlciBBY2NvdW50cwABAAQAAAABAAAADUFkbWluaXN0cmF0b3IAAAAAAAAADkFkbWluaXN0cmF0aW9uAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Group Accounts">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAA7QkAgAAAAAAFAA5AMP////8ETmFtZQAADEAhB0Jvb2xlYW4AGEBAAAH/////AAELUGVybWlzc2lvbnMASwDxAAAAAAAAAAIYU2VjIEFkbWluaXN0cmF0aW9uLmx2bGliDUdyb3VwVHlwZS5jdGwAHEBQAAIAAAACDUdyb3VwIEFjY291bnQAHEBAAAH/////AAMOR3JvdXAgQWNjb3VudHMAAAEABAAAAAIAAAAOQWRtaW5pc3RyYXRpb24AAAANAQEBAQEBAQEBAQEBAQAAAAhPcGVyYXRvcgAAAA0BAAAAAQAAAQEAAAABAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Tools Menu Items">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAAEsAkAgAAAAAAIAA5AMP////8ETmFtZQAAEkAw/////whGdW5jdGlvbgAAYQDxAAAAAAAAAAETVG9vbGJhciBCdXR0b25zLmN0bABFQBYAAwROb25lF1N0aW11bHVzIFByb2ZpbGUgRWRpdG9yC0RhdGEgVmlld2VyAAAOVG9vbGJhciBCdXR0b24AAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAYwDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZVG9vbHMgTWVudSBJdGVtcyBUeXBlLmN0bAAmQFAABgAAAAEAAgADAAQABQ9Ub29scyBNZW51IEl0ZW0AHkBAAAH/////AAYQVG9vbHMgTWVudSBJdGVtcwAAAQAHAAAACAAAABdNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlcgAAABpNb2RlbCBQYXJhbWV0ZXIgTWFuYWdlci52aQAAAABQVEgwAAAABAAAAAAAAAAAAAEtAAAAAS0AAAAAUFRIMAAAAAQAAAAAAAAAAAATVGVzdCBQcm9maWxlIEVkaXRvcgAAABVUZXN0IEVkaXRvciAoU3RlcCkudmkAAQAAUFRIMAAAAAQAAAAAAAAAAAARQmF0Y2ggVGVzdCBFZGl0b3IAAAAWVGVzdCBFZGl0b3IgKEJhdGNoKS52aQAAAABQVEgwAAAABAAAAAAAAAAAABBURE1TIEZpbGUgVmlld2VyAAAAF3Njcl9URE1TIERhdGEgVmlld2VyLnZpAAIAAFBUSDAAAAAEAAAAAAAAAAAAAS0AAAABLQAAAABQVEgwAAAABAAAAAAAAAAAABNDaGFubmVsIERhdGEgVmlld2VyAAAAFkNoYW5uZWwgRGF0YSBWaWV3ZXIudmkAAAAAUFRIMAAAAAQAAAAAAAAAAAAOQ29uc29sZSBWaWV3ZXIAAAASVmlldyBSVCBDb25zb2xlLnZpAAAAAFBUSDAAAAAEAAAAAAAAAAAAAA==</Data>
					</Variant>
				</Property>
				<Property Name="Engine Components">
					<Variant>
						<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
						<Data>AAACOQkAgAAAAAAIABJAMP////8IRnVuY3Rpb24AAA5AIQlTaG93SXRlbT8AL0AWAAMETm9uZQxXYWl0Q29tcGxldGUIV2FpdFN5bmMAAApMYXVuY2hUeXBlAAARQAMAC1N5bmNUaW1lb3V0ABpAMv////8QQ3VzdG9tIFRvb2wgUGF0aAAAaQDxxyxnxAAAAAIRTklWU19TaGFyZWQubHZsaWINUGF0aCB0eXBlLmN0bABBQBYAAwhBYnNvbHV0ZQhSZWxhdGl2ZQxUb0FwcERhdGFEaXIAABVDdXN0b20gVG9vbCBQYXRoIFR5cGUAaQDxAAAAAAAAAAIaTklWU1Byb2pfRmlsZW1hbmFnZXIubHZsaWIZRW5naW5lIENvbXBvbmVudCBUeXBlLmN0bAAsQFAABgAAAAEAAgADAAQABRVFbmdpbmUgQ29tcG9uZW50IEl0ZW0AHkBAAAH/////AAYRRW5naW5lIENvbXBvbmVudHMAAQAHAAAABAAAABJzdWJfQ2FsaWJyYXRpb24udmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAVVGVzdCBFZGl0b3IgKFN0ZXApLnZpAAAAAAAAAFBUSDAAAAAEAAAAAAAAAAAAFlRlc3QgRWRpdG9yIChCYXRjaCkudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAaTW9kZWwgUGFyYW1ldGVyIE1hbmFnZXIudmkAAAAAAAAAUFRIMAAAAAQAAAAAAAAAAAAA</Data>
					</Variant>
				</Property>
				<Property Name="Hidden Channels">
					<StringArray />
				</Property>
			</Properties>
			<Errors />
			<Section Name="Screens" TypeGUID="cdfadfe0-c84a-4268-a677-4f2f3525465e">
				<Description />
				<Properties>
					<Property Name="Path">
						<DependentFile Type="Relative" Path="CalcChanLatchTest.nivsscreen">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Services" TypeGUID="736a951c-d9c8-457f-96a9-cd0ef16011a5">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Model Parameter Manager" TypeGUID="cc686646-9933-410d-a553-6308e6e06897">
				<Description />
				<Properties>
					<Property Name="Function">
						<String>Model Parameter Manager.vi</String>
					</Property>
					<Property Name="Path">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Sync Options">
						<String>WaitSync</String>
					</Property>
					<Property Name="Sync Timeout">
						<I32>10000</I32>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Profiles" TypeGUID="c3bd79ec-3336-4b06-868e-3217c640edd5">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Calibration" TypeGUID="38433223-24A0-4b32-9339-370EC5AA31B4">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Alarm Responses" TypeGUID="3b1ab560-d77a-41f2-adb4-0c0250b010b3">
			<Description />
			<Properties />
			<Errors />
			<Section Name="Response High" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>true</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>10</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>0</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Response Med" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>true</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>21</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>11</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="Response Low" TypeGUID="99267DF5-8C59-4AAC-B020-7591F4886206">
				<Description />
				<Properties>
					<Property Name="Show Dialog">
						<Boolean>false</Boolean>
					</Property>
					<Property Name="Play Sound">
						<String>Disabled</String>
					</Property>
					<Property Name="Wave File">
						<DependentFile Type="Absolute" Path="">
							<Version />
							<RTDestination />
							<SupportedTarget />
							<MD5 />
						</DependentFile>
					</Property>
					<Property Name="Log Alarms">
						<String>Enabled</String>
					</Property>
					<Property Name="Log File">
						<String>Logs\Alarm Log.txt</String>
					</Property>
					<Property Name="Max Priority">
						<U32>31</U32>
					</Property>
					<Property Name="Min Priority">
						<U32>22</U32>
					</Property>
					<Property Name="Enable Response">
						<Boolean>true</Boolean>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
		<Section Name="Custom Files" TypeGUID="9e2cb626-3583-4345-aeb6-b9fead6ec565">
			<Description />
			<Properties />
			<Errors />
		</Section>
		<Section Name="Dependencies" TypeGUID="e5b093fa-a709-4df2-807e-a403422ba675">
			<Description />
			<Properties />
			<Errors />
			<Section Name="CalcChanLatchTest.nivssdf [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanLatchTest\CalcChanLatchTest.nivssdf]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanLatchTest\CalcChanLatchTest.nivssdf</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
			<Section Name="CalcChanLatchTest.nivsscreen [C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanLatchTest\CalcChanLatchTest.nivsscreen]" TypeGUID="369b9797-43bd-4cdf-8352-81032feed666">
				<Description />
				<Properties>
					<Property Name="Path">
						<String>C:\Users\Public\Documents\National Instruments\NI VeriStand 2010\AutoTestProjects\CalcChanLatchTest\CalcChanLatchTest.nivsscreen</String>
					</Property>
				</Properties>
				<Errors />
			</Section>
		</Section>
	</Root>
</Document>
````

<!--NI_OSS_SOURCE repo=niveristand-python path=tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivsscreen sha256=53111a171cf0c37fa4c6936d09f2c56ee68fb8f15e8387df46c54f5daee05c67 bytes=22857 -->
## FILE: tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivsscreen

- repository: `ni/niveristand-python`
- source_path: `tests/testutilities/legacy_files/CalcChanLatchTest/CalcChanLatchTest.nivsscreen`
- sha256: `53111a171cf0c37fa4c6936d09f2c56ee68fb8f15e8387df46c54f5daee05c67`
- bytes: 22857

````text
﻿<?xml version="1.0" encoding="utf-8"?>
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="System definition.xsd">
	<MD5Checksum />
	<Version Major="2010" Minor="0" Fix="0" Build="0" />
	<Content>Definition</Content>
	<Root Name="WorkspaceScreen" TypeGUID="2e39a440-e372-11de-8a39-0800200c9a66">
		<Properties>
			<Property Name="Screen Data">
				<Variant>
					<Type>AAAACgAUQDD/////C2RhdGEgc3RyaW5n</Type>
					<Data>AAA/cgkAgAAAAABYABRAMP////8LVGVtcGxhdGUgVkkAEUADAApQb3NpdGlvbiBYAAARQAMAClBvc2l0aW9uIFkAABBAMP////8GQ3VzdG9tAAAUQCEOU2hvdyBUaXRsZSBCYXIAAAlAAwACSUQAABJAIQ1BbHdheXMgT24gVG9wABJAIQxBbGxvdyBSZXNpemUAABRAIQ5BbGxvdyBNaW5pbWl6ZQAAEEAhC0FsbG93IENsb3NlABRAIQ5TaXplIHRvIFNjcmVlbgAAD0ADAAlTY3JlZW4uSUQAGUAWAAIGTm9ybWFsA05ldwAABVN0YXRlAA5AMP////8FVGl0bGUACUACAANbMF0ACUACAANbMV0ACUACAANbMl0ACUACAANbM10AHEBQAAQADgAPABAAEQ1XaW5kb3cgQm91bmRzABFACAALQ2hhbm5lbCBSZWYADkAw/////wRVbml0AAAUQCEORGVmYXVsdCBVbml0cz8AABJAIQxGbGFzaCBMaW1pdD8AAA1ABwAHQ29sb3IgMQANQAcAB0NvbG9yIDIADUAHAAdDb2xvciAzAA1ABwAHQ29sb3IgNAAPQAcACUJjayBDb2xvcgARQAcACkZvcmUgQ29sb3IAAA1ACgAHTGltaXQgMQANQAoAB0xpbWl0IDIADUAKAAdMaW1pdCAzAA1ACgAHTGltaXQgNAATQAMADExpbWl0IE1vZGUgMQAAE0ADAAxMaW1pdCBNb2RlIDIAABNAAwAMTGltaXQgTW9kZSAzAAATQAMADExpbWl0IE1vZGUgNAAAFUADAA9TY2FsZSBQcmVjaXNpb24AD0AKAAlTY2FsZSBNaW4AD0AKAAlTY2FsZSBNYXgADUADAAZGb3JtYXQAAA9AAwAJUHJlY2lzaW9uABVAAwAPQmFja2dyb3VuZCBUeXBlABFAAwALVmFyaWFibGUgSUQAEEBAAAH/////ACsDSURzABRAMP////8LVmFyaWFibGUgSUQAEkBAAAH/////AC0FVW5pdHMAFEBAAAH/////AC0GTGFiZWxzAAATQAoADFNjYWxlIEZhY3RvcgAAE0AKAAxTY2FsZSBPZmZzZXQAABFABwALVmFyaWFibGUgSUQAGkBAAAH/////ADIMWVNjYWxlIEluZGV4AAANQAUABkZvcm1hdAAAD0AFAAlQcmVjaXNpb24ACUAFAANGaXQADkAw/////wVMYWJlbAAWQCERVXNlIERlZmF1bHQgTGFiZWwAEkAhDUxhYmVsIFZpc2libGUACUAKAANNaW4ACUAKAANNYXgASwDxAAAAAAAAAAEgY2x1c3Rlcl9HcmFwaCBTY2FsZSBTZXR0aW5ncy5jdGwAIkBQAAgANAA1ADYANwA4ADkAOgA7BlhTY2FsZQAAFEBAAAH/////ADwHWVNjYWxlcwAPQAUACUJhciBTdHlsZQANQAIAB0ZpbGwgVG8AE0AHAAxGaWxsL1B0Q29sb3IAABFABQAKTGluZSBTdHlsZQAAEUAFAApMaW5lIFdpZHRoAAALQAcABUNvbG9yAA1ABQAGSW50ZXJwAAARQAUAC1BvaW50IFN0eWxlAEgA8QAAAAAAAAABH2NsdXN0ZXJfR3JhcGggUGxvdCBTZXR0aW5ncy5jdGwAIEBQAAgAPgA/AEAAQQBCAEMARABFBFBsb3QAABJAQAAB/////wBGBVBsb3RzABNACgANVXBkYXRlIFBlcmlvZAAVQAoADkhpc3RvcnkgTGVuZ3RoAAAUQHAACAAAAAIAAAZNeS5SZWYAABBAIQtJcyBDb250cm9sPwAWQDD/////DENoYW5uZWwgUGF0aAAAGkBAAAH/////AEwNQ2hhbm5lbCBQYXRocwAQQFMLQ3VzdG9tIERhdGEAqwDxxieWWAAAAAEgY2x1c3Rlcl9TY3JlZW4gSXRlbSBTZXR0aW5ncy5jdGwAgkBQADYAAAABAAIAAwAEAAUABgAHAAgACQAKAAsADAANABIAEwAUABUAFgAXABgAGQAaABsAHAAdAB4AHwAgACEAIgAjACQAJQAmACcAKAApACoALAAuAC8AMAAxADMAPAA9AEcASABJAEoASwBNAE4LU2NyZWVuIEl0ZW0AEkBAAAH/////AE8FSXRlbXMADkAw/////wROYW1lAAAUQDD/////C0Rlc2NyaXB0aW9uAVMA8QAAAAAAAAABH2VudW1fVXNlciBBZG1pbiBQZXJtaXNzaW9ucy5jdGwBK0AWAA0HRGVmYXVsdA5BZG1pbmlzdHJhdGlvbhdDaGFubmVsIFNjYWxpbmcgVXRpbGl0eRFBZGQgRGlzcGxheSBJdGVtcxNDaGFuZ2UgVXNlciBQcm9maWxlI0VkaXQgU3RpbXVsdXMgUHJvZmlsZSBFZGl0b3IgSGVhZGVyGkVkaXQgRGlzcGxheSBJdGVtIFNldHRpbmdzG01vZGVsIFBhcmFtZXRlciBDYWxpYnJhdGlvbhJSdW50aW1lIEFsYXJtIEVkaXQPRWRpdCBUb29scyBNZW51FkVkaXQgRW5naW5lIENvbXBvbmVudHMaQ29uZmlndXJlIFZpc2libGUgQ2hhbm5lbHMNRmF1bHQgTWFuYWdlcgAAClBlcm1pc3Npb24AAAxAIQdMb2FkZWQ/ABRAIQ9BbHdheXMgVmlzaWJsZT8AVwDxAAAAAAAAAAEkY2x1c3Rlcl9FbnRpcmUgU2NyZWVuIERlZmluaXRpb24uY3RsACpAUAAKAFAAUQBSAAUAAQACAAYAUwBUAFULU2NyZWVuLkRhdGEAJkBAAAH/////AFYZU2NyZWVuIEl0ZW0gQ2x1c3RlciBBcnJheQABAFcAAAABAAAAJgAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAByCAQAAAAAAAAXQAAAAAAAKTGF0Y2hfVF8xMAFyArICOgLvAAAAAAAAEU4AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGIAAT4AAAAAAQAAADpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9MYXRjaF9UXzEwCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAa7gEAAAAAAAAF0AAAAAAACUxhdGNoX1RfOQFyAnYCOgKzAAAAAAAAEU0AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGJwAP4AAAAAAQAAADlUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9MYXRjaF9UXzkJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABEKAQAAAAAAAAXQAAAAAAAJTGF0Y2hfVF84AXICOgI6AncAAAAAAAARTAAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYtABLQAAAAABAAAAOVRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0xhdGNoX1RfOAkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAA28BAAAAAAAABdAAAAAAAAlMYXRjaF9UXzcBcgH+AjoCOwAAAAAAABFLAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABjQAESAAAAAAEAAAA5VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvTGF0Y2hfVF83CQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAPmwEAAAAAAAAF0AAAAAAACUxhdGNoX1RfNgFyAcICOgH/AAAAAAAAEUoAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGOwAUIAAAAAAQAAADlUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9MYXRjaF9UXzYJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABZXAQAAAAAAAAXQAAAAAAAJTGF0Y2hfVF81AXIBhgI6AcMAAAAAAAARSQAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZCABVwAAAAABAAAAOVRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0xhdGNoX1RfNQkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAACu8BAAAAAAAABdAAAAAAAAlMYXRjaF9UXzQBcgFKAjoBhwAAAAAAABFIAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABkkAFHAAAAAAEAAAA5VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvTGF0Y2hfVF80CQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAADAEAAAAAAAAF0AAAAAAACUxhdGNoX1RfMwFyAQ4COgFLAAAAAAAAEUcAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGUQAWgAAAAAAQAAADlUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9MYXRjaF9UXzMJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAABIAQAAAAAAAAXQAAAAAAAJTGF0Y2hfVF8yAXIA0gI6AQ8AAAAAAAARRgAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZYABeQAAAAABAAAAOVRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0xhdGNoX1RfMgkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAFvUBAAAAAAAABdAAAAAAAAlMYXRjaF9UXzEBcgCWAjoA0wAAAAAAABFFAAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABl4AF6AAAAAAEAAAA5VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvTGF0Y2hfVF8xCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAC1QEAAAAAAAAF0AAAAAAACUxhdGNoX1RfMAFyAFoCOgCXAAAAAAAAEUQAAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGZgAW8AAAAAAQAAADlUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9MYXRjaF9UXzAJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAAMNAQAAAAAAAAXQAAAAAAALRXhhY3RfZlRfMTADKgKyA/IC7///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABmwAFwAAAAAAEAAAA7VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvRXhhY3RfZlRfMTAJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABcqAQAAAAAAAAXQAAAAAAALTGF0Y2hfZlRfMTACTgKyAxYC7///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABnMAGCAAAAAAEAAAA7VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvTGF0Y2hfZlRfMTAJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABrIAQAAAAAAAAXQAAAAAAAKRXhhY3RfZlRfOQMqAnYD8gKz//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGewAYkAAAAAAQAAADpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9FeGFjdF9mVF85CQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAT9AEAAAAAAAAF0AAAAAAACkxhdGNoX2ZUXzkCTgJ2AxYCs///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABoIAGPAAAAAAEAAAA6VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvTGF0Y2hfZlRfOQkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAIl0BAAAAAAAABdAAAAAAAApFeGFjdF9mVF84AyoCOgPyAnf//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaJABlQAAAAABAAAAOlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0V4YWN0X2ZUXzgJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAAFAAQAAAAAAAAXQAAAAAAAKTGF0Y2hfZlRfOAJOAjoDFgJ3//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGjwAZoAAAAAAQAAADpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9MYXRjaF9mVF84CQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAUngEAAAAAAAAF0AAAAAAACkV4YWN0X2ZUXzcDKgH+A/ICO///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABpYAGgAAAAAAEAAAA6VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvRXhhY3RfZlRfNwkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAIe4BAAAAAAAABdAAAAAAAApMYXRjaF9mVF83Ak4B/gMWAjv//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAadABpgAAAAABAAAAOlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0xhdGNoX2ZUXzcJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABJzAQAAAAAAAAXQAAAAAAAKRXhhY3RfZlRfNgMqAcID8gH///////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGpAAawAAAAAAQAAADpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9FeGFjdF9mVF82CQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAArwEAAAAAAAAF0AAAAAAACkxhdGNoX2ZUXzYCTgHCAxYB////////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABqsAGyAAAAAAEAAAA6VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvTGF0Y2hfZlRfNgkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAADHABAAAAAAAABdAAAAAAAAdEZWx0YSBUAHgAWgFAAJf//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAayABuAAAAAABAAAAM1RhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1N5c3RlbSBWYXJpYWJsZXMvRGVsdGEgVAkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAE48BAAAAAAAABdAAAAAAAApFeGFjdF9mVF81AyoBhgPyAcP//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa5ABvgAAAAABAAAAOlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0V4YWN0X2ZUXzUJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABchAQAAAAAAAAXQAAAAAAAKTGF0Y2hfZlRfNQJOAYYDFgHD//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGwAAcQAAAAAAQAAADpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9MYXRjaF9mVF81CQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAPZgEAAAAAAAAF0AAAAAAACkV4YWN0X2ZUXzQDKgFKA/IBh///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABscAHKAAAAAAEAAAA6VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvRXhhY3RfZlRfNAkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAFokBAAAAAAAABdAAAAAAAApMYXRjaF9mVF80Ak4BSgMWAYf//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbOAB0AAAAAABAAAAOlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0xhdGNoX2ZUXzQJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAAo6AQAAAAAAAAXQAAAAAAAKRXhhY3RfZlRfMwMqAQ4D8gFL//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG1QAdYAAAAAAQAAADpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9FeGFjdF9mVF8zCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAlBgEAAAAAAAAF0AAAAAAACkxhdGNoX2ZUXzMCTgEOAxYBS///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABtwAHcAAAAAAEAAAA6VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvTGF0Y2hfZlRfMwkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAADB0BAAAAAAAABdAAAAAAAApFeGFjdF9mVF8yAyoA0gPyAQ///////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAbjAB4gAAAAABAAAAOlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0V4YWN0X2ZUXzIJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAACAFAQAAAAAAAAXQAAAAAAAKTGF0Y2hfZlRfMgJOANIDFgEP//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG6gAegAAAAAAQAAADpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9MYXRjaF9mVF8yCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAb5wEAAAAAAAAF0AAAAAAACkV4YWN0X2ZUXzEDKgCWA/IA0///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABvEAHuAAAAAAEAAAA6VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvRXhhY3RfZlRfMQkAgAAAAAABAAQAAAABAAAAAAAAAAAAHU51bWVyaWMgSW5kaWNhdG9yIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAABukBAAAAAAAABdAAAAAAAApMYXRjaF9mVF8xAk4AlgMWANP//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAb4AB9AAAAAABAAAAOlRhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL0NhbGN1bGF0ZWQgVmFyaWFibGVzL0xhdGNoX2ZUXzEJAIAAAAAAAQAEAAAAAQAAAAAAAAAAAB1OdW1lcmljIEluZGljYXRvciAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAAZTAQAAAAAAAAXQAAAAAAAKRXhhY3RfZlRfMAMqAFoD8gCX//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG/wAfoAAAAAAQAAADpUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9DYWxjdWxhdGVkIFZhcmlhYmxlcy9FeGFjdF9mVF8wCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAdTnVtZXJpYyBJbmRpY2F0b3IgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAANlgEAAAAAAAAF0AAAAAAACkxhdGNoX2ZUXzACTgBaAxYAl///////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABwYAIAAAAAAAEAAAA6VGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvQ2FsY3VsYXRlZCBWYXJpYWJsZXMvTGF0Y2hfZlRfMAkAgAAAAAABAAQAAAABAAAAAAAAAAAAG051bWVyaWMgQ29udHJvbCAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAABX8AQAAAAAAAAXQAAAAAAABUwBuAaQBNgHh//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHDQAgYBAAAAAQAAACtUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9Vc2VyIFZhcmlhYmxlcy9TCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAbTnVtZXJpYyBDb250cm9sIC0gTWVkaXVtLnZpAAAAAAAAAAAAAAAAAAAAItkBAAAAAAAABdAAAAAAAAFSAG4BXgE2AZv//////////wAAAAABAADvAAAA7wAAAP/+AAD//gAAAAAAAP//AAAAAAAAAAAAQFkAAAAAAABAJAAAAAAAAEBWgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAP/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcTACCwEAAAABAAAAK1RhcmdldHMgU2VjdGlvbi9Db250cm9sbGVyL1VzZXIgVmFyaWFibGVzL1IJAIAAAAAAAQAEAAAAAQAAAAAAAAAAABtOdW1lcmljIENvbnRyb2wgLSBNZWRpdW0udmkAAAAAAAAAAAAAAAAAAAAHzwEAAAAAAAAF0AAAAAAAAVEAbgEYATYBVf//////////AAAAAAEAAO8AAADvAAAA//4AAP/+AAAAAAAA//8AAAAAAAAAAABAWQAAAAAAAEAkAAAAAAAAQFaAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAA/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABxoAIRAQAAAAEAAAArVGFyZ2V0cyBTZWN0aW9uL0NvbnRyb2xsZXIvVXNlciBWYXJpYWJsZXMvUQkAgAAAAAABAAQAAAABAAAAAAAAAAAAG051bWVyaWMgQ29udHJvbCAtIE1lZGl1bS52aQAAAAAAAAAAAAAAAAAAAAtvAQAAAAAAAAXQAAAAAAABUABuANIBNgEP//////////8AAAAAAQAA7wAAAO8AAAD//gAA//4AAAAAAAD//wAAAAAAAAAAAEBZAAAAAAAAQCQAAAAAAABAVoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAD/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHIgAhgBAAAAAQAAACtUYXJnZXRzIFNlY3Rpb24vQ29udHJvbGxlci9Vc2VyIFZhcmlhYmxlcy9QCQCAAAAAAAEABAAAAAEAAAAAAAAAAAAMRW1wdHkgU2NyZWVuAAAAAAAABdAAAAAAAAAAAAAAAAEAAAAAAA==</Data>
				</Variant>
			</Property>
			<Property Name="Screen Order">
				<I32Array>
					<Elem>1488</Elem>
				</I32Array>
			</Property>
			<Property Name="EscapeEnabled">
				<Boolean>false</Boolean>
			</Property>
			<Property Name="ShowPropPageOnDrop">
				<Boolean>true</Boolean>
			</Property>
			<Property Name="Workspace Loc and Size Left">
				<U16>65475</U16>
			</Property>
			<Property Name="Workspace Loc and Size Top">
				<U16>22</U16>
			</Property>
			<Property Name="Workspace Loc and Size Right">
				<U16>1081</U16>
			</Property>
			<Property Name="Workspace Loc and Size Bottom">
				<U16>829</U16>
			</Property>
		</Properties>
		<Errors />
	</Root>
</Document>
````
