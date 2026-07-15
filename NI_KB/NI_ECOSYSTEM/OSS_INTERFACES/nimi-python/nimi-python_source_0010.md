# NI OSS SOURCE SNAPSHOT: nimi-python

<!--NI_OSS_SNAPSHOT repo=ni/nimi-python commit=6511f8025f072f7f7021953888b916bbdc31aa2a -->

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/_grpc_stub_interpreter.py sha256=aaf3f1235d6a4807740e8b806f348641e2933969c8e7222c535d980315a5ee21 bytes=23202 -->
## FILE: generated/nifgen/nifgen/_grpc_stub_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/_grpc_stub_interpreter.py`
- sha256: `aaf3f1235d6a4807740e8b806f348641e2933969c8e7222c535d980315a5ee21`
- bytes: 23202

````python
# -*- coding: utf-8 -*-
# This file was generated

import grpc
import hightime  # noqa: F401
import session_pb2 as session_grpc_types
import threading
import warnings

from . import enums as enums  # noqa: F401
from . import errors as errors
from . import nifgen_pb2 as grpc_types
from . import nifgen_pb2_grpc as nifgen_grpc


class GrpcStubInterpreter(object):
    '''Interpreter for interacting with a gRPC Stub class'''

    def __init__(self, grpc_options):
        self._grpc_options = grpc_options
        self._lock = threading.RLock()
        self._client = nifgen_grpc.NiFgenStub(grpc_options.grpc_channel)
        self.set_session_handle()

    def set_session_handle(self, value=session_grpc_types.Session()):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def _invoke(self, func, request, metadata=None):
        try:
            response = func(request, metadata=metadata)
            error_code = response.status
            error_message = ''
        except grpc.RpcError as rpc_error:
            error_code = None
            error_message = rpc_error.details()
            for entry in rpc_error.trailing_metadata() or []:
                if entry.key == 'ni-error':
                    value = entry.value if isinstance(entry.value, str) else entry.value.decode('utf-8')
                    try:
                        error_code = int(value)
                    except ValueError:
                        error_message += f'\nError status: {value}'

            grpc_error = rpc_error.code()
            if grpc_error == grpc.StatusCode.NOT_FOUND:
                raise errors.DriverTooOldError() from None
            elif grpc_error == grpc.StatusCode.INVALID_ARGUMENT:
                raise ValueError(error_message) from None
            elif grpc_error == grpc.StatusCode.UNAVAILABLE:
                error_message = 'Failed to connect to server'
            elif grpc_error == grpc.StatusCode.UNIMPLEMENTED:
                error_message = (
                    'This operation is not supported by the NI gRPC Device Server being used. Upgrade NI gRPC Device Server.'
                )

            if error_code is None:
                raise errors.RpcError(grpc_error, error_message) from None

        if error_code < 0:
            raise errors.DriverError(error_code, error_message)
        elif error_code > 0:
            if not error_message:
                try:
                    error_message = self.error_message(error_code)
                except errors.Error:
                    error_message = 'Failed to retrieve error description.'
            warnings.warn(errors.DriverWarning(error_code, error_message))
        return response

    def abort(self):  # noqa: N802
        self._invoke(
            self._client.AbortGeneration,
            grpc_types.AbortGenerationRequest(vi=self._vi),
        )

    def allocate_named_waveform(self, channel_name, waveform_name, waveform_size):  # noqa: N802
        self._invoke(
            self._client.AllocateNamedWaveform,
            grpc_types.AllocateNamedWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_name=waveform_name, waveform_size=waveform_size),
        )

    def allocate_waveform(self, channel_name, waveform_size):  # noqa: N802
        response = self._invoke(
            self._client.AllocateWaveform,
            grpc_types.AllocateWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_size=waveform_size),
        )
        return response.waveform_handle

    def clear_arb_memory(self):  # noqa: N802
        self._invoke(
            self._client.ClearArbMemory,
            grpc_types.ClearArbMemoryRequest(vi=self._vi),
        )

    def clear_arb_sequence(self, sequence_handle):  # noqa: N802
        self._invoke(
            self._client.ClearArbSequence,
            grpc_types.ClearArbSequenceRequest(vi=self._vi, sequence_handle_raw=sequence_handle),
        )

    def clear_arb_waveform(self, waveform_handle):  # noqa: N802
        self._invoke(
            self._client.ClearArbWaveform,
            grpc_types.ClearArbWaveformRequest(vi=self._vi, waveform_handle_raw=waveform_handle),
        )

    def clear_freq_list(self, frequency_list_handle):  # noqa: N802
        self._invoke(
            self._client.ClearFreqList,
            grpc_types.ClearFreqListRequest(vi=self._vi, frequency_list_handle_raw=frequency_list_handle),
        )

    def clear_user_standard_waveform(self, channel_name):  # noqa: N802
        self._invoke(
            self._client.ClearUserStandardWaveform,
            grpc_types.ClearUserStandardWaveformRequest(vi=self._vi, channel_name=channel_name),
        )

    def commit(self):  # noqa: N802
        self._invoke(
            self._client.Commit,
            grpc_types.CommitRequest(vi=self._vi),
        )

    def configure_arb_sequence(self, channel_name, sequence_handle, gain, offset):  # noqa: N802
        self._invoke(
            self._client.ConfigureArbSequence,
            grpc_types.ConfigureArbSequenceRequest(vi=self._vi, channel_name=channel_name, sequence_handle=sequence_handle, gain=gain, offset=offset),
        )

    def configure_arb_waveform(self, channel_name, waveform_handle, gain, offset):  # noqa: N802
        self._invoke(
            self._client.ConfigureArbWaveform,
            grpc_types.ConfigureArbWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_handle=waveform_handle, gain=gain, offset=offset),
        )

    def configure_freq_list(self, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase):  # noqa: N802
        self._invoke(
            self._client.ConfigureFreqList,
            grpc_types.ConfigureFreqListRequest(vi=self._vi, channel_name=channel_name, frequency_list_handle=frequency_list_handle, amplitude=amplitude, dc_offset=dc_offset, start_phase=start_phase),
        )

    def configure_standard_waveform(self, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        self._invoke(
            self._client.ConfigureStandardWaveform,
            grpc_types.ConfigureStandardWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_raw=waveform.value, amplitude=amplitude, dc_offset=dc_offset, frequency=frequency, start_phase=start_phase),
        )

    def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array):  # noqa: N802
        response = self._invoke(
            self._client.CreateAdvancedArbSequence,
            grpc_types.CreateAdvancedArbSequenceRequest(vi=self._vi, waveform_handles_array=waveform_handles_array, loop_counts_array=loop_counts_array, sample_counts_array=sample_counts_array, marker_location_array=marker_location_array),
        )
        return response.coerced_markers_array, response.sequence_handle

    def create_arb_sequence(self, waveform_handles_array, loop_counts_array):  # noqa: N802
        response = self._invoke(
            self._client.CreateArbSequence,
            grpc_types.CreateArbSequenceRequest(vi=self._vi, waveform_handles_array=waveform_handles_array, loop_counts_array=loop_counts_array),
        )
        return response.sequence_handle

    def create_freq_list(self, waveform, frequency_array, duration_array):  # noqa: N802
        response = self._invoke(
            self._client.CreateFreqList,
            grpc_types.CreateFreqListRequest(vi=self._vi, waveform_raw=waveform.value, frequency_array=frequency_array, duration_array=duration_array),
        )
        return response.frequency_list_handle

    def create_waveform_f64(self, channel_name, waveform_data_array):  # noqa: N802
        response = self._invoke(
            self._client.CreateWaveformF64,
            grpc_types.CreateWaveformF64Request(vi=self._vi, channel_name=channel_name, waveform_data_array=waveform_data_array),
        )
        return response.waveform_handle

    def create_waveform_f64_numpy(self, channel_name, waveform_data_array):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def create_waveform_from_file_f64(self, channel_name, file_name, byte_order):  # noqa: N802
        response = self._invoke(
            self._client.CreateWaveformFromFileF64,
            grpc_types.CreateWaveformFromFileF64Request(vi=self._vi, channel_name=channel_name, file_name=file_name, byte_order_raw=byte_order.value),
        )
        return response.waveform_handle

    def create_waveform_from_file_i16(self, channel_name, file_name, byte_order):  # noqa: N802
        response = self._invoke(
            self._client.CreateWaveformFromFileI16,
            grpc_types.CreateWaveformFromFileI16Request(vi=self._vi, channel_name=channel_name, file_name=file_name, byte_order_raw=byte_order.value),
        )
        return response.waveform_handle

    def create_waveform_i16_numpy(self, channel_name, waveform_data_array):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def define_user_standard_waveform(self, channel_name, waveform_data_array):  # noqa: N802
        self._invoke(
            self._client.DefineUserStandardWaveform,
            grpc_types.DefineUserStandardWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_data_array=waveform_data_array),
        )

    def delete_named_waveform(self, channel_name, waveform_name):  # noqa: N802
        self._invoke(
            self._client.DeleteNamedWaveform,
            grpc_types.DeleteNamedWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_name=waveform_name),
        )

    def delete_script(self, channel_name, script_name):  # noqa: N802
        self._invoke(
            self._client.DeleteScript,
            grpc_types.DeleteScriptRequest(vi=self._vi, channel_name=channel_name, script_name=script_name),
        )

    def disable(self):  # noqa: N802
        self._invoke(
            self._client.Disable,
            grpc_types.DisableRequest(vi=self._vi),
        )

    def export_attribute_configuration_buffer(self):  # noqa: N802
        response = self._invoke(
            self._client.ExportAttributeConfigurationBuffer,
            grpc_types.ExportAttributeConfigurationBufferRequest(vi=self._vi),
        )
        return response.configuration

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        self._invoke(
            self._client.ExportAttributeConfigurationFile,
            grpc_types.ExportAttributeConfigurationFileRequest(vi=self._vi, file_path=file_path),
        )

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViBoolean,
            grpc_types.GetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViInt32,
            grpc_types.GetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViReal64,
            grpc_types.GetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        response = self._invoke(
            self._client.GetAttributeViString,
            grpc_types.GetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id),
        )
        return response.attribute_value

    def get_channel_name(self, index):  # noqa: N802
        response = self._invoke(
            self._client.GetChannelName,
            grpc_types.GetChannelNameRequest(vi=self._vi, index=index),
        )
        return response.channel_string

    def get_error(self):  # noqa: N802
        response = self._invoke(
            self._client.GetError,
            grpc_types.GetErrorRequest(vi=self._vi),
        )
        return response.error_code, response.error_description

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastDateAndTime,
            grpc_types.GetExtCalLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_ext_cal_last_temp(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalLastTemp,
            grpc_types.GetExtCalLastTempRequest(vi=self._vi),
        )
        return response.temperature

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        response = self._invoke(
            self._client.GetExtCalRecommendedInterval,
            grpc_types.GetExtCalRecommendedIntervalRequest(vi=self._vi),
        )
        return response.months

    def get_hardware_state(self):  # noqa: N802
        response = self._invoke(
            self._client.GetHardwareState,
            grpc_types.GetHardwareStateRequest(vi=self._vi),
        )
        return enums.HardwareState(response.state_raw)

    def get_self_cal_last_date_and_time(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastDateAndTime,
            grpc_types.GetSelfCalLastDateAndTimeRequest(vi=self._vi),
        )
        return response.year, response.month, response.day, response.hour, response.minute

    def get_self_cal_last_temp(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalLastTemp,
            grpc_types.GetSelfCalLastTempRequest(vi=self._vi),
        )
        return response.temperature

    def get_self_cal_supported(self):  # noqa: N802
        response = self._invoke(
            self._client.GetSelfCalSupported,
            grpc_types.GetSelfCalSupportedRequest(vi=self._vi),
        )
        return response.self_cal_supported

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationBuffer,
            grpc_types.ImportAttributeConfigurationBufferRequest(vi=self._vi, configuration=configuration),
        )

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        self._invoke(
            self._client.ImportAttributeConfigurationFile,
            grpc_types.ImportAttributeConfigurationFileRequest(vi=self._vi, file_path=file_path),
        )

    def initialize_with_channels(self, resource_name, channel_name, reset_device, option_string):  # noqa: N802
        metadata = (
            ('ni-api-key', self._grpc_options.api_key),
        )
        response = self._invoke(
            self._client.InitializeWithChannels,
            grpc_types.InitializeWithChannelsRequest(resource_name=resource_name, channel_name=channel_name, reset_device=reset_device, option_string=option_string, session_name=self._grpc_options.session_name, initialization_behavior=self._grpc_options.initialization_behavior),
            metadata=metadata,
        )
        self._close_on_exit = response.new_session_initialized
        return response.vi

    def initiate_generation(self):  # noqa: N802
        self._invoke(
            self._client.InitiateGeneration,
            grpc_types.InitiateGenerationRequest(vi=self._vi),
        )

    def is_done(self):  # noqa: N802
        response = self._invoke(
            self._client.IsDone,
            grpc_types.IsDoneRequest(vi=self._vi),
        )
        return response.done

    def lock(self):  # noqa: N802
        self._lock.acquire()

    def query_arb_seq_capabilities(self):  # noqa: N802
        response = self._invoke(
            self._client.QueryArbSeqCapabilities,
            grpc_types.QueryArbSeqCapabilitiesRequest(vi=self._vi),
        )
        return response.maximum_number_of_sequences, response.minimum_sequence_length, response.maximum_sequence_length, response.maximum_loop_count

    def query_arb_wfm_capabilities(self):  # noqa: N802
        response = self._invoke(
            self._client.QueryArbWfmCapabilities,
            grpc_types.QueryArbWfmCapabilitiesRequest(vi=self._vi),
        )
        return response.maximum_number_of_waveforms, response.waveform_quantum, response.minimum_waveform_size, response.maximum_waveform_size

    def query_freq_list_capabilities(self):  # noqa: N802
        response = self._invoke(
            self._client.QueryFreqListCapabilities,
            grpc_types.QueryFreqListCapabilitiesRequest(vi=self._vi),
        )
        return response.maximum_number_of_freq_lists, response.minimum_frequency_list_length, response.maximum_frequency_list_length, response.minimum_frequency_list_duration, response.maximum_frequency_list_duration, response.frequency_list_duration_quantum

    def read_current_temperature(self):  # noqa: N802
        response = self._invoke(
            self._client.ReadCurrentTemperature,
            grpc_types.ReadCurrentTemperatureRequest(vi=self._vi),
        )
        return response.temperature

    def reset_device(self):  # noqa: N802
        self._invoke(
            self._client.ResetDevice,
            grpc_types.ResetDeviceRequest(vi=self._vi),
        )

    def reset_with_defaults(self):  # noqa: N802
        self._invoke(
            self._client.ResetWithDefaults,
            grpc_types.ResetWithDefaultsRequest(vi=self._vi),
        )

    def self_cal(self):  # noqa: N802
        self._invoke(
            self._client.SelfCal,
            grpc_types.SelfCalRequest(vi=self._vi),
        )

    def send_software_edge_trigger(self, trigger, trigger_id):  # noqa: N802
        self._invoke(
            self._client.SendSoftwareEdgeTrigger,
            grpc_types.SendSoftwareEdgeTriggerRequest(vi=self._vi, trigger_raw=trigger.value, trigger_id=trigger_id),
        )

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViBoolean,
            grpc_types.SetAttributeViBooleanRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value=attribute_value),
        )

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViInt32,
            grpc_types.SetAttributeViInt32Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViReal64,
            grpc_types.SetAttributeViReal64Request(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        self._invoke(
            self._client.SetAttributeViString,
            grpc_types.SetAttributeViStringRequest(vi=self._vi, channel_name=channel_name, attribute_id=attribute_id, attribute_value_raw=attribute_value),
        )

    def set_named_waveform_next_write_position(self, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        self._invoke(
            self._client.SetNamedWaveformNextWritePosition,
            grpc_types.SetNamedWaveformNextWritePositionRequest(vi=self._vi, channel_name=channel_name, waveform_name=waveform_name, relative_to_raw=relative_to.value, offset=offset),
        )

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        raise NotImplementedError('set_runtime_environment is not supported over gRPC')

    def set_waveform_next_write_position(self, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        self._invoke(
            self._client.SetWaveformNextWritePosition,
            grpc_types.SetWaveformNextWritePositionRequest(vi=self._vi, channel_name=channel_name, waveform_handle=waveform_handle, relative_to_raw=relative_to.value, offset=offset),
        )

    def unlock(self):  # noqa: N802
        self._lock.release()

    def wait_until_done(self, max_time):  # noqa: N802
        self._invoke(
            self._client.WaitUntilDone,
            grpc_types.WaitUntilDoneRequest(vi=self._vi, max_time=max_time),
        )

    def write_binary16_waveform_numpy(self, channel_name, waveform_handle, data):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def write_named_waveform_f64(self, channel_name, waveform_name, data):  # noqa: N802
        self._invoke(
            self._client.WriteNamedWaveformF64,
            grpc_types.WriteNamedWaveformF64Request(vi=self._vi, channel_name=channel_name, waveform_name=waveform_name, data=data),
        )

    def write_named_waveform_f64_numpy(self, channel_name, waveform_name, data):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def write_named_waveform_i16_numpy(self, channel_name, waveform_name, data):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def write_script(self, channel_name, script):  # noqa: N802
        self._invoke(
            self._client.WriteScript,
            grpc_types.WriteScriptRequest(vi=self._vi, channel_name=channel_name, script=script),
        )

    def write_waveform(self, channel_name, waveform_handle, data):  # noqa: N802
        self._invoke(
            self._client.WriteWaveform,
            grpc_types.WriteWaveformRequest(vi=self._vi, channel_name=channel_name, waveform_handle=waveform_handle, data=data),
        )

    def write_waveform_numpy(self, channel_name, waveform_handle, data):  # noqa: N802
        raise NotImplementedError('numpy-specific methods are not supported over gRPC')

    def close(self):  # noqa: N802
        self._invoke(
            self._client.Close,
            grpc_types.CloseRequest(vi=self._vi),
        )

    def error_message(self, error_code):  # noqa: N802
        response = self._invoke(
            self._client.ErrorMessage,
            grpc_types.ErrorMessageRequest(vi=self._vi, error_code=error_code),
        )
        return response.error_message

    def reset(self):  # noqa: N802
        self._invoke(
            self._client.Reset,
            grpc_types.ResetRequest(vi=self._vi),
        )

    def self_test(self):  # noqa: N802
        response = self._invoke(
            self._client.SelfTest,
            grpc_types.SelfTestRequest(vi=self._vi),
        )
        return response.self_test_result, response.self_test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/_library.py sha256=e6e64d4d13c45e9fc6254c93db351593a615f57516d2e863b9918c3d0e37fbef bytes=48679 -->
## FILE: generated/nifgen/nifgen/_library.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/_library.py`
- sha256: `e6e64d4d13c45e9fc6254c93db351593a615f57516d2e863b9918c3d0e37fbef`
- bytes: 48679

````python
# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nifgen.errors as errors
import threading

from nifgen._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niFgen_AbortGeneration_cfunc = None
        self.niFgen_AllocateNamedWaveform_cfunc = None
        self.niFgen_AllocateWaveform_cfunc = None
        self.niFgen_ClearArbMemory_cfunc = None
        self.niFgen_ClearArbSequence_cfunc = None
        self.niFgen_ClearArbWaveform_cfunc = None
        self.niFgen_ClearFreqList_cfunc = None
        self.niFgen_ClearUserStandardWaveform_cfunc = None
        self.niFgen_Commit_cfunc = None
        self.niFgen_ConfigureArbSequence_cfunc = None
        self.niFgen_ConfigureArbWaveform_cfunc = None
        self.niFgen_ConfigureFreqList_cfunc = None
        self.niFgen_ConfigureStandardWaveform_cfunc = None
        self.niFgen_CreateAdvancedArbSequence_cfunc = None
        self.niFgen_CreateArbSequence_cfunc = None
        self.niFgen_CreateFreqList_cfunc = None
        self.niFgen_CreateWaveformF64_cfunc = None
        self.niFgen_CreateWaveformFromFileF64_cfunc = None
        self.niFgen_CreateWaveformFromFileI16_cfunc = None
        self.niFgen_CreateWaveformI16_cfunc = None
        self.niFgen_DefineUserStandardWaveform_cfunc = None
        self.niFgen_DeleteNamedWaveform_cfunc = None
        self.niFgen_DeleteScript_cfunc = None
        self.niFgen_Disable_cfunc = None
        self.niFgen_ExportAttributeConfigurationBuffer_cfunc = None
        self.niFgen_ExportAttributeConfigurationFile_cfunc = None
        self.niFgen_GetAttributeViBoolean_cfunc = None
        self.niFgen_GetAttributeViInt32_cfunc = None
        self.niFgen_GetAttributeViReal64_cfunc = None
        self.niFgen_GetAttributeViString_cfunc = None
        self.niFgen_GetChannelName_cfunc = None
        self.niFgen_GetError_cfunc = None
        self.niFgen_GetExtCalLastDateAndTime_cfunc = None
        self.niFgen_GetExtCalLastTemp_cfunc = None
        self.niFgen_GetExtCalRecommendedInterval_cfunc = None
        self.niFgen_GetHardwareState_cfunc = None
        self.niFgen_GetSelfCalLastDateAndTime_cfunc = None
        self.niFgen_GetSelfCalLastTemp_cfunc = None
        self.niFgen_GetSelfCalSupported_cfunc = None
        self.niFgen_ImportAttributeConfigurationBuffer_cfunc = None
        self.niFgen_ImportAttributeConfigurationFile_cfunc = None
        self.niFgen_InitializeWithChannels_cfunc = None
        self.niFgen_InitiateGeneration_cfunc = None
        self.niFgen_IsDone_cfunc = None
        self.niFgen_LockSession_cfunc = None
        self.niFgen_QueryArbSeqCapabilities_cfunc = None
        self.niFgen_QueryArbWfmCapabilities_cfunc = None
        self.niFgen_QueryFreqListCapabilities_cfunc = None
        self.niFgen_ReadCurrentTemperature_cfunc = None
        self.niFgen_ResetDevice_cfunc = None
        self.niFgen_ResetWithDefaults_cfunc = None
        self.niFgen_SelfCal_cfunc = None
        self.niFgen_SendSoftwareEdgeTrigger_cfunc = None
        self.niFgen_SetAttributeViBoolean_cfunc = None
        self.niFgen_SetAttributeViInt32_cfunc = None
        self.niFgen_SetAttributeViReal64_cfunc = None
        self.niFgen_SetAttributeViString_cfunc = None
        self.niFgen_SetNamedWaveformNextWritePosition_cfunc = None
        self.niFgen_SetRuntimeEnvironment_cfunc = None
        self.niFgen_SetWaveformNextWritePosition_cfunc = None
        self.niFgen_UnlockSession_cfunc = None
        self.niFgen_WaitUntilDone_cfunc = None
        self.niFgen_WriteBinary16Waveform_cfunc = None
        self.niFgen_WriteNamedWaveformF64_cfunc = None
        self.niFgen_WriteNamedWaveformI16_cfunc = None
        self.niFgen_WriteScript_cfunc = None
        self.niFgen_WriteWaveform_cfunc = None
        self.niFgen_close_cfunc = None
        self.niFgen_error_message_cfunc = None
        self.niFgen_reset_cfunc = None
        self.niFgen_self_test_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niFgen_AbortGeneration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AbortGeneration_cfunc is None:
                self.niFgen_AbortGeneration_cfunc = self._get_library_function('niFgen_AbortGeneration')
                self.niFgen_AbortGeneration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_AbortGeneration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AbortGeneration_cfunc(vi)

    def niFgen_AllocateNamedWaveform(self, vi, channel_name, waveform_name, waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AllocateNamedWaveform_cfunc is None:
                self.niFgen_AllocateNamedWaveform_cfunc = self._get_library_function('niFgen_AllocateNamedWaveform')
                self.niFgen_AllocateNamedWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32]  # noqa: F405
                self.niFgen_AllocateNamedWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AllocateNamedWaveform_cfunc(vi, channel_name, waveform_name, waveform_size)

    def niFgen_AllocateWaveform(self, vi, channel_name, waveform_size, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_AllocateWaveform_cfunc is None:
                self.niFgen_AllocateWaveform_cfunc = self._get_library_function('niFgen_AllocateWaveform')
                self.niFgen_AllocateWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_AllocateWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_AllocateWaveform_cfunc(vi, channel_name, waveform_size, waveform_handle)

    def niFgen_ClearArbMemory(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbMemory_cfunc is None:
                self.niFgen_ClearArbMemory_cfunc = self._get_library_function('niFgen_ClearArbMemory')
                self.niFgen_ClearArbMemory_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ClearArbMemory_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbMemory_cfunc(vi)

    def niFgen_ClearArbSequence(self, vi, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbSequence_cfunc is None:
                self.niFgen_ClearArbSequence_cfunc = self._get_library_function('niFgen_ClearArbSequence')
                self.niFgen_ClearArbSequence_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbSequence_cfunc(vi, sequence_handle)

    def niFgen_ClearArbWaveform(self, vi, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearArbWaveform_cfunc is None:
                self.niFgen_ClearArbWaveform_cfunc = self._get_library_function('niFgen_ClearArbWaveform')
                self.niFgen_ClearArbWaveform_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearArbWaveform_cfunc(vi, waveform_handle)

    def niFgen_ClearFreqList(self, vi, frequency_list_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearFreqList_cfunc is None:
                self.niFgen_ClearFreqList_cfunc = self._get_library_function('niFgen_ClearFreqList')
                self.niFgen_ClearFreqList_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_ClearFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearFreqList_cfunc(vi, frequency_list_handle)

    def niFgen_ClearUserStandardWaveform(self, vi, channel_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ClearUserStandardWaveform_cfunc is None:
                self.niFgen_ClearUserStandardWaveform_cfunc = self._get_library_function('niFgen_ClearUserStandardWaveform')
                self.niFgen_ClearUserStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ClearUserStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ClearUserStandardWaveform_cfunc(vi, channel_name)

    def niFgen_Commit(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_Commit_cfunc is None:
                self.niFgen_Commit_cfunc = self._get_library_function('niFgen_Commit')
                self.niFgen_Commit_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_Commit_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_Commit_cfunc(vi)

    def niFgen_ConfigureArbSequence(self, vi, channel_name, sequence_handle, gain, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureArbSequence_cfunc is None:
                self.niFgen_ConfigureArbSequence_cfunc = self._get_library_function('niFgen_ConfigureArbSequence')
                self.niFgen_ConfigureArbSequence_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureArbSequence_cfunc(vi, channel_name, sequence_handle, gain, offset)

    def niFgen_ConfigureArbWaveform(self, vi, channel_name, waveform_handle, gain, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureArbWaveform_cfunc is None:
                self.niFgen_ConfigureArbWaveform_cfunc = self._get_library_function('niFgen_ConfigureArbWaveform')
                self.niFgen_ConfigureArbWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureArbWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureArbWaveform_cfunc(vi, channel_name, waveform_handle, gain, offset)

    def niFgen_ConfigureFreqList(self, vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureFreqList_cfunc is None:
                self.niFgen_ConfigureFreqList_cfunc = self._get_library_function('niFgen_ConfigureFreqList')
                self.niFgen_ConfigureFreqList_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureFreqList_cfunc(vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase)

    def niFgen_ConfigureStandardWaveform(self, vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ConfigureStandardWaveform_cfunc is None:
                self.niFgen_ConfigureStandardWaveform_cfunc = self._get_library_function('niFgen_ConfigureStandardWaveform')
                self.niFgen_ConfigureStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViReal64, ViReal64, ViReal64, ViReal64]  # noqa: F405
                self.niFgen_ConfigureStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ConfigureStandardWaveform_cfunc(vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase)

    def niFgen_CreateAdvancedArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateAdvancedArbSequence_cfunc is None:
                self.niFgen_CreateAdvancedArbSequence_cfunc = self._get_library_function('niFgen_CreateAdvancedArbSequence')
                self.niFgen_CreateAdvancedArbSequence_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateAdvancedArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateAdvancedArbSequence_cfunc(vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle)

    def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateArbSequence_cfunc is None:
                self.niFgen_CreateArbSequence_cfunc = self._get_library_function('niFgen_CreateArbSequence')
                self.niFgen_CreateArbSequence_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateArbSequence_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateArbSequence_cfunc(vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle)

    def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateFreqList_cfunc is None:
                self.niFgen_CreateFreqList_cfunc = self._get_library_function('niFgen_CreateFreqList')
                self.niFgen_CreateFreqList_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateFreqList_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateFreqList_cfunc(vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle)

    def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformF64_cfunc is None:
                self.niFgen_CreateWaveformF64_cfunc = self._get_library_function('niFgen_CreateWaveformF64')
                self.niFgen_CreateWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformF64_cfunc(vi, channel_name, waveform_size, waveform_data_array, waveform_handle)

    def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileF64_cfunc is None:
                self.niFgen_CreateWaveformFromFileF64_cfunc = self._get_library_function('niFgen_CreateWaveformFromFileF64')
                self.niFgen_CreateWaveformFromFileF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformFromFileF64_cfunc(vi, channel_name, file_name, byte_order, waveform_handle)

    def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformFromFileI16_cfunc is None:
                self.niFgen_CreateWaveformFromFileI16_cfunc = self._get_library_function('niFgen_CreateWaveformFromFileI16')
                self.niFgen_CreateWaveformFromFileI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformFromFileI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformFromFileI16_cfunc(vi, channel_name, file_name, byte_order, waveform_handle)

    def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        with self._func_lock:
            if self.niFgen_CreateWaveformI16_cfunc is None:
                self.niFgen_CreateWaveformI16_cfunc = self._get_library_function('niFgen_CreateWaveformI16')
                self.niFgen_CreateWaveformI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_CreateWaveformI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_CreateWaveformI16_cfunc(vi, channel_name, waveform_size, waveform_data_array, waveform_handle)

    def niFgen_DefineUserStandardWaveform(self, vi, channel_name, waveform_size, waveform_data_array):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DefineUserStandardWaveform_cfunc is None:
                self.niFgen_DefineUserStandardWaveform_cfunc = self._get_library_function('niFgen_DefineUserStandardWaveform')
                self.niFgen_DefineUserStandardWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_DefineUserStandardWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DefineUserStandardWaveform_cfunc(vi, channel_name, waveform_size, waveform_data_array)

    def niFgen_DeleteNamedWaveform(self, vi, channel_name, waveform_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DeleteNamedWaveform_cfunc is None:
                self.niFgen_DeleteNamedWaveform_cfunc = self._get_library_function('niFgen_DeleteNamedWaveform')
                self.niFgen_DeleteNamedWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DeleteNamedWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DeleteNamedWaveform_cfunc(vi, channel_name, waveform_name)

    def niFgen_DeleteScript(self, vi, channel_name, script_name):  # noqa: N802
        with self._func_lock:
            if self.niFgen_DeleteScript_cfunc is None:
                self.niFgen_DeleteScript_cfunc = self._get_library_function('niFgen_DeleteScript')
                self.niFgen_DeleteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_DeleteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_DeleteScript_cfunc(vi, channel_name, script_name)

    def niFgen_Disable(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_Disable_cfunc is None:
                self.niFgen_Disable_cfunc = self._get_library_function('niFgen_Disable')
                self.niFgen_Disable_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_Disable_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_Disable_cfunc(vi)

    def niFgen_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ExportAttributeConfigurationBuffer_cfunc is None:
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFgen_ExportAttributeConfigurationBuffer')
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFgen_ExportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ExportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niFgen_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ExportAttributeConfigurationFile_cfunc is None:
                self.niFgen_ExportAttributeConfigurationFile_cfunc = self._get_library_function('niFgen_ExportAttributeConfigurationFile')
                self.niFgen_ExportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ExportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ExportAttributeConfigurationFile_cfunc(vi, file_path)

    def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViBoolean_cfunc is None:
                self.niFgen_GetAttributeViBoolean_cfunc = self._get_library_function('niFgen_GetAttributeViBoolean')
                self.niFgen_GetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_GetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViInt32_cfunc is None:
                self.niFgen_GetAttributeViInt32_cfunc = self._get_library_function('niFgen_GetAttributeViInt32')
                self.niFgen_GetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViReal64_cfunc is None:
                self.niFgen_GetAttributeViReal64_cfunc = self._get_library_function('niFgen_GetAttributeViReal64')
                self.niFgen_GetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetAttributeViString_cfunc is None:
                self.niFgen_GetAttributeViString_cfunc = self._get_library_function('niFgen_GetAttributeViString')
                self.niFgen_GetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetAttributeViString_cfunc(vi, channel_name, attribute_id, array_size, attribute_value)

    def niFgen_GetChannelName(self, vi, index, buffer_size, channel_string):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetChannelName_cfunc is None:
                self.niFgen_GetChannelName_cfunc = self._get_library_function('niFgen_GetChannelName')
                self.niFgen_GetChannelName_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetChannelName_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetChannelName_cfunc(vi, index, buffer_size, channel_string)

    def niFgen_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetError_cfunc is None:
                self.niFgen_GetError_cfunc = self._get_library_function('niFgen_GetError')
                self.niFgen_GetError_cfunc.argtypes = [ViSession, ctypes.POINTER(ViStatus), ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_GetError_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetError_cfunc(vi, error_code, error_description_buffer_size, error_description)

    def niFgen_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetExtCalLastDateAndTime_cfunc is None:
                self.niFgen_GetExtCalLastDateAndTime_cfunc = self._get_library_function('niFgen_GetExtCalLastDateAndTime')
                self.niFgen_GetExtCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetExtCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetExtCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niFgen_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetExtCalLastTemp_cfunc is None:
                self.niFgen_GetExtCalLastTemp_cfunc = self._get_library_function('niFgen_GetExtCalLastTemp')
                self.niFgen_GetExtCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetExtCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetExtCalLastTemp_cfunc(vi, temperature)

    def niFgen_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetExtCalRecommendedInterval_cfunc is None:
                self.niFgen_GetExtCalRecommendedInterval_cfunc = self._get_library_function('niFgen_GetExtCalRecommendedInterval')
                self.niFgen_GetExtCalRecommendedInterval_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetExtCalRecommendedInterval_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetExtCalRecommendedInterval_cfunc(vi, months)

    def niFgen_GetHardwareState(self, vi, state):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetHardwareState_cfunc is None:
                self.niFgen_GetHardwareState_cfunc = self._get_library_function('niFgen_GetHardwareState')
                self.niFgen_GetHardwareState_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetHardwareState_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetHardwareState_cfunc(vi, state)

    def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalLastDateAndTime_cfunc is None:
                self.niFgen_GetSelfCalLastDateAndTime_cfunc = self._get_library_function('niFgen_GetSelfCalLastDateAndTime')
                self.niFgen_GetSelfCalLastDateAndTime_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_GetSelfCalLastDateAndTime_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalLastDateAndTime_cfunc(vi, year, month, day, hour, minute)

    def niFgen_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalLastTemp_cfunc is None:
                self.niFgen_GetSelfCalLastTemp_cfunc = self._get_library_function('niFgen_GetSelfCalLastTemp')
                self.niFgen_GetSelfCalLastTemp_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_GetSelfCalLastTemp_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalLastTemp_cfunc(vi, temperature)

    def niFgen_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        with self._func_lock:
            if self.niFgen_GetSelfCalSupported_cfunc is None:
                self.niFgen_GetSelfCalSupported_cfunc = self._get_library_function('niFgen_GetSelfCalSupported')
                self.niFgen_GetSelfCalSupported_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_GetSelfCalSupported_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_GetSelfCalSupported_cfunc(vi, self_cal_supported)

    def niFgen_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ImportAttributeConfigurationBuffer_cfunc is None:
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc = self._get_library_function('niFgen_ImportAttributeConfigurationBuffer')
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViInt8)]  # noqa: F405
                self.niFgen_ImportAttributeConfigurationBuffer_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ImportAttributeConfigurationBuffer_cfunc(vi, size_in_bytes, configuration)

    def niFgen_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ImportAttributeConfigurationFile_cfunc is None:
                self.niFgen_ImportAttributeConfigurationFile_cfunc = self._get_library_function('niFgen_ImportAttributeConfigurationFile')
                self.niFgen_ImportAttributeConfigurationFile_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_ImportAttributeConfigurationFile_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ImportAttributeConfigurationFile_cfunc(vi, file_path)

    def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitializeWithChannels_cfunc is None:
                self.niFgen_InitializeWithChannels_cfunc = self._get_library_function('niFgen_InitializeWithChannels')
                self.niFgen_InitializeWithChannels_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViBoolean, ctypes.POINTER(ViChar), ctypes.POINTER(ViSession)]  # noqa: F405
                self.niFgen_InitializeWithChannels_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitializeWithChannels_cfunc(resource_name, channel_name, reset_device, option_string, vi)

    def niFgen_InitiateGeneration(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_InitiateGeneration_cfunc is None:
                self.niFgen_InitiateGeneration_cfunc = self._get_library_function('niFgen_InitiateGeneration')
                self.niFgen_InitiateGeneration_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_InitiateGeneration_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_InitiateGeneration_cfunc(vi)

    def niFgen_IsDone(self, vi, done):  # noqa: N802
        with self._func_lock:
            if self.niFgen_IsDone_cfunc is None:
                self.niFgen_IsDone_cfunc = self._get_library_function('niFgen_IsDone')
                self.niFgen_IsDone_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_IsDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_IsDone_cfunc(vi, done)

    def niFgen_LockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niFgen_LockSession_cfunc is None:
                self.niFgen_LockSession_cfunc = self._get_library_function('niFgen_LockSession')
                self.niFgen_LockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_LockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_LockSession_cfunc(vi, caller_has_lock)

    def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryArbSeqCapabilities_cfunc is None:
                self.niFgen_QueryArbSeqCapabilities_cfunc = self._get_library_function('niFgen_QueryArbSeqCapabilities')
                self.niFgen_QueryArbSeqCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_QueryArbSeqCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryArbSeqCapabilities_cfunc(vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count)

    def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryArbWfmCapabilities_cfunc is None:
                self.niFgen_QueryArbWfmCapabilities_cfunc = self._get_library_function('niFgen_QueryArbWfmCapabilities')
                self.niFgen_QueryArbWfmCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niFgen_QueryArbWfmCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryArbWfmCapabilities_cfunc(vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size)

    def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum):  # noqa: N802
        with self._func_lock:
            if self.niFgen_QueryFreqListCapabilities_cfunc is None:
                self.niFgen_QueryFreqListCapabilities_cfunc = self._get_library_function('niFgen_QueryFreqListCapabilities')
                self.niFgen_QueryFreqListCapabilities_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViInt32), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64), ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_QueryFreqListCapabilities_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_QueryFreqListCapabilities_cfunc(vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum)

    def niFgen_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ReadCurrentTemperature_cfunc is None:
                self.niFgen_ReadCurrentTemperature_cfunc = self._get_library_function('niFgen_ReadCurrentTemperature')
                self.niFgen_ReadCurrentTemperature_cfunc.argtypes = [ViSession, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_ReadCurrentTemperature_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ReadCurrentTemperature_cfunc(vi, temperature)

    def niFgen_ResetDevice(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ResetDevice_cfunc is None:
                self.niFgen_ResetDevice_cfunc = self._get_library_function('niFgen_ResetDevice')
                self.niFgen_ResetDevice_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ResetDevice_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ResetDevice_cfunc(vi)

    def niFgen_ResetWithDefaults(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_ResetWithDefaults_cfunc is None:
                self.niFgen_ResetWithDefaults_cfunc = self._get_library_function('niFgen_ResetWithDefaults')
                self.niFgen_ResetWithDefaults_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_ResetWithDefaults_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_ResetWithDefaults_cfunc(vi)

    def niFgen_SelfCal(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SelfCal_cfunc is None:
                self.niFgen_SelfCal_cfunc = self._get_library_function('niFgen_SelfCal')
                self.niFgen_SelfCal_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_SelfCal_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SelfCal_cfunc(vi)

    def niFgen_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_id):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SendSoftwareEdgeTrigger_cfunc is None:
                self.niFgen_SendSoftwareEdgeTrigger_cfunc = self._get_library_function('niFgen_SendSoftwareEdgeTrigger')
                self.niFgen_SendSoftwareEdgeTrigger_cfunc.argtypes = [ViSession, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SendSoftwareEdgeTrigger_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SendSoftwareEdgeTrigger_cfunc(vi, trigger, trigger_id)

    def niFgen_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViBoolean_cfunc is None:
                self.niFgen_SetAttributeViBoolean_cfunc = self._get_library_function('niFgen_SetAttributeViBoolean')
                self.niFgen_SetAttributeViBoolean_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViBoolean]  # noqa: F405
                self.niFgen_SetAttributeViBoolean_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViBoolean_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViInt32_cfunc is None:
                self.niFgen_SetAttributeViInt32_cfunc = self._get_library_function('niFgen_SetAttributeViInt32')
                self.niFgen_SetAttributeViInt32_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViInt32]  # noqa: F405
                self.niFgen_SetAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViInt32_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViReal64_cfunc is None:
                self.niFgen_SetAttributeViReal64_cfunc = self._get_library_function('niFgen_SetAttributeViReal64')
                self.niFgen_SetAttributeViReal64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ViReal64]  # noqa: F405
                self.niFgen_SetAttributeViReal64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViReal64_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetAttributeViString_cfunc is None:
                self.niFgen_SetAttributeViString_cfunc = self._get_library_function('niFgen_SetAttributeViString')
                self.niFgen_SetAttributeViString_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViAttr, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SetAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetAttributeViString_cfunc(vi, channel_name, attribute_id, attribute_value)

    def niFgen_SetNamedWaveformNextWritePosition(self, vi, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetNamedWaveformNextWritePosition_cfunc is None:
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc = self._get_library_function('niFgen_SetNamedWaveformNextWritePosition')
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ViInt32]  # noqa: F405
                self.niFgen_SetNamedWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetNamedWaveformNextWritePosition_cfunc(vi, channel_name, waveform_name, relative_to, offset)

    def niFgen_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetRuntimeEnvironment_cfunc is None:
                self.niFgen_SetRuntimeEnvironment_cfunc = self._get_library_function('niFgen_SetRuntimeEnvironment')
                self.niFgen_SetRuntimeEnvironment_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_SetRuntimeEnvironment_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetRuntimeEnvironment_cfunc(environment, environment_version, reserved1, reserved2)

    def niFgen_SetWaveformNextWritePosition(self, vi, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        with self._func_lock:
            if self.niFgen_SetWaveformNextWritePosition_cfunc is None:
                self.niFgen_SetWaveformNextWritePosition_cfunc = self._get_library_function('niFgen_SetWaveformNextWritePosition')
                self.niFgen_SetWaveformNextWritePosition_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ViInt32]  # noqa: F405
                self.niFgen_SetWaveformNextWritePosition_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_SetWaveformNextWritePosition_cfunc(vi, channel_name, waveform_handle, relative_to, offset)

    def niFgen_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        with self._func_lock:
            if self.niFgen_UnlockSession_cfunc is None:
                self.niFgen_UnlockSession_cfunc = self._get_library_function('niFgen_UnlockSession')
                self.niFgen_UnlockSession_cfunc.argtypes = [ViSession, ctypes.POINTER(ViBoolean)]  # noqa: F405
                self.niFgen_UnlockSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_UnlockSession_cfunc(vi, caller_has_lock)

    def niFgen_WaitUntilDone(self, vi, max_time):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WaitUntilDone_cfunc is None:
                self.niFgen_WaitUntilDone_cfunc = self._get_library_function('niFgen_WaitUntilDone')
                self.niFgen_WaitUntilDone_cfunc.argtypes = [ViSession, ViInt32]  # noqa: F405
                self.niFgen_WaitUntilDone_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WaitUntilDone_cfunc(vi, max_time)

    def niFgen_WriteBinary16Waveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteBinary16Waveform_cfunc is None:
                self.niFgen_WriteBinary16Waveform_cfunc = self._get_library_function('niFgen_WriteBinary16Waveform')
                self.niFgen_WriteBinary16Waveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteBinary16Waveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteBinary16Waveform_cfunc(vi, channel_name, waveform_handle, size, data)

    def niFgen_WriteNamedWaveformF64(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformF64_cfunc is None:
                self.niFgen_WriteNamedWaveformF64_cfunc = self._get_library_function('niFgen_WriteNamedWaveformF64')
                self.niFgen_WriteNamedWaveformF64_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteNamedWaveformF64_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteNamedWaveformF64_cfunc(vi, channel_name, waveform_name, size, data)

    def niFgen_WriteNamedWaveformI16(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteNamedWaveformI16_cfunc is None:
                self.niFgen_WriteNamedWaveformI16_cfunc = self._get_library_function('niFgen_WriteNamedWaveformI16')
                self.niFgen_WriteNamedWaveformI16_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar), ViInt32, ctypes.POINTER(ViInt16)]  # noqa: F405
                self.niFgen_WriteNamedWaveformI16_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteNamedWaveformI16_cfunc(vi, channel_name, waveform_name, size, data)

    def niFgen_WriteScript(self, vi, channel_name, script):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteScript_cfunc is None:
                self.niFgen_WriteScript_cfunc = self._get_library_function('niFgen_WriteScript')
                self.niFgen_WriteScript_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_WriteScript_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteScript_cfunc(vi, channel_name, script)

    def niFgen_WriteWaveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        with self._func_lock:
            if self.niFgen_WriteWaveform_cfunc is None:
                self.niFgen_WriteWaveform_cfunc = self._get_library_function('niFgen_WriteWaveform')
                self.niFgen_WriteWaveform_cfunc.argtypes = [ViSession, ctypes.POINTER(ViChar), ViInt32, ViInt32, ctypes.POINTER(ViReal64)]  # noqa: F405
                self.niFgen_WriteWaveform_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_WriteWaveform_cfunc(vi, channel_name, waveform_handle, size, data)

    def niFgen_close(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_close_cfunc is None:
                self.niFgen_close_cfunc = self._get_library_function('niFgen_close')
                self.niFgen_close_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_close_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_close_cfunc(vi)

    def niFgen_error_message(self, vi, error_code, error_message):  # noqa: N802
        with self._func_lock:
            if self.niFgen_error_message_cfunc is None:
                self.niFgen_error_message_cfunc = self._get_library_function('niFgen_error_message')
                self.niFgen_error_message_cfunc.argtypes = [ViSession, ViStatus, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_error_message_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_error_message_cfunc(vi, error_code, error_message)

    def niFgen_reset(self, vi):  # noqa: N802
        with self._func_lock:
            if self.niFgen_reset_cfunc is None:
                self.niFgen_reset_cfunc = self._get_library_function('niFgen_reset')
                self.niFgen_reset_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niFgen_reset_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_reset_cfunc(vi)

    def niFgen_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        with self._func_lock:
            if self.niFgen_self_test_cfunc is None:
                self.niFgen_self_test_cfunc = self._get_library_function('niFgen_self_test')
                self.niFgen_self_test_cfunc.argtypes = [ViSession, ctypes.POINTER(ViInt16), ctypes.POINTER(ViChar)]  # noqa: F405
                self.niFgen_self_test_cfunc.restype = ViStatus  # noqa: F405
        return self.niFgen_self_test_cfunc(vi, self_test_result, self_test_message)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/_library_interpreter.py sha256=e0c9c47f21f714d5623e5c463d7ef2835f4d5c0efdc6a911f97e5d6bf6b12a2e bytes=55293 -->
## FILE: generated/nifgen/nifgen/_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/_library_interpreter.py`
- sha256: `e0c9c47f21f714d5623e5c463d7ef2835f4d5c0efdc6a911f97e5d6bf6b12a2e`
- bytes: 55293

````python
# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import platform

import nifgen._library_singleton as _library_singleton
import nifgen._visatype as _visatype
import nifgen.enums as enums  # noqa: F401
import nifgen.errors as errors


_was_runtime_environment_set = None


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        global _was_runtime_environment_set
        if _was_runtime_environment_set is None:
            try:
                runtime_env = platform.python_implementation()
                version = platform.python_version()
                self.set_runtime_environment(
                    runtime_env,
                    version,
                    '',
                    ''
                )
            except errors.DriverTooOldError:
                pass
            finally:
                _was_runtime_environment_set = True
        # Initialize _vi to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._vi = value

    def get_session_handle(self):
        return self._vi

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        try:
            returned_error_code, error_string = self.get_error()
            if returned_error_code == error_code:
                return error_string
        except errors.Error:
            pass

        try:
            # get_error reads the session's error queue, which may have been overwritten,
            # causing it to return a mismatched error code. error_message takes the error
            # code directly as a parameter and looks up its description without reading the
            # queue, it will return the description for the specific error code.
            # Use error_message in current session before the handle reset in the next block.

            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass

        save_vi = self.get_session_handle()
        try:
            # It is expected for get_error to raise when the session is invalid
            # (IVI spec requires GetError to fail).
            # Use error_message instead. It doesn't require a session.

            self.set_session_handle()
            error_string = self.error_message(error_code)
            return error_string
        except errors.Error:
            pass
        finally:
            self.set_session_handle(save_vi)
        return "Failed to retrieve error description."

    def abort(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_AbortGeneration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_named_waveform(self, channel_name, waveform_name, waveform_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        waveform_size_ctype = _visatype.ViInt32(waveform_size)  # case S150
        error_code = self._library.niFgen_AllocateNamedWaveform(vi_ctype, channel_name_ctype, waveform_name_ctype, waveform_size_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def allocate_waveform(self, channel_name, waveform_size):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(waveform_size)  # case S150
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_AllocateWaveform(vi_ctype, channel_name_ctype, waveform_size_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def clear_arb_memory(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ClearArbMemory(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_sequence(self, sequence_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sequence_handle_ctype = _visatype.ViInt32(sequence_handle)  # case S150
        error_code = self._library.niFgen_ClearArbSequence(vi_ctype, sequence_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_arb_waveform(self, waveform_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        error_code = self._library.niFgen_ClearArbWaveform(vi_ctype, waveform_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_freq_list(self, frequency_list_handle):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        frequency_list_handle_ctype = _visatype.ViInt32(frequency_list_handle)  # case S150
        error_code = self._library.niFgen_ClearFreqList(vi_ctype, frequency_list_handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def clear_user_standard_waveform(self, channel_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        error_code = self._library.niFgen_ClearUserStandardWaveform(vi_ctype, channel_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def commit(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_Commit(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_sequence(self, channel_name, sequence_handle, gain, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        sequence_handle_ctype = _visatype.ViInt32(sequence_handle)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        error_code = self._library.niFgen_ConfigureArbSequence(vi_ctype, channel_name_ctype, sequence_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_arb_waveform(self, channel_name, waveform_handle, gain, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        gain_ctype = _visatype.ViReal64(gain)  # case S150
        offset_ctype = _visatype.ViReal64(offset)  # case S150
        error_code = self._library.niFgen_ConfigureArbWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, gain_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_freq_list(self, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        frequency_list_handle_ctype = _visatype.ViInt32(frequency_list_handle)  # case S150
        amplitude_ctype = _visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = _visatype.ViReal64(dc_offset)  # case S150
        start_phase_ctype = _visatype.ViReal64(start_phase)  # case S150
        error_code = self._library.niFgen_ConfigureFreqList(vi_ctype, channel_name_ctype, frequency_list_handle_ctype, amplitude_ctype, dc_offset_ctype, start_phase_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def configure_standard_waveform(self, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_ctype = _visatype.ViInt32(waveform.value)  # case S130
        amplitude_ctype = _visatype.ViReal64(amplitude)  # case S150
        dc_offset_ctype = _visatype.ViReal64(dc_offset)  # case S150
        frequency_ctype = _visatype.ViReal64(frequency)  # case S150
        start_phase_ctype = _visatype.ViReal64(start_phase)  # case S150
        error_code = self._library.niFgen_ConfigureStandardWaveform(vi_ctype, channel_name_ctype, waveform_ctype, amplitude_ctype, dc_offset_ctype, frequency_ctype, start_phase_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sequence_length_ctype = _visatype.ViInt32(0 if waveform_handles_array is None else len(waveform_handles_array))  # case S160
        waveform_handles_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_handles_array, library_type=_visatype.ViInt32)  # case B550
        loop_counts_array_ctype = _get_ctypes_pointer_for_buffer(value=loop_counts_array, library_type=_visatype.ViInt32)  # case B550
        sample_counts_array_ctype = _get_ctypes_pointer_for_buffer(value=sample_counts_array, library_type=_visatype.ViInt32)  # case B550
        marker_location_array_ctype = _get_ctypes_pointer_for_buffer(value=marker_location_array, library_type=_visatype.ViInt32)  # case B550
        coerced_markers_array_size = (0 if marker_location_array is None else len(marker_location_array))  # case B560
        coerced_markers_array_ctype = _get_ctypes_pointer_for_buffer(library_type=_visatype.ViInt32, size=coerced_markers_array_size)  # case B560
        sequence_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateAdvancedArbSequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, sample_counts_array_ctype, marker_location_array_ctype, coerced_markers_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return [int(coerced_markers_array_ctype[i]) for i in range((0 if marker_location_array is None else len(marker_location_array)))], int(sequence_handle_ctype.value)

    def create_arb_sequence(self, waveform_handles_array, loop_counts_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        sequence_length_ctype = _visatype.ViInt32(0 if waveform_handles_array is None else len(waveform_handles_array))  # case S160
        waveform_handles_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_handles_array, library_type=_visatype.ViInt32)  # case B550
        loop_counts_array_ctype = _get_ctypes_pointer_for_buffer(value=loop_counts_array, library_type=_visatype.ViInt32)  # case B550
        sequence_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateArbSequence(vi_ctype, sequence_length_ctype, waveform_handles_array_ctype, loop_counts_array_ctype, None if sequence_handle_ctype is None else (ctypes.pointer(sequence_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(sequence_handle_ctype.value)

    def create_freq_list(self, waveform, frequency_array, duration_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        waveform_ctype = _visatype.ViInt32(waveform.value)  # case S130
        frequency_list_length_ctype = _visatype.ViInt32(0 if frequency_array is None else len(frequency_array))  # case S160
        frequency_array_ctype = _get_ctypes_pointer_for_buffer(value=frequency_array, library_type=_visatype.ViReal64)  # case B550
        duration_array_ctype = _get_ctypes_pointer_for_buffer(value=duration_array, library_type=_visatype.ViReal64)  # case B550
        frequency_list_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateFreqList(vi_ctype, waveform_ctype, frequency_list_length_ctype, frequency_array_ctype, duration_array_ctype, None if frequency_list_handle_ctype is None else (ctypes.pointer(frequency_list_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(frequency_list_handle_ctype.value)

    def create_waveform_f64(self, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_array = _convert_to_array(value=waveform_data_array, array_type="d")  # case B550
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array_array, library_type=_visatype.ViReal64)  # case B550
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformF64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_f64_numpy(self, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformF64(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_from_file_f64(self, channel_name, file_name, byte_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case C020
        byte_order_ctype = _visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformFromFileF64(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_from_file_i16(self, channel_name, file_name, byte_order):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        file_name_ctype = ctypes.create_string_buffer(file_name.encode(self._encoding))  # case C020
        byte_order_ctype = _visatype.ViInt32(byte_order.value)  # case S130
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformFromFileI16(vi_ctype, channel_name_ctype, file_name_ctype, byte_order_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def create_waveform_i16_numpy(self, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array)  # case B510
        waveform_handle_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_CreateWaveformI16(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype, None if waveform_handle_ctype is None else (ctypes.pointer(waveform_handle_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(waveform_handle_ctype.value)

    def define_user_standard_waveform(self, channel_name, waveform_data_array):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_size_ctype = _visatype.ViInt32(0 if waveform_data_array is None else len(waveform_data_array))  # case S160
        waveform_data_array_ctype = _get_ctypes_pointer_for_buffer(value=waveform_data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_DefineUserStandardWaveform(vi_ctype, channel_name_ctype, waveform_size_ctype, waveform_data_array_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_named_waveform(self, channel_name, waveform_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_DeleteNamedWaveform(vi_ctype, channel_name_ctype, waveform_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def delete_script(self, channel_name, script_name):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        script_name_ctype = ctypes.create_string_buffer(script_name.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_DeleteScript(vi_ctype, channel_name_ctype, script_name_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def disable(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_Disable(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def export_attribute_configuration_buffer(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32()  # case S170
        configuration_ctype = None  # case B580
        error_code = self._library.niFgen_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        size_in_bytes_ctype = _visatype.ViInt32(error_code)  # case S180
        configuration_size = size_in_bytes_ctype.value  # case B590
        configuration_array = array.array("b", [0]) * configuration_size  # case B590
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration_array, library_type=_visatype.ViInt8)  # case B590
        error_code = self._library.niFgen_ExportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return configuration_array

    def export_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_ExportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_attribute_vi_boolean(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFgen_GetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(attribute_value_ctype.value)

    def get_attribute_vi_int32(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_attribute_vi_real64(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_GetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(attribute_value_ctype.value)

    def get_attribute_vi_string(self, channel_name, attribute_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        array_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niFgen_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        array_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * array_size_ctype.value)()  # case C060
        error_code = self._library.niFgen_GetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, array_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def get_channel_name(self, index):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        buffer_size_ctype = _visatype.ViInt32()  # case S170
        channel_string_ctype = None  # case C050
        error_code = self._library.niFgen_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        channel_string_ctype = (_visatype.ViChar * buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFgen_GetChannelName(vi_ctype, index_ctype, buffer_size_ctype, channel_string_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return channel_string_ctype.value.decode(self._encoding)

    def get_error(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus()  # case S220
        error_description_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_description_ctype = None  # case C050
        error_code = self._library.niFgen_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_description_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_description_ctype = (_visatype.ViChar * error_description_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niFgen_GetError(vi_ctype, None if error_code_ctype is None else (ctypes.pointer(error_code_ctype)), error_description_buffer_size_ctype, error_description_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return int(error_code_ctype.value), error_description_ctype.value.decode(self._encoding)

    def get_ext_cal_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetExtCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_ext_cal_last_temp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_GetExtCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_ext_cal_recommended_interval(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        months_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetExtCalRecommendedInterval(vi_ctype, None if months_ctype is None else (ctypes.pointer(months_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(months_ctype.value)

    def get_hardware_state(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        state_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetHardwareState(vi_ctype, None if state_ctype is None else (ctypes.pointer(state_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return enums.HardwareState(state_ctype.value)

    def get_self_cal_last_date_and_time(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        year_ctype = _visatype.ViInt32()  # case S220
        month_ctype = _visatype.ViInt32()  # case S220
        day_ctype = _visatype.ViInt32()  # case S220
        hour_ctype = _visatype.ViInt32()  # case S220
        minute_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_GetSelfCalLastDateAndTime(vi_ctype, None if year_ctype is None else (ctypes.pointer(year_ctype)), None if month_ctype is None else (ctypes.pointer(month_ctype)), None if day_ctype is None else (ctypes.pointer(day_ctype)), None if hour_ctype is None else (ctypes.pointer(hour_ctype)), None if minute_ctype is None else (ctypes.pointer(minute_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(year_ctype.value), int(month_ctype.value), int(day_ctype.value), int(hour_ctype.value), int(minute_ctype.value)

    def get_self_cal_last_temp(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_GetSelfCalLastTemp(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def get_self_cal_supported(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_cal_supported_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFgen_GetSelfCalSupported(vi_ctype, None if self_cal_supported_ctype is None else (ctypes.pointer(self_cal_supported_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(self_cal_supported_ctype.value)

    def import_attribute_configuration_buffer(self, configuration):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        size_in_bytes_ctype = _visatype.ViInt32(0 if configuration is None else len(configuration))  # case S160
        configuration_ctype = _get_ctypes_pointer_for_buffer(value=configuration, library_type=_visatype.ViInt8)  # case B550
        error_code = self._library.niFgen_ImportAttributeConfigurationBuffer(vi_ctype, size_in_bytes_ctype, configuration_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def import_attribute_configuration_file(self, file_path):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        file_path_ctype = ctypes.create_string_buffer(file_path.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_ImportAttributeConfigurationFile(vi_ctype, file_path_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def initialize_with_channels(self, resource_name, channel_name, reset_device, option_string):  # noqa: N802
        resource_name_ctype = ctypes.create_string_buffer(resource_name.encode(self._encoding))  # case C020
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C020
        reset_device_ctype = _visatype.ViBoolean(reset_device)  # case S150
        option_string_ctype = ctypes.create_string_buffer(option_string.encode(self._encoding))  # case C020
        vi_ctype = _visatype.ViSession()  # case S220
        error_code = self._library.niFgen_InitializeWithChannels(resource_name_ctype, channel_name_ctype, reset_device_ctype, option_string_ctype, None if vi_ctype is None else (ctypes.pointer(vi_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        self._close_on_exit = True
        return int(vi_ctype.value)

    def initiate_generation(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_InitiateGeneration(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def is_done(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        done_ctype = _visatype.ViBoolean()  # case S220
        error_code = self._library.niFgen_IsDone(vi_ctype, None if done_ctype is None else (ctypes.pointer(done_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return bool(done_ctype.value)

    def lock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_LockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def query_arb_seq_capabilities(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_number_of_sequences_ctype = _visatype.ViInt32()  # case S220
        minimum_sequence_length_ctype = _visatype.ViInt32()  # case S220
        maximum_sequence_length_ctype = _visatype.ViInt32()  # case S220
        maximum_loop_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_QueryArbSeqCapabilities(vi_ctype, None if maximum_number_of_sequences_ctype is None else (ctypes.pointer(maximum_number_of_sequences_ctype)), None if minimum_sequence_length_ctype is None else (ctypes.pointer(minimum_sequence_length_ctype)), None if maximum_sequence_length_ctype is None else (ctypes.pointer(maximum_sequence_length_ctype)), None if maximum_loop_count_ctype is None else (ctypes.pointer(maximum_loop_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_sequences_ctype.value), int(minimum_sequence_length_ctype.value), int(maximum_sequence_length_ctype.value), int(maximum_loop_count_ctype.value)

    def query_arb_wfm_capabilities(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_number_of_waveforms_ctype = _visatype.ViInt32()  # case S220
        waveform_quantum_ctype = _visatype.ViInt32()  # case S220
        minimum_waveform_size_ctype = _visatype.ViInt32()  # case S220
        maximum_waveform_size_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niFgen_QueryArbWfmCapabilities(vi_ctype, None if maximum_number_of_waveforms_ctype is None else (ctypes.pointer(maximum_number_of_waveforms_ctype)), None if waveform_quantum_ctype is None else (ctypes.pointer(waveform_quantum_ctype)), None if minimum_waveform_size_ctype is None else (ctypes.pointer(minimum_waveform_size_ctype)), None if maximum_waveform_size_ctype is None else (ctypes.pointer(maximum_waveform_size_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_waveforms_ctype.value), int(waveform_quantum_ctype.value), int(minimum_waveform_size_ctype.value), int(maximum_waveform_size_ctype.value)

    def query_freq_list_capabilities(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        maximum_number_of_freq_lists_ctype = _visatype.ViInt32()  # case S220
        minimum_frequency_list_length_ctype = _visatype.ViInt32()  # case S220
        maximum_frequency_list_length_ctype = _visatype.ViInt32()  # case S220
        minimum_frequency_list_duration_ctype = _visatype.ViReal64()  # case S220
        maximum_frequency_list_duration_ctype = _visatype.ViReal64()  # case S220
        frequency_list_duration_quantum_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_QueryFreqListCapabilities(vi_ctype, None if maximum_number_of_freq_lists_ctype is None else (ctypes.pointer(maximum_number_of_freq_lists_ctype)), None if minimum_frequency_list_length_ctype is None else (ctypes.pointer(minimum_frequency_list_length_ctype)), None if maximum_frequency_list_length_ctype is None else (ctypes.pointer(maximum_frequency_list_length_ctype)), None if minimum_frequency_list_duration_ctype is None else (ctypes.pointer(minimum_frequency_list_duration_ctype)), None if maximum_frequency_list_duration_ctype is None else (ctypes.pointer(maximum_frequency_list_duration_ctype)), None if frequency_list_duration_quantum_ctype is None else (ctypes.pointer(frequency_list_duration_quantum_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(maximum_number_of_freq_lists_ctype.value), int(minimum_frequency_list_length_ctype.value), int(maximum_frequency_list_length_ctype.value), float(minimum_frequency_list_duration_ctype.value), float(maximum_frequency_list_duration_ctype.value), float(frequency_list_duration_quantum_ctype.value)

    def read_current_temperature(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        temperature_ctype = _visatype.ViReal64()  # case S220
        error_code = self._library.niFgen_ReadCurrentTemperature(vi_ctype, None if temperature_ctype is None else (ctypes.pointer(temperature_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return float(temperature_ctype.value)

    def reset_device(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ResetDevice(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def reset_with_defaults(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_ResetWithDefaults(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_cal(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_SelfCal(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def send_software_edge_trigger(self, trigger, trigger_id):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        trigger_ctype = _visatype.ViInt32(trigger.value)  # case S130
        trigger_id_ctype = ctypes.create_string_buffer(trigger_id.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SendSoftwareEdgeTrigger(vi_ctype, trigger_ctype, trigger_id_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_boolean(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViBoolean(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViBoolean(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_int32(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViInt32(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_real64(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViReal64(attribute_value)  # case S150
        error_code = self._library.niFgen_SetAttributeViReal64(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_attribute_vi_string(self, channel_name, attribute_id, attribute_value):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        attribute_id_ctype = _visatype.ViAttr(attribute_id)  # case S150
        attribute_value_ctype = ctypes.create_string_buffer(attribute_value.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SetAttributeViString(vi_ctype, channel_name_ctype, attribute_id_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_named_waveform_next_write_position(self, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        error_code = self._library.niFgen_SetNamedWaveformNextWritePosition(vi_ctype, channel_name_ctype, waveform_name_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_runtime_environment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        environment_ctype = ctypes.create_string_buffer(environment.encode(self._encoding))  # case C020
        environment_version_ctype = ctypes.create_string_buffer(environment_version.encode(self._encoding))  # case C020
        reserved1_ctype = ctypes.create_string_buffer(reserved1.encode(self._encoding))  # case C020
        reserved2_ctype = ctypes.create_string_buffer(reserved2.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_SetRuntimeEnvironment(environment_ctype, environment_version_ctype, reserved1_ctype, reserved2_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def set_waveform_next_write_position(self, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        relative_to_ctype = _visatype.ViInt32(relative_to.value)  # case S130
        offset_ctype = _visatype.ViInt32(offset)  # case S150
        error_code = self._library.niFgen_SetWaveformNextWritePosition(vi_ctype, channel_name_ctype, waveform_handle_ctype, relative_to_ctype, offset_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def unlock(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_UnlockSession(vi_ctype, None)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def wait_until_done(self, max_time):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        max_time_ctype = _visatype.ViInt32(max_time)  # case S150
        error_code = self._library.niFgen_WaitUntilDone(vi_ctype, max_time_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_binary16_waveform_numpy(self, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = _get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteBinary16Waveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_named_waveform_f64(self, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = _convert_to_array(value=data, array_type="d")  # case B550
        data_ctype = _get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_WriteNamedWaveformF64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_named_waveform_f64_numpy(self, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = _get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteNamedWaveformF64(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_named_waveform_i16_numpy(self, channel_name, waveform_name, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_name_ctype = ctypes.create_string_buffer(waveform_name.encode(self._encoding))  # case C020
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = _get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteNamedWaveformI16(vi_ctype, channel_name_ctype, waveform_name_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_script(self, channel_name, script):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        script_ctype = ctypes.create_string_buffer(script.encode(self._encoding))  # case C020
        error_code = self._library.niFgen_WriteScript(vi_ctype, channel_name_ctype, script_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform(self, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_array = _convert_to_array(value=data, array_type="d")  # case B550
        data_ctype = _get_ctypes_pointer_for_buffer(value=data_array, library_type=_visatype.ViReal64)  # case B550
        error_code = self._library.niFgen_WriteWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def write_waveform_numpy(self, channel_name, waveform_handle, data):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        channel_name_ctype = ctypes.create_string_buffer(channel_name.encode(self._encoding))  # case C010
        waveform_handle_ctype = _visatype.ViInt32(waveform_handle)  # case S150
        size_ctype = _visatype.ViInt32(0 if data is None else len(data))  # case S160
        data_ctype = _get_ctypes_pointer_for_buffer(value=data)  # case B510
        error_code = self._library.niFgen_WriteWaveform(vi_ctype, channel_name_ctype, waveform_handle_ctype, size_ctype, data_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def close(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_close(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def error_message(self, error_code):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code_ctype = _visatype.ViStatus(error_code)  # case S150
        error_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFgen_error_message(vi_ctype, error_code_ctype, error_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_message_ctype.value.decode(self._encoding)

    def reset(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        error_code = self._library.niFgen_reset(vi_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def self_test(self):  # noqa: N802
        vi_ctype = _visatype.ViSession(self._vi)  # case S110
        self_test_result_ctype = _visatype.ViInt16()  # case S220
        self_test_message_ctype = (_visatype.ViChar * 256)()  # case C070
        error_code = self._library.niFgen_self_test(vi_ctype, None if self_test_result_ctype is None else (ctypes.pointer(self_test_result_ctype)), self_test_message_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(self_test_result_ctype.value), self_test_message_ctype.value.decode(self._encoding)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/_library_singleton.py sha256=c425807d44abb2171e0a760d3f60ccf5c65ea5be62c8f01a7dbcaaed1f3d93a6 bytes=1693 -->
## FILE: generated/nifgen/nifgen/_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/_library_singleton.py`
- sha256: `c425807d44abb2171e0a760d3f60ccf5c65ea5be62c8f01a7dbcaaed1f3d93a6`
- bytes: 1693

````python
# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import nifgen._library as _library
import nifgen.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'nifgen', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'niFgen_32.dll', 'type': 'windll'},
                             '64bit': {'name': 'niFgen_64.dll', 'type': 'cdll'}}}


def _get_library_name():
    try:
        lib_name = ctypes.util.find_library(_library_info[platform.system()][platform.architecture()[0]]['name'])  # We find and return full path to the DLL
        if lib_name is None:
            raise errors.DriverNotInstalledError()
        return lib_name
    except KeyError:
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for nifgen.
    '''
    global _instance

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == 'windll':
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:
                    assert library_type == 'cdll'
                    ctypes_library = ctypes.CDLL(_get_library_name())
            except OSError:
                raise errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
        return _instance
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: generated/nifgen/nifgen/_visatype.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/_visatype.py`
- sha256: `ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92`
- bytes: 662

````python
import ctypes


'''Definitions of the VISA types used by the C API of the driver runtime.
These are aliased directly to ctypes types so can be used directly to call into the library.
'''


ViChar = ctypes.c_char
ViInt8 = ctypes.c_int8
ViUInt8 = ctypes.c_uint8
ViInt16 = ctypes.c_int16
ViUInt16 = ctypes.c_uint16
ViInt32 = ctypes.c_int32
ViUInt32 = ctypes.c_uint32
ViInt64 = ctypes.c_int64
ViUInt64 = ctypes.c_uint64
ViString = ctypes.c_char_p
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double

# Types that are based on other visatypes
ViBoolean = ViUInt16
ViStatus = ViInt32
ViSession = ViUInt32
ViAttr = ViUInt32
ViConstString = ViString
ViRsrc = ViString
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/enums.py sha256=ca2db232d9b0a1d253a64cc1f12e712499ad2f09a6d7fa058560784ee462109e bytes=10563 -->
## FILE: generated/nifgen/nifgen/enums.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/enums.py`
- sha256: `ca2db232d9b0a1d253a64cc1f12e712499ad2f09a6d7fa058560784ee462109e`
- bytes: 10563

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import Enum


class AnalogPath(Enum):
    MAIN = 0
    r'''
    Specifies use of the main path.  NI-FGEN chooses the amplifier based on the user-specified gain.
    '''
    DIRECT = 1
    r'''
    Specifies use of the direct path.
    '''
    FIXED_LOW_GAIN = 2
    r'''
    Specifies use of the low-gain amplifier in the main path, no matter  what value the user specifies for gain. This setting limits the output  range.
    '''
    FIXED_HIGH_GAIN = 3
    r'''
    Specifies use of the high-gain amplifier in the main path.
    '''


class BusType(Enum):
    INVALID = 0
    r'''
    Indicates an invalid bus type.
    '''
    AT = 1
    r'''
    Indicates the signal generator is the AT bus type.
    '''
    PCI = 2
    r'''
    Indicates the signal generator is the PCI bus type.
    '''
    PXI = 3
    r'''
    Indicates the signal generator is the PXI bus type.
    '''
    VXI = 4
    r'''
    Indicates the signal generator is the VXI bus type.
    '''
    PCMCIA = 5
    r'''
    Indicates the signal generator is the PCI-CMA bus type.
    '''
    PXIE = 6
    r'''
    Indicates the signal generator is the PXI Express bus type.
    '''


class ByteOrder(Enum):
    LITTLE = 0
    BIG = 1


class ClockMode(Enum):
    HIGH_RESOLUTION = 0
    r'''
    High resolution sampling—Sample rate is generated by a high–resolution clock source.
    '''
    DIVIDE_DOWN = 1
    r'''
    Divide down sampling—Sample rates are generated by dividing the source frequency.
    '''
    AUTOMATIC = 2
    r'''
    Automatic Selection—NI-FGEN selects between the divide–down and high–resolution clocking modes.
    '''


class DataMarkerEventLevelPolarity(Enum):
    HIGH = 101
    r'''
    When the operation is ready to start, the Ready for Start  event level is high.
    '''
    LOW = 102
    r'''
    When the operation is ready to start, the Ready for Start  event level is low.
    '''


class EventPulseWidthUnits(Enum):
    SAMPLE_CLOCK_PERIODS = 101
    r'''
    Specifies the pulse width in Sample clock periods.
    '''
    SECONDS = 102
    r'''
    Specifies the pulse width in seconds.
    '''


class HardwareState(Enum):
    IDLE = 0
    WAITING_FOR_START_TRIGGER = 100
    RUNNING = 200
    DONE = 600
    HARDWARE_ERROR = 1000


class IdleBehavior(Enum):
    HOLD_LAST = 400
    r'''
    While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.
    '''
    JUMP_TO = 401
    r'''
    While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value property.
    '''


class OutputMode(Enum):
    FUNC = 0
    r'''
    Standard Method mode—  Generates standard method waveforms  such as sine, square, triangle, and so on.
    '''
    ARB = 1
    r'''
    Arbitrary waveform mode—Generates  waveforms from user-created/provided  waveform arrays of numeric data.
    '''
    SEQ = 2
    r'''
    Arbitrary sequence mode —  Generates downloaded waveforms  in an order your specify.
    '''
    FREQ_LIST = 101
    r'''
    Frequency List mode—Generates a  standard method using a list of  frequencies you define.
    '''
    SCRIPT = 102
    r'''
    **Script mode—**\ Allows you to use scripting to link and loop multiple
    waveforms in complex combinations.
    '''


class ReferenceClockSource(Enum):
    CLOCK_IN = 'ClkIn'
    r'''
    Specifies that the CLK IN input signal from the front panel connector is
    used as the Reference Clock source.
    '''
    NONE = 'None'
    r'''
    Specifies that a Reference Clock is not used.
    '''
    ONBOARD_REFERENCE_CLOCK = 'OnboardRefClk'
    r'''
    Specifies that the onboard Reference Clock is used as the Reference
    Clock source.
    '''
    PXI_CLOCK = 'PXI_Clk'
    r'''
    Specifies that the PXI Clock is used as the Reference Clock source.
    '''
    RTSI_7 = 'RTSI7'
    r'''
    Specifies that the RTSI line 7 is used as the Reference Clock source.
    '''


class RelativeTo(Enum):
    START = 0
    CURRENT = 1


class SampleClockSource(Enum):
    CLOCK_IN = 'ClkIn'
    r'''
    Specifies that the signal at the CLK IN front panel connector is used as
    the Sample Clock source.
    '''
    DDC_CLOCK_IN = 'DDC_ClkIn'
    r'''
    Specifies that the Sample Clock from the DDC connector is used as the Sample
    Clock source.
    '''
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    Specifies that the onboard clock is used as the Sample Clock source.
    '''
    PXI_STAR_LINE = 'PXI_Star'
    r'''
    Specifies that the PXI\_STAR trigger line is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_0_RTSI_0 = 'PXI_Trig0'
    r'''
    Specifies that the PXI or RTSI line 0 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_1_RTSI_1 = 'PXI_Trig1'
    r'''
    Specifies that the PXI or RTSI line 1 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_2_RTSI_2 = 'PXI_Trig2'
    r'''
    Specifies that the PXI or RTSI line 2 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_3_RTSI_3 = 'PXI_Trig3'
    r'''
    Specifies that the PXI or RTSI line 3 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_4_RTSI_4 = 'PXI_Trig4'
    r'''
    Specifies that the PXI or RTSI line 4 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_5_RTSI_5 = 'PXI_Trig5'
    r'''
    Specifies that the PXI or RTSI line 5 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_6_RTSI_6 = 'PXI_Trig6'
    r'''
    Specifies that the PXI or RTSI line 6 is used as the Sample Clock
    source.
    '''
    PXI_TRIGGER_LINE_7_RTSI_7 = 'PXI_Trig7'
    r'''
    Specifies that the PXI or RTSI line 7 is used as the Sample Clock
    source.
    '''


class SampleClockTimebaseSource(Enum):
    CLOCK_IN = 'ClkIn'
    r'''
    Specifies that the external signal on the CLK IN front panel connector
    is used as the source.
    '''
    ONBOARD_CLOCK = 'OnboardClock'
    r'''
    Specifies that the onboard Sample Clock timebase is used as the source.
    '''


class ScriptTriggerDigitalEdgeEdge(Enum):
    RISING = 101
    r'''
    Rising Edge
    '''
    FALLING = 102
    r'''
    Falling Edge
    '''


class ScriptTriggerType(Enum):
    TRIG_NONE = 101
    r'''
    No trigger is configured. Signal generation starts immediately.
    '''
    DIGITAL_EDGE = 102
    r'''
    Trigger is asserted when a digital edge is detected.
    '''
    DIGITAL_LEVEL = 103
    r'''
    Trigger is asserted when a digital level is detected.
    '''
    SOFTWARE_EDGE = 104
    r'''
    Trigger is asserted when a software edge is detected.
    '''


class StartTriggerDigitalEdgeEdge(Enum):
    RISING = 101
    r'''
    Rising Edge
    '''
    FALLING = 102
    r'''
    Falling Edge
    '''


class StartTriggerType(Enum):
    TRIG_NONE = 101
    r'''
    None
    '''
    DIGITAL_EDGE = 102
    r'''
    Digital Edge
    '''
    SOFTWARE_EDGE = 104
    r'''
    Software Edge
    '''
    P2P_ENDPOINT_FULLNESS = 106
    r'''
    P2P Endpoint Fullness
    '''


class TerminalConfiguration(Enum):
    SINGLE_ENDED = 300
    r'''
    Single-ended operation
    '''
    DIFFERENTIAL = 301
    r'''
    Differential operation
    '''


class Trigger(Enum):
    START = 1004
    SCRIPT = 103


class TriggerMode(Enum):
    SINGLE = 1
    r'''
    Single Trigger Mode - The waveform you describe in the sequence list is  generated only once by going through the entire staging list. Only one  trigger is required to start the waveform generation. You can use Single  trigger mode with the output mode in any mode. After a trigger is  received, the waveform generation starts from the first stage and  continues through to the last stage. Then, the last stage generates  repeatedly until you stop the waveform generation.
    '''
    CONTINUOUS = 2
    r'''
    Continuous Trigger Mode - The waveform you describe in the staging list generates infinitely by repeatedly cycling through the staging list.  After a trigger is received, the waveform generation starts from the  first stage and continues through to the last stage. After the last stage  completes, the waveform generation loops back to the start of the  first stage and continues until it is stopped. Only one trigger is  required to start the waveform generation.
    '''
    STEPPED = 3
    r'''
    Stepped Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates. Then, the device waits for the  next trigger signal. On the next trigger, the waveform described by the  second stage generates, and so on. After the staging list completes,  the waveform generation returns to the first stage and continues in a  cyclic fashion. After any stage has generated completely, the first  eight samples of the next stage are repeated continuously until the next  trigger is received.
    trigger mode.

    Note: In Frequency List mode, Stepped trigger mode is the same as Burst
    '''
    BURST = 4
    r'''
    Burst Trigger Mode - After a start trigger is received, the waveform  described by the first stage generates until another trigger is  received. At the next trigger, the buffer of the previous stage completes, and then the waveform described by the second stage generates. After the staging list completes, the waveform generation  returns to the first stage and continues in a cyclic fashion. In  Frequency List mode, the duration instruction is ignored, and the trigger  switches the frequency to the next frequency in the list.
    trigger mode.

    Note: In Frequency List mode, Stepped trigger mode is the same as Burst
    '''


class WaitBehavior(Enum):
    HOLD_LAST = 400
    r'''
    While in an Idle or Wait state, the output signal remains  at the last voltage generated prior to entering the state.
    '''
    JUMP_TO = 401
    r'''
    While in an Idle or Wait state, the output signal remains  at the value configured in the Idle or Wait value property.
    '''


class Waveform(Enum):
    SINE = 1
    r'''
    Sinusoid waveform
    '''
    SQUARE = 2
    r'''
    Square waveform
    '''
    TRIANGLE = 3
    r'''
    Triange waveform
    '''
    RAMP_UP = 4
    r'''
    Positive ramp waveform
    '''
    RAMP_DOWN = 5
    r'''
    Negative ramp waveform
    '''
    DC = 6
    r'''
    Constant voltage
    '''
    NOISE = 101
    r'''
    White noise
    '''
    USER = 102
    r'''
    User-defined waveform as defined by the define_user_standard_waveform method.
    '''
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/errors.py sha256=a130cc1bc6bc97b228952dc89bd74f385ff611289779de216f05cfade9cdf2f4 bytes=4349 -->
## FILE: generated/nifgen/nifgen/errors.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/errors.py`
- sha256: `a130cc1bc6bc97b228952dc89bd74f385ff611289779de216f05cfade9cdf2f4`
- bytes: 4349

````python
# -*- coding: utf-8 -*-
# This file was generated


import platform
import warnings


def _is_success(code):
    return (code == 0)


def _is_error(code):
    return (code < 0)


def _is_warning(code):
    return (code > 0)


class Error(Exception):
    '''Base error class for NI-FGEN'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-FGEN driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-FGEN driver'''

    def __init__(self, code, description):
        assert _is_warning(code), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__('Warning {} occurred.\n\n{}'.format(code, description))


class RpcError(Error):
    '''An error specific to sessions to the NI gRPC Device Server'''

    def __init__(self, rpc_code, description):
        self.rpc_code = rpc_code
        self.description = description
        try:
            import grpc
            rpc_error = str(grpc.StatusCode(self.rpc_code))
        except Exception:
            rpc_error = str(self.rpc_code)
        super(RpcError, self).__init__(rpc_error + ": " + self.description)


class UnsupportedConfigurationError(Error):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Error):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-FGEN runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-FGEN driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-FGEN runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-FGEN driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-FGEN runtime returned an unexpected value. This can occur if it is too new for the nifgen Python module. Upgrade the nifgen Python module.')


class InvalidRepeatedCapabilityError(Error):
    '''An error due to an invalid character in a repeated capability'''

    def __init__(self, invalid_character, invalid_string):
        super(InvalidRepeatedCapabilityError, self).__init__('An invalid character ({}) was found in repeated capability string ({})'.format(invalid_character, invalid_string))


class SelfTestError(Error):
    '''An error due to a failed self-test'''

    def __init__(self, code, msg):
        self.code = code
        self.message = msg
        super(SelfTestError, self).__init__('Self-test failed with code {}: {}'.format(code, msg))


def handle_error(library_interpreter, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by nifgen.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    '''

    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ''
    else:
        description = library_interpreter.get_error_description(code)

    if _is_error(code):
        raise DriverError(code, description)

    assert _is_warning(code)
    warnings.warn(DriverWarning(code, description))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/grpc_session_options.py sha256=896ee5158b7b3f14941560a541e127ec492095cf98f1d224e7771b31f5d72ab2 bytes=3452 -->
## FILE: generated/nifgen/nifgen/grpc_session_options.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/grpc_session_options.py`
- sha256: `896ee5158b7b3f14941560a541e127ec492095cf98f1d224e7771b31f5d72ab2`
- bytes: 3452

````python
# -*- coding: utf-8 -*-
# This file was generated

from enum import IntEnum


# This constant specifies the gRPC package and service used by this API.
# Customers can pass this value to the MeasurementLink discovery service to resolve the server instance that provides this interface.
GRPC_SERVICE_INTERFACE_NAME = 'nifgen_grpc.NiFgen'

# This constant specifies the API license key required by the NI gRPC Device Server that comes with
# MeasurementLink 2023 Q1.
MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY = 'DE10751B-3EE0-44EC-A93B-800E6A3C89E4'


class SessionInitializationBehavior(IntEnum):
    AUTO = 0
    r'''
    The NI gRPC Device Server will attach to an existing session with the specified name if it exists, otherwise the server
    will initialize a new session.

    Note:
    When using the Session as a context manager and the context exits, the behavior depends on what happened when the constructor
    was called. If it resulted in a new session being initialized on the NI gRPC Device Server, then it will automatically close the
    server session. If it instead attached to an existing session, then it will detach from the server session and leave it open.
    '''
    INITIALIZE_SERVER_SESSION = 1
    r'''
    Require the NI gRPC Device Server to initialize a new session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will automatically close the
    server session.
    '''
    ATTACH_TO_SERVER_SESSION = 2
    r'''
    Require the NI gRPC Device Server to attach to an existing session with the specified name.

    Note:
    When using the Session as a context manager and the context exits, it will detach from the server session
    and leave it open.
    '''


class GrpcSessionOptions(object):
    '''Collection of options that specifies session behaviors related to gRPC.'''

    def __init__(
        self,
        grpc_channel,
        session_name,
        *,
        api_key=MEASUREMENTLINK_23Q1_NIMI_PYTHON_API_KEY,
        initialization_behavior=SessionInitializationBehavior.AUTO
    ):
        r'''Collection of options that specifies session behaviors related to gRPC.

        Creates and returns an object you can pass to a Session constructor.

        Args:
            grpc_channel (grpc.Channel): Specifies the channel to the NI gRPC Device Server.

            session_name (str): User-specified name that identifies the driver session on the NI gRPC Device
                Server. This is different from the resource name parameter many APIs take as a separate
                parameter. Specifying a name makes it easy to share sessions across multiple gRPC clients.
                You can use an empty string if you want to always initialize a new session on the server.
                To attach to an existing session, you must specify the session name it was initialized with.

            api_key (str): Specifies the API license key required by the NI gRPC Device Server.

            initialization_behavior (enum): Specifies whether it is acceptable to initialize a new
                session or attach to an existing one, or if only one of the behaviors is desired.
                The driver session exists on the NI gRPC Device Server.
        '''
        self.grpc_channel = grpc_channel
        self.session_name = session_name
        self.api_key = api_key
        self.initialization_behavior = initialization_behavior
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/nidevice_pb2.py sha256=9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54 bytes=2009 -->
## FILE: generated/nifgen/nifgen/nidevice_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/nidevice_pb2.py`
- sha256: `9a935a95cbe830099345438b27f1460989b073de2e873f43cb394ac0df4ced54`
- bytes: 2009

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nidevice.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0enidevice.proto\x12\rnidevice_grpc\"2\n\x0fNIComplexNumber\x12\x0c\n\x04real\x18\x01 \x01(\x01\x12\x11\n\timaginary\x18\x02 \x01(\x01\"5\n\x12NIComplexNumberF32\x12\x0c\n\x04real\x18\x01 \x01(\x02\x12\x11\n\timaginary\x18\x02 \x01(\x02\"/\n\x0cNIComplexI16\x12\x0c\n\x04real\x18\x01 \x01(\x11\x12\x11\n\timaginary\x18\x02 \x01(\x11\"r\n\x0fSmtSpectrumInfo\x12\x15\n\rspectrum_type\x18\x01 \x01(\r\x12\x11\n\tlinear_db\x18\x02 \x01(\r\x12\x0e\n\x06window\x18\x03 \x01(\r\x12\x13\n\x0bwindow_size\x18\x04 \x01(\x11\x12\x10\n\x08\x66\x66t_size\x18\x05 \x01(\x11\x42\x42\n\x12\x63om.ni.grpc.deviceB\x08NiDeviceP\x01\xaa\x02\x1fNationalInstruments.Grpc.Deviceb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nidevice_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.ni.grpc.deviceB\010NiDeviceP\001\252\002\037NationalInstruments.Grpc.Device'
  _globals['_NICOMPLEXNUMBER']._serialized_start=33
  _globals['_NICOMPLEXNUMBER']._serialized_end=83
  _globals['_NICOMPLEXNUMBERF32']._serialized_start=85
  _globals['_NICOMPLEXNUMBERF32']._serialized_end=138
  _globals['_NICOMPLEXI16']._serialized_start=140
  _globals['_NICOMPLEXI16']._serialized_end=187
  _globals['_SMTSPECTRUMINFO']._serialized_start=189
  _globals['_SMTSPECTRUMINFO']._serialized_end=303
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/nidevice_pb2_grpc.py sha256=d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09 bytes=159 -->
## FILE: generated/nifgen/nifgen/nidevice_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/nidevice_pb2_grpc.py`
- sha256: `d686e804f171693117b7d030ec4023f205c70c234c8590f6557aa8702f65fe09`
- bytes: 159

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/nifgen_pb2.py sha256=498e0132a21cd8baf535676cd851e3234b3b063cf6361e52405d67f1996c535c bytes=129275 -->
## FILE: generated/nifgen/nifgen/nifgen_pb2.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/nifgen_pb2.py`
- sha256: `498e0132a21cd8baf535676cd851e3234b3b063cf6361e52405d67f1996c535c`
- bytes: 129275

````python
# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nifgen.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import nidevice_pb2 as nidevice__pb2
import session_pb2 as session__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cnifgen.proto\x12\x0bnifgen_grpc\x1a\x0enidevice.proto\x1a\rsession.proto\"\xb1\x01\n\x0bInitRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12M\n\x17initialization_behavior\x18\x05 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"~\n\x0cInitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"\xd3\x01\n\x16InitWithOptionsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x10\n\x08id_query\x18\x03 \x01(\x08\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"\x89\x01\n\x17InitWithOptionsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"\xde\x01\n\x1dInitializeWithChannelsRequest\x12\x14\n\x0csession_name\x18\x01 \x01(\t\x12\x15\n\rresource_name\x18\x02 \x01(\t\x12\x14\n\x0c\x63hannel_name\x18\x03 \x01(\t\x12\x14\n\x0creset_device\x18\x04 \x01(\x08\x12\x15\n\roption_string\x18\x05 \x01(\t\x12M\n\x17initialization_behavior\x18\x06 \x01(\x0e\x32,.nidevice_grpc.SessionInitializationBehavior\"\x90\x01\n\x1eInitializeWithChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x02vi\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x19\n\rerror_message\x18\x03 \x01(\tB\x02\x18\x01\x12\x1f\n\x17new_session_initialized\x18\x04 \x01(\x08\"2\n\x0c\x43loseRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rCloseResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"2\n\x0cResetRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x1f\n\rResetResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"5\n\x0fSelfTestRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"W\n\x10SelfTestResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x18\n\x10self_test_result\x18\x02 \x01(\x11\x12\x19\n\x11self_test_message\x18\x03 \x01(\t\"7\n\x11\x45rrorQueryRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"O\n\x12\x45rrorQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x15\n\rerror_message\x18\x03 \x01(\t\"M\n\x13\x45rrorMessageRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11\"=\n\x14\x45rrorMessageResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\":\n\x14RevisionQueryRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"f\n\x15RevisionQueryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x1ainstrument_driver_revision\x18\x02 \x01(\t\x12\x19\n\x11\x66irmware_revision\x18\x03 \x01(\t\"5\n\x0fGetErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"Q\n\x10GetErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x12\n\nerror_code\x18\x02 \x01(\x11\x12\x19\n\x11\x65rror_description\x18\x03 \x01(\t\"7\n\x11\x43learErrorRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"$\n\x12\x43learErrorResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"M\n\x13\x45rrorHandlerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\nerror_code\x18\x02 \x01(\x11\"=\n\x14\x45rrorHandlerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rerror_message\x18\x02 \x01(\t\"J\n\x15GetChannelNameRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\r\n\x05index\x18\x02 \x01(\x11\"@\n\x16GetChannelNameResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x16\n\x0e\x63hannel_string\x18\x02 \x01(\t\"B\n\x1cResetInterchangeCheckRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"/\n\x1dResetInterchangeCheckResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"E\n\x1f\x43learInterchangeWarningsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"2\n ClearInterchangeWarningsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"D\n\x1eInvalidateAllAttributesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"1\n\x1fInvalidateAllAttributesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\">\n\x18ResetWithDefaultsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"+\n\x19ResetWithDefaultsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"4\n\x0e\x44isableRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"!\n\x0f\x44isableResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"3\n\rCommitRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\" \n\x0e\x43ommitResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"=\n\x17GetHardwareStateRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"h\n\x18GetHardwareStateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12)\n\x05state\x18\x02 \x01(\x0e\x32\x1a.nifgen_grpc.HardwareState\x12\x11\n\tstate_raw\x18\x03 \x01(\x11\"L\n\x14WaitUntilDoneRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08max_time\x18\x02 \x01(\x11\"\'\n\x15WaitUntilDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"3\n\rIsDoneRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\".\n\x0eIsDoneResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04\x64one\x18\x02 \x01(\x08\"8\n\x12ResetDeviceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"%\n\x13ResetDeviceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"q\n\x1d\x43onfigureOperationModeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x16\n\x0eoperation_mode\x18\x03 \x01(\x11\"0\n\x1e\x43onfigureOperationModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x9f\x01\n\x1a\x43onfigureOutputModeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12.\n\x0boutput_mode\x18\x02 \x01(\x0e\x32\x17.nifgen_grpc.OutputModeH\x00\x12\x19\n\x0foutput_mode_raw\x18\x03 \x01(\x11H\x00\x42\x12\n\x10output_mode_enum\"-\n\x1b\x43onfigureOutputModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x87\x01\n\x1e\x43onfigureReferenceClockRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1e\n\x16reference_clock_source\x18\x02 \x01(\t\x12!\n\x19reference_clock_frequency\x18\x03 \x01(\x01\"1\n\x1f\x43onfigureReferenceClockResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"n\n\x1f\x43onfigureOutputImpedanceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\timpedance\x18\x03 \x01(\x01\"2\n ConfigureOutputImpedanceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"j\n\x1d\x43onfigureOutputEnabledRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x0f\n\x07\x65nabled\x18\x03 \x01(\x08\"0\n\x1e\x43onfigureOutputEnabledResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"P\n\x18\x43onfigureChannelsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x10\n\x08\x63hannels\x18\x02 \x01(\t\"+\n\x19\x43onfigureChannelsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"?\n\x19InitiateGenerationRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\",\n\x1aInitiateGenerationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"<\n\x16\x41\x62ortGenerationRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\")\n\x17\x41\x62ortGenerationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xfe\x01\n ConfigureStandardWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12)\n\x08waveform\x18\x03 \x01(\x0e\x32\x15.nifgen_grpc.WaveformH\x00\x12\x16\n\x0cwaveform_raw\x18\x04 \x01(\x11H\x00\x12\x11\n\tamplitude\x18\x05 \x01(\x01\x12\x11\n\tdc_offset\x18\x06 \x01(\x01\x12\x11\n\tfrequency\x18\x07 \x01(\x01\x12\x13\n\x0bstart_phase\x18\x08 \x01(\x01\x42\x0f\n\rwaveform_enum\"3\n!ConfigureStandardWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"z\n!DefineUserStandardWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x1b\n\x13waveform_data_array\x18\x03 \x03(\x01\"4\n\"DefineUserStandardWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\\\n ClearUserStandardWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"3\n!ClearUserStandardWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"h\n\x19\x43onfigureFrequencyRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tfrequency\x18\x03 \x01(\x01\",\n\x1a\x43onfigureFrequencyResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"h\n\x19\x43onfigureAmplitudeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tamplitude\x18\x03 \x01(\x01\",\n\x1a\x43onfigureAmplitudeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"D\n\x1eQueryArbWfmCapabilitiesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\xae\x01\n\x1fQueryArbWfmCapabilitiesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12#\n\x1bmaximum_number_of_waveforms\x18\x02 \x01(\x11\x12\x18\n\x10waveform_quantum\x18\x03 \x01(\x11\x12\x1d\n\x15minimum_waveform_size\x18\x04 \x01(\x11\x12\x1d\n\x15maximum_waveform_size\x18\x05 \x01(\x11\"q\n\x18\x43reateWaveformF64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x1b\n\x13waveform_data_array\x18\x03 \x03(\x01\"D\n\x19\x43reateWaveformF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11\"q\n\x18\x43reateWaveformI16Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x1b\n\x13waveform_data_array\x18\x03 \x03(\x11\"D\n\x19\x43reateWaveformI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11\"\x98\x01\n\x1f\x43reateWaveformComplexF64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12;\n\x13waveform_data_array\x18\x03 \x03(\x0b\x32\x1e.nidevice_grpc.NIComplexNumber\"K\n CreateWaveformComplexF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11\"\xca\x01\n CreateWaveformFromFileI16Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12,\n\nbyte_order\x18\x04 \x01(\x0e\x32\x16.nifgen_grpc.ByteOrderH\x00\x12\x18\n\x0e\x62yte_order_raw\x18\x05 \x01(\x11H\x00\x42\x11\n\x0f\x62yte_order_enum\"L\n!CreateWaveformFromFileI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11\"\xca\x01\n CreateWaveformFromFileF64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12,\n\nbyte_order\x18\x04 \x01(\x0e\x32\x16.nifgen_grpc.ByteOrderH\x00\x12\x18\n\x0e\x62yte_order_raw\x18\x05 \x01(\x11H\x00\x42\x11\n\x0f\x62yte_order_enum\"L\n!CreateWaveformFromFileF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11\"U\n\x1a\x43onfigureSampleRateRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x13\n\x0bsample_rate\x18\x02 \x01(\x01\"-\n\x1b\x43onfigureSampleRateResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8e\x01\n\x1b\x43onfigureArbWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12\x0c\n\x04gain\x18\x04 \x01(\x01\x12\x0e\n\x06offset\x18\x05 \x01(\x01\".\n\x1c\x43onfigureArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xac\x01\n\x17\x43learArbWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x36\n\x0fwaveform_handle\x18\x02 \x01(\x0e\x32\x1b.nifgen_grpc.WaveformHandleH\x00\x12\x1d\n\x13waveform_handle_raw\x18\x03 \x01(\x11H\x00\x42\x16\n\x14waveform_handle_enum\"*\n\x18\x43learArbWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x86\x01\n\x1c\x41llocateNamedWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x15\n\rwaveform_size\x18\x04 \x01(\x11\"/\n\x1d\x41llocateNamedWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xea\x01\n(SetNamedWaveformNextWritePositionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12.\n\x0brelative_to\x18\x04 \x01(\x0e\x32\x17.nifgen_grpc.RelativeToH\x00\x12\x19\n\x0frelative_to_raw\x18\x05 \x01(\x11H\x00\x12\x0e\n\x06offset\x18\x06 \x01(\x11\x42\x12\n\x10relative_to_enum\";\n)SetNamedWaveformNextWritePositionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"}\n\x1cWriteNamedWaveformF64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\x01\"/\n\x1dWriteNamedWaveformF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"}\n\x1cWriteNamedWaveformI16Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\x11\"/\n\x1dWriteNamedWaveformI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa4\x01\n#WriteNamedWaveformComplexF64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12,\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1e.nidevice_grpc.NIComplexNumber\"6\n$WriteNamedWaveformComplexF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa1\x01\n#WriteNamedWaveformComplexI16Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\x12)\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1b.nidevice_grpc.NIComplexI16\"6\n$WriteNamedWaveformComplexI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"m\n\x1a\x44\x65leteNamedWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_name\x18\x03 \x01(\t\"-\n\x1b\x44\x65leteNamedWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"D\n\x1eQueryArbSeqCapabilitiesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\xb4\x01\n\x1fQueryArbSeqCapabilitiesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12#\n\x1bmaximum_number_of_sequences\x18\x02 \x01(\x11\x12\x1f\n\x17minimum_sequence_length\x18\x03 \x01(\x11\x12\x1f\n\x17maximum_sequence_length\x18\x04 \x01(\x11\x12\x1a\n\x12maximum_loop_count\x18\x05 \x01(\x11\"y\n\x18\x43reateArbSequenceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1e\n\x16waveform_handles_array\x18\x02 \x03(\x11\x12\x19\n\x11loop_counts_array\x18\x03 \x03(\x11\"D\n\x19\x43reateArbSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fsequence_handle\x18\x02 \x01(\x11\"\xbd\x01\n CreateAdvancedArbSequenceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1e\n\x16waveform_handles_array\x18\x02 \x03(\x11\x12\x19\n\x11loop_counts_array\x18\x03 \x03(\x11\x12\x1b\n\x13sample_counts_array\x18\x04 \x03(\x11\x12\x1d\n\x15marker_location_array\x18\x05 \x03(\x11\"k\n!CreateAdvancedArbSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1d\n\x15\x63oerced_markers_array\x18\x02 \x03(\x11\x12\x17\n\x0fsequence_handle\x18\x03 \x01(\x11\"\x8e\x01\n\x1b\x43onfigureArbSequenceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x17\n\x0fsequence_handle\x18\x03 \x01(\x11\x12\x0c\n\x04gain\x18\x04 \x01(\x01\x12\x0e\n\x06offset\x18\x05 \x01(\x01\".\n\x1c\x43onfigureArbSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xac\x01\n\x17\x43learArbSequenceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x36\n\x0fsequence_handle\x18\x02 \x01(\x0e\x32\x1b.nifgen_grpc.SequenceHandleH\x00\x12\x1d\n\x13sequence_handle_raw\x18\x03 \x01(\x11H\x00\x42\x16\n\x14sequence_handle_enum\"*\n\x18\x43learArbSequenceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\";\n\x15\x43learArbMemoryRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"(\n\x16\x43learArbMemoryResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"F\n QueryFreqListCapabilitiesRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\xa2\x02\n!QueryFreqListCapabilitiesResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12$\n\x1cmaximum_number_of_freq_lists\x18\x02 \x01(\x11\x12%\n\x1dminimum_frequency_list_length\x18\x03 \x01(\x11\x12%\n\x1dmaximum_frequency_list_length\x18\x04 \x01(\x11\x12\'\n\x1fminimum_frequency_list_duration\x18\x05 \x01(\x01\x12\'\n\x1fmaximum_frequency_list_duration\x18\x06 \x01(\x01\x12\'\n\x1f\x66requency_list_duration_quantum\x18\x07 \x01(\x01\"\xc0\x01\n\x15\x43reateFreqListRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12)\n\x08waveform\x18\x02 \x01(\x0e\x32\x15.nifgen_grpc.WaveformH\x00\x12\x16\n\x0cwaveform_raw\x18\x03 \x01(\x11H\x00\x12\x17\n\x0f\x66requency_array\x18\x04 \x03(\x01\x12\x16\n\x0e\x64uration_array\x18\x05 \x03(\x01\x42\x0f\n\rwaveform_enum\"G\n\x16\x43reateFreqListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1d\n\x15\x66requency_list_handle\x18\x02 \x01(\x11\"\xae\x01\n\x18\x43onfigureFreqListRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x1d\n\x15\x66requency_list_handle\x18\x03 \x01(\x11\x12\x11\n\tamplitude\x18\x04 \x01(\x01\x12\x11\n\tdc_offset\x18\x05 \x01(\x01\x12\x13\n\x0bstart_phase\x18\x06 \x01(\x01\"+\n\x19\x43onfigureFreqListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xc1\x01\n\x14\x43learFreqListRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x42\n\x15\x66requency_list_handle\x18\x02 \x01(\x0e\x32!.nifgen_grpc.FrequencyListOptionsH\x00\x12#\n\x19\x66requency_list_handle_raw\x18\x03 \x01(\x11H\x00\x42\x1c\n\x1a\x66requency_list_handle_enum\"\'\n\x15\x43learFreqListResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"^\n\x12WriteScriptRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x0e\n\x06script\x18\x03 \x01(\t\"%\n\x13WriteScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"d\n\x13\x44\x65leteScriptRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x13\n\x0bscript_name\x18\x03 \x01(\t\"&\n\x14\x44\x65leteScriptResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb9\x01\n\x13\x45xportSignalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12%\n\x06signal\x18\x02 \x01(\x0e\x32\x13.nifgen_grpc.SignalH\x00\x12\x14\n\nsignal_raw\x18\x03 \x01(\x11H\x00\x12\x19\n\x11signal_identifier\x18\x04 \x01(\t\x12\x17\n\x0foutput_terminal\x18\x05 \x01(\tB\r\n\x0bsignal_enum\"&\n\x14\x45xportSignalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xb5\x02\n\x15RouteSignalOutRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x39\n\x11route_signal_from\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.RouteSignalFromH\x00\x12\x1f\n\x15route_signal_from_raw\x18\x04 \x01(\x11H\x00\x12\x35\n\x0froute_signal_to\x18\x05 \x01(\x0e\x32\x1a.nifgen_grpc.RouteSignalToH\x01\x12\x1d\n\x13route_signal_to_raw\x18\x06 \x01(\x11H\x01\x42\x18\n\x16route_signal_from_enumB\x16\n\x14route_signal_to_enum\"(\n\x16RouteSignalOutResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa8\x01\n\x1eSendSoftwareEdgeTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\'\n\x07trigger\x18\x02 \x01(\x0e\x32\x14.nifgen_grpc.TriggerH\x00\x12\x15\n\x0btrigger_raw\x18\x03 \x01(\x11H\x00\x12\x12\n\ntrigger_id\x18\x04 \x01(\tB\x0e\n\x0ctrigger_enum\"1\n\x1fSendSoftwareEdgeTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"k\n\'ConfigureDigitalEdgeStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x0c\n\x04\x65\x64ge\x18\x03 \x01(\x11\":\n(ConfigureDigitalEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"N\n(ConfigureSoftwareEdgeStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\";\n)ConfigureSoftwareEdgeStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"@\n\x1a\x44isableStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"-\n\x1b\x44isableStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"z\n/ConfigureP2PEndpointFullnessStartTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12#\n\x1bp2p_endpoint_fullness_level\x18\x02 \x01(\x11\"B\n0ConfigureP2PEndpointFullnessStartTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x80\x01\n(ConfigureDigitalEdgeScriptTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\ntrigger_id\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x0c\n\x04\x65\x64ge\x18\x04 \x01(\x11\";\n)ConfigureDigitalEdgeScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xd6\x01\n)ConfigureDigitalLevelScriptTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\ntrigger_id\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x30\n\x0ctrigger_when\x18\x04 \x01(\x0e\x32\x18.nifgen_grpc.TriggerWhenH\x00\x12\x1a\n\x10trigger_when_raw\x18\x05 \x01(\x11H\x00\x42\x13\n\x11trigger_when_enum\"<\n*ConfigureDigitalLevelScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"c\n)ConfigureSoftwareEdgeScriptTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\ntrigger_id\x18\x02 \x01(\t\"<\n*ConfigureSoftwareEdgeScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"U\n\x1b\x44isableScriptTriggerRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x12\n\ntrigger_id\x18\x02 \x01(\t\".\n\x1c\x44isableScriptTriggerResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x9a\x01\n\x19\x43onfigureClockModeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12,\n\nclock_mode\x18\x02 \x01(\x0e\x32\x16.nifgen_grpc.ClockModeH\x00\x12\x18\n\x0e\x63lock_mode_raw\x18\x03 \x01(\x11H\x00\x42\x11\n\x0f\x63lock_mode_enum\",\n\x1a\x43onfigureClockModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"d\n%AdjustSampleClockRelativeDelayRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x17\n\x0f\x61\x64justment_time\x18\x02 \x01(\x01\"8\n&AdjustSampleClockRelativeDelayResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"j\n\x17\x41llocateWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x15\n\rwaveform_size\x18\x03 \x01(\x11\"C\n\x18\x41llocateWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11\"\xe7\x01\n#SetWaveformNextWritePositionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12.\n\x0brelative_to\x18\x04 \x01(\x0e\x32\x17.nifgen_grpc.RelativeToH\x00\x12\x19\n\x0frelative_to_raw\x18\x05 \x01(\x11H\x00\x12\x0e\n\x06offset\x18\x06 \x01(\x11\x42\x12\n\x10relative_to_enum\"6\n$SetWaveformNextWritePositionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"w\n\x14WriteWaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\x01\"\'\n\x15WriteWaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x7f\n\x1cWriteBinary16WaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12\x0c\n\x04\x64\x61ta\x18\x04 \x03(\x11\"/\n\x1dWriteBinary16WaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa1\x01\n\x1eWriteWaveformComplexF64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12,\n\x04\x64\x61ta\x18\x03 \x03(\x0b\x32\x1e.nidevice_grpc.NIComplexNumber\x12\x17\n\x0fwaveform_handle\x18\x04 \x01(\x11\"1\n\x1fWriteWaveformComplexF64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa3\x01\n#WriteComplexBinary16WaveformRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x17\n\x0fwaveform_handle\x18\x03 \x01(\x11\x12)\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x1b.nidevice_grpc.NIComplexI16\"6\n$WriteComplexBinary16WaveformResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"4\n\x0eSelfCalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"!\n\x0fSelfCalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"@\n\x1aGetSelfCalSupportedRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"I\n\x1bGetSelfCalSupportedResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12self_cal_supported\x18\x02 \x01(\x08\"F\n GetSelfCalLastDateAndTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"{\n!GetSelfCalLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11\"E\n\x1fGetExtCalLastDateAndTimeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"z\n GetExtCalLastDateAndTimeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0c\n\x04year\x18\x02 \x01(\x11\x12\r\n\x05month\x18\x03 \x01(\x11\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x11\x12\x0c\n\x04hour\x18\x05 \x01(\x11\x12\x0e\n\x06minute\x18\x06 \x01(\x11\"?\n\x19GetSelfCalLastTempRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"A\n\x1aGetSelfCalLastTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\">\n\x18GetExtCalLastTempRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"@\n\x19GetExtCalLastTempResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\"I\n#GetExtCalRecommendedIntervalRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"F\n$GetExtCalRecommendedIntervalResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x0e\n\x06months\x18\x02 \x01(\x11\"C\n\x1dReadCurrentTemperatureRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"E\n\x1eReadCurrentTemperatureResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0btemperature\x18\x02 \x01(\x01\"\x83\x01\n+ConfigureCustomFIRFilterCoefficientsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x1a\n\x12\x63oefficients_array\x18\x03 \x03(\x01\">\n,ConfigureCustomFIRFilterCoefficientsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"[\n\x1fGetFIRFilterCoefficientsRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"s\n GetFIRFilterCoefficientsResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x1a\n\x12\x63oefficients_array\x18\x02 \x03(\x01\x12#\n\x1bnumber_of_coefficients_read\x18\x03 \x01(\x11\"]\n\x1eGetStreamEndpointHandleRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x17\n\x0fstream_endpoint\x18\x02 \x01(\t\"H\n\x1fGetStreamEndpointHandleResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rreader_handle\x18\x02 \x01(\r\"n\n\x1aWriteP2PEndpointI16Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rendpoint_name\x18\x02 \x01(\t\x12\x15\n\rendpoint_data\x18\x03 \x03(\x11\"-\n\x1bWriteP2PEndpointI16Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"{\n\x1f\x43onfigureSynchronizationRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x1e\n\x16synchronization_source\x18\x03 \x01(\x11\"2\n ConfigureSynchronizationResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"Z\n\x1e\x45nableDigitalPatterningRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"1\n\x1f\x45nableDigitalPatterningResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"[\n\x1f\x44isableDigitalPatterningRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"2\n DisableDigitalPatterningResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"V\n\x1a\x45nableDigitalFilterRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"-\n\x1b\x45nableDigitalFilterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"W\n\x1b\x44isableDigitalFilterRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\".\n\x1c\x44isableDigitalFilterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"z\n\x19\x45nableAnalogFilterRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12#\n\x1b\x66ilter_correction_frequency\x18\x03 \x01(\x01\",\n\x1a\x45nableAnalogFilterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"V\n\x1a\x44isableAnalogFilterRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\"-\n\x1b\x44isableAnalogFilterResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"d\n!ConfigureSampleClockSourceRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x1b\n\x13sample_clock_source\x18\x02 \x01(\t\"4\n\"ConfigureSampleClockSourceResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xba\x01\n\x1b\x43onfigureTriggerModeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x30\n\x0ctrigger_mode\x18\x03 \x01(\x0e\x32\x18.nifgen_grpc.TriggerModeH\x00\x12\x1a\n\x10trigger_mode_raw\x18\x04 \x01(\x11H\x00\x42\x13\n\x11trigger_mode_enum\".\n\x1c\x43onfigureTriggerModeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"`\n\'ImportAttributeConfigurationFileRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\":\n(ImportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"`\n\'ExportAttributeConfigurationFileRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x11\n\tfile_path\x18\x02 \x01(\t\":\n(ExportAttributeConfigurationFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"f\n)ImportAttributeConfigurationBufferRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c\"<\n*ImportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"O\n)ExportAttributeConfigurationBufferRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\"S\n*ExportAttributeConfigurationBufferResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x15\n\rconfiguration\x18\x02 \x01(\x0c\"\xa7\x01\n\x1aSetAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x1b\n\x13\x61ttribute_value_raw\x18\x04 \x01(\x03\"-\n\x1bSetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa9\x01\n\x1c\x43heckAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x1b\n\x13\x61ttribute_value_raw\x18\x04 \x01(\x03\"/\n\x1d\x43heckAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8a\x01\n\x1aGetAttributeViInt64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\"F\n\x1bGetAttributeViInt64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x03\"\x85\x02\n\x1aSetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x42\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32\'.nifgen_grpc.NiFgenInt32AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x11H\x00\x42\x16\n\x14\x61ttribute_value_enum\"-\n\x1bSetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x87\x02\n\x1bSetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x43\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32(.nifgen_grpc.NiFgenReal64AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x01H\x00\x42\x16\n\x14\x61ttribute_value_enum\".\n\x1cSetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x94\x02\n\x1bSetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x1d\n\x13\x61ttribute_value_raw\x18\x04 \x01(\tH\x00\x12P\n\x16\x61ttribute_value_mapped\x18\x05 \x01(\x0e\x32..nifgen_grpc.NiFgenStringAttributeValuesMappedH\x00\x42\x16\n\x14\x61ttribute_value_enum\".\n\x1cSetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa5\x01\n\x1cSetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x17\n\x0f\x61ttribute_value\x18\x04 \x01(\x08\"/\n\x1dSetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xbd\x01\n\x1cSetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12/\n\x0f\x61ttribute_value\x18\x04 \x01(\x0b\x32\x16.nidevice_grpc.Session\"/\n\x1dSetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x87\x02\n\x1c\x43heckAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x42\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32\'.nifgen_grpc.NiFgenInt32AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x11H\x00\x42\x16\n\x14\x61ttribute_value_enum\"/\n\x1d\x43heckAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x89\x02\n\x1d\x43heckAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x43\n\x0f\x61ttribute_value\x18\x04 \x01(\x0e\x32(.nifgen_grpc.NiFgenReal64AttributeValuesH\x00\x12\x1d\n\x13\x61ttribute_value_raw\x18\x05 \x01(\x01H\x00\x42\x16\n\x14\x61ttribute_value_enum\"0\n\x1e\x43heckAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x96\x02\n\x1d\x43heckAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x1d\n\x13\x61ttribute_value_raw\x18\x04 \x01(\tH\x00\x12P\n\x16\x61ttribute_value_mapped\x18\x05 \x01(\x0e\x32..nifgen_grpc.NiFgenStringAttributeValuesMappedH\x00\x42\x16\n\x14\x61ttribute_value_enum\"0\n\x1e\x43heckAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xa7\x01\n\x1e\x43heckAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12\x17\n\x0f\x61ttribute_value\x18\x04 \x01(\x08\"1\n\x1f\x43heckAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xbf\x01\n\x1e\x43heckAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\x12/\n\x0f\x61ttribute_value\x18\x04 \x01(\x0b\x32\x16.nidevice_grpc.Session\"1\n\x1f\x43heckAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\x8a\x01\n\x1aGetAttributeViInt32Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\"F\n\x1bGetAttributeViInt32Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x11\"\x8b\x01\n\x1bGetAttributeViReal64Request\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\"G\n\x1cGetAttributeViReal64Response\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x01\"\x8b\x01\n\x1bGetAttributeViStringRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\"G\n\x1cGetAttributeViStringResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\t\"\x8c\x01\n\x1cGetAttributeViBooleanRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\"H\n\x1dGetAttributeViBooleanResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0f\x61ttribute_value\x18\x02 \x01(\x08\"\x8c\x01\n\x1cGetAttributeViSessionRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\"`\n\x1dGetAttributeViSessionResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12/\n\x0f\x61ttribute_value\x18\x02 \x01(\x0b\x32\x16.nidevice_grpc.Session\"\x85\x01\n\x15ResetAttributeRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x32\n\x0c\x61ttribute_id\x18\x03 \x01(\x0e\x32\x1c.nifgen_grpc.NiFgenAttribute\"(\n\x16ResetAttributeResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"Y\n\x1cManualEnableP2PStreamRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x15\n\rendpoint_name\x18\x02 \x01(\t\"/\n\x1dManualEnableP2PStreamResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\"\xba\x01\n CreateWaveformFromFileHWSRequest\x12\"\n\x02vi\x18\x01 \x01(\x0b\x32\x16.nidevice_grpc.Session\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x11\n\tfile_name\x18\x03 \x01(\t\x12\x1e\n\x16use_rate_from_waveform\x18\x04 \x01(\x08\x12)\n!use_gain_and_offset_from_waveform\x18\x05 \x01(\x08\"L\n!CreateWaveformFromFileHWSResponse\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x17\n\x0fwaveform_handle\x18\x02 \x01(\x11*\xa9S\n\x0fNiFgenAttribute\x12 \n\x1cNIFGEN_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\"\n\x1cNIFGEN_ATTRIBUTE_OUTPUT_MODE\x10\xd1\xa5L\x12%\n\x1fNIFGEN_ATTRIBUTE_OUTPUT_ENABLED\x10\xd3\xa5L\x12#\n\x1dNIFGEN_ATTRIBUTE_DIGITAL_GAIN\x10\xae\x9a\x46\x12\"\n\x1cNIFGEN_ATTRIBUTE_ANALOG_PATH\x10\x8e\x9a\x46\x12%\n\x1fNIFGEN_ATTRIBUTE_LOAD_IMPEDANCE\x10\x8c\x9a\x46\x12\'\n!NIFGEN_ATTRIBUTE_OUTPUT_IMPEDANCE\x10\xd4\xa5L\x12-\n\'NIFGEN_ATTRIBUTE_TERMINAL_CONFIGURATION\x10\x9d\x9b\x46\x12)\n#NIFGEN_ATTRIBUTE_COMMON_MODE_OFFSET\x10\x9e\x9b\x46\x12$\n\x1eNIFGEN_ATTRIBUTE_CHANNEL_DELAY\x10\xa1\x9b\x46\x12%\n\x1fNIFGEN_ATTRIBUTE_ABSOLUTE_DELAY\x10\xcd\x9b\x46\x12,\n&NIFGEN_ATTRIBUTE_ANALOG_FILTER_ENABLED\x10\x97\x99\x46\x12-\n\'NIFGEN_ATTRIBUTE_DIGITAL_FILTER_ENABLED\x10\x96\x99\x46\x12:\n4NIFGEN_ATTRIBUTE_DIGITAL_FILTER_INTERPOLATION_FACTOR\x10\x8a\x9a\x46\x12\x32\n,NIFGEN_ATTRIBUTE_FLATNESS_CORRECTION_ENABLED\x10\xf3\x9a\x46\x12\'\n!NIFGEN_ATTRIBUTE_ANALOG_DATA_MASK\x10\x9a\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_ANALOG_STATIC_VALUE\x10\x9b\x9a\x46\x12(\n\"NIFGEN_ATTRIBUTE_DIGITAL_DATA_MASK\x10\x9c\x9a\x46\x12+\n%NIFGEN_ATTRIBUTE_DIGITAL_STATIC_VALUE\x10\x9d\x9a\x46\x12.\n(NIFGEN_ATTRIBUTE_DIGITAL_PATTERN_ENABLED\x10\x95\x99\x46\x12(\n\"NIFGEN_ATTRIBUTE_AUX_POWER_ENABLED\x10\xcb\x9b\x46\x12$\n\x1eNIFGEN_ATTRIBUTE_IDLE_BEHAVIOR\x10\xa9\x9b\x46\x12!\n\x1bNIFGEN_ATTRIBUTE_IDLE_VALUE\x10\xaa\x9b\x46\x12$\n\x1eNIFGEN_ATTRIBUTE_WAIT_BEHAVIOR\x10\xab\x9b\x46\x12!\n\x1bNIFGEN_ATTRIBUTE_WAIT_VALUE\x10\xac\x9b\x46\x12\x1f\n\x19NIFGEN_ATTRIBUTE_ARB_GAIN\x10\x9a\xa7L\x12!\n\x1bNIFGEN_ATTRIBUTE_ARB_OFFSET\x10\x9b\xa7L\x12\'\n!NIFGEN_ATTRIBUTE_WAVEFORM_QUANTUM\x10\x9e\xa7L\x12(\n\"NIFGEN_ATTRIBUTE_MAX_NUM_WAVEFORMS\x10\x9d\xa7L\x12(\n\"NIFGEN_ATTRIBUTE_MIN_WAVEFORM_SIZE\x10\x9f\xa7L\x12(\n\"NIFGEN_ATTRIBUTE_MAX_WAVEFORM_SIZE\x10\xa0\xa7L\x12*\n$NIFGEN_ATTRIBUTE_ARB_WAVEFORM_HANDLE\x10\x99\xa7L\x12*\n$NIFGEN_ATTRIBUTE_ARB_MARKER_POSITION\x10\xf7\x9a\x46\x12\'\n!NIFGEN_ATTRIBUTE_ARB_REPEAT_COUNT\x10\xf8\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_ARB_SEQUENCE_HANDLE\x10\xa3\xa7L\x12(\n\"NIFGEN_ATTRIBUTE_MAX_NUM_SEQUENCES\x10\xa4\xa7L\x12*\n$NIFGEN_ATTRIBUTE_MIN_SEQUENCE_LENGTH\x10\xa5\xa7L\x12*\n$NIFGEN_ATTRIBUTE_MAX_SEQUENCE_LENGTH\x10\xa6\xa7L\x12%\n\x1fNIFGEN_ATTRIBUTE_MAX_LOOP_COUNT\x10\xa7\xa7L\x12)\n#NIFGEN_ATTRIBUTE_SCRIPT_TO_GENERATE\x10\xbe\x9a\x46\x12/\n)NIFGEN_ATTRIBUTE_FILE_TRANSFER_BLOCK_SIZE\x10\xa0\x9a\x46\x12/\n)NIFGEN_ATTRIBUTE_DATA_TRANSFER_BLOCK_SIZE\x10\xa1\x9a\x46\x12\x36\n0NIFGEN_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_BANDWIDTH\x10\xa5\x9b\x46\x12)\n#NIFGEN_ATTRIBUTE_DIRECT_DMA_ENABLED\x10\xa4\x9a\x46\x12-\n\'NIFGEN_ATTRIBUTE_DIRECT_DMA_WINDOW_SIZE\x10\xa5\x9a\x46\x12\x30\n*NIFGEN_ATTRIBUTE_DIRECT_DMA_WINDOW_ADDRESS\x10\xc2\x9a\x46\x12.\n(NIFGEN_ATTRIBUTE_STREAMING_WAVEFORM_NAME\x10\xf6\x9a\x46\x12\x30\n*NIFGEN_ATTRIBUTE_STREAMING_WAVEFORM_HANDLE\x10\xf4\x9a\x46\x12<\n6NIFGEN_ATTRIBUTE_STREAMING_SPACE_AVAILABLE_IN_WAVEFORM\x10\xf5\x9a\x46\x12.\n(NIFGEN_ATTRIBUTE_STREAMING_WRITE_TIMEOUT\x10\xc9\x9b\x46\x12:\n4NIFGEN_ATTRIBUTE_DATA_TRANSFER_PREFERRED_PACKET_SIZE\x10\xa6\x9b\x46\x12<\n6NIFGEN_ATTRIBUTE_DATA_TRANSFER_MAXIMUM_IN_FLIGHT_READS\x10\xa7\x9b\x46\x12\x34\n.NIFGEN_ATTRIBUTE_PCI_DMA_OPTIMIZATIONS_ENABLED\x10\x9a\x9b\x46\x12\"\n\x1cNIFGEN_ATTRIBUTE_OSP_ENABLED\x10\xa6\x9a\x46\x12\"\n\x1cNIFGEN_ATTRIBUTE_OSP_IQ_RATE\x10\xa8\x9a\x46\x12/\n)NIFGEN_ATTRIBUTE_OSP_DATA_PROCESSING_MODE\x10\xa7\x9a\x46\x12\x1f\n\x19NIFGEN_ATTRIBUTE_OSP_MODE\x10\xa2\x9b\x46\x12*\n$NIFGEN_ATTRIBUTE_OSP_FREQUENCY_SHIFT\x10\xa3\x9b\x46\x12*\n$NIFGEN_ATTRIBUTE_OSP_CARRIER_ENABLED\x10\xa9\x9a\x46\x12,\n&NIFGEN_ATTRIBUTE_OSP_CARRIER_FREQUENCY\x10\xaa\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_OSP_CARRIER_PHASE_I\x10\xab\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_OSP_CARRIER_PHASE_Q\x10\xac\x9a\x46\x12<\n6NIFGEN_ATTRIBUTE_OSP_COMPENSATE_FOR_FILTER_GROUP_DELAY\x10\xb5\x9b\x46\x12*\n$NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_TYPE\x10\xad\x9a\x46\x12-\n\'NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_ENABLED\x10\xaf\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_INTERPOLATION\x10\xb0\x9a\x46\x12-\n\'NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_ENABLED\x10\xb1\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_INTERPOLATION\x10\xb2\x9a\x46\x12>\n8NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_ROOT_RAISED_COSINE_ALPHA\x10\xb3\x9a\x46\x12\x39\n3NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_RAISED_COSINE_ALPHA\x10\xb4\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_FLAT_PASSBAND\x10\xb5\x9a\x46\x12\x31\n+NIFGEN_ATTRIBUTE_OSP_FIR_FILTER_GAUSSIAN_BT\x10\xb6\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_OSP_CIC_FILTER_GAIN\x10\xb7\x9a\x46\x12,\n&NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_GAIN_I\x10\xb8\x9a\x46\x12,\n&NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_GAIN_Q\x10\xb9\x9a\x46\x12.\n(NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_OFFSET_I\x10\xba\x9a\x46\x12.\n(NIFGEN_ATTRIBUTE_OSP_PRE_FILTER_OFFSET_Q\x10\xbb\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_OSP_OVERFLOW_ERROR_REPORTING\x10\xbc\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_OSP_OVERFLOW_STATUS\x10\xbd\x9a\x46\x12\"\n\x1cNIFGEN_ATTRIBUTE_P2P_ENABLED\x10\xb7\x9b\x46\x12/\n)NIFGEN_ATTRIBUTE_P2P_DESTINATION_CHANNELS\x10\xb8\x9b\x46\x12(\n\"NIFGEN_ATTRIBUTE_P2P_ENDPOINT_SIZE\x10\xb9\x9b\x46\x12\x36\n0NIFGEN_ATTRIBUTE_P2P_SPACE_AVAILABLE_IN_ENDPOINT\x10\xba\x9b\x46\x12;\n5NIFGEN_ATTRIBUTE_P2P_MOST_SPACE_AVAILABLE_IN_ENDPOINT\x10\xbb\x9b\x46\x12)\n#NIFGEN_ATTRIBUTE_P2P_ENDPOINT_COUNT\x10\xbc\x9b\x46\x12<\n6NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INTERVAL\x10\xc0\x9b\x46\x12\x43\n=NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_INITIAL_CREDITS\x10\xc8\x9b\x46\x12\x37\n1NIFGEN_ATTRIBUTE_P2P_MANUAL_CONFIGURATION_ENABLED\x10\xbd\x9b\x46\x12;\n5NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_ADDRESS\x10\xbe\x9b\x46\x12@\n:NIFGEN_ATTRIBUTE_P2P_DATA_TRANSFER_PERMISSION_ADDRESS_TYPE\x10\xbf\x9b\x46\x12\x32\n,NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_ADDRESS\x10\xc1\x9b\x46\x12\x37\n1NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_ADDRESS_TYPE\x10\xc2\x9b\x46\x12/\n)NIFGEN_ATTRIBUTE_P2P_ENDPOINT_WINDOW_SIZE\x10\xc3\x9b\x46\x12@\n:NIFGEN_ATTRIBUTE_P2P_ENDPOINT_FULLNESS_START_TRIGGER_LEVEL\x10\xca\x9b\x46\x12\x34\n.NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_ADDRESS\x10\xc5\x9b\x46\x12\x39\n3NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_ADDRESS_TYPE\x10\xc6\x9b\x46\x12\x32\n,NIFGEN_ATTRIBUTE_P2P_DONE_NOTIFICATION_VALUE\x10\xc7\x9b\x46\x12$\n\x1eNIFGEN_ATTRIBUTE_FUNC_WAVEFORM\x10\xb5\xa6L\x12%\n\x1fNIFGEN_ATTRIBUTE_FUNC_AMPLITUDE\x10\xb6\xa6L\x12%\n\x1fNIFGEN_ATTRIBUTE_FUNC_DC_OFFSET\x10\xb7\xa6L\x12\'\n!NIFGEN_ATTRIBUTE_FUNC_START_PHASE\x10\xb9\xa6L\x12+\n%NIFGEN_ATTRIBUTE_FUNC_DUTY_CYCLE_HIGH\x10\xba\xa6L\x12+\n%NIFGEN_ATTRIBUTE_SYNC_DUTY_CYCLE_HIGH\x10\x99\x99\x46\x12/\n)NIFGEN_ATTRIBUTE_SYNC_OUT_OUTPUT_TERMINAL\x10\xfa\x9a\x46\x12%\n\x1fNIFGEN_ATTRIBUTE_FUNC_FREQUENCY\x10\xb8\xa6L\x12\'\n!NIFGEN_ATTRIBUTE_FUNC_BUFFER_SIZE\x10\x9e\x9a\x46\x12+\n%NIFGEN_ATTRIBUTE_FUNC_MAX_BUFFER_SIZE\x10\x9f\x9a\x46\x12\'\n!NIFGEN_ATTRIBUTE_FREQ_LIST_HANDLE\x10\x80\x9a\x46\x12)\n#NIFGEN_ATTRIBUTE_MAX_NUM_FREQ_LISTS\x10\x81\x9a\x46\x12+\n%NIFGEN_ATTRIBUTE_MIN_FREQ_LIST_LENGTH\x10\x82\x9a\x46\x12+\n%NIFGEN_ATTRIBUTE_MAX_FREQ_LIST_LENGTH\x10\x83\x9a\x46\x12-\n\'NIFGEN_ATTRIBUTE_MIN_FREQ_LIST_DURATION\x10\x84\x9a\x46\x12-\n\'NIFGEN_ATTRIBUTE_MAX_FREQ_LIST_DURATION\x10\x85\x9a\x46\x12\x31\n+NIFGEN_ATTRIBUTE_FREQ_LIST_DURATION_QUANTUM\x10\x86\x9a\x46\x12-\n\'NIFGEN_ATTRIBUTE_REFERENCE_CLOCK_SOURCE\x10\xa1\x99\x46\x12*\n$NIFGEN_ATTRIBUTE_REF_CLOCK_FREQUENCY\x10\x9b\x99\x46\x12?\n9NIFGEN_ATTRIBUTE_EXPORTED_REFERENCE_CLOCK_OUTPUT_TERMINAL\x10\xf1\x9a\x46\x12G\nANIFGEN_ATTRIBUTE_EXPORTED_ONBOARD_REFERENCE_CLOCK_OUTPUT_TERMINAL\x10\xf2\x9a\x46\x12&\n NIFGEN_ATTRIBUTE_ARB_SAMPLE_RATE\x10\x9c\xa7L\x12!\n\x1bNIFGEN_ATTRIBUTE_CLOCK_MODE\x10\x9e\x99\x46\x12*\n$NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_SOURCE\x10\xa0\x99\x46\x12<\n6NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_OUTPUT_TERMINAL\x10\xf0\x9a\x46\x12\x34\n.NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_DIVISOR\x10\x8b\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_TIMEBASE_SOURCE\x10\x9f\x9b\x46\x12\x31\n+NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_TIMEBASE_RATE\x10\xa0\x9b\x46\x12\x45\n?NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_TIMEBASE_OUTPUT_TERMINAL\x10\xf9\x9a\x46\x12=\n7NIFGEN_ATTRIBUTE_EXPORTED_SAMPLE_CLOCK_TIMEBASE_DIVISOR\x10\x96\x9a\x46\x12\x37\n1NIFGEN_ATTRIBUTE_EXTERNAL_SAMPLE_CLOCK_MULTIPLIER\x10\xa8\x9b\x46\x12\x32\n,NIFGEN_ATTRIBUTE_SAMPLE_CLOCK_ABSOLUTE_DELAY\x10\x97\x9a\x46\x12\x31\n+NIFGEN_ATTRIBUTE_OSCILLATOR_PHASE_DAC_VALUE\x10\x98\x9a\x46\x12\x38\n2NIFGEN_ATTRIBUTE_EXTERNAL_CLOCK_DELAY_BINARY_VALUE\x10\x99\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_TERMINAL\x10\xe8\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_MARKER_EVENT_OUTPUT_BEHAVIOR\x10\x86\x9b\x46\x12\x32\n,NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_POLARITY\x10\xe9\x9a\x46\x12/\n)NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH\x10\x84\x9b\x46\x12\x35\n/NIFGEN_ATTRIBUTE_MARKER_EVENT_PULSE_WIDTH_UNITS\x10\x85\x9b\x46\x12\x38\n2NIFGEN_ATTRIBUTE_MARKER_EVENT_TOGGLE_INITIAL_STATE\x10\x87\x9b\x46\x12)\n#NIFGEN_ATTRIBUTE_MARKER_EVENT_DELAY\x10\x92\x9b\x46\x12/\n)NIFGEN_ATTRIBUTE_MARKER_EVENT_DELAY_UNITS\x10\x93\x9b\x46\x12\x34\n.NIFGEN_ATTRIBUTE_ALL_MARKER_EVENTS_LIVE_STATUS\x10\x88\x9b\x46\x12/\n)NIFGEN_ATTRIBUTE_MARKER_EVENT_LIVE_STATUS\x10\x89\x9b\x46\x12\x37\n1NIFGEN_ATTRIBUTE_ALL_MARKER_EVENTS_LATCHED_STATUS\x10\x8d\x9b\x46\x12\x32\n,NIFGEN_ATTRIBUTE_MARKER_EVENT_LATCHED_STATUS\x10\x8e\x9b\x46\x12\x38\n2NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_DATA_BIT_NUMBER\x10\x81\x9b\x46\x12\x37\n1NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_LEVEL_POLARITY\x10\x82\x9b\x46\x12\x38\n2NIFGEN_ATTRIBUTE_DATA_MARKER_EVENT_OUTPUT_TERMINAL\x10\x83\x9b\x46\x12<\n6NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_OUTPUT_TERMINAL\x10\xe6\x9a\x46\x12?\n9NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_LEVEL_ACTIVE_LEVEL\x10\xe7\x9a\x46\x12\x38\n2NIFGEN_ATTRIBUTE_READY_FOR_START_EVENT_LIVE_STATUS\x10\x8c\x9b\x46\x12\x34\n.NIFGEN_ATTRIBUTE_STARTED_EVENT_OUTPUT_TERMINAL\x10\xea\x9a\x46\x12\x34\n.NIFGEN_ATTRIBUTE_STARTED_EVENT_OUTPUT_BEHAVIOR\x10\xfb\x9a\x46\x12\x37\n1NIFGEN_ATTRIBUTE_STARTED_EVENT_LEVEL_ACTIVE_LEVEL\x10\xec\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_POLARITY\x10\xee\x9a\x46\x12\x36\n0NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_WIDTH_UNITS\x10\xfd\x9a\x46\x12\x30\n*NIFGEN_ATTRIBUTE_STARTED_EVENT_PULSE_WIDTH\x10\xff\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_STARTED_EVENT_DELAY\x10\x94\x9b\x46\x12\x30\n*NIFGEN_ATTRIBUTE_STARTED_EVENT_DELAY_UNITS\x10\x95\x9b\x46\x12\x33\n-NIFGEN_ATTRIBUTE_STARTED_EVENT_LATCHED_STATUS\x10\x90\x9b\x46\x12\x31\n+NIFGEN_ATTRIBUTE_DONE_EVENT_OUTPUT_TERMINAL\x10\xeb\x9a\x46\x12\x31\n+NIFGEN_ATTRIBUTE_DONE_EVENT_OUTPUT_BEHAVIOR\x10\xfc\x9a\x46\x12\x34\n.NIFGEN_ATTRIBUTE_DONE_EVENT_LEVEL_ACTIVE_LEVEL\x10\xed\x9a\x46\x12\x30\n*NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_POLARITY\x10\xef\x9a\x46\x12\x33\n-NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_WIDTH_UNITS\x10\xfe\x9a\x46\x12-\n\'NIFGEN_ATTRIBUTE_DONE_EVENT_PULSE_WIDTH\x10\x80\x9b\x46\x12\'\n!NIFGEN_ATTRIBUTE_DONE_EVENT_DELAY\x10\x96\x9b\x46\x12-\n\'NIFGEN_ATTRIBUTE_DONE_EVENT_DELAY_UNITS\x10\x97\x9b\x46\x12\x30\n*NIFGEN_ATTRIBUTE_DONE_EVENT_LATCHED_STATUS\x10\x8f\x9b\x46\x12#\n\x1dNIFGEN_ATTRIBUTE_TRIGGER_MODE\x10\x9c\x99\x46\x12\"\n\x1cNIFGEN_ATTRIBUTE_BURST_COUNT\x10\xae\xa8L\x12)\n#NIFGEN_ATTRIBUTE_START_TRIGGER_TYPE\x10\xc8\x9a\x46\x12\x38\n2NIFGEN_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_SOURCE\x10\xc9\x9a\x46\x12\x36\n0NIFGEN_ATTRIBUTE_DIGITAL_EDGE_START_TRIGGER_EDGE\x10\xca\x9a\x46\x12=\n7NIFGEN_ATTRIBUTE_EXPORTED_START_TRIGGER_OUTPUT_TERMINAL\x10\xcb\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_SCRIPT_TRIGGER_TYPE\x10\xd2\x9a\x46\x12\x39\n3NIFGEN_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_SOURCE\x10\xd3\x9a\x46\x12\x37\n1NIFGEN_ATTRIBUTE_DIGITAL_EDGE_SCRIPT_TRIGGER_EDGE\x10\xd4\x9a\x46\x12:\n4NIFGEN_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_SOURCE\x10\xd5\x9a\x46\x12@\n:NIFGEN_ATTRIBUTE_DIGITAL_LEVEL_SCRIPT_TRIGGER_ACTIVE_LEVEL\x10\xd6\x9a\x46\x12>\n8NIFGEN_ATTRIBUTE_EXPORTED_SCRIPT_TRIGGER_OUTPUT_TERMINAL\x10\xd7\x9a\x46\x12\x1f\n\x19NIFGEN_ATTRIBUTE_BUS_TYPE\x10\x87\x9a\x46\x12\"\n\x1cNIFGEN_ATTRIBUTE_MEMORY_SIZE\x10\xa2\x9a\x46\x12$\n\x1eNIFGEN_ATTRIBUTE_SERIAL_NUMBER\x10\xa3\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_MARKER_EVENTS_COUNT\x10\xbf\x9a\x46\x12/\n)NIFGEN_ATTRIBUTE_DATA_MARKER_EVENTS_COUNT\x10\xc1\x9a\x46\x12,\n&NIFGEN_ATTRIBUTE_SCRIPT_TRIGGERS_COUNT\x10\xc0\x9a\x46\x12*\n$NIFGEN_ATTRIBUTE_VIDEO_WAVEFORM_TYPE\x10\x88\x9a\x46\x12(\n\"NIFGEN_ATTRIBUTE_FPGA_BITFILE_PATH\x10\xcc\x9b\x46\x12\x32\n,NIFGEN_ATTRIBUTE_FILTER_CORRECTION_FREQUENCY\x10\x98\x99\x46\x12%\n\x1fNIFGEN_ATTRIBUTE_TRIGGER_SOURCE\x10\xfe\xa7L\x12&\n NIFGEN_ATTRIBUTE_SYNCHRONIZATION\x10\x9f\x99\x46\x12(\n\"NIFGEN_ATTRIBUTE_ID_QUERY_RESPONSE\x10\xb1\x98\x46\x12%\n\x1fNIFGEN_ATTRIBUTE_GAIN_DAC_VALUE\x10\x8f\x9a\x46\x12\'\n!NIFGEN_ATTRIBUTE_OFFSET_DAC_VALUE\x10\x90\x9a\x46\x12\x30\n*NIFGEN_ATTRIBUTE_OSCILLATOR_FREQ_DAC_VALUE\x10\x91\x9a\x46\x12\x30\n*NIFGEN_ATTRIBUTE_PRE_AMPLIFIER_ATTENUATION\x10\x94\x9a\x46\x12\x31\n+NIFGEN_ATTRIBUTE_POST_AMPLIFIER_ATTENUATION\x10\x95\x9a\x46\x12\x1c\n\x16NIFGEN_ATTRIBUTE_CACHE\x10\x94\x8b@\x12\"\n\x1cNIFGEN_ATTRIBUTE_RANGE_CHECK\x10\x92\x8b@\x12.\n(NIFGEN_ATTRIBUTE_QUERY_INSTRUMENT_STATUS\x10\x93\x8b@\x12\'\n!NIFGEN_ATTRIBUTE_RECORD_COERCIONS\x10\x96\x8b@\x12\x1f\n\x19NIFGEN_ATTRIBUTE_SIMULATE\x10\x95\x8b@\x12(\n\"NIFGEN_ATTRIBUTE_INTERCHANGE_CHECK\x10\xa5\x8b@\x12\x32\n,NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_DESCRIPTION\x10\x92\x8f@\x12-\n\'NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_PREFIX\x10\xbe\x8d@\x12-\n\'NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_VENDOR\x10\x91\x8f@\x12/\n)NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_REVISION\x10\xb7\x8f@\x12?\n9NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MAJOR_VERSION\x10\x93\x8f@\x12?\n9NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_CLASS_SPEC_MINOR_VERSION\x10\x94\x8f@\x12\x32\n,NIFGEN_ATTRIBUTE_SUPPORTED_INSTRUMENT_MODELS\x10\xd7\x8d@\x12)\n#NIFGEN_ATTRIBUTE_GROUP_CAPABILITIES\x10\xa1\x8e@\x12$\n\x1eNIFGEN_ATTRIBUTE_CHANNEL_COUNT\x10\xdb\x8c@\x12.\n(NIFGEN_ATTRIBUTE_INSTRUMENT_MANUFACTURER\x10\x8f\x8f@\x12\'\n!NIFGEN_ATTRIBUTE_INSTRUMENT_MODEL\x10\x90\x8f@\x12\x33\n-NIFGEN_ATTRIBUTE_INSTRUMENT_FIRMWARE_REVISION\x10\x8e\x8f@\x12&\n NIFGEN_ATTRIBUTE_MODULE_REVISION\x10\xb6\x9b\x46\x12-\n\'NIFGEN_ATTRIBUTE_IO_RESOURCE_DESCRIPTOR\x10\xc0\x8d@\x12#\n\x1dNIFGEN_ATTRIBUTE_LOGICAL_NAME\x10\xc1\x8d@\x12#\n\x1dNIFGEN_ATTRIBUTE_DRIVER_SETUP\x10\x97\x8b@\x12\x34\n.NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_MAJOR_VERSION\x10\x87\x8f@\x12\x34\n.NIFGEN_ATTRIBUTE_SPECIFIC_DRIVER_MINOR_VERSION\x10\x88\x8f@\x12*\n$NIFGEN_ATTRIBUTE_UPDATE_CLOCK_SOURCE\x10\x9a\x99\x46*\xd9\x01\n\nOutputMode\x12&\n\"OUTPUT_MODE_NIFGEN_VAL_OUTPUT_FUNC\x10\x00\x12%\n!OUTPUT_MODE_NIFGEN_VAL_OUTPUT_ARB\x10\x01\x12%\n!OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SEQ\x10\x02\x12+\n\'OUTPUT_MODE_NIFGEN_VAL_OUTPUT_FREQ_LIST\x10\x65\x12(\n$OUTPUT_MODE_NIFGEN_VAL_OUTPUT_SCRIPT\x10\x66*\xc1\x02\n\x08Waveform\x12\x18\n\x14WAVEFORM_UNSPECIFIED\x10\x00\x12 \n\x1cWAVEFORM_NIFGEN_VAL_WFM_SINE\x10\x01\x12\"\n\x1eWAVEFORM_NIFGEN_VAL_WFM_SQUARE\x10\x02\x12$\n WAVEFORM_NIFGEN_VAL_WFM_TRIANGLE\x10\x03\x12#\n\x1fWAVEFORM_NIFGEN_VAL_WFM_RAMP_UP\x10\x04\x12%\n!WAVEFORM_NIFGEN_VAL_WFM_RAMP_DOWN\x10\x05\x12\x1e\n\x1aWAVEFORM_NIFGEN_VAL_WFM_DC\x10\x06\x12!\n\x1dWAVEFORM_NIFGEN_VAL_WFM_NOISE\x10\x65\x12 \n\x1cWAVEFORM_NIFGEN_VAL_WFM_USER\x10\x66*\xa0\x04\n\x06Signal\x12\x16\n\x12SIGNAL_UNSPECIFIED\x10\x00\x12.\n)SIGNAL_NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK\x10\xfb\x07\x12\x1f\n\x1aSIGNAL_NIFGEN_VAL_SYNC_OUT\x10\xea\x07\x12$\n\x1fSIGNAL_NIFGEN_VAL_START_TRIGGER\x10\xec\x07\x12#\n\x1eSIGNAL_NIFGEN_VAL_MARKER_EVENT\x10\xe9\x07\x12,\n\'SIGNAL_NIFGEN_VAL_SAMPLE_CLOCK_TIMEBASE\x10\xee\x07\x12&\n!SIGNAL_NIFGEN_VAL_SYNCHRONIZATION\x10\xef\x07\x12\"\n\x1eSIGNAL_NIFGEN_VAL_SAMPLE_CLOCK\x10\x65\x12%\n!SIGNAL_NIFGEN_VAL_REFERENCE_CLOCK\x10\x66\x12$\n SIGNAL_NIFGEN_VAL_SCRIPT_TRIGGER\x10g\x12+\n\'SIGNAL_NIFGEN_VAL_READY_FOR_START_EVENT\x10i\x12#\n\x1fSIGNAL_NIFGEN_VAL_STARTED_EVENT\x10j\x12 \n\x1cSIGNAL_NIFGEN_VAL_DONE_EVENT\x10k\x12\'\n#SIGNAL_NIFGEN_VAL_DATA_MARKER_EVENT\x10l*\xbf\x01\n\x0bTriggerMode\x12\x1c\n\x18TRIGGER_MODE_UNSPECIFIED\x10\x00\x12\"\n\x1eTRIGGER_MODE_NIFGEN_VAL_SINGLE\x10\x01\x12&\n\"TRIGGER_MODE_NIFGEN_VAL_CONTINUOUS\x10\x02\x12#\n\x1fTRIGGER_MODE_NIFGEN_VAL_STEPPED\x10\x03\x12!\n\x1dTRIGGER_MODE_NIFGEN_VAL_BURST\x10\x04*\x82\x01\n\tClockMode\x12)\n%CLOCK_MODE_NIFGEN_VAL_HIGH_RESOLUTION\x10\x00\x12%\n!CLOCK_MODE_NIFGEN_VAL_DIVIDE_DOWN\x10\x01\x12#\n\x1f\x43LOCK_MODE_NIFGEN_VAL_AUTOMATIC\x10\x02*v\n\nRelativeTo\x12\x32\n.RELATIVE_TO_NIFGEN_VAL_WAVEFORM_POSITION_START\x10\x00\x12\x34\n0RELATIVE_TO_NIFGEN_VAL_WAVEFORM_POSITION_CURRENT\x10\x01*\xe8\x01\n\rHardwareState\x12\"\n\x1eHARDWARE_STATE_NIFGEN_VAL_IDLE\x10\x00\x12\x37\n3HARDWARE_STATE_NIFGEN_VAL_WAITING_FOR_START_TRIGGER\x10\x64\x12&\n!HARDWARE_STATE_NIFGEN_VAL_RUNNING\x10\xc8\x01\x12#\n\x1eHARDWARE_STATE_NIFGEN_VAL_DONE\x10\xd8\x04\x12-\n(HARDWARE_STATE_NIFGEN_VAL_HARDWARE_ERROR\x10\xe8\x07*Z\n\tByteOrder\x12\'\n#BYTE_ORDER_NIFGEN_VAL_LITTLE_ENDIAN\x10\x00\x12$\n BYTE_ORDER_NIFGEN_VAL_BIG_ENDIAN\x10\x01*|\n\x0bTriggerWhen\x12\x1c\n\x18TRIGGER_WHEN_UNSPECIFIED\x10\x00\x12\'\n#TRIGGER_WHEN_NIFGEN_VAL_ACTIVE_HIGH\x10\x65\x12&\n\"TRIGGER_WHEN_NIFGEN_VAL_ACTIVE_LOW\x10\x66*p\n\x07Trigger\x12\x17\n\x13TRIGGER_UNSPECIFIED\x10\x00\x12%\n TRIGGER_NIFGEN_VAL_START_TRIGGER\x10\xec\x07\x12%\n!TRIGGER_NIFGEN_VAL_SCRIPT_TRIGGER\x10g*y\n\x14\x46requencyListOptions\x12&\n\"FREQUENCY_LIST_OPTIONS_UNSPECIFIED\x10\x00\x12\x39\n,FREQUENCY_LIST_OPTIONS_NIFGEN_VAL_ALL_FLISTS\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\x89\x07\n\x0fRouteSignalFrom\x12!\n\x1dROUTE_SIGNAL_FROM_UNSPECIFIED\x10\x00\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_MARKER\x10\xe9\x07\x12*\n%ROUTE_SIGNAL_FROM_NIFGEN_VAL_SYNC_OUT\x10\xea\x07\x12\x33\n.ROUTE_SIGNAL_FROM_NIFGEN_VAL_OUT_START_TRIGGER\x10\xec\x07\x12-\n(ROUTE_SIGNAL_FROM_NIFGEN_VAL_BOARD_CLOCK\x10\xee\x07\x12\x31\n,ROUTE_SIGNAL_FROM_NIFGEN_VAL_SYNCHRONIZATION\x10\xef\x07\x12.\n*ROUTE_SIGNAL_FROM_NIFGEN_VAL_SOFTWARE_TRIG\x10\x02\x12)\n$ROUTE_SIGNAL_FROM_NIFGEN_VAL_REF_OUT\x10\xf0\x07\x12+\n&ROUTE_SIGNAL_FROM_NIFGEN_VAL_CLOCK_OUT\x10\xf1\x07\x12*\n%ROUTE_SIGNAL_FROM_NIFGEN_VAL_PXI_STAR\x10\x83\x01\x12\'\n\"ROUTE_SIGNAL_FROM_NIFGEN_VAL_PFI_0\x10\xf3\x07\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_0\x10\x8d\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_1\x10\x8e\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_2\x10\x8f\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_3\x10\x90\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_4\x10\x91\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_5\x10\x92\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_6\x10\x93\x01\x12(\n#ROUTE_SIGNAL_FROM_NIFGEN_VAL_RTSI_7\x10\xf2\x07\x12\x39\n4ROUTE_SIGNAL_FROM_NIFGEN_VAL_ONBOARD_REFERENCE_CLOCK\x10\xfb\x07*\x91\x04\n\rRouteSignalTo\x12\x1f\n\x1bROUTE_SIGNAL_TO_UNSPECIFIED\x10\x00\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_0\x10\x8d\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_1\x10\x8e\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_2\x10\x8f\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_3\x10\x90\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_4\x10\x91\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_5\x10\x92\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_6\x10\x93\x01\x12&\n!ROUTE_SIGNAL_TO_NIFGEN_VAL_RTSI_7\x10\xf2\x07\x12\'\n\"ROUTE_SIGNAL_TO_NIFGEN_VAL_REF_OUT\x10\xf0\x07\x12%\n ROUTE_SIGNAL_TO_NIFGEN_VAL_PFI_0\x10\xf3\x07\x12%\n ROUTE_SIGNAL_TO_NIFGEN_VAL_PFI_1\x10\xf4\x07\x12(\n#ROUTE_SIGNAL_TO_NIFGEN_VAL_PXI_STAR\x10\x83\x01*h\n\x0eSequenceHandle\x12\x1f\n\x1bSEQUENCE_HANDLE_UNSPECIFIED\x10\x00\x12\x35\n(SEQUENCE_HANDLE_NIFGEN_VAL_ALL_SEQUENCES\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*h\n\x0eWaveformHandle\x12\x1f\n\x1bWAVEFORM_HANDLE_UNSPECIFIED\x10\x00\x12\x35\n(WAVEFORM_HANDLE_NIFGEN_VAL_ALL_WAVEFORMS\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01*\xc1Q\n\x1aNiFgenInt32AttributeValues\x12\x1c\n\x18NIFGEN_INT32_UNSPECIFIED\x10\x00\x12/\n+NIFGEN_INT32_ADDRESS_TYPE_VAL_ADDR_PHYSICAL\x10\x00\x12.\n*NIFGEN_INT32_ADDRESS_TYPE_VAL_ADDR_VIRTUAL\x10\x01\x12\x31\n-NIFGEN_INT32_ANALOG_PATH_VAL_MAIN_ANALOG_PATH\x10\x00\x12\x33\n/NIFGEN_INT32_ANALOG_PATH_VAL_DIRECT_ANALOG_PATH\x10\x01\x12;\n7NIFGEN_INT32_ANALOG_PATH_VAL_FIXED_LOW_GAIN_ANALOG_PATH\x10\x02\x12<\n8NIFGEN_INT32_ANALOG_PATH_VAL_FIXED_HIGH_GAIN_ANALOG_PATH\x10\x03\x12\x46\n@NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_FIRST_SEQUENCE_HANDLE\x10\xa0\x8d\x06\x12\x45\n?NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_LAST_SEQUENCE_HANDLE\x10\xaf\xdb\x06\x12\x43\n6NIFGEN_INT32_ARBITRARY_SEQUENCE_HANDLE_VAL_NO_SEQUENCE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x45\n@NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_FIRST_WAVEFORM_HANDLE\x10\x90N\x12\x44\n?NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_LAST_WAVEFORM_HANDLE\x10\xf7U\x12\x43\n6NIFGEN_INT32_ARBITRARY_WAVEFORM_HANDLE_VAL_NO_WAVEFORM\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12=\n0NIFGEN_INT32_BURST_COUNT_VAL_GENERATE_CONTINUOUS\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12)\n%NIFGEN_INT32_BUS_TYPE_VAL_BUS_INVALID\x10\x00\x12$\n NIFGEN_INT32_BUS_TYPE_VAL_BUS_AT\x10\x01\x12%\n!NIFGEN_INT32_BUS_TYPE_VAL_BUS_PCI\x10\x02\x12%\n!NIFGEN_INT32_BUS_TYPE_VAL_BUS_PXI\x10\x03\x12%\n!NIFGEN_INT32_BUS_TYPE_VAL_BUS_VXI\x10\x04\x12(\n$NIFGEN_INT32_BUS_TYPE_VAL_BUS_PCMCIA\x10\x05\x12&\n\"NIFGEN_INT32_BUS_TYPE_VAL_BUS_PXIE\x10\x06\x12/\n+NIFGEN_INT32_CLOCK_MODE_VAL_HIGH_RESOLUTION\x10\x00\x12+\n\'NIFGEN_INT32_CLOCK_MODE_VAL_DIVIDE_DOWN\x10\x01\x12)\n%NIFGEN_INT32_CLOCK_MODE_VAL_AUTOMATIC\x10\x02\x12\x41\n=NIFGEN_INT32_DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_HIGH\x10\x65\x12@\n<NIFGEN_INT32_DATA_MARKER_EVENT_LEVEL_POLARITY_VAL_ACTIVE_LOW\x10\x66\x12\x32\n.NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_REAL\x10\x00\x12\x35\n1NIFGEN_INT32_DATA_PROCESSING_MODE_VAL_OSP_COMPLEX\x10\x01\x12\x38\n4NIFGEN_INT32_DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH\x10\x65\x12\x37\n3NIFGEN_INT32_DONE_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW\x10\x66\x12@\n<NIFGEN_INT32_DONE_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10\x65\x12\x33\n/NIFGEN_INT32_DONE_EVENT_DELAY_UNITS_VAL_SECONDS\x10\x66\x12\x35\n1NIFGEN_INT32_DONE_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE\x10\x65\x12\x35\n1NIFGEN_INT32_DONE_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL\x10\x66\x12:\n6NIFGEN_INT32_DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH\x10\x65\x12\x39\n5NIFGEN_INT32_DONE_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW\x10\x66\x12\x46\nBNIFGEN_INT32_DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10\x65\x12\x39\n5NIFGEN_INT32_DONE_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS\x10\x66\x12)\n%NIFGEN_INT32_FILTER_TYPE_VAL_OSP_FLAT\x10\x00\x12\x32\n.NIFGEN_INT32_FILTER_TYPE_VAL_OSP_RAISED_COSINE\x10\x01\x12\x37\n3NIFGEN_INT32_FILTER_TYPE_VAL_OSP_ROOT_RAISED_COSINE\x10\x02\x12-\n)NIFGEN_INT32_FILTER_TYPE_VAL_OSP_GAUSSIAN\x10\x03\x12+\n\'NIFGEN_INT32_FILTER_TYPE_VAL_OSP_CUSTOM\x10\x04\x12\x43\n=NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_FIRST_FREQ_LIST_HANDLE\x10\xc0\x9a\x0c\x12\x42\n<NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_LAST_FREQ_LIST_HANDLE\x10\xcf\xe8\x0c\x12@\n3NIFGEN_INT32_FREQUENCY_LIST_HANDLE_VAL_NO_FREQ_LIST\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x33\n.NIFGEN_INT32_IDLE_BEHAVIOR_VAL_HOLD_LAST_VALUE\x10\x90\x03\x12\x31\n,NIFGEN_INT32_IDLE_BEHAVIOR_VAL_JUMP_TO_VALUE\x10\x91\x03\x12\x42\n>NIFGEN_INT32_MARKER_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10\x65\x12\x35\n1NIFGEN_INT32_MARKER_EVENT_DELAY_UNITS_VAL_SECONDS\x10\x66\x12\x37\n3NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE\x10\x65\x12\x37\n3NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL\x10\x66\x12\x38\n4NIFGEN_INT32_MARKER_EVENT_OUTPUT_BEHAVIOR_VAL_TOGGLE\x10g\x12<\n8NIFGEN_INT32_MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH\x10\x65\x12;\n7NIFGEN_INT32_MARKER_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW\x10\x66\x12H\nDNIFGEN_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10\x65\x12;\n7NIFGEN_INT32_MARKER_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS\x10\x66\x12;\n7NIFGEN_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_HIGH\x10\x65\x12:\n6NIFGEN_INT32_MARKER_EVENT_TOGGLE_INITIAL_STATE_VAL_LOW\x10\x66\x12$\n NIFGEN_INT32_OSP_MODE_VAL_OSP_IF\x10\x00\x12*\n&NIFGEN_INT32_OSP_MODE_VAL_OSP_BASEBAND\x10\x01\x12G\nCNIFGEN_INT32_OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_ERROR\x10\x00\x12J\nFNIFGEN_INT32_OSP_OVERFLOW_ERROR_REPORTING_VAL_ERROR_REPORTING_DISABLED\x10\x02\x12:\n6NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_NONE\x10\x00\x12G\nCNIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_I\x10\x01\x12G\nCNIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_GAIN_Q\x10\x02\x12I\nENIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_I\x10\x04\x12I\nENIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PRE_FILTER_OFFSET_Q\x10\x08\x12\x42\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_I\x10\x10\x12\x43\n?NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_I\x10\x10\x12\x42\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_FIR_FILTER_Q\x10 \x12\x43\n?NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_PFIR_FILTER_Q\x10 \x12\x42\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_I\x10@\x12\x43\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CIC_FILTER_Q\x10\x80\x01\x12\x43\n>NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_COMPLEX_DATA\x10\x80\x02\x12\x44\n?NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_I\x10\x80\x04\x12\x44\n?NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_CFIR_FILTER_Q\x10\x80\x08\x12@\n;NIFGEN_INT32_OSP_OVERFLOW_STATUS_VAL_OSP_OVERFLOW_EQUALIZER\x10\x80\x10\x12,\n(NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_FUNC\x10\x00\x12+\n\'NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_ARB\x10\x01\x12+\n\'NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_SEQ\x10\x02\x12\x31\n-NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_FREQ_LIST\x10\x65\x12.\n*NIFGEN_INT32_OUTPUT_MODE_VAL_OUTPUT_SCRIPT\x10\x66\x12\x43\n?NIFGEN_INT32_READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH\x10\x65\x12\x42\n>NIFGEN_INT32_READY_FOR_START_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW\x10\x66\x12\x41\n=NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE\x10\x65\x12\x42\n>NIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE\x10\x66\x12J\nFNIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_HIGH\x10\x65\x12I\nENIFGEN_INT32_SCRIPT_TRIGGER_DIGITAL_LEVEL_ACTIVE_LEVEL_VAL_ACTIVE_LOW\x10\x66\x12\x32\n.NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_TRIG_NONE\x10\x65\x12\x35\n1NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_EDGE\x10\x66\x12\x36\n2NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_DIGITAL_LEVEL\x10g\x12\x36\n2NIFGEN_INT32_SCRIPT_TRIGGER_TYPE_VAL_SOFTWARE_EDGE\x10h\x12@\n<NIFGEN_INT32_START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_RISING_EDGE\x10\x65\x12\x41\n=NIFGEN_INT32_START_TRIGGER_DIGITAL_EDGE_EDGE_VAL_FALLING_EDGE\x10\x66\x12\x31\n-NIFGEN_INT32_START_TRIGGER_TYPE_VAL_TRIG_NONE\x10\x65\x12\x34\n0NIFGEN_INT32_START_TRIGGER_TYPE_VAL_DIGITAL_EDGE\x10\x66\x12\x35\n1NIFGEN_INT32_START_TRIGGER_TYPE_VAL_SOFTWARE_EDGE\x10h\x12=\n9NIFGEN_INT32_START_TRIGGER_TYPE_VAL_P2P_ENDPOINT_FULLNESS\x10j\x12;\n7NIFGEN_INT32_STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_HIGH\x10\x65\x12:\n6NIFGEN_INT32_STARTED_EVENT_ACTIVE_LEVEL_VAL_ACTIVE_LOW\x10\x66\x12\x43\n?NIFGEN_INT32_STARTED_EVENT_DELAY_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10\x65\x12\x36\n2NIFGEN_INT32_STARTED_EVENT_DELAY_UNITS_VAL_SECONDS\x10\x66\x12\x38\n4NIFGEN_INT32_STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_PULSE\x10\x65\x12\x38\n4NIFGEN_INT32_STARTED_EVENT_OUTPUT_BEHAVIOR_VAL_LEVEL\x10\x66\x12=\n9NIFGEN_INT32_STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_HIGH\x10\x65\x12<\n8NIFGEN_INT32_STARTED_EVENT_PULSE_POLARITY_VAL_ACTIVE_LOW\x10\x66\x12I\nENIFGEN_INT32_STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SAMPLE_CLOCK_PERIODS\x10\x65\x12<\n8NIFGEN_INT32_STARTED_EVENT_PULSE_WIDTH_UNITS_VAL_SECONDS\x10\x66\x12\x30\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL0\x10o\x12\x30\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL1\x10p\x12\x30\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL2\x10q\x12\x30\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL3\x10r\x12\x30\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL4\x10s\x12\x30\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL5\x10t\x12\x30\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_TTL6\x10u\x12\x33\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_0\x10\x8d\x01\x12\x33\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_1\x10\x8e\x01\x12\x33\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_2\x10\x8f\x01\x12\x33\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_3\x10\x90\x01\x12\x33\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_4\x10\x91\x01\x12\x33\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_5\x10\x92\x01\x12\x33\n.NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_RTSI_6\x10\x93\x01\x12\x31\n,NIFGEN_INT32_SYNCHRONIZATION_SOURCE_VAL_NONE\x10\xe8\x07\x12\x39\n4NIFGEN_INT32_TERMINAL_CONFIGURATION_VAL_SINGLE_ENDED\x10\xac\x02\x12\x39\n4NIFGEN_INT32_TERMINAL_CONFIGURATION_VAL_DIFFERENTIAL\x10\xad\x02\x12(\n$NIFGEN_INT32_TRIGGER_MODE_VAL_SINGLE\x10\x01\x12,\n(NIFGEN_INT32_TRIGGER_MODE_VAL_CONTINUOUS\x10\x02\x12)\n%NIFGEN_INT32_TRIGGER_MODE_VAL_STEPPED\x10\x03\x12\'\n#NIFGEN_INT32_TRIGGER_MODE_VAL_BURST\x10\x04\x12-\n)NIFGEN_INT32_TRIGGER_SOURCE_VAL_IMMEDIATE\x10\x00\x12,\n(NIFGEN_INT32_TRIGGER_SOURCE_VAL_EXTERNAL\x10\x01\x12\x31\n-NIFGEN_INT32_TRIGGER_SOURCE_VAL_SOFTWARE_TRIG\x10\x02\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL0\x10o\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL1\x10p\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL2\x10q\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL3\x10r\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL4\x10s\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL5\x10t\x12(\n$NIFGEN_INT32_TRIGGER_SOURCE_VAL_TTL6\x10u\x12-\n(NIFGEN_INT32_TRIGGER_SOURCE_VAL_PXI_STAR\x10\x83\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_0\x10\x8d\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_1\x10\x8e\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_2\x10\x8f\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_3\x10\x90\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_4\x10\x91\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_5\x10\x92\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_6\x10\x93\x01\x12+\n&NIFGEN_INT32_TRIGGER_SOURCE_VAL_RTSI_7\x10\xf2\x07\x12*\n%NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_0\x10\xf3\x07\x12*\n%NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_1\x10\xf4\x07\x12*\n%NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_2\x10\xf5\x07\x12*\n%NIFGEN_INT32_TRIGGER_SOURCE_VAL_PFI_3\x10\xf6\x07\x12\x33\n.NIFGEN_INT32_TRIGGER_SOURCE_VAL_OTHER_TERMINAL\x10\xfa\x07\x12\x31\n-NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_INTERNAL\x10\x00\x12\x31\n-NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_EXTERNAL\x10\x01\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL1\x10p\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL2\x10q\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL3\x10r\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL4\x10s\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL5\x10t\x12-\n)NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_TTL6\x10u\x12\x32\n-NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_PXI_STAR\x10\x83\x01\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_0\x10\x8d\x01\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_1\x10\x8e\x01\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_2\x10\x8f\x01\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_3\x10\x90\x01\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_4\x10\x91\x01\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_5\x10\x92\x01\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_6\x10\x93\x01\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_RTSI_7\x10\xf2\x07\x12\x38\n3NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_OTHER_TERMINAL\x10\xfa\x07\x12\x30\n+NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_CLK_IN\x10\xb2\t\x12\x34\n/NIFGEN_INT32_UPDATE_CLOCK_SOURCE_VAL_DDC_CLK_IN\x10\xb3\t\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_B\x10\x00\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_D\x10\x01\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_G\x10\x02\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_H\x10\x03\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_I\x10\x04\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_M\x10\x05\x12.\n*NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_PAL_N\x10\x06\x12/\n+NIFGEN_INT32_VIDEO_WAVEFORM_TYPE_VAL_NTSC_M\x10\x07\x12\x33\n.NIFGEN_INT32_WAIT_BEHAVIOR_VAL_HOLD_LAST_VALUE\x10\x90\x03\x12\x31\n,NIFGEN_INT32_WAIT_BEHAVIOR_VAL_JUMP_TO_VALUE\x10\x91\x03\x12&\n\"NIFGEN_INT32_WAVEFORM_VAL_WFM_SINE\x10\x01\x12(\n$NIFGEN_INT32_WAVEFORM_VAL_WFM_SQUARE\x10\x02\x12*\n&NIFGEN_INT32_WAVEFORM_VAL_WFM_TRIANGLE\x10\x03\x12)\n%NIFGEN_INT32_WAVEFORM_VAL_WFM_RAMP_UP\x10\x04\x12+\n\'NIFGEN_INT32_WAVEFORM_VAL_WFM_RAMP_DOWN\x10\x05\x12$\n NIFGEN_INT32_WAVEFORM_VAL_WFM_DC\x10\x06\x12\'\n#NIFGEN_INT32_WAVEFORM_VAL_WFM_NOISE\x10\x65\x12&\n\"NIFGEN_INT32_WAVEFORM_VAL_WFM_USER\x10\x66\x1a\x02\x10\x01*\xa7\x02\n\x1bNiFgenReal64AttributeValues\x12\x1d\n\x19NIFGEN_REAL64_UNSPECIFIED\x10\x00\x12\x44\n7NIFGEN_REAL64_LOAD_IMPEDANCE_VAL_MATCHED_LOAD_IMPEDANCE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12.\n*NIFGEN_REAL64_OUTPUT_IMPEDANCE_VAL_50_OHMS\x10\x32\x12.\n*NIFGEN_REAL64_OUTPUT_IMPEDANCE_VAL_75_OHMS\x10K\x12?\n2NIFGEN_REAL64_SAMPLE_RATE_VAL_EXTERNAL_SAMPLE_RATE\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x1a\x02\x10\x01*\xcf\n\n!NiFgenStringAttributeValuesMapped\x12$\n NIFGEN_STRING_MAPPED_UNSPECIFIED\x10\x00\x12I\nENIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_CLOCK_IN_COLLISION_AVOIDANCE\x10\x01\x12\x45\nANIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_NONE_COLLISION_AVOIDANCE\x10\x02\x12X\nTNIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_ONBOARD_REFERENCE_CLOCK_COLLISION_AVOIDANCE\x10\x03\x12J\nFNIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_PXI_CLOCK_COLLISION_AVOIDANCE\x10\x04\x12G\nCNIFGEN_STRING_REFERENCE_CLOCK_SOURCE_VAL_RTSI_7_COLLISION_AVOIDANCE\x10\x05\x12\x32\n.NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_CLOCK_IN\x10\x06\x12\x36\n2NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_DDC_CLOCK_IN\x10\x07\x12\x37\n3NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_ONBOARD_CLOCK\x10\x08\x12\x37\n3NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_STAR_LINE\x10\t\x12\x43\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_0_RTSI_0\x10\n\x12\x43\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_1_RTSI_1\x10\x0b\x12\x43\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_2_RTSI_2\x10\x0c\x12\x43\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_3_RTSI_3\x10\r\x12\x43\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_4_RTSI_4\x10\x0e\x12\x43\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_5_RTSI_5\x10\x0f\x12\x43\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_6_RTSI_6\x10\x10\x12\x43\n?NIFGEN_STRING_SAMPLE_CLOCK_SOURCE_VAL_PXI_TRIGGER_LINE_7_RTSI_7\x10\x11\x12;\n7NIFGEN_STRING_SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_CLOCK_IN\x10\x12\x12@\n<NIFGEN_STRING_SAMPLE_CLOCK_TIMEBASE_SOURCE_VAL_ONBOARD_CLOCK\x10\x13\x32\xdbn\n\x06NiFgen\x12;\n\x04Init\x12\x18.nifgen_grpc.InitRequest\x1a\x19.nifgen_grpc.InitResponse\x12\\\n\x0fInitWithOptions\x12#.nifgen_grpc.InitWithOptionsRequest\x1a$.nifgen_grpc.InitWithOptionsResponse\x12q\n\x16InitializeWithChannels\x12*.nifgen_grpc.InitializeWithChannelsRequest\x1a+.nifgen_grpc.InitializeWithChannelsResponse\x12>\n\x05\x43lose\x12\x19.nifgen_grpc.CloseRequest\x1a\x1a.nifgen_grpc.CloseResponse\x12>\n\x05Reset\x12\x19.nifgen_grpc.ResetRequest\x1a\x1a.nifgen_grpc.ResetResponse\x12G\n\x08SelfTest\x12\x1c.nifgen_grpc.SelfTestRequest\x1a\x1d.nifgen_grpc.SelfTestResponse\x12M\n\nErrorQuery\x12\x1e.nifgen_grpc.ErrorQueryRequest\x1a\x1f.nifgen_grpc.ErrorQueryResponse\x12S\n\x0c\x45rrorMessage\x12 .nifgen_grpc.ErrorMessageRequest\x1a!.nifgen_grpc.ErrorMessageResponse\x12V\n\rRevisionQuery\x12!.nifgen_grpc.RevisionQueryRequest\x1a\".nifgen_grpc.RevisionQueryResponse\x12G\n\x08GetError\x12\x1c.nifgen_grpc.GetErrorRequest\x1a\x1d.nifgen_grpc.GetErrorResponse\x12M\n\nClearError\x12\x1e.nifgen_grpc.ClearErrorRequest\x1a\x1f.nifgen_grpc.ClearErrorResponse\x12S\n\x0c\x45rrorHandler\x12 .nifgen_grpc.ErrorHandlerRequest\x1a!.nifgen_grpc.ErrorHandlerResponse\x12Y\n\x0eGetChannelName\x12\".nifgen_grpc.GetChannelNameRequest\x1a#.nifgen_grpc.GetChannelNameResponse\x12n\n\x15ResetInterchangeCheck\x12).nifgen_grpc.ResetInterchangeCheckRequest\x1a*.nifgen_grpc.ResetInterchangeCheckResponse\x12w\n\x18\x43learInterchangeWarnings\x12,.nifgen_grpc.ClearInterchangeWarningsRequest\x1a-.nifgen_grpc.ClearInterchangeWarningsResponse\x12t\n\x17InvalidateAllAttributes\x12+.nifgen_grpc.InvalidateAllAttributesRequest\x1a,.nifgen_grpc.InvalidateAllAttributesResponse\x12\x62\n\x11ResetWithDefaults\x12%.nifgen_grpc.ResetWithDefaultsRequest\x1a&.nifgen_grpc.ResetWithDefaultsResponse\x12\x44\n\x07\x44isable\x12\x1b.nifgen_grpc.DisableRequest\x1a\x1c.nifgen_grpc.DisableResponse\x12\x41\n\x06\x43ommit\x12\x1a.nifgen_grpc.CommitRequest\x1a\x1b.nifgen_grpc.CommitResponse\x12_\n\x10GetHardwareState\x12$.nifgen_grpc.GetHardwareStateRequest\x1a%.nifgen_grpc.GetHardwareStateResponse\x12V\n\rWaitUntilDone\x12!.nifgen_grpc.WaitUntilDoneRequest\x1a\".nifgen_grpc.WaitUntilDoneResponse\x12\x41\n\x06IsDone\x12\x1a.nifgen_grpc.IsDoneRequest\x1a\x1b.nifgen_grpc.IsDoneResponse\x12P\n\x0bResetDevice\x12\x1f.nifgen_grpc.ResetDeviceRequest\x1a .nifgen_grpc.ResetDeviceResponse\x12q\n\x16\x43onfigureOperationMode\x12*.nifgen_grpc.ConfigureOperationModeRequest\x1a+.nifgen_grpc.ConfigureOperationModeResponse\x12h\n\x13\x43onfigureOutputMode\x12\'.nifgen_grpc.ConfigureOutputModeRequest\x1a(.nifgen_grpc.ConfigureOutputModeResponse\x12t\n\x17\x43onfigureReferenceClock\x12+.nifgen_grpc.ConfigureReferenceClockRequest\x1a,.nifgen_grpc.ConfigureReferenceClockResponse\x12w\n\x18\x43onfigureOutputImpedance\x12,.nifgen_grpc.ConfigureOutputImpedanceRequest\x1a-.nifgen_grpc.ConfigureOutputImpedanceResponse\x12q\n\x16\x43onfigureOutputEnabled\x12*.nifgen_grpc.ConfigureOutputEnabledRequest\x1a+.nifgen_grpc.ConfigureOutputEnabledResponse\x12\x62\n\x11\x43onfigureChannels\x12%.nifgen_grpc.ConfigureChannelsRequest\x1a&.nifgen_grpc.ConfigureChannelsResponse\x12\x65\n\x12InitiateGeneration\x12&.nifgen_grpc.InitiateGenerationRequest\x1a\'.nifgen_grpc.InitiateGenerationResponse\x12\\\n\x0f\x41\x62ortGeneration\x12#.nifgen_grpc.AbortGenerationRequest\x1a$.nifgen_grpc.AbortGenerationResponse\x12z\n\x19\x43onfigureStandardWaveform\x12-.nifgen_grpc.ConfigureStandardWaveformRequest\x1a..nifgen_grpc.ConfigureStandardWaveformResponse\x12}\n\x1a\x44\x65\x66ineUserStandardWaveform\x12..nifgen_grpc.DefineUserStandardWaveformRequest\x1a/.nifgen_grpc.DefineUserStandardWaveformResponse\x12z\n\x19\x43learUserStandardWaveform\x12-.nifgen_grpc.ClearUserStandardWaveformRequest\x1a..nifgen_grpc.ClearUserStandardWaveformResponse\x12\x65\n\x12\x43onfigureFrequency\x12&.nifgen_grpc.ConfigureFrequencyRequest\x1a\'.nifgen_grpc.ConfigureFrequencyResponse\x12\x65\n\x12\x43onfigureAmplitude\x12&.nifgen_grpc.ConfigureAmplitudeRequest\x1a\'.nifgen_grpc.ConfigureAmplitudeResponse\x12t\n\x17QueryArbWfmCapabilities\x12+.nifgen_grpc.QueryArbWfmCapabilitiesRequest\x1a,.nifgen_grpc.QueryArbWfmCapabilitiesResponse\x12\x62\n\x11\x43reateWaveformF64\x12%.nifgen_grpc.CreateWaveformF64Request\x1a&.nifgen_grpc.CreateWaveformF64Response\x12\x62\n\x11\x43reateWaveformI16\x12%.nifgen_grpc.CreateWaveformI16Request\x1a&.nifgen_grpc.CreateWaveformI16Response\x12w\n\x18\x43reateWaveformComplexF64\x12,.nifgen_grpc.CreateWaveformComplexF64Request\x1a-.nifgen_grpc.CreateWaveformComplexF64Response\x12z\n\x19\x43reateWaveformFromFileI16\x12-.nifgen_grpc.CreateWaveformFromFileI16Request\x1a..nifgen_grpc.CreateWaveformFromFileI16Response\x12z\n\x19\x43reateWaveformFromFileF64\x12-.nifgen_grpc.CreateWaveformFromFileF64Request\x1a..nifgen_grpc.CreateWaveformFromFileF64Response\x12h\n\x13\x43onfigureSampleRate\x12\'.nifgen_grpc.ConfigureSampleRateRequest\x1a(.nifgen_grpc.ConfigureSampleRateResponse\x12k\n\x14\x43onfigureArbWaveform\x12(.nifgen_grpc.ConfigureArbWaveformRequest\x1a).nifgen_grpc.ConfigureArbWaveformResponse\x12_\n\x10\x43learArbWaveform\x12$.nifgen_grpc.ClearArbWaveformRequest\x1a%.nifgen_grpc.ClearArbWaveformResponse\x12n\n\x15\x41llocateNamedWaveform\x12).nifgen_grpc.AllocateNamedWaveformRequest\x1a*.nifgen_grpc.AllocateNamedWaveformResponse\x12\x92\x01\n!SetNamedWaveformNextWritePosition\x12\x35.nifgen_grpc.SetNamedWaveformNextWritePositionRequest\x1a\x36.nifgen_grpc.SetNamedWaveformNextWritePositionResponse\x12n\n\x15WriteNamedWaveformF64\x12).nifgen_grpc.WriteNamedWaveformF64Request\x1a*.nifgen_grpc.WriteNamedWaveformF64Response\x12n\n\x15WriteNamedWaveformI16\x12).nifgen_grpc.WriteNamedWaveformI16Request\x1a*.nifgen_grpc.WriteNamedWaveformI16Response\x12\x83\x01\n\x1cWriteNamedWaveformComplexF64\x12\x30.nifgen_grpc.WriteNamedWaveformComplexF64Request\x1a\x31.nifgen_grpc.WriteNamedWaveformComplexF64Response\x12\x83\x01\n\x1cWriteNamedWaveformComplexI16\x12\x30.nifgen_grpc.WriteNamedWaveformComplexI16Request\x1a\x31.nifgen_grpc.WriteNamedWaveformComplexI16Response\x12h\n\x13\x44\x65leteNamedWaveform\x12\'.nifgen_grpc.DeleteNamedWaveformRequest\x1a(.nifgen_grpc.DeleteNamedWaveformResponse\x12t\n\x17QueryArbSeqCapabilities\x12+.nifgen_grpc.QueryArbSeqCapabilitiesRequest\x1a,.nifgen_grpc.QueryArbSeqCapabilitiesResponse\x12\x62\n\x11\x43reateArbSequence\x12%.nifgen_grpc.CreateArbSequenceRequest\x1a&.nifgen_grpc.CreateArbSequenceResponse\x12z\n\x19\x43reateAdvancedArbSequence\x12-.nifgen_grpc.CreateAdvancedArbSequenceRequest\x1a..nifgen_grpc.CreateAdvancedArbSequenceResponse\x12k\n\x14\x43onfigureArbSequence\x12(.nifgen_grpc.ConfigureArbSequenceRequest\x1a).nifgen_grpc.ConfigureArbSequenceResponse\x12_\n\x10\x43learArbSequence\x12$.nifgen_grpc.ClearArbSequenceRequest\x1a%.nifgen_grpc.ClearArbSequenceResponse\x12Y\n\x0e\x43learArbMemory\x12\".nifgen_grpc.ClearArbMemoryRequest\x1a#.nifgen_grpc.ClearArbMemoryResponse\x12z\n\x19QueryFreqListCapabilities\x12-.nifgen_grpc.QueryFreqListCapabilitiesRequest\x1a..nifgen_grpc.QueryFreqListCapabilitiesResponse\x12Y\n\x0e\x43reateFreqList\x12\".nifgen_grpc.CreateFreqListRequest\x1a#.nifgen_grpc.CreateFreqListResponse\x12\x62\n\x11\x43onfigureFreqList\x12%.nifgen_grpc.ConfigureFreqListRequest\x1a&.nifgen_grpc.ConfigureFreqListResponse\x12V\n\rClearFreqList\x12!.nifgen_grpc.ClearFreqListRequest\x1a\".nifgen_grpc.ClearFreqListResponse\x12P\n\x0bWriteScript\x12\x1f.nifgen_grpc.WriteScriptRequest\x1a .nifgen_grpc.WriteScriptResponse\x12S\n\x0c\x44\x65leteScript\x12 .nifgen_grpc.DeleteScriptRequest\x1a!.nifgen_grpc.DeleteScriptResponse\x12S\n\x0c\x45xportSignal\x12 .nifgen_grpc.ExportSignalRequest\x1a!.nifgen_grpc.ExportSignalResponse\x12Y\n\x0eRouteSignalOut\x12\".nifgen_grpc.RouteSignalOutRequest\x1a#.nifgen_grpc.RouteSignalOutResponse\x12t\n\x17SendSoftwareEdgeTrigger\x12+.nifgen_grpc.SendSoftwareEdgeTriggerRequest\x1a,.nifgen_grpc.SendSoftwareEdgeTriggerResponse\x12\x8f\x01\n ConfigureDigitalEdgeStartTrigger\x12\x34.nifgen_grpc.ConfigureDigitalEdgeStartTriggerRequest\x1a\x35.nifgen_grpc.ConfigureDigitalEdgeStartTriggerResponse\x12\x92\x01\n!ConfigureSoftwareEdgeStartTrigger\x12\x35.nifgen_grpc.ConfigureSoftwareEdgeStartTriggerRequest\x1a\x36.nifgen_grpc.ConfigureSoftwareEdgeStartTriggerResponse\x12h\n\x13\x44isableStartTrigger\x12\'.nifgen_grpc.DisableStartTriggerRequest\x1a(.nifgen_grpc.DisableStartTriggerResponse\x12\xa7\x01\n(ConfigureP2PEndpointFullnessStartTrigger\x12<.nifgen_grpc.ConfigureP2PEndpointFullnessStartTriggerRequest\x1a=.nifgen_grpc.ConfigureP2PEndpointFullnessStartTriggerResponse\x12\x92\x01\n!ConfigureDigitalEdgeScriptTrigger\x12\x35.nifgen_grpc.ConfigureDigitalEdgeScriptTriggerRequest\x1a\x36.nifgen_grpc.ConfigureDigitalEdgeScriptTriggerResponse\x12\x95\x01\n\"ConfigureDigitalLevelScriptTrigger\x12\x36.nifgen_grpc.ConfigureDigitalLevelScriptTriggerRequest\x1a\x37.nifgen_grpc.ConfigureDigitalLevelScriptTriggerResponse\x12\x95\x01\n\"ConfigureSoftwareEdgeScriptTrigger\x12\x36.nifgen_grpc.ConfigureSoftwareEdgeScriptTriggerRequest\x1a\x37.nifgen_grpc.ConfigureSoftwareEdgeScriptTriggerResponse\x12k\n\x14\x44isableScriptTrigger\x12(.nifgen_grpc.DisableScriptTriggerRequest\x1a).nifgen_grpc.DisableScriptTriggerResponse\x12\x65\n\x12\x43onfigureClockMode\x12&.nifgen_grpc.ConfigureClockModeRequest\x1a\'.nifgen_grpc.ConfigureClockModeResponse\x12\x89\x01\n\x1e\x41\x64justSampleClockRelativeDelay\x12\x32.nifgen_grpc.AdjustSampleClockRelativeDelayRequest\x1a\x33.nifgen_grpc.AdjustSampleClockRelativeDelayResponse\x12_\n\x10\x41llocateWaveform\x12$.nifgen_grpc.AllocateWaveformRequest\x1a%.nifgen_grpc.AllocateWaveformResponse\x12\x83\x01\n\x1cSetWaveformNextWritePosition\x12\x30.nifgen_grpc.SetWaveformNextWritePositionRequest\x1a\x31.nifgen_grpc.SetWaveformNextWritePositionResponse\x12V\n\rWriteWaveform\x12!.nifgen_grpc.WriteWaveformRequest\x1a\".nifgen_grpc.WriteWaveformResponse\x12n\n\x15WriteBinary16Waveform\x12).nifgen_grpc.WriteBinary16WaveformRequest\x1a*.nifgen_grpc.WriteBinary16WaveformResponse\x12t\n\x17WriteWaveformComplexF64\x12+.nifgen_grpc.WriteWaveformComplexF64Request\x1a,.nifgen_grpc.WriteWaveformComplexF64Response\x12\x83\x01\n\x1cWriteComplexBinary16Waveform\x12\x30.nifgen_grpc.WriteComplexBinary16WaveformRequest\x1a\x31.nifgen_grpc.WriteComplexBinary16WaveformResponse\x12\x44\n\x07SelfCal\x12\x1b.nifgen_grpc.SelfCalRequest\x1a\x1c.nifgen_grpc.SelfCalResponse\x12h\n\x13GetSelfCalSupported\x12\'.nifgen_grpc.GetSelfCalSupportedRequest\x1a(.nifgen_grpc.GetSelfCalSupportedResponse\x12z\n\x19GetSelfCalLastDateAndTime\x12-.nifgen_grpc.GetSelfCalLastDateAndTimeRequest\x1a..nifgen_grpc.GetSelfCalLastDateAndTimeResponse\x12w\n\x18GetExtCalLastDateAndTime\x12,.nifgen_grpc.GetExtCalLastDateAndTimeRequest\x1a-.nifgen_grpc.GetExtCalLastDateAndTimeResponse\x12\x65\n\x12GetSelfCalLastTemp\x12&.nifgen_grpc.GetSelfCalLastTempRequest\x1a\'.nifgen_grpc.GetSelfCalLastTempResponse\x12\x62\n\x11GetExtCalLastTemp\x12%.nifgen_grpc.GetExtCalLastTempRequest\x1a&.nifgen_grpc.GetExtCalLastTempResponse\x12\x83\x01\n\x1cGetExtCalRecommendedInterval\x12\x30.nifgen_grpc.GetExtCalRecommendedIntervalRequest\x1a\x31.nifgen_grpc.GetExtCalRecommendedIntervalResponse\x12q\n\x16ReadCurrentTemperature\x12*.nifgen_grpc.ReadCurrentTemperatureRequest\x1a+.nifgen_grpc.ReadCurrentTemperatureResponse\x12\x9b\x01\n$ConfigureCustomFIRFilterCoefficients\x12\x38.nifgen_grpc.ConfigureCustomFIRFilterCoefficientsRequest\x1a\x39.nifgen_grpc.ConfigureCustomFIRFilterCoefficientsResponse\x12w\n\x18GetFIRFilterCoefficients\x12,.nifgen_grpc.GetFIRFilterCoefficientsRequest\x1a-.nifgen_grpc.GetFIRFilterCoefficientsResponse\x12t\n\x17GetStreamEndpointHandle\x12+.nifgen_grpc.GetStreamEndpointHandleRequest\x1a,.nifgen_grpc.GetStreamEndpointHandleResponse\x12h\n\x13WriteP2PEndpointI16\x12\'.nifgen_grpc.WriteP2PEndpointI16Request\x1a(.nifgen_grpc.WriteP2PEndpointI16Response\x12w\n\x18\x43onfigureSynchronization\x12,.nifgen_grpc.ConfigureSynchronizationRequest\x1a-.nifgen_grpc.ConfigureSynchronizationResponse\x12t\n\x17\x45nableDigitalPatterning\x12+.nifgen_grpc.EnableDigitalPatterningRequest\x1a,.nifgen_grpc.EnableDigitalPatterningResponse\x12w\n\x18\x44isableDigitalPatterning\x12,.nifgen_grpc.DisableDigitalPatterningRequest\x1a-.nifgen_grpc.DisableDigitalPatterningResponse\x12h\n\x13\x45nableDigitalFilter\x12\'.nifgen_grpc.EnableDigitalFilterRequest\x1a(.nifgen_grpc.EnableDigitalFilterResponse\x12k\n\x14\x44isableDigitalFilter\x12(.nifgen_grpc.DisableDigitalFilterRequest\x1a).nifgen_grpc.DisableDigitalFilterResponse\x12\x65\n\x12\x45nableAnalogFilter\x12&.nifgen_grpc.EnableAnalogFilterRequest\x1a\'.nifgen_grpc.EnableAnalogFilterResponse\x12h\n\x13\x44isableAnalogFilter\x12\'.nifgen_grpc.DisableAnalogFilterRequest\x1a(.nifgen_grpc.DisableAnalogFilterResponse\x12}\n\x1a\x43onfigureSampleClockSource\x12..nifgen_grpc.ConfigureSampleClockSourceRequest\x1a/.nifgen_grpc.ConfigureSampleClockSourceResponse\x12k\n\x14\x43onfigureTriggerMode\x12(.nifgen_grpc.ConfigureTriggerModeRequest\x1a).nifgen_grpc.ConfigureTriggerModeResponse\x12\x8f\x01\n ImportAttributeConfigurationFile\x12\x34.nifgen_grpc.ImportAttributeConfigurationFileRequest\x1a\x35.nifgen_grpc.ImportAttributeConfigurationFileResponse\x12\x8f\x01\n ExportAttributeConfigurationFile\x12\x34.nifgen_grpc.ExportAttributeConfigurationFileRequest\x1a\x35.nifgen_grpc.ExportAttributeConfigurationFileResponse\x12\x95\x01\n\"ImportAttributeConfigurationBuffer\x12\x36.nifgen_grpc.ImportAttributeConfigurationBufferRequest\x1a\x37.nifgen_grpc.ImportAttributeConfigurationBufferResponse\x12\x95\x01\n\"ExportAttributeConfigurationBuffer\x12\x36.nifgen_grpc.ExportAttributeConfigurationBufferRequest\x1a\x37.nifgen_grpc.ExportAttributeConfigurationBufferResponse\x12h\n\x13SetAttributeViInt64\x12\'.nifgen_grpc.SetAttributeViInt64Request\x1a(.nifgen_grpc.SetAttributeViInt64Response\x12n\n\x15\x43heckAttributeViInt64\x12).nifgen_grpc.CheckAttributeViInt64Request\x1a*.nifgen_grpc.CheckAttributeViInt64Response\x12h\n\x13GetAttributeViInt64\x12\'.nifgen_grpc.GetAttributeViInt64Request\x1a(.nifgen_grpc.GetAttributeViInt64Response\x12h\n\x13SetAttributeViInt32\x12\'.nifgen_grpc.SetAttributeViInt32Request\x1a(.nifgen_grpc.SetAttributeViInt32Response\x12k\n\x14SetAttributeViReal64\x12(.nifgen_grpc.SetAttributeViReal64Request\x1a).nifgen_grpc.SetAttributeViReal64Response\x12k\n\x14SetAttributeViString\x12(.nifgen_grpc.SetAttributeViStringRequest\x1a).nifgen_grpc.SetAttributeViStringResponse\x12n\n\x15SetAttributeViBoolean\x12).nifgen_grpc.SetAttributeViBooleanRequest\x1a*.nifgen_grpc.SetAttributeViBooleanResponse\x12n\n\x15SetAttributeViSession\x12).nifgen_grpc.SetAttributeViSessionRequest\x1a*.nifgen_grpc.SetAttributeViSessionResponse\x12n\n\x15\x43heckAttributeViInt32\x12).nifgen_grpc.CheckAttributeViInt32Request\x1a*.nifgen_grpc.CheckAttributeViInt32Response\x12q\n\x16\x43heckAttributeViReal64\x12*.nifgen_grpc.CheckAttributeViReal64Request\x1a+.nifgen_grpc.CheckAttributeViReal64Response\x12q\n\x16\x43heckAttributeViString\x12*.nifgen_grpc.CheckAttributeViStringRequest\x1a+.nifgen_grpc.CheckAttributeViStringResponse\x12t\n\x17\x43heckAttributeViBoolean\x12+.nifgen_grpc.CheckAttributeViBooleanRequest\x1a,.nifgen_grpc.CheckAttributeViBooleanResponse\x12t\n\x17\x43heckAttributeViSession\x12+.nifgen_grpc.CheckAttributeViSessionRequest\x1a,.nifgen_grpc.CheckAttributeViSessionResponse\x12h\n\x13GetAttributeViInt32\x12\'.nifgen_grpc.GetAttributeViInt32Request\x1a(.nifgen_grpc.GetAttributeViInt32Response\x12k\n\x14GetAttributeViReal64\x12(.nifgen_grpc.GetAttributeViReal64Request\x1a).nifgen_grpc.GetAttributeViReal64Response\x12k\n\x14GetAttributeViString\x12(.nifgen_grpc.GetAttributeViStringRequest\x1a).nifgen_grpc.GetAttributeViStringResponse\x12n\n\x15GetAttributeViBoolean\x12).nifgen_grpc.GetAttributeViBooleanRequest\x1a*.nifgen_grpc.GetAttributeViBooleanResponse\x12n\n\x15GetAttributeViSession\x12).nifgen_grpc.GetAttributeViSessionRequest\x1a*.nifgen_grpc.GetAttributeViSessionResponse\x12Y\n\x0eResetAttribute\x12\".nifgen_grpc.ResetAttributeRequest\x1a#.nifgen_grpc.ResetAttributeResponse\x12n\n\x15ManualEnableP2PStream\x12).nifgen_grpc.ManualEnableP2PStreamRequest\x1a*.nifgen_grpc.ManualEnableP2PStreamResponse\x12z\n\x19\x43reateWaveformFromFileHWS\x12-.nifgen_grpc.CreateWaveformFromFileHWSRequest\x1a..nifgen_grpc.CreateWaveformFromFileHWSResponseB<\n\x10\x63om.ni.grpc.fgenB\x06NiFgenP\x01\xaa\x02\x1dNationalInstruments.Grpc.Fgenb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'nifgen_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\020com.ni.grpc.fgenB\006NiFgenP\001\252\002\035NationalInstruments.Grpc.Fgen'
  _NIFGENINT32ATTRIBUTEVALUES._options = None
  _NIFGENINT32ATTRIBUTEVALUES._serialized_options = b'\020\001'
  _NIFGENREAL64ATTRIBUTEVALUES._options = None
  _NIFGENREAL64ATTRIBUTEVALUES._serialized_options = b'\020\001'
  _INITRESPONSE.fields_by_name['error_message']._options = None
  _INITRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _INITWITHOPTIONSRESPONSE.fields_by_name['error_message']._options = None
  _INITWITHOPTIONSRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _INITIALIZEWITHCHANNELSRESPONSE.fields_by_name['error_message']._options = None
  _INITIALIZEWITHCHANNELSRESPONSE.fields_by_name['error_message']._serialized_options = b'\030\001'
  _globals['_NIFGENATTRIBUTE']._serialized_start=24660
  _globals['_NIFGENATTRIBUTE']._serialized_end=35325
  _globals['_OUTPUTMODE']._serialized_start=35328
  _globals['_OUTPUTMODE']._serialized_end=35545
  _globals['_WAVEFORM']._serialized_start=35548
  _globals['_WAVEFORM']._serialized_end=35869
  _globals['_SIGNAL']._serialized_start=35872
  _globals['_SIGNAL']._serialized_end=36416
  _globals['_TRIGGERMODE']._serialized_start=36419
  _globals['_TRIGGERMODE']._serialized_end=36610
  _globals['_CLOCKMODE']._serialized_start=36613
  _globals['_CLOCKMODE']._serialized_end=36743
  _globals['_RELATIVETO']._serialized_start=36745
  _globals['_RELATIVETO']._serialized_end=36863
  _globals['_HARDWARESTATE']._serialized_start=36866
  _globals['_HARDWARESTATE']._serialized_end=37098
  _globals['_BYTEORDER']._serialized_start=37100
  _globals['_BYTEORDER']._serialized_end=37190
  _globals['_TRIGGERWHEN']._serialized_start=37192
  _globals['_TRIGGERWHEN']._serialized_end=37316
  _globals['_TRIGGER']._serialized_start=37318
  _globals['_TRIGGER']._serialized_end=37430
  _globals['_FREQUENCYLISTOPTIONS']._serialized_start=37432
  _globals['_FREQUENCYLISTOPTIONS']._serialized_end=37553
  _globals['_ROUTESIGNALFROM']._serialized_start=37556
  _globals['_ROUTESIGNALFROM']._serialized_end=38461
  _globals['_ROUTESIGNALTO']._serialized_start=38464
  _globals['_ROUTESIGNALTO']._serialized_end=38993
  _globals['_SEQUENCEHANDLE']._serialized_start=38995
  _globals['_SEQUENCEHANDLE']._serialized_end=39099
  _globals['_WAVEFORMHANDLE']._serialized_start=39101
  _globals['_WAVEFORMHANDLE']._serialized_end=39205
  _globals['_NIFGENINT32ATTRIBUTEVALUES']._serialized_start=39208
  _globals['_NIFGENINT32ATTRIBUTEVALUES']._serialized_end=49641
  _globals['_NIFGENREAL64ATTRIBUTEVALUES']._serialized_start=49644
  _globals['_NIFGENREAL64ATTRIBUTEVALUES']._serialized_end=49939
  _globals['_NIFGENSTRINGATTRIBUTEVALUESMAPPED']._serialized_start=49942
  _globals['_NIFGENSTRINGATTRIBUTEVALUESMAPPED']._serialized_end=51301
  _globals['_INITREQUEST']._serialized_start=61
  _globals['_INITREQUEST']._serialized_end=238
  _globals['_INITRESPONSE']._serialized_start=240
  _globals['_INITRESPONSE']._serialized_end=366
  _globals['_INITWITHOPTIONSREQUEST']._serialized_start=369
  _globals['_INITWITHOPTIONSREQUEST']._serialized_end=580
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_start=583
  _globals['_INITWITHOPTIONSRESPONSE']._serialized_end=720
  _globals['_INITIALIZEWITHCHANNELSREQUEST']._serialized_start=723
  _globals['_INITIALIZEWITHCHANNELSREQUEST']._serialized_end=945
  _globals['_INITIALIZEWITHCHANNELSRESPONSE']._serialized_start=948
  _globals['_INITIALIZEWITHCHANNELSRESPONSE']._serialized_end=1092
  _globals['_CLOSEREQUEST']._serialized_start=1094
  _globals['_CLOSEREQUEST']._serialized_end=1144
  _globals['_CLOSERESPONSE']._serialized_start=1146
  _globals['_CLOSERESPONSE']._serialized_end=1177
  _globals['_RESETREQUEST']._serialized_start=1179
  _globals['_RESETREQUEST']._serialized_end=1229
  _globals['_RESETRESPONSE']._serialized_start=1231
  _globals['_RESETRESPONSE']._serialized_end=1262
  _globals['_SELFTESTREQUEST']._serialized_start=1264
  _globals['_SELFTESTREQUEST']._serialized_end=1317
  _globals['_SELFTESTRESPONSE']._serialized_start=1319
  _globals['_SELFTESTRESPONSE']._serialized_end=1406
  _globals['_ERRORQUERYREQUEST']._serialized_start=1408
  _globals['_ERRORQUERYREQUEST']._serialized_end=1463
  _globals['_ERRORQUERYRESPONSE']._serialized_start=1465
  _globals['_ERRORQUERYRESPONSE']._serialized_end=1544
  _globals['_ERRORMESSAGEREQUEST']._serialized_start=1546
  _globals['_ERRORMESSAGEREQUEST']._serialized_end=1623
  _globals['_ERRORMESSAGERESPONSE']._serialized_start=1625
  _globals['_ERRORMESSAGERESPONSE']._serialized_end=1686
  _globals['_REVISIONQUERYREQUEST']._serialized_start=1688
  _globals['_REVISIONQUERYREQUEST']._serialized_end=1746
  _globals['_REVISIONQUERYRESPONSE']._serialized_start=1748
  _globals['_REVISIONQUERYRESPONSE']._serialized_end=1850
  _globals['_GETERRORREQUEST']._serialized_start=1852
  _globals['_GETERRORREQUEST']._serialized_end=1905
  _globals['_GETERRORRESPONSE']._serialized_start=1907
  _globals['_GETERRORRESPONSE']._serialized_end=1988
  _globals['_CLEARERRORREQUEST']._serialized_start=1990
  _globals['_CLEARERRORREQUEST']._serialized_end=2045
  _globals['_CLEARERRORRESPONSE']._serialized_start=2047
  _globals['_CLEARERRORRESPONSE']._serialized_end=2083
  _globals['_ERRORHANDLERREQUEST']._serialized_start=2085
  _globals['_ERRORHANDLERREQUEST']._serialized_end=2162
  _globals['_ERRORHANDLERRESPONSE']._serialized_start=2164
  _globals['_ERRORHANDLERRESPONSE']._serialized_end=2225
  _globals['_GETCHANNELNAMEREQUEST']._serialized_start=2227
  _globals['_GETCHANNELNAMEREQUEST']._serialized_end=2301
  _globals['_GETCHANNELNAMERESPONSE']._serialized_start=2303
  _globals['_GETCHANNELNAMERESPONSE']._serialized_end=2367
  _globals['_RESETINTERCHANGECHECKREQUEST']._serialized_start=2369
  _globals['_RESETINTERCHANGECHECKREQUEST']._serialized_end=2435
  _globals['_RESETINTERCHANGECHECKRESPONSE']._serialized_start=2437
  _globals['_RESETINTERCHANGECHECKRESPONSE']._serialized_end=2484
  _globals['_CLEARINTERCHANGEWARNINGSREQUEST']._serialized_start=2486
  _globals['_CLEARINTERCHANGEWARNINGSREQUEST']._serialized_end=2555
  _globals['_CLEARINTERCHANGEWARNINGSRESPONSE']._serialized_start=2557
  _globals['_CLEARINTERCHANGEWARNINGSRESPONSE']._serialized_end=2607
  _globals['_INVALIDATEALLATTRIBUTESREQUEST']._serialized_start=2609
  _globals['_INVALIDATEALLATTRIBUTESREQUEST']._serialized_end=2677
  _globals['_INVALIDATEALLATTRIBUTESRESPONSE']._serialized_start=2679
  _globals['_INVALIDATEALLATTRIBUTESRESPONSE']._serialized_end=2728
  _globals['_RESETWITHDEFAULTSREQUEST']._serialized_start=2730
  _globals['_RESETWITHDEFAULTSREQUEST']._serialized_end=2792
  _globals['_RESETWITHDEFAULTSRESPONSE']._serialized_start=2794
  _globals['_RESETWITHDEFAULTSRESPONSE']._serialized_end=2837
  _globals['_DISABLEREQUEST']._serialized_start=2839
  _globals['_DISABLEREQUEST']._serialized_end=2891
  _globals['_DISABLERESPONSE']._serialized_start=2893
  _globals['_DISABLERESPONSE']._serialized_end=2926
  _globals['_COMMITREQUEST']._serialized_start=2928
  _globals['_COMMITREQUEST']._serialized_end=2979
  _globals['_COMMITRESPONSE']._serialized_start=2981
  _globals['_COMMITRESPONSE']._serialized_end=3013
  _globals['_GETHARDWARESTATEREQUEST']._serialized_start=3015
  _globals['_GETHARDWARESTATEREQUEST']._serialized_end=3076
  _globals['_GETHARDWARESTATERESPONSE']._serialized_start=3078
  _globals['_GETHARDWARESTATERESPONSE']._serialized_end=3182
  _globals['_WAITUNTILDONEREQUEST']._serialized_start=3184
  _globals['_WAITUNTILDONEREQUEST']._serialized_end=3260
  _globals['_WAITUNTILDONERESPONSE']._serialized_start=3262
  _globals['_WAITUNTILDONERESPONSE']._serialized_end=3301
  _globals['_ISDONEREQUEST']._serialized_start=3303
  _globals['_ISDONEREQUEST']._serialized_end=3354
  _globals['_ISDONERESPONSE']._serialized_start=3356
  _globals['_ISDONERESPONSE']._serialized_end=3402
  _globals['_RESETDEVICEREQUEST']._serialized_start=3404
  _globals['_RESETDEVICEREQUEST']._serialized_end=3460
  _globals['_RESETDEVICERESPONSE']._serialized_start=3462
  _globals['_RESETDEVICERESPONSE']._serialized_end=3499
  _globals['_CONFIGUREOPERATIONMODEREQUEST']._serialized_start=3501
  _globals['_CONFIGUREOPERATIONMODEREQUEST']._serialized_end=3614
  _globals['_CONFIGUREOPERATIONMODERESPONSE']._serialized_start=3616
  _globals['_CONFIGUREOPERATIONMODERESPONSE']._serialized_end=3664
  _globals['_CONFIGUREOUTPUTMODEREQUEST']._serialized_start=3667
  _globals['_CONFIGUREOUTPUTMODEREQUEST']._serialized_end=3826
  _globals['_CONFIGUREOUTPUTMODERESPONSE']._serialized_start=3828
  _globals['_CONFIGUREOUTPUTMODERESPONSE']._serialized_end=3873
  _globals['_CONFIGUREREFERENCECLOCKREQUEST']._serialized_start=3876
  _globals['_CONFIGUREREFERENCECLOCKREQUEST']._serialized_end=4011
  _globals['_CONFIGUREREFERENCECLOCKRESPONSE']._serialized_start=4013
  _globals['_CONFIGUREREFERENCECLOCKRESPONSE']._serialized_end=4062
  _globals['_CONFIGUREOUTPUTIMPEDANCEREQUEST']._serialized_start=4064
  _globals['_CONFIGUREOUTPUTIMPEDANCEREQUEST']._serialized_end=4174
  _globals['_CONFIGUREOUTPUTIMPEDANCERESPONSE']._serialized_start=4176
  _globals['_CONFIGUREOUTPUTIMPEDANCERESPONSE']._serialized_end=4226
  _globals['_CONFIGUREOUTPUTENABLEDREQUEST']._serialized_start=4228
  _globals['_CONFIGUREOUTPUTENABLEDREQUEST']._serialized_end=4334
  _globals['_CONFIGUREOUTPUTENABLEDRESPONSE']._serialized_start=4336
  _globals['_CONFIGUREOUTPUTENABLEDRESPONSE']._serialized_end=4384
  _globals['_CONFIGURECHANNELSREQUEST']._serialized_start=4386
  _globals['_CONFIGURECHANNELSREQUEST']._serialized_end=4466
  _globals['_CONFIGURECHANNELSRESPONSE']._serialized_start=4468
  _globals['_CONFIGURECHANNELSRESPONSE']._serialized_end=4511
  _globals['_INITIATEGENERATIONREQUEST']._serialized_start=4513
  _globals['_INITIATEGENERATIONREQUEST']._serialized_end=4576
  _globals['_INITIATEGENERATIONRESPONSE']._serialized_start=4578
  _globals['_INITIATEGENERATIONRESPONSE']._serialized_end=4622
  _globals['_ABORTGENERATIONREQUEST']._serialized_start=4624
  _globals['_ABORTGENERATIONREQUEST']._serialized_end=4684
  _globals['_ABORTGENERATIONRESPONSE']._serialized_start=4686
  _globals['_ABORTGENERATIONRESPONSE']._serialized_end=4727
  _globals['_CONFIGURESTANDARDWAVEFORMREQUEST']._serialized_start=4730
  _globals['_CONFIGURESTANDARDWAVEFORMREQUEST']._serialized_end=4984
  _globals['_CONFIGURESTANDARDWAVEFORMRESPONSE']._serialized_start=4986
  _globals['_CONFIGURESTANDARDWAVEFORMRESPONSE']._serialized_end=5037
  _globals['_DEFINEUSERSTANDARDWAVEFORMREQUEST']._serialized_start=5039
  _globals['_DEFINEUSERSTANDARDWAVEFORMREQUEST']._serialized_end=5161
  _globals['_DEFINEUSERSTANDARDWAVEFORMRESPONSE']._serialized_start=5163
  _globals['_DEFINEUSERSTANDARDWAVEFORMRESPONSE']._serialized_end=5215
  _globals['_CLEARUSERSTANDARDWAVEFORMREQUEST']._serialized_start=5217
  _globals['_CLEARUSERSTANDARDWAVEFORMREQUEST']._serialized_end=5309
  _globals['_CLEARUSERSTANDARDWAVEFORMRESPONSE']._serialized_start=5311
  _globals['_CLEARUSERSTANDARDWAVEFORMRESPONSE']._serialized_end=5362
  _globals['_CONFIGUREFREQUENCYREQUEST']._serialized_start=5364
  _globals['_CONFIGUREFREQUENCYREQUEST']._serialized_end=5468
  _globals['_CONFIGUREFREQUENCYRESPONSE']._serialized_start=5470
  _globals['_CONFIGUREFREQUENCYRESPONSE']._serialized_end=5514
  _globals['_CONFIGUREAMPLITUDEREQUEST']._serialized_start=5516
  _globals['_CONFIGUREAMPLITUDEREQUEST']._serialized_end=5620
  _globals['_CONFIGUREAMPLITUDERESPONSE']._serialized_start=5622
  _globals['_CONFIGUREAMPLITUDERESPONSE']._serialized_end=5666
  _globals['_QUERYARBWFMCAPABILITIESREQUEST']._serialized_start=5668
  _globals['_QUERYARBWFMCAPABILITIESREQUEST']._serialized_end=5736
  _globals['_QUERYARBWFMCAPABILITIESRESPONSE']._serialized_start=5739
  _globals['_QUERYARBWFMCAPABILITIESRESPONSE']._serialized_end=5913
  _globals['_CREATEWAVEFORMF64REQUEST']._serialized_start=5915
  _globals['_CREATEWAVEFORMF64REQUEST']._serialized_end=6028
  _globals['_CREATEWAVEFORMF64RESPONSE']._serialized_start=6030
  _globals['_CREATEWAVEFORMF64RESPONSE']._serialized_end=6098
  _globals['_CREATEWAVEFORMI16REQUEST']._serialized_start=6100
  _globals['_CREATEWAVEFORMI16REQUEST']._serialized_end=6213
  _globals['_CREATEWAVEFORMI16RESPONSE']._serialized_start=6215
  _globals['_CREATEWAVEFORMI16RESPONSE']._serialized_end=6283
  _globals['_CREATEWAVEFORMCOMPLEXF64REQUEST']._serialized_start=6286
  _globals['_CREATEWAVEFORMCOMPLEXF64REQUEST']._serialized_end=6438
  _globals['_CREATEWAVEFORMCOMPLEXF64RESPONSE']._serialized_start=6440
  _globals['_CREATEWAVEFORMCOMPLEXF64RESPONSE']._serialized_end=6515
  _globals['_CREATEWAVEFORMFROMFILEI16REQUEST']._serialized_start=6518
  _globals['_CREATEWAVEFORMFROMFILEI16REQUEST']._serialized_end=6720
  _globals['_CREATEWAVEFORMFROMFILEI16RESPONSE']._serialized_start=6722
  _globals['_CREATEWAVEFORMFROMFILEI16RESPONSE']._serialized_end=6798
  _globals['_CREATEWAVEFORMFROMFILEF64REQUEST']._serialized_start=6801
  _globals['_CREATEWAVEFORMFROMFILEF64REQUEST']._serialized_end=7003
  _globals['_CREATEWAVEFORMFROMFILEF64RESPONSE']._serialized_start=7005
  _globals['_CREATEWAVEFORMFROMFILEF64RESPONSE']._serialized_end=7081
  _globals['_CONFIGURESAMPLERATEREQUEST']._serialized_start=7083
  _globals['_CONFIGURESAMPLERATEREQUEST']._serialized_end=7168
  _globals['_CONFIGURESAMPLERATERESPONSE']._serialized_start=7170
  _globals['_CONFIGURESAMPLERATERESPONSE']._serialized_end=7215
  _globals['_CONFIGUREARBWAVEFORMREQUEST']._serialized_start=7218
  _globals['_CONFIGUREARBWAVEFORMREQUEST']._serialized_end=7360
  _globals['_CONFIGUREARBWAVEFORMRESPONSE']._serialized_start=7362
  _globals['_CONFIGUREARBWAVEFORMRESPONSE']._serialized_end=7408
  _globals['_CLEARARBWAVEFORMREQUEST']._serialized_start=7411
  _globals['_CLEARARBWAVEFORMREQUEST']._serialized_end=7583
  _globals['_CLEARARBWAVEFORMRESPONSE']._serialized_start=7585
  _globals['_CLEARARBWAVEFORMRESPONSE']._serialized_end=7627
  _globals['_ALLOCATENAMEDWAVEFORMREQUEST']._serialized_start=7630
  _globals['_ALLOCATENAMEDWAVEFORMREQUEST']._serialized_end=7764
  _globals['_ALLOCATENAMEDWAVEFORMRESPONSE']._serialized_start=7766
  _globals['_ALLOCATENAMEDWAVEFORMRESPONSE']._serialized_end=7813
  _globals['_SETNAMEDWAVEFORMNEXTWRITEPOSITIONREQUEST']._serialized_start=7816
  _globals['_SETNAMEDWAVEFORMNEXTWRITEPOSITIONREQUEST']._serialized_end=8050
  _globals['_SETNAMEDWAVEFORMNEXTWRITEPOSITIONRESPONSE']._serialized_start=8052
  _globals['_SETNAMEDWAVEFORMNEXTWRITEPOSITIONRESPONSE']._serialized_end=8111
  _globals['_WRITENAMEDWAVEFORMF64REQUEST']._serialized_start=8113
  _globals['_WRITENAMEDWAVEFORMF64REQUEST']._serialized_end=8238
  _globals['_WRITENAMEDWAVEFORMF64RESPONSE']._serialized_start=8240
  _globals['_WRITENAMEDWAVEFORMF64RESPONSE']._serialized_end=8287
  _globals['_WRITENAMEDWAVEFORMI16REQUEST']._serialized_start=8289
  _globals['_WRITENAMEDWAVEFORMI16REQUEST']._serialized_end=8414
  _globals['_WRITENAMEDWAVEFORMI16RESPONSE']._serialized_start=8416
  _globals['_WRITENAMEDWAVEFORMI16RESPONSE']._serialized_end=8463
  _globals['_WRITENAMEDWAVEFORMCOMPLEXF64REQUEST']._serialized_start=8466
  _globals['_WRITENAMEDWAVEFORMCOMPLEXF64REQUEST']._serialized_end=8630
  _globals['_WRITENAMEDWAVEFORMCOMPLEXF64RESPONSE']._serialized_start=8632
  _globals['_WRITENAMEDWAVEFORMCOMPLEXF64RESPONSE']._serialized_end=8686
  _globals['_WRITENAMEDWAVEFORMCOMPLEXI16REQUEST']._serialized_start=8689
  _globals['_WRITENAMEDWAVEFORMCOMPLEXI16REQUEST']._serialized_end=8850
  _globals['_WRITENAMEDWAVEFORMCOMPLEXI16RESPONSE']._serialized_start=8852
  _globals['_WRITENAMEDWAVEFORMCOMPLEXI16RESPONSE']._serialized_end=8906
  _globals['_DELETENAMEDWAVEFORMREQUEST']._serialized_start=8908
  _globals['_DELETENAMEDWAVEFORMREQUEST']._serialized_end=9017
  _globals['_DELETENAMEDWAVEFORMRESPONSE']._serialized_start=9019
  _globals['_DELETENAMEDWAVEFORMRESPONSE']._serialized_end=9064
  _globals['_QUERYARBSEQCAPABILITIESREQUEST']._serialized_start=9066
  _globals['_QUERYARBSEQCAPABILITIESREQUEST']._serialized_end=9134
  _globals['_QUERYARBSEQCAPABILITIESRESPONSE']._serialized_start=9137
  _globals['_QUERYARBSEQCAPABILITIESRESPONSE']._serialized_end=9317
  _globals['_CREATEARBSEQUENCEREQUEST']._serialized_start=9319
  _globals['_CREATEARBSEQUENCEREQUEST']._serialized_end=9440
  _globals['_CREATEARBSEQUENCERESPONSE']._serialized_start=9442
  _globals['_CREATEARBSEQUENCERESPONSE']._serialized_end=9510
  _globals['_CREATEADVANCEDARBSEQUENCEREQUEST']._serialized_start=9513
  _globals['_CREATEADVANCEDARBSEQUENCEREQUEST']._serialized_end=9702
  _globals['_CREATEADVANCEDARBSEQUENCERESPONSE']._serialized_start=9704
  _globals['_CREATEADVANCEDARBSEQUENCERESPONSE']._serialized_end=9811
  _globals['_CONFIGUREARBSEQUENCEREQUEST']._serialized_start=9814
  _globals['_CONFIGUREARBSEQUENCEREQUEST']._serialized_end=9956
  _globals['_CONFIGUREARBSEQUENCERESPONSE']._serialized_start=9958
  _globals['_CONFIGUREARBSEQUENCERESPONSE']._serialized_end=10004
  _globals['_CLEARARBSEQUENCEREQUEST']._serialized_start=10007
  _globals['_CLEARARBSEQUENCEREQUEST']._serialized_end=10179
  _globals['_CLEARARBSEQUENCERESPONSE']._serialized_start=10181
  _globals['_CLEARARBSEQUENCERESPONSE']._serialized_end=10223
  _globals['_CLEARARBMEMORYREQUEST']._serialized_start=10225
  _globals['_CLEARARBMEMORYREQUEST']._serialized_end=10284
  _globals['_CLEARARBMEMORYRESPONSE']._serialized_start=10286
  _globals['_CLEARARBMEMORYRESPONSE']._serialized_end=10326
  _globals['_QUERYFREQLISTCAPABILITIESREQUEST']._serialized_start=10328
  _globals['_QUERYFREQLISTCAPABILITIESREQUEST']._serialized_end=10398
  _globals['_QUERYFREQLISTCAPABILITIESRESPONSE']._serialized_start=10401
  _globals['_QUERYFREQLISTCAPABILITIESRESPONSE']._serialized_end=10691
  _globals['_CREATEFREQLISTREQUEST']._serialized_start=10694
  _globals['_CREATEFREQLISTREQUEST']._serialized_end=10886
  _globals['_CREATEFREQLISTRESPONSE']._serialized_start=10888
  _globals['_CREATEFREQLISTRESPONSE']._serialized_end=10959
  _globals['_CONFIGUREFREQLISTREQUEST']._serialized_start=10962
  _globals['_CONFIGUREFREQLISTREQUEST']._serialized_end=11136
  _globals['_CONFIGUREFREQLISTRESPONSE']._serialized_start=11138
  _globals['_CONFIGUREFREQLISTRESPONSE']._serialized_end=11181
  _globals['_CLEARFREQLISTREQUEST']._serialized_start=11184
  _globals['_CLEARFREQLISTREQUEST']._serialized_end=11377
  _globals['_CLEARFREQLISTRESPONSE']._serialized_start=11379
  _globals['_CLEARFREQLISTRESPONSE']._serialized_end=11418
  _globals['_WRITESCRIPTREQUEST']._serialized_start=11420
  _globals['_WRITESCRIPTREQUEST']._serialized_end=11514
  _globals['_WRITESCRIPTRESPONSE']._serialized_start=11516
  _globals['_WRITESCRIPTRESPONSE']._serialized_end=11553
  _globals['_DELETESCRIPTREQUEST']._serialized_start=11555
  _globals['_DELETESCRIPTREQUEST']._serialized_end=11655
  _globals['_DELETESCRIPTRESPONSE']._serialized_start=11657
  _globals['_DELETESCRIPTRESPONSE']._serialized_end=11695
  _globals['_EXPORTSIGNALREQUEST']._serialized_start=11698
  _globals['_EXPORTSIGNALREQUEST']._serialized_end=11883
  _globals['_EXPORTSIGNALRESPONSE']._serialized_start=11885
  _globals['_EXPORTSIGNALRESPONSE']._serialized_end=11923
  _globals['_ROUTESIGNALOUTREQUEST']._serialized_start=11926
  _globals['_ROUTESIGNALOUTREQUEST']._serialized_end=12235
  _globals['_ROUTESIGNALOUTRESPONSE']._serialized_start=12237
  _globals['_ROUTESIGNALOUTRESPONSE']._serialized_end=12277
  _globals['_SENDSOFTWAREEDGETRIGGERREQUEST']._serialized_start=12280
  _globals['_SENDSOFTWAREEDGETRIGGERREQUEST']._serialized_end=12448
  _globals['_SENDSOFTWAREEDGETRIGGERRESPONSE']._serialized_start=12450
  _globals['_SENDSOFTWAREEDGETRIGGERRESPONSE']._serialized_end=12499
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERREQUEST']._serialized_start=12501
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERREQUEST']._serialized_end=12608
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERRESPONSE']._serialized_start=12610
  _globals['_CONFIGUREDIGITALEDGESTARTTRIGGERRESPONSE']._serialized_end=12668
  _globals['_CONFIGURESOFTWAREEDGESTARTTRIGGERREQUEST']._serialized_start=12670
  _globals['_CONFIGURESOFTWAREEDGESTARTTRIGGERREQUEST']._serialized_end=12748
  _globals['_CONFIGURESOFTWAREEDGESTARTTRIGGERRESPONSE']._serialized_start=12750
  _globals['_CONFIGURESOFTWAREEDGESTARTTRIGGERRESPONSE']._serialized_end=12809
  _globals['_DISABLESTARTTRIGGERREQUEST']._serialized_start=12811
  _globals['_DISABLESTARTTRIGGERREQUEST']._serialized_end=12875
  _globals['_DISABLESTARTTRIGGERRESPONSE']._serialized_start=12877
  _globals['_DISABLESTARTTRIGGERRESPONSE']._serialized_end=12922
  _globals['_CONFIGUREP2PENDPOINTFULLNESSSTARTTRIGGERREQUEST']._serialized_start=12924
  _globals['_CONFIGUREP2PENDPOINTFULLNESSSTARTTRIGGERREQUEST']._serialized_end=13046
  _globals['_CONFIGUREP2PENDPOINTFULLNESSSTARTTRIGGERRESPONSE']._serialized_start=13048
  _globals['_CONFIGUREP2PENDPOINTFULLNESSSTARTTRIGGERRESPONSE']._serialized_end=13114
  _globals['_CONFIGUREDIGITALEDGESCRIPTTRIGGERREQUEST']._serialized_start=13117
  _globals['_CONFIGUREDIGITALEDGESCRIPTTRIGGERREQUEST']._serialized_end=13245
  _globals['_CONFIGUREDIGITALEDGESCRIPTTRIGGERRESPONSE']._serialized_start=13247
  _globals['_CONFIGUREDIGITALEDGESCRIPTTRIGGERRESPONSE']._serialized_end=13306
  _globals['_CONFIGUREDIGITALLEVELSCRIPTTRIGGERREQUEST']._serialized_start=13309
  _globals['_CONFIGUREDIGITALLEVELSCRIPTTRIGGERREQUEST']._serialized_end=13523
  _globals['_CONFIGUREDIGITALLEVELSCRIPTTRIGGERRESPONSE']._serialized_start=13525
  _globals['_CONFIGUREDIGITALLEVELSCRIPTTRIGGERRESPONSE']._serialized_end=13585
  _globals['_CONFIGURESOFTWAREEDGESCRIPTTRIGGERREQUEST']._serialized_start=13587
  _globals['_CONFIGURESOFTWAREEDGESCRIPTTRIGGERREQUEST']._serialized_end=13686
  _globals['_CONFIGURESOFTWAREEDGESCRIPTTRIGGERRESPONSE']._serialized_start=13688
  _globals['_CONFIGURESOFTWAREEDGESCRIPTTRIGGERRESPONSE']._serialized_end=13748
  _globals['_DISABLESCRIPTTRIGGERREQUEST']._serialized_start=13750
  _globals['_DISABLESCRIPTTRIGGERREQUEST']._serialized_end=13835
  _globals['_DISABLESCRIPTTRIGGERRESPONSE']._serialized_start=13837
  _globals['_DISABLESCRIPTTRIGGERRESPONSE']._serialized_end=13883
  _globals['_CONFIGURECLOCKMODEREQUEST']._serialized_start=13886
  _globals['_CONFIGURECLOCKMODEREQUEST']._serialized_end=14040
  _globals['_CONFIGURECLOCKMODERESPONSE']._serialized_start=14042
  _globals['_CONFIGURECLOCKMODERESPONSE']._serialized_end=14086
  _globals['_ADJUSTSAMPLECLOCKRELATIVEDELAYREQUEST']._serialized_start=14088
  _globals['_ADJUSTSAMPLECLOCKRELATIVEDELAYREQUEST']._serialized_end=14188
  _globals['_ADJUSTSAMPLECLOCKRELATIVEDELAYRESPONSE']._serialized_start=14190
  _globals['_ADJUSTSAMPLECLOCKRELATIVEDELAYRESPONSE']._serialized_end=14246
  _globals['_ALLOCATEWAVEFORMREQUEST']._serialized_start=14248
  _globals['_ALLOCATEWAVEFORMREQUEST']._serialized_end=14354
  _globals['_ALLOCATEWAVEFORMRESPONSE']._serialized_start=14356
  _globals['_ALLOCATEWAVEFORMRESPONSE']._serialized_end=14423
  _globals['_SETWAVEFORMNEXTWRITEPOSITIONREQUEST']._serialized_start=14426
  _globals['_SETWAVEFORMNEXTWRITEPOSITIONREQUEST']._serialized_end=14657
  _globals['_SETWAVEFORMNEXTWRITEPOSITIONRESPONSE']._serialized_start=14659
  _globals['_SETWAVEFORMNEXTWRITEPOSITIONRESPONSE']._serialized_end=14713
  _globals['_WRITEWAVEFORMREQUEST']._serialized_start=14715
  _globals['_WRITEWAVEFORMREQUEST']._serialized_end=14834
  _globals['_WRITEWAVEFORMRESPONSE']._serialized_start=14836
  _globals['_WRITEWAVEFORMRESPONSE']._serialized_end=14875
  _globals['_WRITEBINARY16WAVEFORMREQUEST']._serialized_start=14877
  _globals['_WRITEBINARY16WAVEFORMREQUEST']._serialized_end=15004
  _globals['_WRITEBINARY16WAVEFORMRESPONSE']._serialized_start=15006
  _globals['_WRITEBINARY16WAVEFORMRESPONSE']._serialized_end=15053
  _globals['_WRITEWAVEFORMCOMPLEXF64REQUEST']._serialized_start=15056
  _globals['_WRITEWAVEFORMCOMPLEXF64REQUEST']._serialized_end=15217
  _globals['_WRITEWAVEFORMCOMPLEXF64RESPONSE']._serialized_start=15219
  _globals['_WRITEWAVEFORMCOMPLEXF64RESPONSE']._serialized_end=15268
  _globals['_WRITECOMPLEXBINARY16WAVEFORMREQUEST']._serialized_start=15271
  _globals['_WRITECOMPLEXBINARY16WAVEFORMREQUEST']._serialized_end=15434
  _globals['_WRITECOMPLEXBINARY16WAVEFORMRESPONSE']._serialized_start=15436
  _globals['_WRITECOMPLEXBINARY16WAVEFORMRESPONSE']._serialized_end=15490
  _globals['_SELFCALREQUEST']._serialized_start=15492
  _globals['_SELFCALREQUEST']._serialized_end=15544
  _globals['_SELFCALRESPONSE']._serialized_start=15546
  _globals['_SELFCALRESPONSE']._serialized_end=15579
  _globals['_GETSELFCALSUPPORTEDREQUEST']._serialized_start=15581
  _globals['_GETSELFCALSUPPORTEDREQUEST']._serialized_end=15645
  _globals['_GETSELFCALSUPPORTEDRESPONSE']._serialized_start=15647
  _globals['_GETSELFCALSUPPORTEDRESPONSE']._serialized_end=15720
  _globals['_GETSELFCALLASTDATEANDTIMEREQUEST']._serialized_start=15722
  _globals['_GETSELFCALLASTDATEANDTIMEREQUEST']._serialized_end=15792
  _globals['_GETSELFCALLASTDATEANDTIMERESPONSE']._serialized_start=15794
  _globals['_GETSELFCALLASTDATEANDTIMERESPONSE']._serialized_end=15917
  _globals['_GETEXTCALLASTDATEANDTIMEREQUEST']._serialized_start=15919
  _globals['_GETEXTCALLASTDATEANDTIMEREQUEST']._serialized_end=15988
  _globals['_GETEXTCALLASTDATEANDTIMERESPONSE']._serialized_start=15990
  _globals['_GETEXTCALLASTDATEANDTIMERESPONSE']._serialized_end=16112
  _globals['_GETSELFCALLASTTEMPREQUEST']._serialized_start=16114
  _globals['_GETSELFCALLASTTEMPREQUEST']._serialized_end=16177
  _globals['_GETSELFCALLASTTEMPRESPONSE']._serialized_start=16179
  _globals['_GETSELFCALLASTTEMPRESPONSE']._serialized_end=16244
  _globals['_GETEXTCALLASTTEMPREQUEST']._serialized_start=16246
  _globals['_GETEXTCALLASTTEMPREQUEST']._serialized_end=16308
  _globals['_GETEXTCALLASTTEMPRESPONSE']._serialized_start=16310
  _globals['_GETEXTCALLASTTEMPRESPONSE']._serialized_end=16374
  _globals['_GETEXTCALRECOMMENDEDINTERVALREQUEST']._serialized_start=16376
  _globals['_GETEXTCALRECOMMENDEDINTERVALREQUEST']._serialized_end=16449
  _globals['_GETEXTCALRECOMMENDEDINTERVALRESPONSE']._serialized_start=16451
  _globals['_GETEXTCALRECOMMENDEDINTERVALRESPONSE']._serialized_end=16521
  _globals['_READCURRENTTEMPERATUREREQUEST']._serialized_start=16523
  _globals['_READCURRENTTEMPERATUREREQUEST']._serialized_end=16590
  _globals['_READCURRENTTEMPERATURERESPONSE']._serialized_start=16592
  _globals['_READCURRENTTEMPERATURERESPONSE']._serialized_end=16661
  _globals['_CONFIGURECUSTOMFIRFILTERCOEFFICIENTSREQUEST']._serialized_start=16664
  _globals['_CONFIGURECUSTOMFIRFILTERCOEFFICIENTSREQUEST']._serialized_end=16795
  _globals['_CONFIGURECUSTOMFIRFILTERCOEFFICIENTSRESPONSE']._serialized_start=16797
  _globals['_CONFIGURECUSTOMFIRFILTERCOEFFICIENTSRESPONSE']._serialized_end=16859
  _globals['_GETFIRFILTERCOEFFICIENTSREQUEST']._serialized_start=16861
  _globals['_GETFIRFILTERCOEFFICIENTSREQUEST']._serialized_end=16952
  _globals['_GETFIRFILTERCOEFFICIENTSRESPONSE']._serialized_start=16954
  _globals['_GETFIRFILTERCOEFFICIENTSRESPONSE']._serialized_end=17069
  _globals['_GETSTREAMENDPOINTHANDLEREQUEST']._serialized_start=17071
  _globals['_GETSTREAMENDPOINTHANDLEREQUEST']._serialized_end=17164
  _globals['_GETSTREAMENDPOINTHANDLERESPONSE']._serialized_start=17166
  _globals['_GETSTREAMENDPOINTHANDLERESPONSE']._serialized_end=17238
  _globals['_WRITEP2PENDPOINTI16REQUEST']._serialized_start=17240
  _globals['_WRITEP2PENDPOINTI16REQUEST']._serialized_end=17350
  _globals['_WRITEP2PENDPOINTI16RESPONSE']._serialized_start=17352
  _globals['_WRITEP2PENDPOINTI16RESPONSE']._serialized_end=17397
  _globals['_CONFIGURESYNCHRONIZATIONREQUEST']._serialized_start=17399
  _globals['_CONFIGURESYNCHRONIZATIONREQUEST']._serialized_end=17522
  _globals['_CONFIGURESYNCHRONIZATIONRESPONSE']._serialized_start=17524
  _globals['_CONFIGURESYNCHRONIZATIONRESPONSE']._serialized_end=17574
  _globals['_ENABLEDIGITALPATTERNINGREQUEST']._serialized_start=17576
  _globals['_ENABLEDIGITALPATTERNINGREQUEST']._serialized_end=17666
  _globals['_ENABLEDIGITALPATTERNINGRESPONSE']._serialized_start=17668
  _globals['_ENABLEDIGITALPATTERNINGRESPONSE']._serialized_end=17717
  _globals['_DISABLEDIGITALPATTERNINGREQUEST']._serialized_start=17719
  _globals['_DISABLEDIGITALPATTERNINGREQUEST']._serialized_end=17810
  _globals['_DISABLEDIGITALPATTERNINGRESPONSE']._serialized_start=17812
  _globals['_DISABLEDIGITALPATTERNINGRESPONSE']._serialized_end=17862
  _globals['_ENABLEDIGITALFILTERREQUEST']._serialized_start=17864
  _globals['_ENABLEDIGITALFILTERREQUEST']._serialized_end=17950
  _globals['_ENABLEDIGITALFILTERRESPONSE']._serialized_start=17952
  _globals['_ENABLEDIGITALFILTERRESPONSE']._serialized_end=17997
  _globals['_DISABLEDIGITALFILTERREQUEST']._serialized_start=17999
  _globals['_DISABLEDIGITALFILTERREQUEST']._serialized_end=18086
  _globals['_DISABLEDIGITALFILTERRESPONSE']._serialized_start=18088
  _globals['_DISABLEDIGITALFILTERRESPONSE']._serialized_end=18134
  _globals['_ENABLEANALOGFILTERREQUEST']._serialized_start=18136
  _globals['_ENABLEANALOGFILTERREQUEST']._serialized_end=18258
  _globals['_ENABLEANALOGFILTERRESPONSE']._serialized_start=18260
  _globals['_ENABLEANALOGFILTERRESPONSE']._serialized_end=18304
  _globals['_DISABLEANALOGFILTERREQUEST']._serialized_start=18306
  _globals['_DISABLEANALOGFILTERREQUEST']._serialized_end=18392
  _globals['_DISABLEANALOGFILTERRESPONSE']._serialized_start=18394
  _globals['_DISABLEANALOGFILTERRESPONSE']._serialized_end=18439
  _globals['_CONFIGURESAMPLECLOCKSOURCEREQUEST']._serialized_start=18441
  _globals['_CONFIGURESAMPLECLOCKSOURCEREQUEST']._serialized_end=18541
  _globals['_CONFIGURESAMPLECLOCKSOURCERESPONSE']._serialized_start=18543
  _globals['_CONFIGURESAMPLECLOCKSOURCERESPONSE']._serialized_end=18595
  _globals['_CONFIGURETRIGGERMODEREQUEST']._serialized_start=18598
  _globals['_CONFIGURETRIGGERMODEREQUEST']._serialized_end=18784
  _globals['_CONFIGURETRIGGERMODERESPONSE']._serialized_start=18786
  _globals['_CONFIGURETRIGGERMODERESPONSE']._serialized_end=18832
  _globals['_IMPORTATTRIBUTECONFIGURATIONFILEREQUEST']._serialized_start=18834
  _globals['_IMPORTATTRIBUTECONFIGURATIONFILEREQUEST']._serialized_end=18930
  _globals['_IMPORTATTRIBUTECONFIGURATIONFILERESPONSE']._serialized_start=18932
  _globals['_IMPORTATTRIBUTECONFIGURATIONFILERESPONSE']._serialized_end=18990
  _globals['_EXPORTATTRIBUTECONFIGURATIONFILEREQUEST']._serialized_start=18992
  _globals['_EXPORTATTRIBUTECONFIGURATIONFILEREQUEST']._serialized_end=19088
  _globals['_EXPORTATTRIBUTECONFIGURATIONFILERESPONSE']._serialized_start=19090
  _globals['_EXPORTATTRIBUTECONFIGURATIONFILERESPONSE']._serialized_end=19148
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_start=19150
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_end=19252
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_start=19254
  _globals['_IMPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_end=19314
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_start=19316
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERREQUEST']._serialized_end=19395
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_start=19397
  _globals['_EXPORTATTRIBUTECONFIGURATIONBUFFERRESPONSE']._serialized_end=19480
  _globals['_SETATTRIBUTEVIINT64REQUEST']._serialized_start=19483
  _globals['_SETATTRIBUTEVIINT64REQUEST']._serialized_end=19650
  _globals['_SETATTRIBUTEVIINT64RESPONSE']._serialized_start=19652
  _globals['_SETATTRIBUTEVIINT64RESPONSE']._serialized_end=19697
  _globals['_CHECKATTRIBUTEVIINT64REQUEST']._serialized_start=19700
  _globals['_CHECKATTRIBUTEVIINT64REQUEST']._serialized_end=19869
  _globals['_CHECKATTRIBUTEVIINT64RESPONSE']._serialized_start=19871
  _globals['_CHECKATTRIBUTEVIINT64RESPONSE']._serialized_end=19918
  _globals['_GETATTRIBUTEVIINT64REQUEST']._serialized_start=19921
  _globals['_GETATTRIBUTEVIINT64REQUEST']._serialized_end=20059
  _globals['_GETATTRIBUTEVIINT64RESPONSE']._serialized_start=20061
  _globals['_GETATTRIBUTEVIINT64RESPONSE']._serialized_end=20131
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_start=20134
  _globals['_SETATTRIBUTEVIINT32REQUEST']._serialized_end=20395
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_start=20397
  _globals['_SETATTRIBUTEVIINT32RESPONSE']._serialized_end=20442
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_start=20445
  _globals['_SETATTRIBUTEVIREAL64REQUEST']._serialized_end=20708
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_start=20710
  _globals['_SETATTRIBUTEVIREAL64RESPONSE']._serialized_end=20756
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_start=20759
  _globals['_SETATTRIBUTEVISTRINGREQUEST']._serialized_end=21035
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_start=21037
  _globals['_SETATTRIBUTEVISTRINGRESPONSE']._serialized_end=21083
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=21086
  _globals['_SETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=21251
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=21253
  _globals['_SETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=21300
  _globals['_SETATTRIBUTEVISESSIONREQUEST']._serialized_start=21303
  _globals['_SETATTRIBUTEVISESSIONREQUEST']._serialized_end=21492
  _globals['_SETATTRIBUTEVISESSIONRESPONSE']._serialized_start=21494
  _globals['_SETATTRIBUTEVISESSIONRESPONSE']._serialized_end=21541
  _globals['_CHECKATTRIBUTEVIINT32REQUEST']._serialized_start=21544
  _globals['_CHECKATTRIBUTEVIINT32REQUEST']._serialized_end=21807
  _globals['_CHECKATTRIBUTEVIINT32RESPONSE']._serialized_start=21809
  _globals['_CHECKATTRIBUTEVIINT32RESPONSE']._serialized_end=21856
  _globals['_CHECKATTRIBUTEVIREAL64REQUEST']._serialized_start=21859
  _globals['_CHECKATTRIBUTEVIREAL64REQUEST']._serialized_end=22124
  _globals['_CHECKATTRIBUTEVIREAL64RESPONSE']._serialized_start=22126
  _globals['_CHECKATTRIBUTEVIREAL64RESPONSE']._serialized_end=22174
  _globals['_CHECKATTRIBUTEVISTRINGREQUEST']._serialized_start=22177
  _globals['_CHECKATTRIBUTEVISTRINGREQUEST']._serialized_end=22455
  _globals['_CHECKATTRIBUTEVISTRINGRESPONSE']._serialized_start=22457
  _globals['_CHECKATTRIBUTEVISTRINGRESPONSE']._serialized_end=22505
  _globals['_CHECKATTRIBUTEVIBOOLEANREQUEST']._serialized_start=22508
  _globals['_CHECKATTRIBUTEVIBOOLEANREQUEST']._serialized_end=22675
  _globals['_CHECKATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=22677
  _globals['_CHECKATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=22726
  _globals['_CHECKATTRIBUTEVISESSIONREQUEST']._serialized_start=22729
  _globals['_CHECKATTRIBUTEVISESSIONREQUEST']._serialized_end=22920
  _globals['_CHECKATTRIBUTEVISESSIONRESPONSE']._serialized_start=22922
  _globals['_CHECKATTRIBUTEVISESSIONRESPONSE']._serialized_end=22971
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_start=22974
  _globals['_GETATTRIBUTEVIINT32REQUEST']._serialized_end=23112
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_start=23114
  _globals['_GETATTRIBUTEVIINT32RESPONSE']._serialized_end=23184
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_start=23187
  _globals['_GETATTRIBUTEVIREAL64REQUEST']._serialized_end=23326
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_start=23328
  _globals['_GETATTRIBUTEVIREAL64RESPONSE']._serialized_end=23399
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_start=23402
  _globals['_GETATTRIBUTEVISTRINGREQUEST']._serialized_end=23541
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_start=23543
  _globals['_GETATTRIBUTEVISTRINGRESPONSE']._serialized_end=23614
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_start=23617
  _globals['_GETATTRIBUTEVIBOOLEANREQUEST']._serialized_end=23757
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_start=23759
  _globals['_GETATTRIBUTEVIBOOLEANRESPONSE']._serialized_end=23831
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_start=23834
  _globals['_GETATTRIBUTEVISESSIONREQUEST']._serialized_end=23974
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_start=23976
  _globals['_GETATTRIBUTEVISESSIONRESPONSE']._serialized_end=24072
  _globals['_RESETATTRIBUTEREQUEST']._serialized_start=24075
  _globals['_RESETATTRIBUTEREQUEST']._serialized_end=24208
  _globals['_RESETATTRIBUTERESPONSE']._serialized_start=24210
  _globals['_RESETATTRIBUTERESPONSE']._serialized_end=24250
  _globals['_MANUALENABLEP2PSTREAMREQUEST']._serialized_start=24252
  _globals['_MANUALENABLEP2PSTREAMREQUEST']._serialized_end=24341
  _globals['_MANUALENABLEP2PSTREAMRESPONSE']._serialized_start=24343
  _globals['_MANUALENABLEP2PSTREAMRESPONSE']._serialized_end=24390
  _globals['_CREATEWAVEFORMFROMFILEHWSREQUEST']._serialized_start=24393
  _globals['_CREATEWAVEFORMFROMFILEHWSREQUEST']._serialized_end=24579
  _globals['_CREATEWAVEFORMFROMFILEHWSRESPONSE']._serialized_start=24581
  _globals['_CREATEWAVEFORMFROMFILEHWSRESPONSE']._serialized_end=24657
  _globals['_NIFGEN']._serialized_start=51304
  _globals['_NIFGEN']._serialized_end=65475
# @@protoc_insertion_point(module_scope)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/nifgen_pb2_grpc.py sha256=b0435cdc6d47b18df15ca55e4b2cf092c42336ec56a3b70462ecdbd8a3f3fb9b bytes=212964 -->
## FILE: generated/nifgen/nifgen/nifgen_pb2_grpc.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/nifgen_pb2_grpc.py`
- sha256: `b0435cdc6d47b18df15ca55e4b2cf092c42336ec56a3b70462ecdbd8a3f3fb9b`
- bytes: 212964

````python
# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import nifgen_pb2 as nifgen__pb2


class NiFgenStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Init = channel.unary_unary(
                '/nifgen_grpc.NiFgen/Init',
                request_serializer=nifgen__pb2.InitRequest.SerializeToString,
                response_deserializer=nifgen__pb2.InitResponse.FromString,
                )
        self.InitWithOptions = channel.unary_unary(
                '/nifgen_grpc.NiFgen/InitWithOptions',
                request_serializer=nifgen__pb2.InitWithOptionsRequest.SerializeToString,
                response_deserializer=nifgen__pb2.InitWithOptionsResponse.FromString,
                )
        self.InitializeWithChannels = channel.unary_unary(
                '/nifgen_grpc.NiFgen/InitializeWithChannels',
                request_serializer=nifgen__pb2.InitializeWithChannelsRequest.SerializeToString,
                response_deserializer=nifgen__pb2.InitializeWithChannelsResponse.FromString,
                )
        self.Close = channel.unary_unary(
                '/nifgen_grpc.NiFgen/Close',
                request_serializer=nifgen__pb2.CloseRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CloseResponse.FromString,
                )
        self.Reset = channel.unary_unary(
                '/nifgen_grpc.NiFgen/Reset',
                request_serializer=nifgen__pb2.ResetRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ResetResponse.FromString,
                )
        self.SelfTest = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SelfTest',
                request_serializer=nifgen__pb2.SelfTestRequest.SerializeToString,
                response_deserializer=nifgen__pb2.SelfTestResponse.FromString,
                )
        self.ErrorQuery = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ErrorQuery',
                request_serializer=nifgen__pb2.ErrorQueryRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ErrorQueryResponse.FromString,
                )
        self.ErrorMessage = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ErrorMessage',
                request_serializer=nifgen__pb2.ErrorMessageRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ErrorMessageResponse.FromString,
                )
        self.RevisionQuery = channel.unary_unary(
                '/nifgen_grpc.NiFgen/RevisionQuery',
                request_serializer=nifgen__pb2.RevisionQueryRequest.SerializeToString,
                response_deserializer=nifgen__pb2.RevisionQueryResponse.FromString,
                )
        self.GetError = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetError',
                request_serializer=nifgen__pb2.GetErrorRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetErrorResponse.FromString,
                )
        self.ClearError = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ClearError',
                request_serializer=nifgen__pb2.ClearErrorRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ClearErrorResponse.FromString,
                )
        self.ErrorHandler = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ErrorHandler',
                request_serializer=nifgen__pb2.ErrorHandlerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ErrorHandlerResponse.FromString,
                )
        self.GetChannelName = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetChannelName',
                request_serializer=nifgen__pb2.GetChannelNameRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetChannelNameResponse.FromString,
                )
        self.ResetInterchangeCheck = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ResetInterchangeCheck',
                request_serializer=nifgen__pb2.ResetInterchangeCheckRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ResetInterchangeCheckResponse.FromString,
                )
        self.ClearInterchangeWarnings = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ClearInterchangeWarnings',
                request_serializer=nifgen__pb2.ClearInterchangeWarningsRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ClearInterchangeWarningsResponse.FromString,
                )
        self.InvalidateAllAttributes = channel.unary_unary(
                '/nifgen_grpc.NiFgen/InvalidateAllAttributes',
                request_serializer=nifgen__pb2.InvalidateAllAttributesRequest.SerializeToString,
                response_deserializer=nifgen__pb2.InvalidateAllAttributesResponse.FromString,
                )
        self.ResetWithDefaults = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ResetWithDefaults',
                request_serializer=nifgen__pb2.ResetWithDefaultsRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ResetWithDefaultsResponse.FromString,
                )
        self.Disable = channel.unary_unary(
                '/nifgen_grpc.NiFgen/Disable',
                request_serializer=nifgen__pb2.DisableRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DisableResponse.FromString,
                )
        self.Commit = channel.unary_unary(
                '/nifgen_grpc.NiFgen/Commit',
                request_serializer=nifgen__pb2.CommitRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CommitResponse.FromString,
                )
        self.GetHardwareState = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetHardwareState',
                request_serializer=nifgen__pb2.GetHardwareStateRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetHardwareStateResponse.FromString,
                )
        self.WaitUntilDone = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WaitUntilDone',
                request_serializer=nifgen__pb2.WaitUntilDoneRequest.SerializeToString,
                response_deserializer=nifgen__pb2.WaitUntilDoneResponse.FromString,
                )
        self.IsDone = channel.unary_unary(
                '/nifgen_grpc.NiFgen/IsDone',
                request_serializer=nifgen__pb2.IsDoneRequest.SerializeToString,
                response_deserializer=nifgen__pb2.IsDoneResponse.FromString,
                )
        self.ResetDevice = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ResetDevice',
                request_serializer=nifgen__pb2.ResetDeviceRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ResetDeviceResponse.FromString,
                )
        self.ConfigureOperationMode = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureOperationMode',
                request_serializer=nifgen__pb2.ConfigureOperationModeRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureOperationModeResponse.FromString,
                )
        self.ConfigureOutputMode = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureOutputMode',
                request_serializer=nifgen__pb2.ConfigureOutputModeRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureOutputModeResponse.FromString,
                )
        self.ConfigureReferenceClock = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureReferenceClock',
                request_serializer=nifgen__pb2.ConfigureReferenceClockRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureReferenceClockResponse.FromString,
                )
        self.ConfigureOutputImpedance = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureOutputImpedance',
                request_serializer=nifgen__pb2.ConfigureOutputImpedanceRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureOutputImpedanceResponse.FromString,
                )
        self.ConfigureOutputEnabled = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureOutputEnabled',
                request_serializer=nifgen__pb2.ConfigureOutputEnabledRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureOutputEnabledResponse.FromString,
                )
        self.ConfigureChannels = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureChannels',
                request_serializer=nifgen__pb2.ConfigureChannelsRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureChannelsResponse.FromString,
                )
        self.InitiateGeneration = channel.unary_unary(
                '/nifgen_grpc.NiFgen/InitiateGeneration',
                request_serializer=nifgen__pb2.InitiateGenerationRequest.SerializeToString,
                response_deserializer=nifgen__pb2.InitiateGenerationResponse.FromString,
                )
        self.AbortGeneration = channel.unary_unary(
                '/nifgen_grpc.NiFgen/AbortGeneration',
                request_serializer=nifgen__pb2.AbortGenerationRequest.SerializeToString,
                response_deserializer=nifgen__pb2.AbortGenerationResponse.FromString,
                )
        self.ConfigureStandardWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureStandardWaveform',
                request_serializer=nifgen__pb2.ConfigureStandardWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureStandardWaveformResponse.FromString,
                )
        self.DefineUserStandardWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/DefineUserStandardWaveform',
                request_serializer=nifgen__pb2.DefineUserStandardWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DefineUserStandardWaveformResponse.FromString,
                )
        self.ClearUserStandardWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ClearUserStandardWaveform',
                request_serializer=nifgen__pb2.ClearUserStandardWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ClearUserStandardWaveformResponse.FromString,
                )
        self.ConfigureFrequency = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureFrequency',
                request_serializer=nifgen__pb2.ConfigureFrequencyRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureFrequencyResponse.FromString,
                )
        self.ConfigureAmplitude = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureAmplitude',
                request_serializer=nifgen__pb2.ConfigureAmplitudeRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureAmplitudeResponse.FromString,
                )
        self.QueryArbWfmCapabilities = channel.unary_unary(
                '/nifgen_grpc.NiFgen/QueryArbWfmCapabilities',
                request_serializer=nifgen__pb2.QueryArbWfmCapabilitiesRequest.SerializeToString,
                response_deserializer=nifgen__pb2.QueryArbWfmCapabilitiesResponse.FromString,
                )
        self.CreateWaveformF64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateWaveformF64',
                request_serializer=nifgen__pb2.CreateWaveformF64Request.SerializeToString,
                response_deserializer=nifgen__pb2.CreateWaveformF64Response.FromString,
                )
        self.CreateWaveformI16 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateWaveformI16',
                request_serializer=nifgen__pb2.CreateWaveformI16Request.SerializeToString,
                response_deserializer=nifgen__pb2.CreateWaveformI16Response.FromString,
                )
        self.CreateWaveformComplexF64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateWaveformComplexF64',
                request_serializer=nifgen__pb2.CreateWaveformComplexF64Request.SerializeToString,
                response_deserializer=nifgen__pb2.CreateWaveformComplexF64Response.FromString,
                )
        self.CreateWaveformFromFileI16 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateWaveformFromFileI16',
                request_serializer=nifgen__pb2.CreateWaveformFromFileI16Request.SerializeToString,
                response_deserializer=nifgen__pb2.CreateWaveformFromFileI16Response.FromString,
                )
        self.CreateWaveformFromFileF64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateWaveformFromFileF64',
                request_serializer=nifgen__pb2.CreateWaveformFromFileF64Request.SerializeToString,
                response_deserializer=nifgen__pb2.CreateWaveformFromFileF64Response.FromString,
                )
        self.ConfigureSampleRate = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureSampleRate',
                request_serializer=nifgen__pb2.ConfigureSampleRateRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureSampleRateResponse.FromString,
                )
        self.ConfigureArbWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureArbWaveform',
                request_serializer=nifgen__pb2.ConfigureArbWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureArbWaveformResponse.FromString,
                )
        self.ClearArbWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ClearArbWaveform',
                request_serializer=nifgen__pb2.ClearArbWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ClearArbWaveformResponse.FromString,
                )
        self.AllocateNamedWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/AllocateNamedWaveform',
                request_serializer=nifgen__pb2.AllocateNamedWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.AllocateNamedWaveformResponse.FromString,
                )
        self.SetNamedWaveformNextWritePosition = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SetNamedWaveformNextWritePosition',
                request_serializer=nifgen__pb2.SetNamedWaveformNextWritePositionRequest.SerializeToString,
                response_deserializer=nifgen__pb2.SetNamedWaveformNextWritePositionResponse.FromString,
                )
        self.WriteNamedWaveformF64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteNamedWaveformF64',
                request_serializer=nifgen__pb2.WriteNamedWaveformF64Request.SerializeToString,
                response_deserializer=nifgen__pb2.WriteNamedWaveformF64Response.FromString,
                )
        self.WriteNamedWaveformI16 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteNamedWaveformI16',
                request_serializer=nifgen__pb2.WriteNamedWaveformI16Request.SerializeToString,
                response_deserializer=nifgen__pb2.WriteNamedWaveformI16Response.FromString,
                )
        self.WriteNamedWaveformComplexF64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteNamedWaveformComplexF64',
                request_serializer=nifgen__pb2.WriteNamedWaveformComplexF64Request.SerializeToString,
                response_deserializer=nifgen__pb2.WriteNamedWaveformComplexF64Response.FromString,
                )
        self.WriteNamedWaveformComplexI16 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteNamedWaveformComplexI16',
                request_serializer=nifgen__pb2.WriteNamedWaveformComplexI16Request.SerializeToString,
                response_deserializer=nifgen__pb2.WriteNamedWaveformComplexI16Response.FromString,
                )
        self.DeleteNamedWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/DeleteNamedWaveform',
                request_serializer=nifgen__pb2.DeleteNamedWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DeleteNamedWaveformResponse.FromString,
                )
        self.QueryArbSeqCapabilities = channel.unary_unary(
                '/nifgen_grpc.NiFgen/QueryArbSeqCapabilities',
                request_serializer=nifgen__pb2.QueryArbSeqCapabilitiesRequest.SerializeToString,
                response_deserializer=nifgen__pb2.QueryArbSeqCapabilitiesResponse.FromString,
                )
        self.CreateArbSequence = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateArbSequence',
                request_serializer=nifgen__pb2.CreateArbSequenceRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CreateArbSequenceResponse.FromString,
                )
        self.CreateAdvancedArbSequence = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateAdvancedArbSequence',
                request_serializer=nifgen__pb2.CreateAdvancedArbSequenceRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CreateAdvancedArbSequenceResponse.FromString,
                )
        self.ConfigureArbSequence = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureArbSequence',
                request_serializer=nifgen__pb2.ConfigureArbSequenceRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureArbSequenceResponse.FromString,
                )
        self.ClearArbSequence = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ClearArbSequence',
                request_serializer=nifgen__pb2.ClearArbSequenceRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ClearArbSequenceResponse.FromString,
                )
        self.ClearArbMemory = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ClearArbMemory',
                request_serializer=nifgen__pb2.ClearArbMemoryRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ClearArbMemoryResponse.FromString,
                )
        self.QueryFreqListCapabilities = channel.unary_unary(
                '/nifgen_grpc.NiFgen/QueryFreqListCapabilities',
                request_serializer=nifgen__pb2.QueryFreqListCapabilitiesRequest.SerializeToString,
                response_deserializer=nifgen__pb2.QueryFreqListCapabilitiesResponse.FromString,
                )
        self.CreateFreqList = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateFreqList',
                request_serializer=nifgen__pb2.CreateFreqListRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CreateFreqListResponse.FromString,
                )
        self.ConfigureFreqList = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureFreqList',
                request_serializer=nifgen__pb2.ConfigureFreqListRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureFreqListResponse.FromString,
                )
        self.ClearFreqList = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ClearFreqList',
                request_serializer=nifgen__pb2.ClearFreqListRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ClearFreqListResponse.FromString,
                )
        self.WriteScript = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteScript',
                request_serializer=nifgen__pb2.WriteScriptRequest.SerializeToString,
                response_deserializer=nifgen__pb2.WriteScriptResponse.FromString,
                )
        self.DeleteScript = channel.unary_unary(
                '/nifgen_grpc.NiFgen/DeleteScript',
                request_serializer=nifgen__pb2.DeleteScriptRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DeleteScriptResponse.FromString,
                )
        self.ExportSignal = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ExportSignal',
                request_serializer=nifgen__pb2.ExportSignalRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ExportSignalResponse.FromString,
                )
        self.RouteSignalOut = channel.unary_unary(
                '/nifgen_grpc.NiFgen/RouteSignalOut',
                request_serializer=nifgen__pb2.RouteSignalOutRequest.SerializeToString,
                response_deserializer=nifgen__pb2.RouteSignalOutResponse.FromString,
                )
        self.SendSoftwareEdgeTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SendSoftwareEdgeTrigger',
                request_serializer=nifgen__pb2.SendSoftwareEdgeTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.SendSoftwareEdgeTriggerResponse.FromString,
                )
        self.ConfigureDigitalEdgeStartTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureDigitalEdgeStartTrigger',
                request_serializer=nifgen__pb2.ConfigureDigitalEdgeStartTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureDigitalEdgeStartTriggerResponse.FromString,
                )
        self.ConfigureSoftwareEdgeStartTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureSoftwareEdgeStartTrigger',
                request_serializer=nifgen__pb2.ConfigureSoftwareEdgeStartTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureSoftwareEdgeStartTriggerResponse.FromString,
                )
        self.DisableStartTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/DisableStartTrigger',
                request_serializer=nifgen__pb2.DisableStartTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DisableStartTriggerResponse.FromString,
                )
        self.ConfigureP2PEndpointFullnessStartTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureP2PEndpointFullnessStartTrigger',
                request_serializer=nifgen__pb2.ConfigureP2PEndpointFullnessStartTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureP2PEndpointFullnessStartTriggerResponse.FromString,
                )
        self.ConfigureDigitalEdgeScriptTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureDigitalEdgeScriptTrigger',
                request_serializer=nifgen__pb2.ConfigureDigitalEdgeScriptTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureDigitalEdgeScriptTriggerResponse.FromString,
                )
        self.ConfigureDigitalLevelScriptTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureDigitalLevelScriptTrigger',
                request_serializer=nifgen__pb2.ConfigureDigitalLevelScriptTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureDigitalLevelScriptTriggerResponse.FromString,
                )
        self.ConfigureSoftwareEdgeScriptTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureSoftwareEdgeScriptTrigger',
                request_serializer=nifgen__pb2.ConfigureSoftwareEdgeScriptTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureSoftwareEdgeScriptTriggerResponse.FromString,
                )
        self.DisableScriptTrigger = channel.unary_unary(
                '/nifgen_grpc.NiFgen/DisableScriptTrigger',
                request_serializer=nifgen__pb2.DisableScriptTriggerRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DisableScriptTriggerResponse.FromString,
                )
        self.ConfigureClockMode = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureClockMode',
                request_serializer=nifgen__pb2.ConfigureClockModeRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureClockModeResponse.FromString,
                )
        self.AdjustSampleClockRelativeDelay = channel.unary_unary(
                '/nifgen_grpc.NiFgen/AdjustSampleClockRelativeDelay',
                request_serializer=nifgen__pb2.AdjustSampleClockRelativeDelayRequest.SerializeToString,
                response_deserializer=nifgen__pb2.AdjustSampleClockRelativeDelayResponse.FromString,
                )
        self.AllocateWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/AllocateWaveform',
                request_serializer=nifgen__pb2.AllocateWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.AllocateWaveformResponse.FromString,
                )
        self.SetWaveformNextWritePosition = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SetWaveformNextWritePosition',
                request_serializer=nifgen__pb2.SetWaveformNextWritePositionRequest.SerializeToString,
                response_deserializer=nifgen__pb2.SetWaveformNextWritePositionResponse.FromString,
                )
        self.WriteWaveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteWaveform',
                request_serializer=nifgen__pb2.WriteWaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.WriteWaveformResponse.FromString,
                )
        self.WriteBinary16Waveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteBinary16Waveform',
                request_serializer=nifgen__pb2.WriteBinary16WaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.WriteBinary16WaveformResponse.FromString,
                )
        self.WriteWaveformComplexF64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteWaveformComplexF64',
                request_serializer=nifgen__pb2.WriteWaveformComplexF64Request.SerializeToString,
                response_deserializer=nifgen__pb2.WriteWaveformComplexF64Response.FromString,
                )
        self.WriteComplexBinary16Waveform = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteComplexBinary16Waveform',
                request_serializer=nifgen__pb2.WriteComplexBinary16WaveformRequest.SerializeToString,
                response_deserializer=nifgen__pb2.WriteComplexBinary16WaveformResponse.FromString,
                )
        self.SelfCal = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SelfCal',
                request_serializer=nifgen__pb2.SelfCalRequest.SerializeToString,
                response_deserializer=nifgen__pb2.SelfCalResponse.FromString,
                )
        self.GetSelfCalSupported = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetSelfCalSupported',
                request_serializer=nifgen__pb2.GetSelfCalSupportedRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetSelfCalSupportedResponse.FromString,
                )
        self.GetSelfCalLastDateAndTime = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetSelfCalLastDateAndTime',
                request_serializer=nifgen__pb2.GetSelfCalLastDateAndTimeRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetSelfCalLastDateAndTimeResponse.FromString,
                )
        self.GetExtCalLastDateAndTime = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetExtCalLastDateAndTime',
                request_serializer=nifgen__pb2.GetExtCalLastDateAndTimeRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetExtCalLastDateAndTimeResponse.FromString,
                )
        self.GetSelfCalLastTemp = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetSelfCalLastTemp',
                request_serializer=nifgen__pb2.GetSelfCalLastTempRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetSelfCalLastTempResponse.FromString,
                )
        self.GetExtCalLastTemp = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetExtCalLastTemp',
                request_serializer=nifgen__pb2.GetExtCalLastTempRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetExtCalLastTempResponse.FromString,
                )
        self.GetExtCalRecommendedInterval = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetExtCalRecommendedInterval',
                request_serializer=nifgen__pb2.GetExtCalRecommendedIntervalRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetExtCalRecommendedIntervalResponse.FromString,
                )
        self.ReadCurrentTemperature = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ReadCurrentTemperature',
                request_serializer=nifgen__pb2.ReadCurrentTemperatureRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ReadCurrentTemperatureResponse.FromString,
                )
        self.ConfigureCustomFIRFilterCoefficients = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureCustomFIRFilterCoefficients',
                request_serializer=nifgen__pb2.ConfigureCustomFIRFilterCoefficientsRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureCustomFIRFilterCoefficientsResponse.FromString,
                )
        self.GetFIRFilterCoefficients = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetFIRFilterCoefficients',
                request_serializer=nifgen__pb2.GetFIRFilterCoefficientsRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetFIRFilterCoefficientsResponse.FromString,
                )
        self.GetStreamEndpointHandle = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetStreamEndpointHandle',
                request_serializer=nifgen__pb2.GetStreamEndpointHandleRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetStreamEndpointHandleResponse.FromString,
                )
        self.WriteP2PEndpointI16 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/WriteP2PEndpointI16',
                request_serializer=nifgen__pb2.WriteP2PEndpointI16Request.SerializeToString,
                response_deserializer=nifgen__pb2.WriteP2PEndpointI16Response.FromString,
                )
        self.ConfigureSynchronization = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureSynchronization',
                request_serializer=nifgen__pb2.ConfigureSynchronizationRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureSynchronizationResponse.FromString,
                )
        self.EnableDigitalPatterning = channel.unary_unary(
                '/nifgen_grpc.NiFgen/EnableDigitalPatterning',
                request_serializer=nifgen__pb2.EnableDigitalPatterningRequest.SerializeToString,
                response_deserializer=nifgen__pb2.EnableDigitalPatterningResponse.FromString,
                )
        self.DisableDigitalPatterning = channel.unary_unary(
                '/nifgen_grpc.NiFgen/DisableDigitalPatterning',
                request_serializer=nifgen__pb2.DisableDigitalPatterningRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DisableDigitalPatterningResponse.FromString,
                )
        self.EnableDigitalFilter = channel.unary_unary(
                '/nifgen_grpc.NiFgen/EnableDigitalFilter',
                request_serializer=nifgen__pb2.EnableDigitalFilterRequest.SerializeToString,
                response_deserializer=nifgen__pb2.EnableDigitalFilterResponse.FromString,
                )
        self.DisableDigitalFilter = channel.unary_unary(
                '/nifgen_grpc.NiFgen/DisableDigitalFilter',
                request_serializer=nifgen__pb2.DisableDigitalFilterRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DisableDigitalFilterResponse.FromString,
                )
        self.EnableAnalogFilter = channel.unary_unary(
                '/nifgen_grpc.NiFgen/EnableAnalogFilter',
                request_serializer=nifgen__pb2.EnableAnalogFilterRequest.SerializeToString,
                response_deserializer=nifgen__pb2.EnableAnalogFilterResponse.FromString,
                )
        self.DisableAnalogFilter = channel.unary_unary(
                '/nifgen_grpc.NiFgen/DisableAnalogFilter',
                request_serializer=nifgen__pb2.DisableAnalogFilterRequest.SerializeToString,
                response_deserializer=nifgen__pb2.DisableAnalogFilterResponse.FromString,
                )
        self.ConfigureSampleClockSource = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureSampleClockSource',
                request_serializer=nifgen__pb2.ConfigureSampleClockSourceRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureSampleClockSourceResponse.FromString,
                )
        self.ConfigureTriggerMode = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ConfigureTriggerMode',
                request_serializer=nifgen__pb2.ConfigureTriggerModeRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ConfigureTriggerModeResponse.FromString,
                )
        self.ImportAttributeConfigurationFile = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ImportAttributeConfigurationFile',
                request_serializer=nifgen__pb2.ImportAttributeConfigurationFileRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ImportAttributeConfigurationFileResponse.FromString,
                )
        self.ExportAttributeConfigurationFile = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ExportAttributeConfigurationFile',
                request_serializer=nifgen__pb2.ExportAttributeConfigurationFileRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ExportAttributeConfigurationFileResponse.FromString,
                )
        self.ImportAttributeConfigurationBuffer = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ImportAttributeConfigurationBuffer',
                request_serializer=nifgen__pb2.ImportAttributeConfigurationBufferRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ImportAttributeConfigurationBufferResponse.FromString,
                )
        self.ExportAttributeConfigurationBuffer = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ExportAttributeConfigurationBuffer',
                request_serializer=nifgen__pb2.ExportAttributeConfigurationBufferRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ExportAttributeConfigurationBufferResponse.FromString,
                )
        self.SetAttributeViInt64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SetAttributeViInt64',
                request_serializer=nifgen__pb2.SetAttributeViInt64Request.SerializeToString,
                response_deserializer=nifgen__pb2.SetAttributeViInt64Response.FromString,
                )
        self.CheckAttributeViInt64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CheckAttributeViInt64',
                request_serializer=nifgen__pb2.CheckAttributeViInt64Request.SerializeToString,
                response_deserializer=nifgen__pb2.CheckAttributeViInt64Response.FromString,
                )
        self.GetAttributeViInt64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetAttributeViInt64',
                request_serializer=nifgen__pb2.GetAttributeViInt64Request.SerializeToString,
                response_deserializer=nifgen__pb2.GetAttributeViInt64Response.FromString,
                )
        self.SetAttributeViInt32 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SetAttributeViInt32',
                request_serializer=nifgen__pb2.SetAttributeViInt32Request.SerializeToString,
                response_deserializer=nifgen__pb2.SetAttributeViInt32Response.FromString,
                )
        self.SetAttributeViReal64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SetAttributeViReal64',
                request_serializer=nifgen__pb2.SetAttributeViReal64Request.SerializeToString,
                response_deserializer=nifgen__pb2.SetAttributeViReal64Response.FromString,
                )
        self.SetAttributeViString = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SetAttributeViString',
                request_serializer=nifgen__pb2.SetAttributeViStringRequest.SerializeToString,
                response_deserializer=nifgen__pb2.SetAttributeViStringResponse.FromString,
                )
        self.SetAttributeViBoolean = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SetAttributeViBoolean',
                request_serializer=nifgen__pb2.SetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nifgen__pb2.SetAttributeViBooleanResponse.FromString,
                )
        self.SetAttributeViSession = channel.unary_unary(
                '/nifgen_grpc.NiFgen/SetAttributeViSession',
                request_serializer=nifgen__pb2.SetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nifgen__pb2.SetAttributeViSessionResponse.FromString,
                )
        self.CheckAttributeViInt32 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CheckAttributeViInt32',
                request_serializer=nifgen__pb2.CheckAttributeViInt32Request.SerializeToString,
                response_deserializer=nifgen__pb2.CheckAttributeViInt32Response.FromString,
                )
        self.CheckAttributeViReal64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CheckAttributeViReal64',
                request_serializer=nifgen__pb2.CheckAttributeViReal64Request.SerializeToString,
                response_deserializer=nifgen__pb2.CheckAttributeViReal64Response.FromString,
                )
        self.CheckAttributeViString = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CheckAttributeViString',
                request_serializer=nifgen__pb2.CheckAttributeViStringRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CheckAttributeViStringResponse.FromString,
                )
        self.CheckAttributeViBoolean = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CheckAttributeViBoolean',
                request_serializer=nifgen__pb2.CheckAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CheckAttributeViBooleanResponse.FromString,
                )
        self.CheckAttributeViSession = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CheckAttributeViSession',
                request_serializer=nifgen__pb2.CheckAttributeViSessionRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CheckAttributeViSessionResponse.FromString,
                )
        self.GetAttributeViInt32 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetAttributeViInt32',
                request_serializer=nifgen__pb2.GetAttributeViInt32Request.SerializeToString,
                response_deserializer=nifgen__pb2.GetAttributeViInt32Response.FromString,
                )
        self.GetAttributeViReal64 = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetAttributeViReal64',
                request_serializer=nifgen__pb2.GetAttributeViReal64Request.SerializeToString,
                response_deserializer=nifgen__pb2.GetAttributeViReal64Response.FromString,
                )
        self.GetAttributeViString = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetAttributeViString',
                request_serializer=nifgen__pb2.GetAttributeViStringRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetAttributeViStringResponse.FromString,
                )
        self.GetAttributeViBoolean = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetAttributeViBoolean',
                request_serializer=nifgen__pb2.GetAttributeViBooleanRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetAttributeViBooleanResponse.FromString,
                )
        self.GetAttributeViSession = channel.unary_unary(
                '/nifgen_grpc.NiFgen/GetAttributeViSession',
                request_serializer=nifgen__pb2.GetAttributeViSessionRequest.SerializeToString,
                response_deserializer=nifgen__pb2.GetAttributeViSessionResponse.FromString,
                )
        self.ResetAttribute = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ResetAttribute',
                request_serializer=nifgen__pb2.ResetAttributeRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ResetAttributeResponse.FromString,
                )
        self.ManualEnableP2PStream = channel.unary_unary(
                '/nifgen_grpc.NiFgen/ManualEnableP2PStream',
                request_serializer=nifgen__pb2.ManualEnableP2PStreamRequest.SerializeToString,
                response_deserializer=nifgen__pb2.ManualEnableP2PStreamResponse.FromString,
                )
        self.CreateWaveformFromFileHWS = channel.unary_unary(
                '/nifgen_grpc.NiFgen/CreateWaveformFromFileHWS',
                request_serializer=nifgen__pb2.CreateWaveformFromFileHWSRequest.SerializeToString,
                response_deserializer=nifgen__pb2.CreateWaveformFromFileHWSResponse.FromString,
                )


class NiFgenServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitWithOptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitializeWithChannels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfTest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ErrorQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ErrorMessage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RevisionQuery(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearError(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ErrorHandler(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetChannelName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetInterchangeCheck(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearInterchangeWarnings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InvalidateAllAttributes(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetWithDefaults(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disable(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Commit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHardwareState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WaitUntilDone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsDone(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetDevice(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureOperationMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureOutputMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureReferenceClock(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureOutputImpedance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureOutputEnabled(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureChannels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InitiateGeneration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AbortGeneration(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureStandardWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DefineUserStandardWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearUserStandardWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureFrequency(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureAmplitude(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryArbWfmCapabilities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWaveformF64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWaveformI16(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWaveformComplexF64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWaveformFromFileI16(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWaveformFromFileF64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSampleRate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureArbWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearArbWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllocateNamedWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetNamedWaveformNextWritePosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteNamedWaveformF64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteNamedWaveformI16(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteNamedWaveformComplexF64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteNamedWaveformComplexI16(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNamedWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryArbSeqCapabilities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateArbSequence(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAdvancedArbSequence(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureArbSequence(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearArbSequence(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearArbMemory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryFreqListCapabilities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFreqList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureFreqList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearFreqList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteScript(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteScript(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportSignal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RouteSignalOut(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSoftwareEdgeTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalEdgeStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSoftwareEdgeStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureP2PEndpointFullnessStartTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalEdgeScriptTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureDigitalLevelScriptTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSoftwareEdgeScriptTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableScriptTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureClockMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AdjustSampleClockRelativeDelay(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllocateWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetWaveformNextWritePosition(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteWaveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteBinary16Waveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteWaveformComplexF64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteComplexBinary16Waveform(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SelfCal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSelfCalSupported(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSelfCalLastDateAndTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExtCalLastDateAndTime(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSelfCalLastTemp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExtCalLastTemp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetExtCalRecommendedInterval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadCurrentTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureCustomFIRFilterCoefficients(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFIRFilterCoefficients(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetStreamEndpointHandle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteP2PEndpointI16(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSynchronization(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableDigitalPatterning(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableDigitalPatterning(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableDigitalFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableDigitalFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableAnalogFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableAnalogFilter(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureSampleClockSource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConfigureTriggerMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportAttributeConfigurationFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportAttributeConfigurationFile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportAttributeConfigurationBuffer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportAttributeConfigurationBuffer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViInt64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViInt64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViInt64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViInt32(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViReal64(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViString(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViBoolean(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttributeViSession(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetAttribute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ManualEnableP2PStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateWaveformFromFileHWS(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NiFgenServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=nifgen__pb2.InitRequest.FromString,
                    response_serializer=nifgen__pb2.InitResponse.SerializeToString,
            ),
            'InitWithOptions': grpc.unary_unary_rpc_method_handler(
                    servicer.InitWithOptions,
                    request_deserializer=nifgen__pb2.InitWithOptionsRequest.FromString,
                    response_serializer=nifgen__pb2.InitWithOptionsResponse.SerializeToString,
            ),
            'InitializeWithChannels': grpc.unary_unary_rpc_method_handler(
                    servicer.InitializeWithChannels,
                    request_deserializer=nifgen__pb2.InitializeWithChannelsRequest.FromString,
                    response_serializer=nifgen__pb2.InitializeWithChannelsResponse.SerializeToString,
            ),
            'Close': grpc.unary_unary_rpc_method_handler(
                    servicer.Close,
                    request_deserializer=nifgen__pb2.CloseRequest.FromString,
                    response_serializer=nifgen__pb2.CloseResponse.SerializeToString,
            ),
            'Reset': grpc.unary_unary_rpc_method_handler(
                    servicer.Reset,
                    request_deserializer=nifgen__pb2.ResetRequest.FromString,
                    response_serializer=nifgen__pb2.ResetResponse.SerializeToString,
            ),
            'SelfTest': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfTest,
                    request_deserializer=nifgen__pb2.SelfTestRequest.FromString,
                    response_serializer=nifgen__pb2.SelfTestResponse.SerializeToString,
            ),
            'ErrorQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.ErrorQuery,
                    request_deserializer=nifgen__pb2.ErrorQueryRequest.FromString,
                    response_serializer=nifgen__pb2.ErrorQueryResponse.SerializeToString,
            ),
            'ErrorMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.ErrorMessage,
                    request_deserializer=nifgen__pb2.ErrorMessageRequest.FromString,
                    response_serializer=nifgen__pb2.ErrorMessageResponse.SerializeToString,
            ),
            'RevisionQuery': grpc.unary_unary_rpc_method_handler(
                    servicer.RevisionQuery,
                    request_deserializer=nifgen__pb2.RevisionQueryRequest.FromString,
                    response_serializer=nifgen__pb2.RevisionQueryResponse.SerializeToString,
            ),
            'GetError': grpc.unary_unary_rpc_method_handler(
                    servicer.GetError,
                    request_deserializer=nifgen__pb2.GetErrorRequest.FromString,
                    response_serializer=nifgen__pb2.GetErrorResponse.SerializeToString,
            ),
            'ClearError': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearError,
                    request_deserializer=nifgen__pb2.ClearErrorRequest.FromString,
                    response_serializer=nifgen__pb2.ClearErrorResponse.SerializeToString,
            ),
            'ErrorHandler': grpc.unary_unary_rpc_method_handler(
                    servicer.ErrorHandler,
                    request_deserializer=nifgen__pb2.ErrorHandlerRequest.FromString,
                    response_serializer=nifgen__pb2.ErrorHandlerResponse.SerializeToString,
            ),
            'GetChannelName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetChannelName,
                    request_deserializer=nifgen__pb2.GetChannelNameRequest.FromString,
                    response_serializer=nifgen__pb2.GetChannelNameResponse.SerializeToString,
            ),
            'ResetInterchangeCheck': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetInterchangeCheck,
                    request_deserializer=nifgen__pb2.ResetInterchangeCheckRequest.FromString,
                    response_serializer=nifgen__pb2.ResetInterchangeCheckResponse.SerializeToString,
            ),
            'ClearInterchangeWarnings': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearInterchangeWarnings,
                    request_deserializer=nifgen__pb2.ClearInterchangeWarningsRequest.FromString,
                    response_serializer=nifgen__pb2.ClearInterchangeWarningsResponse.SerializeToString,
            ),
            'InvalidateAllAttributes': grpc.unary_unary_rpc_method_handler(
                    servicer.InvalidateAllAttributes,
                    request_deserializer=nifgen__pb2.InvalidateAllAttributesRequest.FromString,
                    response_serializer=nifgen__pb2.InvalidateAllAttributesResponse.SerializeToString,
            ),
            'ResetWithDefaults': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetWithDefaults,
                    request_deserializer=nifgen__pb2.ResetWithDefaultsRequest.FromString,
                    response_serializer=nifgen__pb2.ResetWithDefaultsResponse.SerializeToString,
            ),
            'Disable': grpc.unary_unary_rpc_method_handler(
                    servicer.Disable,
                    request_deserializer=nifgen__pb2.DisableRequest.FromString,
                    response_serializer=nifgen__pb2.DisableResponse.SerializeToString,
            ),
            'Commit': grpc.unary_unary_rpc_method_handler(
                    servicer.Commit,
                    request_deserializer=nifgen__pb2.CommitRequest.FromString,
                    response_serializer=nifgen__pb2.CommitResponse.SerializeToString,
            ),
            'GetHardwareState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHardwareState,
                    request_deserializer=nifgen__pb2.GetHardwareStateRequest.FromString,
                    response_serializer=nifgen__pb2.GetHardwareStateResponse.SerializeToString,
            ),
            'WaitUntilDone': grpc.unary_unary_rpc_method_handler(
                    servicer.WaitUntilDone,
                    request_deserializer=nifgen__pb2.WaitUntilDoneRequest.FromString,
                    response_serializer=nifgen__pb2.WaitUntilDoneResponse.SerializeToString,
            ),
            'IsDone': grpc.unary_unary_rpc_method_handler(
                    servicer.IsDone,
                    request_deserializer=nifgen__pb2.IsDoneRequest.FromString,
                    response_serializer=nifgen__pb2.IsDoneResponse.SerializeToString,
            ),
            'ResetDevice': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetDevice,
                    request_deserializer=nifgen__pb2.ResetDeviceRequest.FromString,
                    response_serializer=nifgen__pb2.ResetDeviceResponse.SerializeToString,
            ),
            'ConfigureOperationMode': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureOperationMode,
                    request_deserializer=nifgen__pb2.ConfigureOperationModeRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureOperationModeResponse.SerializeToString,
            ),
            'ConfigureOutputMode': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureOutputMode,
                    request_deserializer=nifgen__pb2.ConfigureOutputModeRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureOutputModeResponse.SerializeToString,
            ),
            'ConfigureReferenceClock': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureReferenceClock,
                    request_deserializer=nifgen__pb2.ConfigureReferenceClockRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureReferenceClockResponse.SerializeToString,
            ),
            'ConfigureOutputImpedance': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureOutputImpedance,
                    request_deserializer=nifgen__pb2.ConfigureOutputImpedanceRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureOutputImpedanceResponse.SerializeToString,
            ),
            'ConfigureOutputEnabled': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureOutputEnabled,
                    request_deserializer=nifgen__pb2.ConfigureOutputEnabledRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureOutputEnabledResponse.SerializeToString,
            ),
            'ConfigureChannels': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureChannels,
                    request_deserializer=nifgen__pb2.ConfigureChannelsRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureChannelsResponse.SerializeToString,
            ),
            'InitiateGeneration': grpc.unary_unary_rpc_method_handler(
                    servicer.InitiateGeneration,
                    request_deserializer=nifgen__pb2.InitiateGenerationRequest.FromString,
                    response_serializer=nifgen__pb2.InitiateGenerationResponse.SerializeToString,
            ),
            'AbortGeneration': grpc.unary_unary_rpc_method_handler(
                    servicer.AbortGeneration,
                    request_deserializer=nifgen__pb2.AbortGenerationRequest.FromString,
                    response_serializer=nifgen__pb2.AbortGenerationResponse.SerializeToString,
            ),
            'ConfigureStandardWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureStandardWaveform,
                    request_deserializer=nifgen__pb2.ConfigureStandardWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureStandardWaveformResponse.SerializeToString,
            ),
            'DefineUserStandardWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.DefineUserStandardWaveform,
                    request_deserializer=nifgen__pb2.DefineUserStandardWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.DefineUserStandardWaveformResponse.SerializeToString,
            ),
            'ClearUserStandardWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearUserStandardWaveform,
                    request_deserializer=nifgen__pb2.ClearUserStandardWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.ClearUserStandardWaveformResponse.SerializeToString,
            ),
            'ConfigureFrequency': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureFrequency,
                    request_deserializer=nifgen__pb2.ConfigureFrequencyRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureFrequencyResponse.SerializeToString,
            ),
            'ConfigureAmplitude': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureAmplitude,
                    request_deserializer=nifgen__pb2.ConfigureAmplitudeRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureAmplitudeResponse.SerializeToString,
            ),
            'QueryArbWfmCapabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryArbWfmCapabilities,
                    request_deserializer=nifgen__pb2.QueryArbWfmCapabilitiesRequest.FromString,
                    response_serializer=nifgen__pb2.QueryArbWfmCapabilitiesResponse.SerializeToString,
            ),
            'CreateWaveformF64': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWaveformF64,
                    request_deserializer=nifgen__pb2.CreateWaveformF64Request.FromString,
                    response_serializer=nifgen__pb2.CreateWaveformF64Response.SerializeToString,
            ),
            'CreateWaveformI16': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWaveformI16,
                    request_deserializer=nifgen__pb2.CreateWaveformI16Request.FromString,
                    response_serializer=nifgen__pb2.CreateWaveformI16Response.SerializeToString,
            ),
            'CreateWaveformComplexF64': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWaveformComplexF64,
                    request_deserializer=nifgen__pb2.CreateWaveformComplexF64Request.FromString,
                    response_serializer=nifgen__pb2.CreateWaveformComplexF64Response.SerializeToString,
            ),
            'CreateWaveformFromFileI16': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWaveformFromFileI16,
                    request_deserializer=nifgen__pb2.CreateWaveformFromFileI16Request.FromString,
                    response_serializer=nifgen__pb2.CreateWaveformFromFileI16Response.SerializeToString,
            ),
            'CreateWaveformFromFileF64': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWaveformFromFileF64,
                    request_deserializer=nifgen__pb2.CreateWaveformFromFileF64Request.FromString,
                    response_serializer=nifgen__pb2.CreateWaveformFromFileF64Response.SerializeToString,
            ),
            'ConfigureSampleRate': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSampleRate,
                    request_deserializer=nifgen__pb2.ConfigureSampleRateRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureSampleRateResponse.SerializeToString,
            ),
            'ConfigureArbWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureArbWaveform,
                    request_deserializer=nifgen__pb2.ConfigureArbWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureArbWaveformResponse.SerializeToString,
            ),
            'ClearArbWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearArbWaveform,
                    request_deserializer=nifgen__pb2.ClearArbWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.ClearArbWaveformResponse.SerializeToString,
            ),
            'AllocateNamedWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.AllocateNamedWaveform,
                    request_deserializer=nifgen__pb2.AllocateNamedWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.AllocateNamedWaveformResponse.SerializeToString,
            ),
            'SetNamedWaveformNextWritePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.SetNamedWaveformNextWritePosition,
                    request_deserializer=nifgen__pb2.SetNamedWaveformNextWritePositionRequest.FromString,
                    response_serializer=nifgen__pb2.SetNamedWaveformNextWritePositionResponse.SerializeToString,
            ),
            'WriteNamedWaveformF64': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteNamedWaveformF64,
                    request_deserializer=nifgen__pb2.WriteNamedWaveformF64Request.FromString,
                    response_serializer=nifgen__pb2.WriteNamedWaveformF64Response.SerializeToString,
            ),
            'WriteNamedWaveformI16': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteNamedWaveformI16,
                    request_deserializer=nifgen__pb2.WriteNamedWaveformI16Request.FromString,
                    response_serializer=nifgen__pb2.WriteNamedWaveformI16Response.SerializeToString,
            ),
            'WriteNamedWaveformComplexF64': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteNamedWaveformComplexF64,
                    request_deserializer=nifgen__pb2.WriteNamedWaveformComplexF64Request.FromString,
                    response_serializer=nifgen__pb2.WriteNamedWaveformComplexF64Response.SerializeToString,
            ),
            'WriteNamedWaveformComplexI16': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteNamedWaveformComplexI16,
                    request_deserializer=nifgen__pb2.WriteNamedWaveformComplexI16Request.FromString,
                    response_serializer=nifgen__pb2.WriteNamedWaveformComplexI16Response.SerializeToString,
            ),
            'DeleteNamedWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNamedWaveform,
                    request_deserializer=nifgen__pb2.DeleteNamedWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.DeleteNamedWaveformResponse.SerializeToString,
            ),
            'QueryArbSeqCapabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryArbSeqCapabilities,
                    request_deserializer=nifgen__pb2.QueryArbSeqCapabilitiesRequest.FromString,
                    response_serializer=nifgen__pb2.QueryArbSeqCapabilitiesResponse.SerializeToString,
            ),
            'CreateArbSequence': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateArbSequence,
                    request_deserializer=nifgen__pb2.CreateArbSequenceRequest.FromString,
                    response_serializer=nifgen__pb2.CreateArbSequenceResponse.SerializeToString,
            ),
            'CreateAdvancedArbSequence': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAdvancedArbSequence,
                    request_deserializer=nifgen__pb2.CreateAdvancedArbSequenceRequest.FromString,
                    response_serializer=nifgen__pb2.CreateAdvancedArbSequenceResponse.SerializeToString,
            ),
            'ConfigureArbSequence': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureArbSequence,
                    request_deserializer=nifgen__pb2.ConfigureArbSequenceRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureArbSequenceResponse.SerializeToString,
            ),
            'ClearArbSequence': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearArbSequence,
                    request_deserializer=nifgen__pb2.ClearArbSequenceRequest.FromString,
                    response_serializer=nifgen__pb2.ClearArbSequenceResponse.SerializeToString,
            ),
            'ClearArbMemory': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearArbMemory,
                    request_deserializer=nifgen__pb2.ClearArbMemoryRequest.FromString,
                    response_serializer=nifgen__pb2.ClearArbMemoryResponse.SerializeToString,
            ),
            'QueryFreqListCapabilities': grpc.unary_unary_rpc_method_handler(
                    servicer.QueryFreqListCapabilities,
                    request_deserializer=nifgen__pb2.QueryFreqListCapabilitiesRequest.FromString,
                    response_serializer=nifgen__pb2.QueryFreqListCapabilitiesResponse.SerializeToString,
            ),
            'CreateFreqList': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateFreqList,
                    request_deserializer=nifgen__pb2.CreateFreqListRequest.FromString,
                    response_serializer=nifgen__pb2.CreateFreqListResponse.SerializeToString,
            ),
            'ConfigureFreqList': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureFreqList,
                    request_deserializer=nifgen__pb2.ConfigureFreqListRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureFreqListResponse.SerializeToString,
            ),
            'ClearFreqList': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearFreqList,
                    request_deserializer=nifgen__pb2.ClearFreqListRequest.FromString,
                    response_serializer=nifgen__pb2.ClearFreqListResponse.SerializeToString,
            ),
            'WriteScript': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteScript,
                    request_deserializer=nifgen__pb2.WriteScriptRequest.FromString,
                    response_serializer=nifgen__pb2.WriteScriptResponse.SerializeToString,
            ),
            'DeleteScript': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteScript,
                    request_deserializer=nifgen__pb2.DeleteScriptRequest.FromString,
                    response_serializer=nifgen__pb2.DeleteScriptResponse.SerializeToString,
            ),
            'ExportSignal': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportSignal,
                    request_deserializer=nifgen__pb2.ExportSignalRequest.FromString,
                    response_serializer=nifgen__pb2.ExportSignalResponse.SerializeToString,
            ),
            'RouteSignalOut': grpc.unary_unary_rpc_method_handler(
                    servicer.RouteSignalOut,
                    request_deserializer=nifgen__pb2.RouteSignalOutRequest.FromString,
                    response_serializer=nifgen__pb2.RouteSignalOutResponse.SerializeToString,
            ),
            'SendSoftwareEdgeTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSoftwareEdgeTrigger,
                    request_deserializer=nifgen__pb2.SendSoftwareEdgeTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.SendSoftwareEdgeTriggerResponse.SerializeToString,
            ),
            'ConfigureDigitalEdgeStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalEdgeStartTrigger,
                    request_deserializer=nifgen__pb2.ConfigureDigitalEdgeStartTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureDigitalEdgeStartTriggerResponse.SerializeToString,
            ),
            'ConfigureSoftwareEdgeStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSoftwareEdgeStartTrigger,
                    request_deserializer=nifgen__pb2.ConfigureSoftwareEdgeStartTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureSoftwareEdgeStartTriggerResponse.SerializeToString,
            ),
            'DisableStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableStartTrigger,
                    request_deserializer=nifgen__pb2.DisableStartTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.DisableStartTriggerResponse.SerializeToString,
            ),
            'ConfigureP2PEndpointFullnessStartTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureP2PEndpointFullnessStartTrigger,
                    request_deserializer=nifgen__pb2.ConfigureP2PEndpointFullnessStartTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureP2PEndpointFullnessStartTriggerResponse.SerializeToString,
            ),
            'ConfigureDigitalEdgeScriptTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalEdgeScriptTrigger,
                    request_deserializer=nifgen__pb2.ConfigureDigitalEdgeScriptTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureDigitalEdgeScriptTriggerResponse.SerializeToString,
            ),
            'ConfigureDigitalLevelScriptTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureDigitalLevelScriptTrigger,
                    request_deserializer=nifgen__pb2.ConfigureDigitalLevelScriptTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureDigitalLevelScriptTriggerResponse.SerializeToString,
            ),
            'ConfigureSoftwareEdgeScriptTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSoftwareEdgeScriptTrigger,
                    request_deserializer=nifgen__pb2.ConfigureSoftwareEdgeScriptTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureSoftwareEdgeScriptTriggerResponse.SerializeToString,
            ),
            'DisableScriptTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableScriptTrigger,
                    request_deserializer=nifgen__pb2.DisableScriptTriggerRequest.FromString,
                    response_serializer=nifgen__pb2.DisableScriptTriggerResponse.SerializeToString,
            ),
            'ConfigureClockMode': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureClockMode,
                    request_deserializer=nifgen__pb2.ConfigureClockModeRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureClockModeResponse.SerializeToString,
            ),
            'AdjustSampleClockRelativeDelay': grpc.unary_unary_rpc_method_handler(
                    servicer.AdjustSampleClockRelativeDelay,
                    request_deserializer=nifgen__pb2.AdjustSampleClockRelativeDelayRequest.FromString,
                    response_serializer=nifgen__pb2.AdjustSampleClockRelativeDelayResponse.SerializeToString,
            ),
            'AllocateWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.AllocateWaveform,
                    request_deserializer=nifgen__pb2.AllocateWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.AllocateWaveformResponse.SerializeToString,
            ),
            'SetWaveformNextWritePosition': grpc.unary_unary_rpc_method_handler(
                    servicer.SetWaveformNextWritePosition,
                    request_deserializer=nifgen__pb2.SetWaveformNextWritePositionRequest.FromString,
                    response_serializer=nifgen__pb2.SetWaveformNextWritePositionResponse.SerializeToString,
            ),
            'WriteWaveform': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteWaveform,
                    request_deserializer=nifgen__pb2.WriteWaveformRequest.FromString,
                    response_serializer=nifgen__pb2.WriteWaveformResponse.SerializeToString,
            ),
            'WriteBinary16Waveform': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteBinary16Waveform,
                    request_deserializer=nifgen__pb2.WriteBinary16WaveformRequest.FromString,
                    response_serializer=nifgen__pb2.WriteBinary16WaveformResponse.SerializeToString,
            ),
            'WriteWaveformComplexF64': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteWaveformComplexF64,
                    request_deserializer=nifgen__pb2.WriteWaveformComplexF64Request.FromString,
                    response_serializer=nifgen__pb2.WriteWaveformComplexF64Response.SerializeToString,
            ),
            'WriteComplexBinary16Waveform': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteComplexBinary16Waveform,
                    request_deserializer=nifgen__pb2.WriteComplexBinary16WaveformRequest.FromString,
                    response_serializer=nifgen__pb2.WriteComplexBinary16WaveformResponse.SerializeToString,
            ),
            'SelfCal': grpc.unary_unary_rpc_method_handler(
                    servicer.SelfCal,
                    request_deserializer=nifgen__pb2.SelfCalRequest.FromString,
                    response_serializer=nifgen__pb2.SelfCalResponse.SerializeToString,
            ),
            'GetSelfCalSupported': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSelfCalSupported,
                    request_deserializer=nifgen__pb2.GetSelfCalSupportedRequest.FromString,
                    response_serializer=nifgen__pb2.GetSelfCalSupportedResponse.SerializeToString,
            ),
            'GetSelfCalLastDateAndTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSelfCalLastDateAndTime,
                    request_deserializer=nifgen__pb2.GetSelfCalLastDateAndTimeRequest.FromString,
                    response_serializer=nifgen__pb2.GetSelfCalLastDateAndTimeResponse.SerializeToString,
            ),
            'GetExtCalLastDateAndTime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExtCalLastDateAndTime,
                    request_deserializer=nifgen__pb2.GetExtCalLastDateAndTimeRequest.FromString,
                    response_serializer=nifgen__pb2.GetExtCalLastDateAndTimeResponse.SerializeToString,
            ),
            'GetSelfCalLastTemp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSelfCalLastTemp,
                    request_deserializer=nifgen__pb2.GetSelfCalLastTempRequest.FromString,
                    response_serializer=nifgen__pb2.GetSelfCalLastTempResponse.SerializeToString,
            ),
            'GetExtCalLastTemp': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExtCalLastTemp,
                    request_deserializer=nifgen__pb2.GetExtCalLastTempRequest.FromString,
                    response_serializer=nifgen__pb2.GetExtCalLastTempResponse.SerializeToString,
            ),
            'GetExtCalRecommendedInterval': grpc.unary_unary_rpc_method_handler(
                    servicer.GetExtCalRecommendedInterval,
                    request_deserializer=nifgen__pb2.GetExtCalRecommendedIntervalRequest.FromString,
                    response_serializer=nifgen__pb2.GetExtCalRecommendedIntervalResponse.SerializeToString,
            ),
            'ReadCurrentTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadCurrentTemperature,
                    request_deserializer=nifgen__pb2.ReadCurrentTemperatureRequest.FromString,
                    response_serializer=nifgen__pb2.ReadCurrentTemperatureResponse.SerializeToString,
            ),
            'ConfigureCustomFIRFilterCoefficients': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureCustomFIRFilterCoefficients,
                    request_deserializer=nifgen__pb2.ConfigureCustomFIRFilterCoefficientsRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureCustomFIRFilterCoefficientsResponse.SerializeToString,
            ),
            'GetFIRFilterCoefficients': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFIRFilterCoefficients,
                    request_deserializer=nifgen__pb2.GetFIRFilterCoefficientsRequest.FromString,
                    response_serializer=nifgen__pb2.GetFIRFilterCoefficientsResponse.SerializeToString,
            ),
            'GetStreamEndpointHandle': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStreamEndpointHandle,
                    request_deserializer=nifgen__pb2.GetStreamEndpointHandleRequest.FromString,
                    response_serializer=nifgen__pb2.GetStreamEndpointHandleResponse.SerializeToString,
            ),
            'WriteP2PEndpointI16': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteP2PEndpointI16,
                    request_deserializer=nifgen__pb2.WriteP2PEndpointI16Request.FromString,
                    response_serializer=nifgen__pb2.WriteP2PEndpointI16Response.SerializeToString,
            ),
            'ConfigureSynchronization': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSynchronization,
                    request_deserializer=nifgen__pb2.ConfigureSynchronizationRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureSynchronizationResponse.SerializeToString,
            ),
            'EnableDigitalPatterning': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableDigitalPatterning,
                    request_deserializer=nifgen__pb2.EnableDigitalPatterningRequest.FromString,
                    response_serializer=nifgen__pb2.EnableDigitalPatterningResponse.SerializeToString,
            ),
            'DisableDigitalPatterning': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableDigitalPatterning,
                    request_deserializer=nifgen__pb2.DisableDigitalPatterningRequest.FromString,
                    response_serializer=nifgen__pb2.DisableDigitalPatterningResponse.SerializeToString,
            ),
            'EnableDigitalFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableDigitalFilter,
                    request_deserializer=nifgen__pb2.EnableDigitalFilterRequest.FromString,
                    response_serializer=nifgen__pb2.EnableDigitalFilterResponse.SerializeToString,
            ),
            'DisableDigitalFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableDigitalFilter,
                    request_deserializer=nifgen__pb2.DisableDigitalFilterRequest.FromString,
                    response_serializer=nifgen__pb2.DisableDigitalFilterResponse.SerializeToString,
            ),
            'EnableAnalogFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.EnableAnalogFilter,
                    request_deserializer=nifgen__pb2.EnableAnalogFilterRequest.FromString,
                    response_serializer=nifgen__pb2.EnableAnalogFilterResponse.SerializeToString,
            ),
            'DisableAnalogFilter': grpc.unary_unary_rpc_method_handler(
                    servicer.DisableAnalogFilter,
                    request_deserializer=nifgen__pb2.DisableAnalogFilterRequest.FromString,
                    response_serializer=nifgen__pb2.DisableAnalogFilterResponse.SerializeToString,
            ),
            'ConfigureSampleClockSource': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureSampleClockSource,
                    request_deserializer=nifgen__pb2.ConfigureSampleClockSourceRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureSampleClockSourceResponse.SerializeToString,
            ),
            'ConfigureTriggerMode': grpc.unary_unary_rpc_method_handler(
                    servicer.ConfigureTriggerMode,
                    request_deserializer=nifgen__pb2.ConfigureTriggerModeRequest.FromString,
                    response_serializer=nifgen__pb2.ConfigureTriggerModeResponse.SerializeToString,
            ),
            'ImportAttributeConfigurationFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ImportAttributeConfigurationFile,
                    request_deserializer=nifgen__pb2.ImportAttributeConfigurationFileRequest.FromString,
                    response_serializer=nifgen__pb2.ImportAttributeConfigurationFileResponse.SerializeToString,
            ),
            'ExportAttributeConfigurationFile': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportAttributeConfigurationFile,
                    request_deserializer=nifgen__pb2.ExportAttributeConfigurationFileRequest.FromString,
                    response_serializer=nifgen__pb2.ExportAttributeConfigurationFileResponse.SerializeToString,
            ),
            'ImportAttributeConfigurationBuffer': grpc.unary_unary_rpc_method_handler(
                    servicer.ImportAttributeConfigurationBuffer,
                    request_deserializer=nifgen__pb2.ImportAttributeConfigurationBufferRequest.FromString,
                    response_serializer=nifgen__pb2.ImportAttributeConfigurationBufferResponse.SerializeToString,
            ),
            'ExportAttributeConfigurationBuffer': grpc.unary_unary_rpc_method_handler(
                    servicer.ExportAttributeConfigurationBuffer,
                    request_deserializer=nifgen__pb2.ExportAttributeConfigurationBufferRequest.FromString,
                    response_serializer=nifgen__pb2.ExportAttributeConfigurationBufferResponse.SerializeToString,
            ),
            'SetAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt64,
                    request_deserializer=nifgen__pb2.SetAttributeViInt64Request.FromString,
                    response_serializer=nifgen__pb2.SetAttributeViInt64Response.SerializeToString,
            ),
            'CheckAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViInt64,
                    request_deserializer=nifgen__pb2.CheckAttributeViInt64Request.FromString,
                    response_serializer=nifgen__pb2.CheckAttributeViInt64Response.SerializeToString,
            ),
            'GetAttributeViInt64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt64,
                    request_deserializer=nifgen__pb2.GetAttributeViInt64Request.FromString,
                    response_serializer=nifgen__pb2.GetAttributeViInt64Response.SerializeToString,
            ),
            'SetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViInt32,
                    request_deserializer=nifgen__pb2.SetAttributeViInt32Request.FromString,
                    response_serializer=nifgen__pb2.SetAttributeViInt32Response.SerializeToString,
            ),
            'SetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViReal64,
                    request_deserializer=nifgen__pb2.SetAttributeViReal64Request.FromString,
                    response_serializer=nifgen__pb2.SetAttributeViReal64Response.SerializeToString,
            ),
            'SetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViString,
                    request_deserializer=nifgen__pb2.SetAttributeViStringRequest.FromString,
                    response_serializer=nifgen__pb2.SetAttributeViStringResponse.SerializeToString,
            ),
            'SetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViBoolean,
                    request_deserializer=nifgen__pb2.SetAttributeViBooleanRequest.FromString,
                    response_serializer=nifgen__pb2.SetAttributeViBooleanResponse.SerializeToString,
            ),
            'SetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAttributeViSession,
                    request_deserializer=nifgen__pb2.SetAttributeViSessionRequest.FromString,
                    response_serializer=nifgen__pb2.SetAttributeViSessionResponse.SerializeToString,
            ),
            'CheckAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViInt32,
                    request_deserializer=nifgen__pb2.CheckAttributeViInt32Request.FromString,
                    response_serializer=nifgen__pb2.CheckAttributeViInt32Response.SerializeToString,
            ),
            'CheckAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViReal64,
                    request_deserializer=nifgen__pb2.CheckAttributeViReal64Request.FromString,
                    response_serializer=nifgen__pb2.CheckAttributeViReal64Response.SerializeToString,
            ),
            'CheckAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViString,
                    request_deserializer=nifgen__pb2.CheckAttributeViStringRequest.FromString,
                    response_serializer=nifgen__pb2.CheckAttributeViStringResponse.SerializeToString,
            ),
            'CheckAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViBoolean,
                    request_deserializer=nifgen__pb2.CheckAttributeViBooleanRequest.FromString,
                    response_serializer=nifgen__pb2.CheckAttributeViBooleanResponse.SerializeToString,
            ),
            'CheckAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckAttributeViSession,
                    request_deserializer=nifgen__pb2.CheckAttributeViSessionRequest.FromString,
                    response_serializer=nifgen__pb2.CheckAttributeViSessionResponse.SerializeToString,
            ),
            'GetAttributeViInt32': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViInt32,
                    request_deserializer=nifgen__pb2.GetAttributeViInt32Request.FromString,
                    response_serializer=nifgen__pb2.GetAttributeViInt32Response.SerializeToString,
            ),
            'GetAttributeViReal64': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViReal64,
                    request_deserializer=nifgen__pb2.GetAttributeViReal64Request.FromString,
                    response_serializer=nifgen__pb2.GetAttributeViReal64Response.SerializeToString,
            ),
            'GetAttributeViString': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViString,
                    request_deserializer=nifgen__pb2.GetAttributeViStringRequest.FromString,
                    response_serializer=nifgen__pb2.GetAttributeViStringResponse.SerializeToString,
            ),
            'GetAttributeViBoolean': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViBoolean,
                    request_deserializer=nifgen__pb2.GetAttributeViBooleanRequest.FromString,
                    response_serializer=nifgen__pb2.GetAttributeViBooleanResponse.SerializeToString,
            ),
            'GetAttributeViSession': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttributeViSession,
                    request_deserializer=nifgen__pb2.GetAttributeViSessionRequest.FromString,
                    response_serializer=nifgen__pb2.GetAttributeViSessionResponse.SerializeToString,
            ),
            'ResetAttribute': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetAttribute,
                    request_deserializer=nifgen__pb2.ResetAttributeRequest.FromString,
                    response_serializer=nifgen__pb2.ResetAttributeResponse.SerializeToString,
            ),
            'ManualEnableP2PStream': grpc.unary_unary_rpc_method_handler(
                    servicer.ManualEnableP2PStream,
                    request_deserializer=nifgen__pb2.ManualEnableP2PStreamRequest.FromString,
                    response_serializer=nifgen__pb2.ManualEnableP2PStreamResponse.SerializeToString,
            ),
            'CreateWaveformFromFileHWS': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateWaveformFromFileHWS,
                    request_deserializer=nifgen__pb2.CreateWaveformFromFileHWSRequest.FromString,
                    response_serializer=nifgen__pb2.CreateWaveformFromFileHWSResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nifgen_grpc.NiFgen', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NiFgen(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/Init',
            nifgen__pb2.InitRequest.SerializeToString,
            nifgen__pb2.InitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitWithOptions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/InitWithOptions',
            nifgen__pb2.InitWithOptionsRequest.SerializeToString,
            nifgen__pb2.InitWithOptionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitializeWithChannels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/InitializeWithChannels',
            nifgen__pb2.InitializeWithChannelsRequest.SerializeToString,
            nifgen__pb2.InitializeWithChannelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Close(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/Close',
            nifgen__pb2.CloseRequest.SerializeToString,
            nifgen__pb2.CloseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reset(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/Reset',
            nifgen__pb2.ResetRequest.SerializeToString,
            nifgen__pb2.ResetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelfTest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SelfTest',
            nifgen__pb2.SelfTestRequest.SerializeToString,
            nifgen__pb2.SelfTestResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ErrorQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ErrorQuery',
            nifgen__pb2.ErrorQueryRequest.SerializeToString,
            nifgen__pb2.ErrorQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ErrorMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ErrorMessage',
            nifgen__pb2.ErrorMessageRequest.SerializeToString,
            nifgen__pb2.ErrorMessageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RevisionQuery(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/RevisionQuery',
            nifgen__pb2.RevisionQueryRequest.SerializeToString,
            nifgen__pb2.RevisionQueryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetError',
            nifgen__pb2.GetErrorRequest.SerializeToString,
            nifgen__pb2.GetErrorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearError(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ClearError',
            nifgen__pb2.ClearErrorRequest.SerializeToString,
            nifgen__pb2.ClearErrorResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ErrorHandler(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ErrorHandler',
            nifgen__pb2.ErrorHandlerRequest.SerializeToString,
            nifgen__pb2.ErrorHandlerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetChannelName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetChannelName',
            nifgen__pb2.GetChannelNameRequest.SerializeToString,
            nifgen__pb2.GetChannelNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetInterchangeCheck(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ResetInterchangeCheck',
            nifgen__pb2.ResetInterchangeCheckRequest.SerializeToString,
            nifgen__pb2.ResetInterchangeCheckResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearInterchangeWarnings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ClearInterchangeWarnings',
            nifgen__pb2.ClearInterchangeWarningsRequest.SerializeToString,
            nifgen__pb2.ClearInterchangeWarningsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InvalidateAllAttributes(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/InvalidateAllAttributes',
            nifgen__pb2.InvalidateAllAttributesRequest.SerializeToString,
            nifgen__pb2.InvalidateAllAttributesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetWithDefaults(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ResetWithDefaults',
            nifgen__pb2.ResetWithDefaultsRequest.SerializeToString,
            nifgen__pb2.ResetWithDefaultsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disable(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/Disable',
            nifgen__pb2.DisableRequest.SerializeToString,
            nifgen__pb2.DisableResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Commit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/Commit',
            nifgen__pb2.CommitRequest.SerializeToString,
            nifgen__pb2.CommitResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetHardwareState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetHardwareState',
            nifgen__pb2.GetHardwareStateRequest.SerializeToString,
            nifgen__pb2.GetHardwareStateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WaitUntilDone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WaitUntilDone',
            nifgen__pb2.WaitUntilDoneRequest.SerializeToString,
            nifgen__pb2.WaitUntilDoneResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IsDone(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/IsDone',
            nifgen__pb2.IsDoneRequest.SerializeToString,
            nifgen__pb2.IsDoneResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetDevice(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ResetDevice',
            nifgen__pb2.ResetDeviceRequest.SerializeToString,
            nifgen__pb2.ResetDeviceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureOperationMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureOperationMode',
            nifgen__pb2.ConfigureOperationModeRequest.SerializeToString,
            nifgen__pb2.ConfigureOperationModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureOutputMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureOutputMode',
            nifgen__pb2.ConfigureOutputModeRequest.SerializeToString,
            nifgen__pb2.ConfigureOutputModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureReferenceClock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureReferenceClock',
            nifgen__pb2.ConfigureReferenceClockRequest.SerializeToString,
            nifgen__pb2.ConfigureReferenceClockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureOutputImpedance(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureOutputImpedance',
            nifgen__pb2.ConfigureOutputImpedanceRequest.SerializeToString,
            nifgen__pb2.ConfigureOutputImpedanceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureOutputEnabled(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureOutputEnabled',
            nifgen__pb2.ConfigureOutputEnabledRequest.SerializeToString,
            nifgen__pb2.ConfigureOutputEnabledResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureChannels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureChannels',
            nifgen__pb2.ConfigureChannelsRequest.SerializeToString,
            nifgen__pb2.ConfigureChannelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InitiateGeneration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/InitiateGeneration',
            nifgen__pb2.InitiateGenerationRequest.SerializeToString,
            nifgen__pb2.InitiateGenerationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AbortGeneration(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/AbortGeneration',
            nifgen__pb2.AbortGenerationRequest.SerializeToString,
            nifgen__pb2.AbortGenerationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureStandardWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureStandardWaveform',
            nifgen__pb2.ConfigureStandardWaveformRequest.SerializeToString,
            nifgen__pb2.ConfigureStandardWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DefineUserStandardWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/DefineUserStandardWaveform',
            nifgen__pb2.DefineUserStandardWaveformRequest.SerializeToString,
            nifgen__pb2.DefineUserStandardWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearUserStandardWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ClearUserStandardWaveform',
            nifgen__pb2.ClearUserStandardWaveformRequest.SerializeToString,
            nifgen__pb2.ClearUserStandardWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureFrequency(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureFrequency',
            nifgen__pb2.ConfigureFrequencyRequest.SerializeToString,
            nifgen__pb2.ConfigureFrequencyResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureAmplitude(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureAmplitude',
            nifgen__pb2.ConfigureAmplitudeRequest.SerializeToString,
            nifgen__pb2.ConfigureAmplitudeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryArbWfmCapabilities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/QueryArbWfmCapabilities',
            nifgen__pb2.QueryArbWfmCapabilitiesRequest.SerializeToString,
            nifgen__pb2.QueryArbWfmCapabilitiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWaveformF64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateWaveformF64',
            nifgen__pb2.CreateWaveformF64Request.SerializeToString,
            nifgen__pb2.CreateWaveformF64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWaveformI16(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateWaveformI16',
            nifgen__pb2.CreateWaveformI16Request.SerializeToString,
            nifgen__pb2.CreateWaveformI16Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWaveformComplexF64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateWaveformComplexF64',
            nifgen__pb2.CreateWaveformComplexF64Request.SerializeToString,
            nifgen__pb2.CreateWaveformComplexF64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWaveformFromFileI16(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateWaveformFromFileI16',
            nifgen__pb2.CreateWaveformFromFileI16Request.SerializeToString,
            nifgen__pb2.CreateWaveformFromFileI16Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWaveformFromFileF64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateWaveformFromFileF64',
            nifgen__pb2.CreateWaveformFromFileF64Request.SerializeToString,
            nifgen__pb2.CreateWaveformFromFileF64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSampleRate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureSampleRate',
            nifgen__pb2.ConfigureSampleRateRequest.SerializeToString,
            nifgen__pb2.ConfigureSampleRateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureArbWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureArbWaveform',
            nifgen__pb2.ConfigureArbWaveformRequest.SerializeToString,
            nifgen__pb2.ConfigureArbWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearArbWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ClearArbWaveform',
            nifgen__pb2.ClearArbWaveformRequest.SerializeToString,
            nifgen__pb2.ClearArbWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllocateNamedWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/AllocateNamedWaveform',
            nifgen__pb2.AllocateNamedWaveformRequest.SerializeToString,
            nifgen__pb2.AllocateNamedWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetNamedWaveformNextWritePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SetNamedWaveformNextWritePosition',
            nifgen__pb2.SetNamedWaveformNextWritePositionRequest.SerializeToString,
            nifgen__pb2.SetNamedWaveformNextWritePositionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteNamedWaveformF64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteNamedWaveformF64',
            nifgen__pb2.WriteNamedWaveformF64Request.SerializeToString,
            nifgen__pb2.WriteNamedWaveformF64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteNamedWaveformI16(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteNamedWaveformI16',
            nifgen__pb2.WriteNamedWaveformI16Request.SerializeToString,
            nifgen__pb2.WriteNamedWaveformI16Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteNamedWaveformComplexF64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteNamedWaveformComplexF64',
            nifgen__pb2.WriteNamedWaveformComplexF64Request.SerializeToString,
            nifgen__pb2.WriteNamedWaveformComplexF64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteNamedWaveformComplexI16(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteNamedWaveformComplexI16',
            nifgen__pb2.WriteNamedWaveformComplexI16Request.SerializeToString,
            nifgen__pb2.WriteNamedWaveformComplexI16Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteNamedWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/DeleteNamedWaveform',
            nifgen__pb2.DeleteNamedWaveformRequest.SerializeToString,
            nifgen__pb2.DeleteNamedWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryArbSeqCapabilities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/QueryArbSeqCapabilities',
            nifgen__pb2.QueryArbSeqCapabilitiesRequest.SerializeToString,
            nifgen__pb2.QueryArbSeqCapabilitiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateArbSequence(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateArbSequence',
            nifgen__pb2.CreateArbSequenceRequest.SerializeToString,
            nifgen__pb2.CreateArbSequenceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAdvancedArbSequence(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateAdvancedArbSequence',
            nifgen__pb2.CreateAdvancedArbSequenceRequest.SerializeToString,
            nifgen__pb2.CreateAdvancedArbSequenceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureArbSequence(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureArbSequence',
            nifgen__pb2.ConfigureArbSequenceRequest.SerializeToString,
            nifgen__pb2.ConfigureArbSequenceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearArbSequence(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ClearArbSequence',
            nifgen__pb2.ClearArbSequenceRequest.SerializeToString,
            nifgen__pb2.ClearArbSequenceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearArbMemory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ClearArbMemory',
            nifgen__pb2.ClearArbMemoryRequest.SerializeToString,
            nifgen__pb2.ClearArbMemoryResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QueryFreqListCapabilities(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/QueryFreqListCapabilities',
            nifgen__pb2.QueryFreqListCapabilitiesRequest.SerializeToString,
            nifgen__pb2.QueryFreqListCapabilitiesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateFreqList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateFreqList',
            nifgen__pb2.CreateFreqListRequest.SerializeToString,
            nifgen__pb2.CreateFreqListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureFreqList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureFreqList',
            nifgen__pb2.ConfigureFreqListRequest.SerializeToString,
            nifgen__pb2.ConfigureFreqListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClearFreqList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ClearFreqList',
            nifgen__pb2.ClearFreqListRequest.SerializeToString,
            nifgen__pb2.ClearFreqListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteScript(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteScript',
            nifgen__pb2.WriteScriptRequest.SerializeToString,
            nifgen__pb2.WriteScriptResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteScript(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/DeleteScript',
            nifgen__pb2.DeleteScriptRequest.SerializeToString,
            nifgen__pb2.DeleteScriptResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportSignal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ExportSignal',
            nifgen__pb2.ExportSignalRequest.SerializeToString,
            nifgen__pb2.ExportSignalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RouteSignalOut(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/RouteSignalOut',
            nifgen__pb2.RouteSignalOutRequest.SerializeToString,
            nifgen__pb2.RouteSignalOutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSoftwareEdgeTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SendSoftwareEdgeTrigger',
            nifgen__pb2.SendSoftwareEdgeTriggerRequest.SerializeToString,
            nifgen__pb2.SendSoftwareEdgeTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalEdgeStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureDigitalEdgeStartTrigger',
            nifgen__pb2.ConfigureDigitalEdgeStartTriggerRequest.SerializeToString,
            nifgen__pb2.ConfigureDigitalEdgeStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSoftwareEdgeStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureSoftwareEdgeStartTrigger',
            nifgen__pb2.ConfigureSoftwareEdgeStartTriggerRequest.SerializeToString,
            nifgen__pb2.ConfigureSoftwareEdgeStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/DisableStartTrigger',
            nifgen__pb2.DisableStartTriggerRequest.SerializeToString,
            nifgen__pb2.DisableStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureP2PEndpointFullnessStartTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureP2PEndpointFullnessStartTrigger',
            nifgen__pb2.ConfigureP2PEndpointFullnessStartTriggerRequest.SerializeToString,
            nifgen__pb2.ConfigureP2PEndpointFullnessStartTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalEdgeScriptTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureDigitalEdgeScriptTrigger',
            nifgen__pb2.ConfigureDigitalEdgeScriptTriggerRequest.SerializeToString,
            nifgen__pb2.ConfigureDigitalEdgeScriptTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureDigitalLevelScriptTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureDigitalLevelScriptTrigger',
            nifgen__pb2.ConfigureDigitalLevelScriptTriggerRequest.SerializeToString,
            nifgen__pb2.ConfigureDigitalLevelScriptTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSoftwareEdgeScriptTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureSoftwareEdgeScriptTrigger',
            nifgen__pb2.ConfigureSoftwareEdgeScriptTriggerRequest.SerializeToString,
            nifgen__pb2.ConfigureSoftwareEdgeScriptTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableScriptTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/DisableScriptTrigger',
            nifgen__pb2.DisableScriptTriggerRequest.SerializeToString,
            nifgen__pb2.DisableScriptTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureClockMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureClockMode',
            nifgen__pb2.ConfigureClockModeRequest.SerializeToString,
            nifgen__pb2.ConfigureClockModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AdjustSampleClockRelativeDelay(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/AdjustSampleClockRelativeDelay',
            nifgen__pb2.AdjustSampleClockRelativeDelayRequest.SerializeToString,
            nifgen__pb2.AdjustSampleClockRelativeDelayResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllocateWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/AllocateWaveform',
            nifgen__pb2.AllocateWaveformRequest.SerializeToString,
            nifgen__pb2.AllocateWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetWaveformNextWritePosition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SetWaveformNextWritePosition',
            nifgen__pb2.SetWaveformNextWritePositionRequest.SerializeToString,
            nifgen__pb2.SetWaveformNextWritePositionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteWaveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteWaveform',
            nifgen__pb2.WriteWaveformRequest.SerializeToString,
            nifgen__pb2.WriteWaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteBinary16Waveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteBinary16Waveform',
            nifgen__pb2.WriteBinary16WaveformRequest.SerializeToString,
            nifgen__pb2.WriteBinary16WaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteWaveformComplexF64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteWaveformComplexF64',
            nifgen__pb2.WriteWaveformComplexF64Request.SerializeToString,
            nifgen__pb2.WriteWaveformComplexF64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteComplexBinary16Waveform(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteComplexBinary16Waveform',
            nifgen__pb2.WriteComplexBinary16WaveformRequest.SerializeToString,
            nifgen__pb2.WriteComplexBinary16WaveformResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SelfCal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SelfCal',
            nifgen__pb2.SelfCalRequest.SerializeToString,
            nifgen__pb2.SelfCalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSelfCalSupported(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetSelfCalSupported',
            nifgen__pb2.GetSelfCalSupportedRequest.SerializeToString,
            nifgen__pb2.GetSelfCalSupportedResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSelfCalLastDateAndTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetSelfCalLastDateAndTime',
            nifgen__pb2.GetSelfCalLastDateAndTimeRequest.SerializeToString,
            nifgen__pb2.GetSelfCalLastDateAndTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExtCalLastDateAndTime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetExtCalLastDateAndTime',
            nifgen__pb2.GetExtCalLastDateAndTimeRequest.SerializeToString,
            nifgen__pb2.GetExtCalLastDateAndTimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSelfCalLastTemp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetSelfCalLastTemp',
            nifgen__pb2.GetSelfCalLastTempRequest.SerializeToString,
            nifgen__pb2.GetSelfCalLastTempResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExtCalLastTemp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetExtCalLastTemp',
            nifgen__pb2.GetExtCalLastTempRequest.SerializeToString,
            nifgen__pb2.GetExtCalLastTempResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetExtCalRecommendedInterval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetExtCalRecommendedInterval',
            nifgen__pb2.GetExtCalRecommendedIntervalRequest.SerializeToString,
            nifgen__pb2.GetExtCalRecommendedIntervalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadCurrentTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ReadCurrentTemperature',
            nifgen__pb2.ReadCurrentTemperatureRequest.SerializeToString,
            nifgen__pb2.ReadCurrentTemperatureResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureCustomFIRFilterCoefficients(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureCustomFIRFilterCoefficients',
            nifgen__pb2.ConfigureCustomFIRFilterCoefficientsRequest.SerializeToString,
            nifgen__pb2.ConfigureCustomFIRFilterCoefficientsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetFIRFilterCoefficients(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetFIRFilterCoefficients',
            nifgen__pb2.GetFIRFilterCoefficientsRequest.SerializeToString,
            nifgen__pb2.GetFIRFilterCoefficientsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetStreamEndpointHandle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetStreamEndpointHandle',
            nifgen__pb2.GetStreamEndpointHandleRequest.SerializeToString,
            nifgen__pb2.GetStreamEndpointHandleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteP2PEndpointI16(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/WriteP2PEndpointI16',
            nifgen__pb2.WriteP2PEndpointI16Request.SerializeToString,
            nifgen__pb2.WriteP2PEndpointI16Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSynchronization(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureSynchronization',
            nifgen__pb2.ConfigureSynchronizationRequest.SerializeToString,
            nifgen__pb2.ConfigureSynchronizationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableDigitalPatterning(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/EnableDigitalPatterning',
            nifgen__pb2.EnableDigitalPatterningRequest.SerializeToString,
            nifgen__pb2.EnableDigitalPatterningResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableDigitalPatterning(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/DisableDigitalPatterning',
            nifgen__pb2.DisableDigitalPatterningRequest.SerializeToString,
            nifgen__pb2.DisableDigitalPatterningResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableDigitalFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/EnableDigitalFilter',
            nifgen__pb2.EnableDigitalFilterRequest.SerializeToString,
            nifgen__pb2.EnableDigitalFilterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableDigitalFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/DisableDigitalFilter',
            nifgen__pb2.DisableDigitalFilterRequest.SerializeToString,
            nifgen__pb2.DisableDigitalFilterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EnableAnalogFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/EnableAnalogFilter',
            nifgen__pb2.EnableAnalogFilterRequest.SerializeToString,
            nifgen__pb2.EnableAnalogFilterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DisableAnalogFilter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/DisableAnalogFilter',
            nifgen__pb2.DisableAnalogFilterRequest.SerializeToString,
            nifgen__pb2.DisableAnalogFilterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureSampleClockSource(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureSampleClockSource',
            nifgen__pb2.ConfigureSampleClockSourceRequest.SerializeToString,
            nifgen__pb2.ConfigureSampleClockSourceResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConfigureTriggerMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ConfigureTriggerMode',
            nifgen__pb2.ConfigureTriggerModeRequest.SerializeToString,
            nifgen__pb2.ConfigureTriggerModeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImportAttributeConfigurationFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ImportAttributeConfigurationFile',
            nifgen__pb2.ImportAttributeConfigurationFileRequest.SerializeToString,
            nifgen__pb2.ImportAttributeConfigurationFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportAttributeConfigurationFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ExportAttributeConfigurationFile',
            nifgen__pb2.ExportAttributeConfigurationFileRequest.SerializeToString,
            nifgen__pb2.ExportAttributeConfigurationFileResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImportAttributeConfigurationBuffer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ImportAttributeConfigurationBuffer',
            nifgen__pb2.ImportAttributeConfigurationBufferRequest.SerializeToString,
            nifgen__pb2.ImportAttributeConfigurationBufferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportAttributeConfigurationBuffer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ExportAttributeConfigurationBuffer',
            nifgen__pb2.ExportAttributeConfigurationBufferRequest.SerializeToString,
            nifgen__pb2.ExportAttributeConfigurationBufferResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViInt64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SetAttributeViInt64',
            nifgen__pb2.SetAttributeViInt64Request.SerializeToString,
            nifgen__pb2.SetAttributeViInt64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViInt64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CheckAttributeViInt64',
            nifgen__pb2.CheckAttributeViInt64Request.SerializeToString,
            nifgen__pb2.CheckAttributeViInt64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViInt64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetAttributeViInt64',
            nifgen__pb2.GetAttributeViInt64Request.SerializeToString,
            nifgen__pb2.GetAttributeViInt64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SetAttributeViInt32',
            nifgen__pb2.SetAttributeViInt32Request.SerializeToString,
            nifgen__pb2.SetAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SetAttributeViReal64',
            nifgen__pb2.SetAttributeViReal64Request.SerializeToString,
            nifgen__pb2.SetAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SetAttributeViString',
            nifgen__pb2.SetAttributeViStringRequest.SerializeToString,
            nifgen__pb2.SetAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SetAttributeViBoolean',
            nifgen__pb2.SetAttributeViBooleanRequest.SerializeToString,
            nifgen__pb2.SetAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/SetAttributeViSession',
            nifgen__pb2.SetAttributeViSessionRequest.SerializeToString,
            nifgen__pb2.SetAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CheckAttributeViInt32',
            nifgen__pb2.CheckAttributeViInt32Request.SerializeToString,
            nifgen__pb2.CheckAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CheckAttributeViReal64',
            nifgen__pb2.CheckAttributeViReal64Request.SerializeToString,
            nifgen__pb2.CheckAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CheckAttributeViString',
            nifgen__pb2.CheckAttributeViStringRequest.SerializeToString,
            nifgen__pb2.CheckAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CheckAttributeViBoolean',
            nifgen__pb2.CheckAttributeViBooleanRequest.SerializeToString,
            nifgen__pb2.CheckAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CheckAttributeViSession',
            nifgen__pb2.CheckAttributeViSessionRequest.SerializeToString,
            nifgen__pb2.CheckAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViInt32(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetAttributeViInt32',
            nifgen__pb2.GetAttributeViInt32Request.SerializeToString,
            nifgen__pb2.GetAttributeViInt32Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViReal64(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetAttributeViReal64',
            nifgen__pb2.GetAttributeViReal64Request.SerializeToString,
            nifgen__pb2.GetAttributeViReal64Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViString(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetAttributeViString',
            nifgen__pb2.GetAttributeViStringRequest.SerializeToString,
            nifgen__pb2.GetAttributeViStringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViBoolean(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetAttributeViBoolean',
            nifgen__pb2.GetAttributeViBooleanRequest.SerializeToString,
            nifgen__pb2.GetAttributeViBooleanResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAttributeViSession(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/GetAttributeViSession',
            nifgen__pb2.GetAttributeViSessionRequest.SerializeToString,
            nifgen__pb2.GetAttributeViSessionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetAttribute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ResetAttribute',
            nifgen__pb2.ResetAttributeRequest.SerializeToString,
            nifgen__pb2.ResetAttributeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ManualEnableP2PStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/ManualEnableP2PStream',
            nifgen__pb2.ManualEnableP2PStreamRequest.SerializeToString,
            nifgen__pb2.ManualEnableP2PStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateWaveformFromFileHWS(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/nifgen_grpc.NiFgen/CreateWaveformFromFileHWS',
            nifgen__pb2.CreateWaveformFromFileHWSRequest.SerializeToString,
            nifgen__pb2.CreateWaveformFromFileHWSResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/session.py sha256=02e6ba11e6bae560b443d2adf1d5334e7723e8d0155149d1eea572a502273762 bytes=215517 -->
## FILE: generated/nifgen/nifgen/session.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/session.py`
- sha256: `02e6ba11e6bae560b443d2adf1d5334e7723e8d0155149d1eea572a502273762`
- bytes: 215517

````python
# -*- coding: utf-8 -*-
# This file was generated
import array  # noqa: F401
# Used by @ivi_synchronized
from functools import wraps

import nifgen._attributes as _attributes
import nifgen._converters as _converters
import nifgen._library_interpreter as _library_interpreter
import nifgen.enums as enums
import nifgen.errors as errors

import hightime
import nitclk

# Used for __repr__
import pprint
pp = pprint.PrettyPrinter(indent=4)


class _Generation(object):
    def __init__(self, session):
        self._session = session
        self._session._initiate_generation()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.abort()


# From https://stackoverflow.com/questions/5929107/decorators-with-parameters
def ivi_synchronized(f):
    @wraps(f)
    def aux(*xs, **kws):
        session = xs[0]  # parameter 0 is 'self' which is the session object
        with session.lock():
            return f(*xs, **kws)
    return aux


class _Lock(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        # _lock_session is called from the lock() function, not here
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._session.unlock()


class _RepeatedCapabilities(object):
    def __init__(self, session, prefix, current_repeated_capability_list):
        self._session = session
        self._prefix = prefix
        # We need at least one element. If we get an empty list, make the one element an empty string
        self._current_repeated_capability_list = current_repeated_capability_list if len(current_repeated_capability_list) > 0 else ['']
        # Now we know there is at lease one entry, so we look if it is an empty string or not
        self._separator = '/' if len(self._current_repeated_capability_list[0]) > 0 else ''

    def __getitem__(self, repeated_capability):
        '''Set/get properties or call methods with a repeated capability (i.e. channels)'''
        rep_caps_list = _converters.convert_repeated_capabilities(repeated_capability, self._prefix)
        complete_rep_cap_list = [current_rep_cap + self._separator + rep_cap for current_rep_cap in self._current_repeated_capability_list for rep_cap in rep_caps_list]

        return _SessionBase(
            repeated_capability_list=complete_rep_cap_list,
            all_channels_in_session=self._session._all_channels_in_session,
            interpreter=self._session._interpreter,
            freeze_it=True
        )


# This is a very simple context manager we can use when we need to set/get attributes
# or call functions from _SessionBase that require no channels. It is tied to the specific
# implementation of _SessionBase and how repeated capabilities are handled.
class _NoChannel(object):
    def __init__(self, session):
        self._session = session

    def __enter__(self):
        self._repeated_capability_cache = self._session._repeated_capability
        self._session._repeated_capability = ''

    def __exit__(self, exc_type, exc_value, traceback):
        self._session._repeated_capability = self._repeated_capability_cache


class _SessionBase(object):
    '''Base class for all NI-FGEN sessions.'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    absolute_delay = _attributes.AttributeViReal64(1150413)
    '''Type: float

    Specifies the sub-Sample Clock delay, in seconds, to apply to the
    waveform. Use this property to reduce the trigger jitter when
    synchronizing multiple devices with NI-TClk. This property can also help
    maintain synchronization repeatability by writing the absolute delay
    value of a previous measurement to the current session.
    To set this property, the waveform generator must be in the Idle
    (Configuration) state.
    **Units**: seconds (s)
    **Valid Values**: Plus or minus half of one Sample Clock period
    **Default Value**: 0.0
    **Supported Waveform Generators**: PXIe-5413/5423/5433

    Note:
    If this property is set, NI-TClk cannot perform any sub-Sample Clock
    adjustment.
    '''
    all_marker_events_latched_status = _attributes.AttributeViInt32(1150349)
    '''Type: int

    Returns a bit field of the latched status of all Marker Events.  Write 0 to this property to clear the latched status of all Marker Events.
    '''
    all_marker_events_live_status = _attributes.AttributeViInt32(1150344)
    '''Type: int

    Returns a bit field of the live status of all Marker Events.
    '''
    analog_data_mask = _attributes.AttributeViInt32(1150234)
    '''Type: int

    Specifies the mask to apply to the analog output. The masked data is replaced with the data in analog_static_value.
    '''
    analog_filter_enabled = _attributes.AttributeViBoolean(1150103)
    '''Type: bool

    Controls whether the signal generator applies to an analog filter to the output signal. This property is valid in arbitrary waveform, arbitrary sequence, and script modes. This property can also be used in standard method and frequency list modes for user-defined waveforms.
    '''
    analog_path = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.AnalogPath, 1150222)
    '''Type: enums.AnalogPath

    Specifies the analog signal path that should be used. The main path allows you to configure gain, offset, analog filter status, output impedance, and output enable. The main path has two amplifier options, high- and low-gain.
    The direct path presents a much smaller gain range, and you cannot adjust offset or the filter status. The direct path also provides a smaller output range but also lower distortion. NI-FGEN normally chooses the amplifier based on the user-specified gain.
    '''
    analog_static_value = _attributes.AttributeViInt32(1150235)
    '''Type: int

    Specifies the static value that replaces data masked by analog_data_mask.
    '''
    arb_gain = _attributes.AttributeViReal64(1250202)
    '''Type: float

    Specifies the factor by which the signal generator scales the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to scale the arbitrary waveform to other ranges.
    For example, when you set this property to 2.0, the output signal ranges from -2.0 V to +2.0 V.
    Use this property when output_mode is set to OutputMode.ARB or OutputMode.SEQ.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].arb_gain`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.arb_gain`
    '''
    arb_marker_position = _attributes.AttributeViInt32(1150327)
    '''Type: int

    Specifies the position for a marker to be asserted in the arbitrary waveform. This property defaults to -1 when no marker position is specified. Use this property when output_mode is set to OutputMode.ARB.
    Use ExportSignal to export the marker signal.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    arb_offset = _attributes.AttributeViReal64(1250203)
    '''Type: float

    Specifies the value that the signal generator adds to the arbitrary waveform data. When you create arbitrary waveforms, you must first normalize the data points to the range -1.0 to +1.0. Use this property to shift the arbitrary waveform range.
    For example, when you set this property to 1.0, the output signal ranges from 2.0 V to 0.0 V.
    Use this property when output_mode is set to OutputMode.ARB or OutputMode.SEQ.
    Units: Volts

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].arb_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.arb_offset`
    '''
    arb_repeat_count = _attributes.AttributeViInt32(1150328)
    '''Type: int

    Specifies number of times to repeat the arbitrary waveform when the triggerMode parameter of ConfigureTriggerMode is set to TriggerMode.SINGLE or TriggerMode.STEPPED. This property is ignored if the triggerMode parameter is set to TriggerMode.CONTINUOUS or TriggerMode.BURST. Use this property when output_mode is set to OutputMode.ARB.
    When used during streaming, this property specifies the number of times to repeat the streaming waveform (the onboard memory allocated for streaming).  For more information about streaming, refer to the Streaming topic.
    '''
    arb_sample_rate = _attributes.AttributeViReal64(1250204)
    '''Type: float

    Specifies the rate at which the signal generator outputs the points in arbitrary waveforms.  Use this property when output_mode is set  to OutputMode.ARB or OutputMode.SEQ.
    Units: Samples/s
    '''
    arb_sequence_handle = _attributes.AttributeViInt32(1250211)
    '''Type: int

    This channel-based property identifies which sequence the signal generator produces. You can create multiple sequences using create_arb_sequence. create_arb_sequence returns a handle that you can use to identify the particular sequence. To configure the signal generator to produce a particular sequence, set this property to the sequence handle.
    Use this property only when output_mode is set to OutputMode.SEQ.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].arb_sequence_handle`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.arb_sequence_handle`
    '''
    arb_waveform_handle = _attributes.AttributeViInt32(1250201)
    '''Type: int

    Selects which arbitrary waveform the signal generator produces. You can create multiple arbitrary waveforms using one of the following niFgen Create Waveform methods:
    create_waveform
    create_waveform
    create_waveform_from_file_i16
    create_waveform_from_file_f64
    These methods return a handle that you can use to identify the particular waveform. To configure the signal generator to produce a particular waveform, set this property to the waveform handle.
    Use this property only when output_mode is set to OutputMode.ARB.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].arb_waveform_handle`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.arb_waveform_handle`
    '''
    aux_power_enabled = _attributes.AttributeViBoolean(1150411)
    '''Type: bool

    Controls the specified auxiliary power pin. Setting this property to TRUE energizes the auxiliary power when the session is committed. When this property is FALSE, the power pin of the connector outputs no power.
    '''
    bus_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.BusType, 1150215)
    '''Type: enums.BusType

    The bus type of the signal generator.
    '''
    channel_delay = _attributes.AttributeViReal64(1150369)
    '''Type: float

    Specifies, in seconds, the delay to apply to the analog output of the channel specified by the channel string. You can use the channel delay to configure the timing relationship between channels on a multichannel device. Values for this property can be zero or positive. A value of zero indicates that the channels are aligned. A positive value delays the analog output by the specified number of seconds.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].channel_delay`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.channel_delay`
    '''
    clock_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ClockMode, 1150110)
    '''Type: enums.ClockMode

    Controls which clock mode is used for the signal generator.
    For signal generators that support it, this property allows switching the sample  clock to High-Resolution mode. When in Divide-Down  mode, the sample rate can only be set to certain frequences, based on  dividing down the update clock. However, in High-Resolution mode, the  sample rate may be set to any value.
    '''
    common_mode_offset = _attributes.AttributeViReal64(1150366)
    '''Type: float

    Specifies, in volts, the value the signal generator adds to or subtracts from the arbitrary waveform data. This property applies only when you set the terminal_configuration property to TerminalConfiguration.DIFFERENTIAL. Common mode offset is applied to the signals generated at each differential output terminal.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].common_mode_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.common_mode_offset`
    '''
    data_marker_events_count = _attributes.AttributeViInt32(1150273)
    '''Type: int

    Returns the number of Data Marker Events supported by the device.
    '''
    data_marker_event_data_bit_number = _attributes.AttributeViInt32(1150337)
    '''Type: int

    Specifies the bit number to assign to the Data Marker Event.

    Tip:
    This property can be set/get on specific data_markers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container data_markers to specify a subset.

    Example: :py:attr:`my_session.data_markers[ ... ].data_marker_event_data_bit_number`

    To set/get on all data_markers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.data_marker_event_data_bit_number`
    '''
    data_marker_event_level_polarity = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.DataMarkerEventLevelPolarity, 1150338)
    '''Type: enums.DataMarkerEventLevelPolarity

    Specifies the output polarity of the Data marker event.

    Tip:
    This property can be set/get on specific data_markers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container data_markers to specify a subset.

    Example: :py:attr:`my_session.data_markers[ ... ].data_marker_event_level_polarity`

    To set/get on all data_markers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.data_marker_event_level_polarity`
    '''
    data_marker_event_output_terminal = _attributes.AttributeViString(1150339)
    '''Type: str

    Specifies the destination terminal for the Data Marker Event.

    Tip:
    This property can be set/get on specific data_markers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container data_markers to specify a subset.

    Example: :py:attr:`my_session.data_markers[ ... ].data_marker_event_output_terminal`

    To set/get on all data_markers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.data_marker_event_output_terminal`
    '''
    data_transfer_block_size = _attributes.AttributeViInt32(1150241)
    '''Type: int

    The number of samples at a time to download to onboard memory. Useful when the total data to be transferred to onboard memory is large.
    '''
    data_transfer_maximum_bandwidth = _attributes.AttributeViReal64(1150373)
    '''Type: float

    Specifies the maximum amount of bus bandwidth (in bytes per second) to use for data transfers. The signal generator limits data transfer speeds on the PCIe bus to the value you specify for this property. Set this property to optimize bus bandwidth usage for multi-device streaming applications by preventing the signal generator from consuming all of the available bandwidth on a PCI express link when waveforms are being written to the onboard memory of the device.
    '''
    data_transfer_maximum_in_flight_reads = _attributes.AttributeViInt32(1150375)
    '''Type: int

    Specifies the maximum number of concurrent PCI Express read requests the signal generator can issue.
    When transferring data from computer memory to device onboard memory across the PCI Express bus, the signal generator can issue multiple memory reads at the same time. In general, the larger the number of read requests, the more efficiently the device uses the bus because the multiple read requests keep the data flowing, even in a PCI Express topology that has high latency due to PCI Express switches in the data path. Most NI devices can issue a large number of read requests (typically 8 or 16). By default, this property is set to the highest value the signal generator supports.
    If other devices in your system cannot tolerate long data latencies, it may be helpful to decrease the number of in-flight read requests the NI signal generator issues. This helps to reduce the amount of data the signal generator reads at one time.
    '''
    data_transfer_preferred_packet_size = _attributes.AttributeViInt32(1150374)
    '''Type: int

    Specifies the preferred size of the data field in a PCI Express read request packet. In general, the larger the packet size, the more efficiently the device uses the bus. By default, NI signal generators use the largest packet size allowed by the system. However, due to different system implementations, some systems may perform better with smaller packet sizes.
    Recommended values for this property are powers of two between 64 and 512.
    In some cases, the signal generator generates packets smaller than  the preferred size you set with this property.
    You cannot change this property while the device is generating a waveform. If you want to change the device configuration, call the abort method or wait for the generation to complete.

    Note:
    :
    '''
    digital_data_mask = _attributes.AttributeViInt32(1150236)
    '''Type: int

    Specifies the mask to apply to the output on the digital connector. The masked data is replaced with the data in digital_static_value.
    '''
    digital_edge_script_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerDigitalEdgeEdge, 1150292)
    '''Type: enums.ScriptTriggerDigitalEdgeEdge

    Specifies the active edge for the Script trigger. This property is used when script_trigger_type is set to Digital Edge.

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_edge`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.digital_edge_script_trigger_edge`
    '''
    digital_edge_script_trigger_source = _attributes.AttributeViString(1150291)
    '''Type: str

    Specifies the source terminal for the Script trigger. This property is used when script_trigger_type is set to Digital Edge.

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].digital_edge_script_trigger_source`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.digital_edge_script_trigger_source`
    '''
    digital_edge_start_trigger_edge = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTriggerDigitalEdgeEdge, 1150282)
    '''Type: enums.StartTriggerDigitalEdgeEdge

    Specifies the active edge for the Start trigger. This property is used only when start_trigger_type is set to Digital Edge.
    '''
    digital_edge_start_trigger_source = _attributes.AttributeViString(1150281)
    '''Type: str

    Specifies the source terminal for the Start trigger. This property is used only when start_trigger_type is set to Digital Edge.
    '''
    digital_filter_enabled = _attributes.AttributeViBoolean(1150102)
    '''Type: bool

    Controls whether the signal generator applies a digital filter to the output signal. This property is valid in arbitrary waveform, arbitrary sequence, and script modes. This property can also be used in standard method and frequency list modes for user-defined waveforms.
    '''
    digital_filter_interpolation_factor = _attributes.AttributeViReal64(1150218)
    '''Type: float

    This property only affects the device when digital_filter_enabled is set to True. If you do not set this property directly, NI-FGEN automatically selects the maximum interpolation factor allowed for the current sample rate. Valid values are 2, 4, and 8.
    '''
    digital_gain = _attributes.AttributeViReal64(1150254)
    '''Type: float

    Specifies a factor by which the signal generator digitally multiplies generated data before converting it to an analog signal in the DAC. For a digital gain greater than 1.0, the product of digital gain times the generated data must be inside the range plus or minus 1.0 (assuming floating point data).  If the product exceeds these limits, the signal generator clips the output signal, and an error results.
    Some signal generators support both digital gain and an analog gain (analog gain is specified with the func_amplitude property or the arb_gain property). Digital gain can be changed during generation without the glitches that may occur when changing analog gains, due to relay switching. However, the DAC output resolution is a method of analog gain, so only analog gain makes full use of the resolution of the DAC.
    '''
    digital_pattern_enabled = _attributes.AttributeViBoolean(1150101)
    '''Type: bool

    Controls whether the signal generator generates a digital pattern of the output signal.
    '''
    digital_static_value = _attributes.AttributeViInt32(1150237)
    '''Type: int

    Specifies the static value that replaces data masked by digital_data_mask.
    '''
    done_event_output_terminal = _attributes.AttributeViString(1150315)
    '''Type: str

    Specifies the destination terminal for the Done Event.
    '''
    done_event_pulse_width = _attributes.AttributeViReal64(1150336)
    '''Type: float

    Specifies the pulse width for the Done Event.
    '''
    done_event_pulse_width_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventPulseWidthUnits, 1150334)
    '''Type: enums.EventPulseWidthUnits

    Specifies the pulse width units for the Done Event.
    '''
    driver_setup = _attributes.AttributeViString(1050007)
    '''Type: str

    Specifies the driver setup portion of the option string that was passed into the InitWithOptions method.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    exported_onboard_reference_clock_output_terminal = _attributes.AttributeViString(1150322)
    '''Type: str

    Specifies the terminal to which to export the Onboard Reference Clock.
    '''
    exported_reference_clock_output_terminal = _attributes.AttributeViString(1150321)
    '''Type: str

    Specifies the terminal to which to export the Reference Clock.
    '''
    exported_sample_clock_divisor = _attributes.AttributeViInt32(1150219)
    '''Type: int

    Specifies the factor by which to divide the Sample clock, also known as the Update clock, before it is exported.  To export the Sample clock, use the ExportSignal method or the  exported_sample_clock_output_terminal property.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    exported_sample_clock_output_terminal = _attributes.AttributeViString(1150320)
    '''Type: str

    Specifies the terminal to which to export the Sample Clock.
    '''
    exported_sample_clock_timebase_divisor = _attributes.AttributeViInt32(1150230)
    '''Type: int

    Specifies the factor by which to divide the sample clock timebase (board clock) before it is exported.  To export the Sample clock timebase, use the ExportSignal method or the  exported_sample_clock_timebase_output_terminal property.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    exported_sample_clock_timebase_output_terminal = _attributes.AttributeViString(1150329)
    '''Type: str

    Specifies the terminal to which to export the Sample clock timebase. If you specify a divisor with the exported_sample_clock_timebase_divisor property,   the Sample clock exported with the exported_sample_clock_timebase_output_terminal  property is the value of the Sample clock timebase after it is divided-down.  For a list of the terminals available on your device, refer to the Device Routes tab in MAX.
    To change the device configuration, call abort or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    exported_script_trigger_output_terminal = _attributes.AttributeViString(1150295)
    '''Type: str

    Specifies the output terminal for the exported Script trigger.
    Setting this property to an empty string means that when you commit the session, the signal is removed from that terminal and, if possible, the terminal is tristated.

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].exported_script_trigger_output_terminal`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.exported_script_trigger_output_terminal`
    '''
    exported_start_trigger_output_terminal = _attributes.AttributeViString(1150283)
    '''Type: str

    Specifies the destination terminal for exporting the Start trigger.
    '''
    external_clock_delay_binary_value = _attributes.AttributeViInt32(1150233)
    '''Type: int

    Binary value of the external clock delay.
    '''
    external_sample_clock_multiplier = _attributes.AttributeViReal64(1150376)
    '''Type: float

    Specifies a multiplication factor to use to obtain a desired sample rate from an external Sample clock.  The resulting sample rate is equal to this factor multiplied by the external Sample clock rate.  You can use this property to generate samples at a rate higher than your external clock rate.  When using this property, you do not need to explicitly set the external clock rate.
    '''
    file_transfer_block_size = _attributes.AttributeViInt32(1150240)
    '''Type: int

    The number of samples at a time to read from the file and download to onboard memory. Used in conjunction with the Create From File and Write From File methods.
    '''
    filter_correction_frequency = _attributes.AttributeViReal64(1150104)
    '''Type: float

    Controls the filter correction frequency of the analog filter. This property corrects for the ripples in the analog filter frequency response at the frequency specified. For standard waveform output, the filter correction frequency should be set to be the same as the frequency of the standard waveform. To have no filter correction, set this property to 0 Hz.
    '''
    flatness_correction_enabled = _attributes.AttributeViBoolean(1150323)
    '''Type: bool

    When True, the signal generator applies a flatness correction factor to the generated sine wave in order to ensure the same output power level at all frequencies.
    This property should be set to False when performing Flatness Calibration.
    '''
    fpga_bitfile_path = _attributes.AttributeViString(1150412)
    '''Type: str

    Gets the absolute file path to the bitfile loaded on the FPGA.
    '''
    freq_list_duration_quantum = _attributes.AttributeViReal64(1150214)
    '''Type: float

    Returns the quantum of which all durations must be a multiple in a  frequency list.
    '''
    freq_list_handle = _attributes.AttributeViInt32(1150208)
    '''Type: int

    Sets which frequency list the signal generator  produces. Create a frequency list using create_freq_list.  create_freq_list returns a handle that you can  use to identify the list.
    '''
    func_amplitude = _attributes.AttributeViReal64(1250102)
    '''Type: float

    Controls the amplitude of the standard waveform that the  signal generator produces. This value is the amplitude at the  output terminal.
    For example, to produce a waveform ranging from -5.00 V to +5.00 V, set  the amplitude to 10.00 V.
    set the Waveform parameter to Waveform.DC.
    Units: Vpk-pk

    Note: This parameter does not affect signal generator behavior when you

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].func_amplitude`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.func_amplitude`
    '''
    func_buffer_size = _attributes.AttributeViInt32(1150238)
    '''Type: int

    This property contains the number of samples used in the standard method waveform  buffer. This property is only valid on devices that implement standard method mode  in software, and is read-only for all other devices.
    implementation of Standard Method Mode on your device.

    Note: Refer to the Standard Method Mode topic for more information on the
    '''
    func_dc_offset = _attributes.AttributeViReal64(1250103)
    '''Type: float

    Controls the DC offset of the standard waveform that the  signal generator produces.  This value is the offset at the output  terminal. The value is the offset from ground to the center of the  waveform that you specify with the Waveform parameter.
    For example, to configure a waveform with an amplitude of 10.00 V to  range from 0.00 V to +10.00 V, set DC Offset to 5.00 V.
    Units: volts

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].func_dc_offset`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.func_dc_offset`
    '''
    func_duty_cycle_high = _attributes.AttributeViReal64(1250106)
    '''Type: float

    Controls the duty cycle of the square wave the signal generator  produces. Specify this property as a percentage of  the time the square wave is high in a cycle.
    set the Waveform parameter to Waveform.SQUARE.
    Units: Percentage of time the waveform is high

    Note: This parameter only affects signal generator behavior when you

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].func_duty_cycle_high`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.func_duty_cycle_high`
    '''
    func_frequency = _attributes.AttributeViReal64(1250104)
    '''Type: float

    Controls the frequency of the standard waveform that the  signal generator produces.
    Units: hertz
    (1) This parameter does not affect signal generator behavior when you  set the Waveform parameter of the configure_standard_waveform method  to Waveform.DC.
    (2) For Waveform.SINE, the range is between 0 MHz and 16 MHz, but the  range is between 0 MHz and 1 MHz for all other waveforms.

    Note:
    :

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].func_frequency`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.func_frequency`
    '''
    func_max_buffer_size = _attributes.AttributeViInt32(1150239)
    '''Type: int

    This property sets the maximum number of samples that can be used in the standard  method waveform buffer. Increasing this value may increase the quality of  the waveform. This property is only valid on devices that implement standard  method mode in software, and is read-only for all other devices.
    implementation of Standard Method Mode on your device.

    Note: Refer to the Standard Method Mode topic for more information on the
    '''
    func_start_phase = _attributes.AttributeViReal64(1250105)
    '''Type: float

    Controls horizontal offset of the standard waveform the  signal generator produces. Specify this property in degrees of  one waveform cycle.
    A start phase of 180 degrees means output generation begins halfway  through the waveform. A start phase of 360 degrees offsets the output by  an entire waveform cycle, which is identical to a start phase of 0  degrees.
    set the Waveform parameter to Waveform.DC.
    Units: Degrees of one cycle

    Note: This parameter does not affect signal generator behavior when you

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].func_start_phase`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.func_start_phase`
    '''
    func_waveform = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.Waveform, 1250101)
    '''Type: enums.Waveform

    This channel-based property specifies which standard waveform the signal generator produces.
    Use this property only when output_mode is set to  OutputMode.FUNC.
    Waveform.SINE      - Sinusoid waveform
    Waveform.SQUARE    - Square waveform
    Waveform.TRIANGLE  - Triangle waveform
    Waveform.RAMP_UP   - Positive ramp waveform
    Waveform.RAMP_DOWN - Negative ramp waveform
    Waveform.DC        - Constant voltage
    Waveform.NOISE     - White noise
    Waveform.USER      - User-defined waveform as defined with
    define_user_standard_waveform

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].func_waveform`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.func_waveform`
    '''
    idle_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.IdleBehavior, 1150377)
    '''Type: enums.IdleBehavior

    Specifies the behavior of the output during the Idle state.  The output can be configured to hold the last generated voltage before entering the Idle state or jump to the Idle Value.
    '''
    idle_value = _attributes.AttributeViInt32(1150378)
    '''Type: int

    Specifies the value to generate in the Idle state.  The Idle Behavior must be configured to jump to this value.
    '''
    instrument_firmware_revision = _attributes.AttributeViString(1050510)
    '''Type: str

    A string that contains the firmware revision information  for the device that you are currently using.
    '''
    instrument_manufacturer = _attributes.AttributeViString(1050511)
    '''Type: str

    A string that contains the name of the device manufacturer you are currently  using.
    '''
    instrument_model = _attributes.AttributeViString(1050512)
    '''Type: str

    A string that contains the model number or name of the device that you  are currently using.
    '''
    io_resource_descriptor = _attributes.AttributeViString(1050304)
    '''Type: str

    Indicates the resource descriptor that NI-FGEN uses to identify the physical device.
    If you initialize NI-FGEN with a logical name, this  property contains the resource descriptor that corresponds  to the entry in the IVI Configuration Utility.
    If you initialize NI-FGEN with the resource  descriptor, this property contains that value.
    '''
    load_impedance = _attributes.AttributeViReal64(1150220)
    '''Type: float

    This channel-based property specifies the load impedance connected to the analog output of the channel. If you set this property to NIFGEN_VAL_MATCHED_LOAD_IMPEDANCE (-1.0), NI-FGEN assumes that the load impedance matches the output impedance. NI-FGEN compensates to give the desired peak-to-peak voltage amplitude or arbitrary gain (relative to 1 V).

    Note:
    One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.
    '''
    logical_name = _attributes.AttributeViString(1050305)
    '''Type: str

    A string containing the logical name that you specified when opening the  current IVI session.
    You may pass a logical name to init or  InitWithOptions.  The IVI Configuration Utility must contain an entry for the logical name.   The logical name entry refers to a virtual instrument section in the  IVI Configuration file. The virtual instrument section specifies a physical  device and initial user options.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    marker_events_count = _attributes.AttributeViInt32(1150271)
    '''Type: int

    Returns the number of markers supported by the device. Use this property when output_mode is set to OutputMode.SCRIPT.
    '''
    marker_event_output_terminal = _attributes.AttributeViString(1150312)
    '''Type: str

    Specifies the destination terminal for the Marker Event.

    Tip:
    This property can be set/get on specific markers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_output_terminal`

    To set/get on all markers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.marker_event_output_terminal`
    '''
    marker_event_pulse_width = _attributes.AttributeViReal64(1150340)
    '''Type: float

    Specifies the pulse width for the Marker Event.

    Tip:
    This property can be set/get on specific markers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width`

    To set/get on all markers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.marker_event_pulse_width`
    '''
    marker_event_pulse_width_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventPulseWidthUnits, 1150341)
    '''Type: enums.EventPulseWidthUnits

    Specifies the pulse width units for the Marker Event.

    Tip:
    This property can be set/get on specific markers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container markers to specify a subset.

    Example: :py:attr:`my_session.markers[ ... ].marker_event_pulse_width_units`

    To set/get on all markers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.marker_event_pulse_width_units`
    '''
    max_freq_list_duration = _attributes.AttributeViReal64(1150213)
    '''Type: float

    Returns the maximum duration of any one step in the frequency  list.
    '''
    max_freq_list_length = _attributes.AttributeViInt32(1150211)
    '''Type: int

    Returns the maximum number of steps that can be in a frequency  list.
    '''
    max_loop_count = _attributes.AttributeViInt32(1250215)
    '''Type: int

    Returns the maximum number of times that the signal generator can repeat a waveform in a sequence. Typically, this value is constant for the signal generator.
    '''
    max_num_freq_lists = _attributes.AttributeViInt32(1150209)
    '''Type: int

    Returns the maximum number of frequency lists the signal generator allows.
    '''
    max_num_sequences = _attributes.AttributeViInt32(1250212)
    '''Type: int

    Returns the maximum number of arbitrary sequences that the signal generator allows. Typically, this value is constant for the signal generator.
    '''
    max_num_waveforms = _attributes.AttributeViInt32(1250205)
    '''Type: int

    Returns the maximum number of arbitrary waveforms that the signal generator allows. Typically, this value is constant for the signal generator.
    '''
    max_sequence_length = _attributes.AttributeViInt32(1250214)
    '''Type: int

    Returns the maximum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.
    '''
    max_waveform_size = _attributes.AttributeViInt32(1250208)
    '''Type: int

    Returns the size, in samples, of the largest waveform that can be created. This property reflects the space currently available, taking into account previously allocated waveforms and instructions.
    '''
    memory_size = _attributes.AttributeViInt32(1150242)
    '''Type: int

    The total amount of memory, in bytes, on the signal generator.
    '''
    min_freq_list_duration = _attributes.AttributeViReal64(1150212)
    '''Type: float

    Returns the minimum number of steps that can be in a frequency  list.
    '''
    min_freq_list_length = _attributes.AttributeViInt32(1150210)
    '''Type: int

    Returns the minimum number of frequency lists that the signal generator allows.
    '''
    min_sequence_length = _attributes.AttributeViInt32(1250213)
    '''Type: int

    Returns the minimum number of arbitrary waveforms that the signal generator allows in a sequence. Typically, this value is constant for the signal generator.
    '''
    min_waveform_size = _attributes.AttributeViInt32(1250207)
    '''Type: int

    Returns the minimum number of points that the signal generator allows in an arbitrary waveform. Typically, this value is constant for the signal generator.
    '''
    module_revision = _attributes.AttributeViString(1150390)
    '''Type: str

    A string that contains the module revision  for the device that you are currently using.
    '''
    channel_count = _attributes.AttributeViInt32(1050203)
    '''Type: int

    Indicates the number of channels that the specific instrument  driver supports.
    For each property for which IVI_VAL_MULTI_CHANNEL is set, the IVI Engine maintains a separate cache value for each channel.
    '''
    output_enabled = _attributes.AttributeViBoolean(1250003)
    '''Type: bool

    This channel-based property specifies whether the signal that the signal generator produces appears at the output connector.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_enabled`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.output_enabled`
    '''
    output_impedance = _attributes.AttributeViReal64(1250004)
    '''Type: float

    This channel-based property specifies the signal generator output impedance at the output connector. NI signal sources modules have an output impedance of 50 ohms and an optional 75 ohms on select modules. If the load impedance matches the output impedance, then the voltage at the signal output connector is at the needed level. The voltage at the signal output connector varies with load output impedance, up to doubling the voltage for a high-impedance load.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].output_impedance`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.output_impedance`
    '''
    output_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.OutputMode, 1250001)
    '''Type: enums.OutputMode

    Sets which output mode the signal generator will use. The value you specify determines which methods and properties you use to configure the waveform the signal generator produces.

    Note: The signal generator must not be in the Generating state when you change this property. To change the device configuration, call abort or wait for the generation to complete.
    '''
    ready_for_start_event_output_terminal = _attributes.AttributeViString(1150310)
    '''Type: str

    Specifies the destination terminal for the Ready for Start Event.
    '''
    reference_clock_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.ReferenceClockSource, 1150113)
    '''Type: enums.ReferenceClockSource

    Specifies the reference clock source used by the signal generator.
    The signal generator derives the frequencies and sample rates that it uses  to generate waveforms from the source you specify.  For example, when you set this property to ClkIn, the signal  generator uses the signal it receives at the CLK IN front  panel connector as the Reference clock.
    To change the device configuration, call abort or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    ref_clock_frequency = _attributes.AttributeViReal64(1150107)
    '''Type: float

    Sets the frequency of the signal generator reference  clock. The signal generator uses the reference clock to derive  frequencies and sample rates when generating output.
    '''
    sample_clock_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.SampleClockSource, 1150112)
    '''Type: enums.SampleClockSource

    Specifies the Sample clock source. If you specify a divisor with the exported_sample_clock_divisor  property, the Sample clock exported with the exported_sample_clock_output_terminal property is the  value of the Sample clock after it is divided-down. For a list of the terminals available on your device, refer  to the Device Routes tab in MAX.
    To change the device configuration, call abort or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    sample_clock_timebase_rate = _attributes.AttributeViReal64(1150368)
    '''Type: float

    Specifies the Sample clock timebase rate. This property applies only to external Sample clock timebases.
    To change the device configuration, call abort or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    sample_clock_timebase_source = _attributes.AttributeEnum(_attributes.AttributeViString, enums.SampleClockTimebaseSource, 1150367)
    '''Type: enums.SampleClockTimebaseSource

    Specifies the Sample Clock Timebase source.
    To change the device configuration, call the abort method or wait for the generation to complete.

    Note: The signal generator must not be in the Generating state when you change this property.
    '''
    script_to_generate = _attributes.AttributeViString(1150270)
    '''Type: str

    Specifies which script the generator produces. To configure the generator to run a particular script, set this property to the name of the script. Use write_script to create multiple scripts. Use this property when output_mode is set to OutputMode.SCRIPT.

    Note: The signal generator must not be in the Generating state when you change this property. To change the device configuration, call abort or wait for the generation to complete.
    '''
    script_triggers_count = _attributes.AttributeViInt32(1150272)
    '''Type: int

    Specifies the number of Script triggers supported by the device. Use this property when output_mode is set to OutputMode.SCRIPT.
    '''
    script_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.ScriptTriggerType, 1150290)
    '''Type: enums.ScriptTriggerType

    Specifies the Script trigger type. Depending upon the value of this property, additional properties may need to be configured to fully configure the trigger.

    Tip:
    This property can be set/get on specific script_triggers within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container script_triggers to specify a subset.

    Example: :py:attr:`my_session.script_triggers[ ... ].script_trigger_type`

    To set/get on all script_triggers, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.script_trigger_type`
    '''
    serial_number = _attributes.AttributeViString(1150243)
    '''Type: str

    The signal generator's serial number.
    '''
    simulate = _attributes.AttributeViBoolean(1050005)
    '''Type: bool

    Specifies whether to simulate NI-FGEN I/O  operations. If simulation is enabled, NI-FGEN  methods perform range checking and call Ivi_GetAttribute and  Ivi_SetAttribute, but they do not perform device I/O.   For output parameters that represent device data, NI-FGEN  methods return calculated values.
    Default Value: False
    Use InitWithOptions to override default value.

    Note:
    One or more of the referenced methods are not in the Python API for this driver.
    '''
    specific_driver_description = _attributes.AttributeViString(1050514)
    '''Type: str

    Returns a brief description of NI-FGEN.
    '''
    major_version = _attributes.AttributeViInt32(1050503)
    '''Type: int

    Returns the major version number of NI-FGEN.
    '''
    minor_version = _attributes.AttributeViInt32(1050504)
    '''Type: int

    Returns the minor version number of NI-FGEN.
    '''
    specific_driver_revision = _attributes.AttributeViString(1050551)
    '''Type: str

    A string that contains additional version information about  NI-FGEN.
    '''
    specific_driver_vendor = _attributes.AttributeViString(1050513)
    '''Type: str

    A string that contains the name of the vendor that supplies NI-FGEN.
    '''
    started_event_output_terminal = _attributes.AttributeViString(1150314)
    '''Type: str

    Specifies the destination terminal for the Started Event.
    '''
    started_event_pulse_width = _attributes.AttributeViReal64(1150335)
    '''Type: float

    Specifies the pulse width for the Started Event.
    '''
    started_event_pulse_width_units = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.EventPulseWidthUnits, 1150333)
    '''Type: enums.EventPulseWidthUnits

    Specifies the pulse width units for the Started Event.
    '''
    start_trigger_type = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.StartTriggerType, 1150280)
    '''Type: enums.StartTriggerType

    Specifies whether you want the Start trigger to be a Digital Edge, or Software trigger. You can also choose None as the value for this property.
    '''
    streaming_space_available_in_waveform = _attributes.AttributeViInt32(1150325)
    '''Type: int

    Indicates the space available (in samples) in the streaming waveform for writing new data. During generation, this available space may be in multiple locations with, for example, part of the available space at the end of the streaming waveform and the rest at the beginning. In this situation, writing a block of waveform data the size of the  total space available in the streaming waveform causes NI-FGEN to return an error, as  NI-FGEN will not wrap the data from the end of the waveform to the beginning and cannot write data past the end of the waveform buffer.
    To avoid writing data past the end of the waveform, write new data to the waveform in a fixed size that is an integer divisor of the total size of the streaming waveform.
    Used in conjunction with the streaming_waveform_handle or streaming_waveform_name properties.
    '''
    streaming_waveform_handle = _attributes.AttributeViInt32(1150324)
    '''Type: int

    Specifies the waveform handle of the waveform used to continuously stream data during generation. This property defaults to -1 when no streaming waveform is specified.
    Used in conjunction with streaming_space_available_in_waveform.
    '''
    streaming_waveform_name = _attributes.AttributeViString(1150326)
    '''Type: str

    Specifies the name of the waveform used to continuously stream data during generation. This property defaults to // when no streaming waveform is specified.
    Use in conjunction with streaming_space_available_in_waveform.
    '''
    streaming_write_timeout = _attributes.AttributeViReal64TimeDeltaSeconds(1150409)
    '''Type: hightime.timedelta, datetime.timedelta, or float in seconds

    Specifies the maximum amount of time allowed to complete a streaming write operation.
    '''
    supported_instrument_models = _attributes.AttributeViString(1050327)
    '''Type: str

    Returns a model code of the device. For NI-FGEN versions that support more than one device, this  property contains a comma-separated list of supported device  models.
    '''
    terminal_configuration = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TerminalConfiguration, 1150365)
    '''Type: enums.TerminalConfiguration

    Specifies whether gain and offset values will be analyzed based on single-ended or differential operation.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].terminal_configuration`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.terminal_configuration`
    '''
    trigger_mode = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.TriggerMode, 1150108)
    '''Type: enums.TriggerMode

    Controls the trigger mode.

    Tip:
    This property can be set/get on specific channels within your :py:class:`nifgen.Session` instance.
    Use Python index notation on the repeated capabilities container channels to specify a subset.

    Example: :py:attr:`my_session.channels[ ... ].trigger_mode`

    To set/get on all channels, you can call the property directly on the :py:class:`nifgen.Session`.

    Example: :py:attr:`my_session.trigger_mode`
    '''
    wait_behavior = _attributes.AttributeEnum(_attributes.AttributeViInt32, enums.WaitBehavior, 1150379)
    '''Type: enums.WaitBehavior

    Specifies the behavior of the output while waiting for a script trigger or during a wait instruction.  The output can be configured to hold the last generated voltage before waiting or jump to the Wait Value.
    '''
    wait_value = _attributes.AttributeViInt32(1150380)
    '''Type: int

    Specifies the value to generate while waiting.  The Wait Behavior must be configured to jump to this value.
    '''
    waveform_quantum = _attributes.AttributeViInt32(1250206)
    '''Type: int

    The size of each arbitrary waveform must be a multiple of a quantum value. This property returns the quantum value that the signal generator allows.
    For example, when this property returns a value of 8, all waveform sizes must be a multiple of 8. Typically, this value is constant for the signal generator.
    '''

    def __init__(self, repeated_capability_list, all_channels_in_session, interpreter, freeze_it=False):
        self._repeated_capability_list = repeated_capability_list
        self._repeated_capability = ','.join(repeated_capability_list)
        self._all_channels_in_session = all_channels_in_session
        self._interpreter = interpreter

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("repeated_capability_list=" + pp.pformat(repeated_capability_list))
        param_list.append("interpreter=" + pp.pformat(interpreter))
        self._param_list = ', '.join(param_list)

        # Instantiate any repeated capability objects
        self.channels = _RepeatedCapabilities(self, '', repeated_capability_list)
        self.script_triggers = _RepeatedCapabilities(self, 'ScriptTrigger', repeated_capability_list)
        self.markers = _RepeatedCapabilities(self, 'Marker', repeated_capability_list)
        self.data_markers = _RepeatedCapabilities(self, 'DataMarker', repeated_capability_list)

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = freeze_it

    def __repr__(self):
        return '{0}.{1}({2})'.format('nifgen', self.__class__.__name__, self._param_list)

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("'{0}' object has no attribute '{1}'".format(type(self).__name__, key))
        object.__setattr__(self, key, value)

    ''' These are code-generated '''

    @ivi_synchronized
    def allocate_named_waveform(self, waveform_name, waveform_size):
        r'''allocate_named_waveform

        Specifies the size of a named waveform up front so that it can be
        allocated in onboard memory before loading the associated data. Data can
        then be loaded in smaller blocks with the niFgen Write (Binary16)
        Waveform methods.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].allocate_named_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.allocate_named_waveform`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            waveform_size (int): Specifies the size of the waveform to allocate in samples.

                **Default Value**: "4096"

        '''
        self._interpreter.allocate_named_waveform(self._repeated_capability, waveform_name, waveform_size)

    @ivi_synchronized
    def allocate_waveform(self, waveform_size):
        r'''allocate_waveform

        Specifies the size of a waveform so that it can be allocated in onboard
        memory before loading the associated data. Data can then be loaded in
        smaller blocks with the Write Binary 16 Waveform methods.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].allocate_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.allocate_waveform`

        Args:
            waveform_size (int): Specifies, in samples, the size of the waveform to allocate.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        waveform_handle = self._interpreter.allocate_waveform(self._repeated_capability, waveform_size)
        return waveform_handle

    @ivi_synchronized
    def clear_user_standard_waveform(self):
        r'''clear_user_standard_waveform

        Clears the user-defined waveform created by the
        define_user_standard_waveform method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].clear_user_standard_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.clear_user_standard_waveform`
        '''
        self._interpreter.clear_user_standard_waveform(self._repeated_capability)

    @ivi_synchronized
    def configure_arb_sequence(self, sequence_handle, gain, offset):
        r'''configure_arb_sequence

        Configures the signal generator properties that affect arbitrary
        sequence generation. Sets the arb_sequence_handle,
        arb_gain, and arb_offset properties.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_arb_sequence`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.configure_arb_sequence`

        Args:
            sequence_handle (int): Specifies the handle of the arbitrary sequence that you want the signal
                generator to produce. NI-FGEN sets the
                arb_sequence_handle property to this value. You can
                create an arbitrary sequence using the create_arb_sequence or
                create_advanced_arb_sequence method. These methods return a
                handle that you use to identify the sequence.

                **Default Value**: None

            gain (float): Specifies the factor by which the signal generator scales the arbitrary
                waveforms in the sequence. When you create an arbitrary waveform, you
                must first normalize the data points to a range of –1.00 to +1.00. You
                can use this parameter to scale the waveform to other ranges. The gain
                is applied before the offset is added.

                For example, to configure the output signal to range from –2.00 to
                +2.00 V, set **gain** to 2.00.

                **Units**: unitless

                **Default Value**: None

            offset (float): Specifies the value the signal generator adds to the arbitrary waveform
                data. When you create arbitrary waveforms, you must first normalize the
                data points to a range of –1.00 to +1.00 V. You can use this parameter
                to shift the range of the arbitrary waveform. NI-FGEN sets the
                arb_offset property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

        '''
        self._interpreter.configure_arb_sequence(self._repeated_capability, sequence_handle, gain, offset)

    @ivi_synchronized
    def configure_arb_waveform(self, waveform_handle, gain, offset):
        r'''configure_arb_waveform

        Configures the properties of the signal generator that affect arbitrary
        waveform generation. Sets the arb_waveform_handle,
        arb_gain, and arb_offset properties.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_arb_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.configure_arb_waveform`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform you want the signal
                generator to produce. NI-FGEN sets the
                arb_waveform_handle property to this value. You can
                create an arbitrary waveform using one of the following niFgen Create
                Waveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64

                These methods return a handle that you use to identify the waveform.

                **Default Value**: None

            gain (float): Specifies the factor by which the signal generator scales the arbitrary
                waveforms in the sequence. When you create an arbitrary waveform, you
                must first normalize the data points to a range of –1.00 to +1.00. You
                can use this parameter to scale the waveform to other ranges. The gain
                is applied before the offset is added.

                For example, to configure the output signal to range from –2.00 to
                +2.00 V, set **gain** to 2.00.

                **Units**: unitless

                **Default Value**: None

            offset (float): Specifies the value the signal generator adds to the arbitrary waveform
                data. When you create arbitrary waveforms, you must first normalize the
                data points to a range of –1.00 to +1.00 V. You can use this parameter
                to shift the range of the arbitrary waveform. NI-FGEN sets the
                arb_offset property to this value.

                For example, to configure the output signal to range from 0.00 to 2.00 V
                instead of –1.00 to 1.00 V, set the offset to 1.00.

                **Units**: volts

                **Default Value**: None

        '''
        self._interpreter.configure_arb_waveform(self._repeated_capability, waveform_handle, gain, offset)

    @ivi_synchronized
    def configure_freq_list(self, frequency_list_handle, amplitude, dc_offset=0.0, start_phase=0.0):
        r'''configure_freq_list

        Configures the properties of the signal generator that affect frequency
        list generation (the freq_list_handle,
        func_amplitude, func_dc_offset, and
        func_start_phase properties).

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_freq_list`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.configure_freq_list`

        Args:
            frequency_list_handle (int): Specifies the handle of the frequency list that you want the signal
                generator to produce. NI-FGEN sets the freq_list_handle
                property to this value. You can create a frequency list using the
                create_freq_list method, which returns a handle that you use to
                identify the list.
                **Default Value**: None

            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the func_amplitude property to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the func_dc_offset
                property to this value.

                **Units**: volts

                **Default Value**: None

            start_phase (float): Specifies the horizontal offset of the standard waveform you want the
                signal generator to produce. Specify this property in degrees of one
                waveform cycle. NI-FGEN sets the func_start_phase
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: None degrees

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter to Waveform.DC.

        '''
        self._interpreter.configure_freq_list(self._repeated_capability, frequency_list_handle, amplitude, dc_offset, start_phase)

    @ivi_synchronized
    def configure_standard_waveform(self, waveform, amplitude, frequency, dc_offset=0.0, start_phase=0.0):
        r'''configure_standard_waveform

        Configures the following properties of the signal generator that affect
        standard waveform generation:

        -  func_waveform
        -  func_amplitude
        -  func_dc_offset
        -  func_frequency
        -  func_start_phase

        Note:
        You must call the ConfigureOutputMode method with the
        **outputMode** parameter set to OutputMode.FUNC before calling
        this method.

        Note:
        One or more of the referenced methods are not in the Python API for this driver.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].configure_standard_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.configure_standard_waveform`

        Args:
            waveform (enums.Waveform): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the func_waveform property to this
                value.

                ****Defined Values****

                **Default Value**: Waveform.SINE

                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SQUARE    | Specifies that the signal generator produces a square waveform.                                                                |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.DC        | Specifies that the signal generator produces a constant voltage.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.NOISE     | Specifies that the signal generator produces white noise.                                                                      |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.USER      | Specifies that the signal generator produces a user-defined waveform as defined with the define_user_standard_waveform method. |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+

            amplitude (float): Specifies the amplitude of the standard waveform that you want the
                signal generator to produce. This value is the amplitude at the output
                terminal. NI-FGEN sets the func_amplitude property to
                this value.

                For example, to produce a waveform ranging from –5.00 V to +5.00 V, set
                the amplitude to 10.00 V.

                **Units**: peak-to-peak voltage

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            frequency (float): | Specifies the frequency of the standard waveform that you want the
                  signal generator to produce. NI-FGEN sets the
                  func_frequency property to this value.

                **Units**: hertz

                **Default Value**: None

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter of the configure_standard_waveform
                method to Waveform.DC.

            dc_offset (float): Specifies the DC offset of the standard waveform that you want the
                signal generator to produce. The value is the offset from ground to the
                center of the waveform you specify with the **waveform** parameter,
                observed at the output terminal. For example, to configure a waveform
                with an amplitude of 10.00 V to range from 0.00 V to +10.00 V, set the
                **dcOffset** to 5.00 V. NI-FGEN sets the func_dc_offset
                property to this value.

                **Units**: volts

                **Default Value**: None

            start_phase (float): Specifies the horizontal offset of the standard waveform that you want
                the signal generator to produce. Specify this parameter in degrees of
                one waveform cycle. NI-FGEN sets the func_start_phase
                property to this value. A start phase of 180 degrees means output
                generation begins halfway through the waveform. A start phase of 360
                degrees offsets the output by an entire waveform cycle, which is
                identical to a start phase of 0 degrees.

                **Units**: degrees of one cycle

                **Default Value**: 0.00

                Note:
                This parameter does not affect signal generator behavior when you set
                the **waveform** parameter to Waveform.DC.

        '''
        if type(waveform) is not enums.Waveform:
            raise TypeError('Parameter waveform must be of type ' + str(enums.Waveform))
        self._interpreter.configure_standard_waveform(self._repeated_capability, waveform, amplitude, dc_offset, frequency, start_phase)

    @ivi_synchronized
    def create_waveform(self, waveform_data_array):
        '''create_waveform

        Creates an onboard waveform for use in Arbitrary Waveform output mode or Arbitrary Sequence output mode.

        Note: You must set output_mode to OutputMode.ARB or OutputMode.SEQ before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.create_waveform`

        Args:
            waveform_data_array (iterable of float or int16): Array of data for the new arbitrary waveform. This may be an iterable of float or int16, or for best performance a numpy.ndarray of dtype int16 or float64.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used in other methods when referring to this waveform.

        '''
        # Check the type by using string comparison so that we don't import numpy unnecessarily.
        if str(type(waveform_data_array)).find("'numpy.ndarray'") != -1:
            import numpy
            if waveform_data_array.dtype == numpy.float64:
                return self._create_waveform_f64_numpy(waveform_data_array)
            elif waveform_data_array.dtype == numpy.int16:
                return self._create_waveform_i16_numpy(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(waveform_data_array.dtype, numpy.float64, numpy.int16))
        elif isinstance(waveform_data_array, array.array):
            if waveform_data_array.typecode == 'd':
                return self._create_waveform_f64(waveform_data_array)
            elif waveform_data_array.typecode == 'h':
                return self._create_waveform_i16(waveform_data_array)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(waveform_data_array.typecode, 'd (double)', 'h (16 bit int)'))

        return self._create_waveform_f64(waveform_data_array)

    @ivi_synchronized
    def _create_waveform_f64(self, waveform_data_array):
        r'''_create_waveform_f64

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._create_waveform_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._create_waveform_f64`

        Args:
            waveform_data_array (array.array("d")): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        waveform_handle = self._interpreter.create_waveform_f64(self._repeated_capability, waveform_data_array)
        return waveform_handle

    @ivi_synchronized
    def _create_waveform_f64_numpy(self, waveform_data_array):
        r'''_create_waveform_f64_numpy

        Creates an onboard waveform from binary F64 (floating point double) data
        for use in Arbitrary Waveform output mode or Arbitrary Sequence output
        mode. The **waveformHandle** returned can later be used for setting the
        active waveform, changing the data in the waveform, building sequences
        of waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._create_waveform_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._create_waveform_f64`

        Args:
            waveform_data_array (numpy.array(dtype=numpy.float64)): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('float64'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=float64, is ' + str(waveform_data_array.dtype))
        if waveform_data_array.ndim != 1:
            raise TypeError('waveform_data_array must be numpy.ndarray of dimension=1, is ' + str(waveform_data_array.ndim))
        waveform_handle = self._interpreter.create_waveform_f64_numpy(self._repeated_capability, waveform_data_array)
        return waveform_handle

    @ivi_synchronized
    def create_waveform_from_file_f64(self, file_name, byte_order):
        r'''create_waveform_from_file_f64

        This method takes the floating point double (F64) data from the
        specified file and creates an onboard waveform for use in Arbitrary
        Waveform or Arbitrary Sequence output mode. The **waveformHandle**
        returned by this method can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        The F64 data must be between –1.0 and +1.0 V. Use the
        digital_gain property to generate different voltage
        outputs.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_waveform_from_file_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.create_waveform_from_file_f64`

        Args:
            file_name (str): The full path and name of the file where the waveform data resides.

            byte_order (enums.ByteOrder): Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** ByteOrder.LITTLE

                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.LITTLE | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.BIG    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                Data written by most applications in Windows (including
                LabWindows™/CVI™) is in Little Endian format. Data written to a file
                from LabVIEW is in Big Endian format by default on all platforms. Big
                Endian and Little Endian refer to the way data is stored in memory,
                which can differ on different processors.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        if type(byte_order) is not enums.ByteOrder:
            raise TypeError('Parameter byte_order must be of type ' + str(enums.ByteOrder))
        waveform_handle = self._interpreter.create_waveform_from_file_f64(self._repeated_capability, file_name, byte_order)
        return waveform_handle

    @ivi_synchronized
    def create_waveform_from_file_i16(self, file_name, byte_order):
        r'''create_waveform_from_file_i16

        Takes the binary 16-bit signed integer (I16) data from the specified
        file and creates an onboard waveform for use in Arbitrary Waveform or
        Arbitrary Sequence output mode. The **waveformHandle** returned by this
        method can later be used for setting the active waveform, changing the
        data in the waveform, building sequences of waveforms, or deleting the
        waveform when it is no longer needed.

        Note:
        The I16 data (values between –32768 and +32767) is assumed to
        represent –1 to +1 V. Use the digital_gain property to
        generate different voltage outputs.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].create_waveform_from_file_i16`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.create_waveform_from_file_i16`

        Args:
            file_name (str): The full path and name of the file where the waveform data resides.

            byte_order (enums.ByteOrder): Specifies the byte order of the data in the file.

                ****Defined Values****

                |
                | ****Default Value**:** ByteOrder.LITTLE

                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.LITTLE | Little Endian Data—The least significant bit is stored at the lowest address, followed by the other bits, in order of increasing significance. |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+
                | ByteOrder.BIG    | Big Endian Data—The most significant bit is stored at the lowest address, followed by the other bits, in order of decreasing significance.     |
                +------------------+------------------------------------------------------------------------------------------------------------------------------------------------+

                Note:
                Data written by most applications in Windows (including
                LabWindows™/CVI™) is in Little Endian format. Data written to a file
                from LabVIEW is in Big Endian format by default on all platforms. Big
                Endian and Little Endian refer to the way data is stored in memory,
                which can differ on different processors.


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        if type(byte_order) is not enums.ByteOrder:
            raise TypeError('Parameter byte_order must be of type ' + str(enums.ByteOrder))
        waveform_handle = self._interpreter.create_waveform_from_file_i16(self._repeated_capability, file_name, byte_order)
        return waveform_handle

    @ivi_synchronized
    def _create_waveform_i16_numpy(self, waveform_data_array):
        r'''_create_waveform_i16_numpy

        Creates an onboard waveform from binary 16-bit signed integer (I16) data
        for use in Arbitrary Waveform or Arbitrary Sequence output mode. The
        **waveformHandle** returned can later be used for setting the active
        waveform, changing the data in the waveform, building sequences of
        waveforms, or deleting the waveform when it is no longer needed.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.ARB or
        OutputMode.SEQ before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._create_waveform_i16`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._create_waveform_i16`

        Args:
            waveform_data_array (numpy.array(dtype=numpy.int16)): Specify the array of data that you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in the Waveform Size parameter.
                You must normalize the data points in the array to be between -32768 and
                +32767.
                ****Default Value**:** None


        Returns:
            waveform_handle (int): The handle that identifies the new waveform. This handle is used later
                when referring to this waveform.

        '''
        import numpy

        if type(waveform_data_array) is not numpy.ndarray:
            raise TypeError('waveform_data_array must be {0}, is {1}'.format(numpy.ndarray, type(waveform_data_array)))
        if numpy.isfortran(waveform_data_array) is True:
            raise TypeError('waveform_data_array must be in C-order')
        if waveform_data_array.dtype is not numpy.dtype('int16'):
            raise TypeError('waveform_data_array must be numpy.ndarray of dtype=int16, is ' + str(waveform_data_array.dtype))
        if waveform_data_array.ndim != 1:
            raise TypeError('waveform_data_array must be numpy.ndarray of dimension=1, is ' + str(waveform_data_array.ndim))
        waveform_handle = self._interpreter.create_waveform_i16_numpy(self._repeated_capability, waveform_data_array)
        return waveform_handle

    @ivi_synchronized
    def define_user_standard_waveform(self, waveform_data_array):
        r'''define_user_standard_waveform

        Defines a user waveform for use in either Standard Method or Frequency
        List output mode.

        To select the waveform, set the **waveform** parameter to
        Waveform.USER with either the configure_standard_waveform
        or the create_freq_list method.

        The waveform data must be scaled between –1.0 and 1.0. Use the
        **amplitude** parameter in the configure_standard_waveform
        method to generate different output voltages.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.FUNC or
        OutputMode.FREQ_LIST before calling this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].define_user_standard_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.define_user_standard_waveform`

        Args:
            waveform_data_array (list of float): Specifies the array of data you want to use for the new arbitrary
                waveform. The array must have at least as many elements as the value
                that you specify in **waveformSize**.

                You must normalize the data points in the array to be between –1.00 and
                +1.00.

                **Default Value**: None

        '''
        self._interpreter.define_user_standard_waveform(self._repeated_capability, waveform_data_array)

    @ivi_synchronized
    def _delete_named_waveform(self, waveform_name):
        r'''_delete_named_waveform

        Removes a previously created arbitrary waveform from the signal
        generator memory and invalidates the waveform handle.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._delete_named_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._delete_named_waveform`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

        '''
        self._interpreter.delete_named_waveform(self._repeated_capability, waveform_name)

    @ivi_synchronized
    def delete_script(self, script_name):
        r'''delete_script

        Deletes the specified script from onboard memory.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].delete_script`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.delete_script`

        Args:
            script_name (str): Specifies the name of the script you want to delete. The script name
                appears in the text of the script following the script keyword.

        '''
        self._interpreter.delete_script(self._repeated_capability, script_name)

    @ivi_synchronized
    def delete_waveform(self, waveform_name_or_handle):
        '''delete_waveform

        Removes a previously created arbitrary waveform from the signal generator memory.

        Note: The signal generator must not be in the Generating state when you call this method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].delete_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.delete_waveform`

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

        '''
        if isinstance(waveform_name_or_handle, str):
            return self._delete_named_waveform(waveform_name_or_handle)
        else:
            return self._clear_arb_waveform(waveform_name_or_handle)

    @ivi_synchronized
    def _get_attribute_vi_boolean(self, attribute_id):
        r'''_get_attribute_vi_boolean

        Queries the value of a ViBoolean property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_boolean`

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (bool): Returns the current value of the property. Pass the address of a
                ViBoolean variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_boolean(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_int32(self, attribute_id):
        r'''_get_attribute_vi_int32

        Queries the value of a ViInt32 property. You can use this method to
        get the values of instrument-specific properties and inherent IVI
        properties. If the property represents an instrument state, this
        method performs instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_int32`

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (int): Returns the current value of the property. Pass the address of a
                ViInt32 variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_int32(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_real64(self, attribute_id):
        r'''_get_attribute_vi_real64

        Queries the value of a ViReal64 property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_real64`

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (float): Returns the current value of the property. Pass the address of a
                ViReal64 variable.

        '''
        attribute_value = self._interpreter.get_attribute_vi_real64(self._repeated_capability, attribute_id)
        return attribute_value

    @ivi_synchronized
    def _get_attribute_vi_string(self, attribute_id):
        r'''_get_attribute_vi_string

        Queries the value of a ViString property.

        You can use this method to get the values of instrument-specific
        properties and inherent IVI properties. If the property represents an
        instrument state, this method performs instrument I/O in the following
        cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid.

        You must provide a ViChar array to serve as a buffer for the value. You
        pass the number of bytes in the buffer as the **arraySize** parameter.
        If the current value of the property, including the terminating NUL
        byte, is larger than the size you indicate in the **arraySize**
        parameter, the method copies **arraySize** – 1 bytes into the buffer,
        places an ASCII NUL byte at the end of the buffer, and returns the array
        size you must pass to get the entire value. For example, if the value is
        123456 and **arraySize** is 4, the method places 123 into the buffer
        and returns 7.

        If you want to call this method just to get the required array size,
        you can pass 0 for **arraySize** and VI_NULL for the **attributeValue**
        buffer.

        If you want the method to fill in the buffer regardless of the number
        of bytes in the value, pass a negative number for the **arraySize**
        parameter.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._get_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._get_attribute_vi_string`

        Args:
            attribute_id (int): Specifies the ID of a property.


        Returns:
            attribute_value (str): The buffer in which the method returns the current value of the
                property. The buffer must be a ViChar data type and have at least as
                many bytes as indicated in the **arraySize** parameter.

                If the current value of the property, including the terminating NUL
                byte, contains more bytes than you indicate in this parameter, the
                method copies **arraySize** – 1 bytes into the buffer, places an ASCII
                NUL byte at the end of the buffer, and returns the array size you must
                pass to get the entire value. For example, if the value is 123456 and
                **arraySize** is 4, the method places 123 into the buffer and returns
                7.

                If you specify 0 for the **arraySize** parameter, you can pass VI_NULL
                for this parameter.

        '''
        attribute_value = self._interpreter.get_attribute_vi_string(self._repeated_capability, attribute_id)
        return attribute_value

    def lock(self):
        '''lock

        Obtains a multithread lock on the device session. Before doing so, the
        software waits until all other execution threads release their locks
        on the device session.

        Other threads may have obtained a lock on this session for the
        following reasons:

            -  The application called the lock method.
            -  A call to NI-FGEN locked the session.
            -  After a call to the lock method returns
               successfully, no other threads can access the device session until
               you call the unlock method or exit out of the with block when using
               lock context manager.
            -  Use the lock method and the
               unlock method around a sequence of calls to
               instrument driver methods if you require that the device retain its
               settings through the end of the sequence.

        You can safely make nested calls to the lock method
        within the same thread. To completely unlock the session, you must
        balance each call to the lock method with a call to
        the unlock method.

        Returns:
            lock (context manager): When used in a with statement, nifgen.Session.lock acts as
            a context manager and unlock will be called when the with block is exited
        '''
        self._interpreter.lock()  # We do not call this in the context manager so that this function can
        # act standalone as well and let the client call unlock() explicitly. If they do use the context manager,
        # that will handle the unlock for them
        return _Lock(self)

    @ivi_synchronized
    def send_software_edge_trigger(self, trigger=None, trigger_id=None):
        '''send_software_edge_trigger

        Sends a command to trigger the signal generator. This VI can act as an
        override for an external edge trigger.

        Note:
        This VI does not override external digital edge triggers of the
        NI 5401/5411/5431.

        Args:
            trigger (enums.Trigger): Trigger specifies the type of software trigger to send

                +----------------+
                | Defined Values |
                +================+
                | Trigger.START  |
                +----------------+
                | Trigger.SCRIPT |
                +----------------+

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

            trigger_id (str): Trigger ID specifies the Script Trigger to use for triggering.

        '''
        if trigger is None or trigger_id is None:
            import warnings
            warnings.warn('trigger and trigger_id should now always be passed in to the method', category=DeprecationWarning)

            # We look at whether we are called directly on the session or a repeated capability container to determine how to behave
            if len(self._repeated_capability) > 0:
                trigger_id = self._repeated_capability
                trigger = enums.Trigger.SCRIPT
            else:
                trigger_id = "None"
                trigger = enums.Trigger.START

        elif trigger is not None and trigger_id is not None:
            pass  # This is how the function should be called

        else:
            raise ValueError('Both trigger ({}) and trigger_id ({}) should be passed in to the method'.format(str(trigger), str(trigger_id)))

        if type(trigger) is not enums.Trigger:
            raise TypeError('Parameter trigger must be of type ' + str(enums.Trigger))
        self._interpreter.send_software_edge_trigger(trigger, trigger_id)

    @ivi_synchronized
    def _set_attribute_vi_boolean(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_boolean

        Sets the value of a ViBoolean property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_boolean`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_boolean`

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (bool): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_boolean(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_int32(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_int32

        Sets the value of a ViInt32 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_int32`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_int32`

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (int): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_int32(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_real64(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_real64

        Sets the value of a ViReal64 property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_real64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_real64`

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (float): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_real64(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_attribute_vi_string(self, attribute_id, attribute_value):
        r'''_set_attribute_vi_string

        Sets the value of a ViString property.

        This is a low-level method that you can use to set the values of
        instrument-specific properties and inherent IVI properties. If the
        property represents an instrument state, this method performs
        instrument I/O in the following cases:

        -  State caching is disabled for the entire session or for the
           particular property.
        -  State caching is enabled and the currently cached value is invalid or
           is different than the value you specify.

        NI-FGEN contains high-level methods that set most of the instrument
        properties. NI recommends that you use the high-level driver methods
        as much as possible. They handle order dependencies and multithread
        locking for you. In addition, they perform status checking only after
        setting all of the properties. In contrast, when you set multiple
        properties using the Set Property methods, the methods check the
        instrument status after each call.

        Also, when state caching is enabled, the high-level methods that
        configure multiple properties perform instrument I/O only for the
        properties whose value you change. Thus, you can safely call the
        high-level methods without the penalty of redundant instrument I/O.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_attribute_vi_string`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_attribute_vi_string`

        Args:
            attribute_id (int): Specifies the ID of a property.

            attribute_value (str): Specifies the value to which you want to set the property. **Default
                Value**: None

                Note:
                Some of the values might not be valid depending on the current
                settings of the instrument session.

        '''
        self._interpreter.set_attribute_vi_string(self._repeated_capability, attribute_id, attribute_value)

    @ivi_synchronized
    def _set_named_waveform_next_write_position(self, waveform_name, relative_to, offset):
        r'''_set_named_waveform_next_write_position

        Sets the position in the waveform to which data is written at the next
        write. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the **waveformHandle** parameter. Subsequent
        writes to that waveform begin where the last write left off, unless this
        method is called again. The **waveformHandle** passed in must have
        been created with a call to one of the following methods:

        -  allocate_waveform
        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_named_waveform_next_write_position`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_named_waveform_next_write_position`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from the **relativeTo** parameter at which to start
                loading the data into the waveform.

        '''
        if type(relative_to) is not enums.RelativeTo:
            raise TypeError('Parameter relative_to must be of type ' + str(enums.RelativeTo))
        self._interpreter.set_named_waveform_next_write_position(self._repeated_capability, waveform_name, relative_to, offset)

    @ivi_synchronized
    def set_next_write_position(self, waveform_name_or_handle, relative_to, offset):
        '''set_next_write_position

        Sets the position in the waveform at which the next waveform data is
        written. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the waveformHandle parameter. Subsequent writes to
        that waveform begin where the last write left off, unless this method
        is called again. The waveformHandle passed in must have been created by
        a call to the allocate_waveform method or one of the following
        create_waveform method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].set_next_write_position`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.set_next_write_position`

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from **relativeTo** at which to start loading the
                data into the waveform.

        '''
        if isinstance(waveform_name_or_handle, str):
            return self._set_named_waveform_next_write_position(waveform_name_or_handle, relative_to, offset)
        else:
            return self._set_waveform_next_write_position(waveform_name_or_handle, relative_to, offset)

    @ivi_synchronized
    def _set_waveform_next_write_position(self, waveform_handle, relative_to, offset):
        r'''_set_waveform_next_write_position

        Sets the position in the waveform at which the next waveform data is
        written. This method allows you to write to arbitrary locations within
        the waveform. These settings apply only to the next write to the
        waveform specified by the waveformHandle parameter. Subsequent writes to
        that waveform begin where the last write left off, unless this method
        is called again. The waveformHandle passed in must have been created by
        a call to the allocate_waveform method or one of the following
        niFgen CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._set_waveform_next_write_position`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._set_waveform_next_write_position`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            relative_to (enums.RelativeTo): Specifies the reference position in the waveform. This position and
                **offset** together determine where to start loading data into the
                waveform.

                ****Defined Values****

                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.START (0)   | Use the start of the waveform as the reference position.                |
                +------------------------+-------------------------------------------------------------------------+
                | RelativeTo.CURRENT (1) | Use the current position within the waveform as the reference position. |
                +------------------------+-------------------------------------------------------------------------+

            offset (int): Specifies the offset from **relativeTo** at which to start loading the
                data into the waveform.

        '''
        if type(relative_to) is not enums.RelativeTo:
            raise TypeError('Parameter relative_to must be of type ' + str(enums.RelativeTo))
        self._interpreter.set_waveform_next_write_position(self._repeated_capability, waveform_handle, relative_to, offset)

    def unlock(self):
        '''unlock

        Releases a lock that you acquired on an device session using
        lock. Refer to lock for additional
        information on session locks.
        '''
        self._interpreter.unlock()

    @ivi_synchronized
    def _write_binary16_waveform_numpy(self, waveform_handle, data):
        r'''_write_binary16_waveform_numpy

        Writes binary data to the waveform in onboard memory. The waveform
        handle passed must have been created by a call to the
        allocate_waveform or the create_waveform method.

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_binary16_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_binary16_waveform`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**. The binary data
                is left-justified.

        '''
        import numpy

        if type(data) is not numpy.ndarray:
            raise TypeError('data must be {0}, is {1}'.format(numpy.ndarray, type(data)))
        if numpy.isfortran(data) is True:
            raise TypeError('data must be in C-order')
        if data.dtype is not numpy.dtype('int16'):
            raise TypeError('data must be numpy.ndarray of dtype=int16, is ' + str(data.dtype))
        if data.ndim != 1:
            raise TypeError('data must be numpy.ndarray of dimension=1, is ' + str(data.ndim))
        self._interpreter.write_binary16_waveform_numpy(self._repeated_capability, waveform_handle, data)

    @ivi_synchronized
    def _write_named_waveform_f64(self, waveform_name, data):
        r'''_write_named_waveform_f64

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or to one of the following niFgen
        Create Waveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_named_waveform_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_named_waveform_f64`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (array.array("d")): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        self._interpreter.write_named_waveform_f64(self._repeated_capability, waveform_name, data)

    @ivi_synchronized
    def _write_named_waveform_f64_numpy(self, waveform_name, data):
        r'''_write_named_waveform_f64_numpy

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or to one of the following niFgen
        Create Waveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_named_waveform_f64`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_named_waveform_f64`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (numpy.array(dtype=numpy.float64)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        import numpy

        if type(data) is not numpy.ndarray:
            raise TypeError('data must be {0}, is {1}'.format(numpy.ndarray, type(data)))
        if numpy.isfortran(data) is True:
            raise TypeError('data must be in C-order')
        if data.dtype is not numpy.dtype('float64'):
            raise TypeError('data must be numpy.ndarray of dtype=float64, is ' + str(data.dtype))
        if data.ndim != 1:
            raise TypeError('data must be numpy.ndarray of dimension=1, is ' + str(data.ndim))
        self._interpreter.write_named_waveform_f64_numpy(self._repeated_capability, waveform_name, data)

    @ivi_synchronized
    def _write_named_waveform_i16_numpy(self, waveform_name, data):
        r'''_write_named_waveform_i16_numpy

        Writes binary data to the named waveform in onboard memory.

        By default, the subsequent call to the write_waveform
        method continues writing data from the position of the last sample
        written. You can set the write position and offset by calling the
        set_next_write_position method. If streaming is
        enabled, you can write more data than the allocated waveform size in
        onboard memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_named_waveform_i16`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_named_waveform_i16`

        Args:
            waveform_name (str): Specifies the name to associate with the allocated waveform.

            data (numpy.array(dtype=numpy.int16)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        import numpy

        if type(data) is not numpy.ndarray:
            raise TypeError('data must be {0}, is {1}'.format(numpy.ndarray, type(data)))
        if numpy.isfortran(data) is True:
            raise TypeError('data must be in C-order')
        if data.dtype is not numpy.dtype('int16'):
            raise TypeError('data must be numpy.ndarray of dtype=int16, is ' + str(data.dtype))
        if data.ndim != 1:
            raise TypeError('data must be numpy.ndarray of dimension=1, is ' + str(data.ndim))
        self._interpreter.write_named_waveform_i16_numpy(self._repeated_capability, waveform_name, data)

    @ivi_synchronized
    def write_script(self, script):
        r'''write_script

        Writes a string containing one or more scripts that govern the
        generation of waveforms.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].write_script`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.write_script`

        Args:
            script (str): Contains the text of the script you want to use for your generation
                operation. Refer to `scripting
                Instructions <REPLACE_DRIVER_SPECIFIC_URL_2(niscripted.chm',%20'scripting_instructions)>`__
                for more information about writing scripts.

        '''
        self._interpreter.write_script(self._repeated_capability, script)

    @ivi_synchronized
    def _write_waveform(self, waveform_handle, data):
        r'''_write_waveform

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or one of the following niFgen
        CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        By default, the subsequent call to the write_waveform method
        continues writing data from the position of the last sample written. You
        can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_waveform`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (array.array("d")): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        self._interpreter.write_waveform(self._repeated_capability, waveform_handle, data)

    @ivi_synchronized
    def _write_waveform_numpy(self, waveform_handle, data):
        r'''_write_waveform_numpy

        Writes floating-point data to the waveform in onboard memory. The
        waveform handle passed in must have been created by a call to the
        allocate_waveform method or one of the following niFgen
        CreateWaveform methods:

        -  create_waveform
        -  create_waveform
        -  create_waveform_from_file_i16
        -  create_waveform_from_file_f64

        By default, the subsequent call to the write_waveform method
        continues writing data from the position of the last sample written. You
        can set the write position and offset by calling the
        set_next_write_position method. If streaming is enabled,
        you can write more data than the allocated waveform size in onboard
        memory. Refer to the
        `Streaming <REPLACE_DRIVER_SPECIFIC_URL_2(streaming)>`__ topic for more
        information about streaming data.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ]._write_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session._write_waveform`

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform previously allocated with
                the allocate_waveform method.

            data (numpy.array(dtype=numpy.float64)): Specifies the array of data to load into the waveform. The array must
                have at least as many elements as the value in **size**.

        '''
        import numpy

        if type(data) is not numpy.ndarray:
            raise TypeError('data must be {0}, is {1}'.format(numpy.ndarray, type(data)))
        if numpy.isfortran(data) is True:
            raise TypeError('data must be in C-order')
        if data.dtype is not numpy.dtype('float64'):
            raise TypeError('data must be numpy.ndarray of dtype=float64, is ' + str(data.dtype))
        if data.ndim != 1:
            raise TypeError('data must be numpy.ndarray of dimension=1, is ' + str(data.ndim))
        self._interpreter.write_waveform_numpy(self._repeated_capability, waveform_handle, data)

    @ivi_synchronized
    def write_waveform(self, waveform_name_or_handle, data):
        '''write_waveform

        Writes data to the waveform in onboard memory.

        By default, subsequent calls to this method
        continue writing data from the position of the last sample written. You
        can set the write position and offset by calling the set_next_write_position
        set_next_write_position method.

        Tip:
        This method can be called on specific channels within your :py:class:`nifgen.Session` instance.
        Use Python index notation on the repeated capabilities container channels to specify a subset,
        and then call this method on the result.

        Example: :py:meth:`my_session.channels[ ... ].write_waveform`

        To call the method on all channels, you can call it directly on the :py:class:`nifgen.Session`.

        Example: :py:meth:`my_session.write_waveform`

        Args:
            waveform_name_or_handle (str or int): The name (str) or handle (int) of an arbitrary waveform previously allocated with allocate_named_waveform, allocate_waveform or create_waveform.

            data (list of float): Array of data to load into the waveform. This may be an iterable of float, or for best performance a numpy.ndarray of dtype int16 or float64.

        '''
        use_named = isinstance(waveform_name_or_handle, str)
        # Check the type by using string comparison so that we don't import numpy unnecessarily.
        if str(type(data)).find("'numpy.ndarray'") != -1:
            import numpy
            if data.dtype == numpy.float64:
                return self._write_named_waveform_f64_numpy(waveform_name_or_handle, data) if use_named else self._write_waveform_numpy(waveform_name_or_handle, data)
            elif data.dtype == numpy.int16:
                return self._write_named_waveform_i16_numpy(waveform_name_or_handle, data) if use_named else self._write_binary16_waveform_numpy(waveform_name_or_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(data.dtype, numpy.float64, numpy.int16))
        elif isinstance(data, array.array):
            if data.typecode == 'd':
                return self._write_named_waveform_f64(waveform_name_or_handle, data) if use_named else self._write_waveform(waveform_name_or_handle, data)
            elif data.typecode == 'h':
                return self._write_named_waveform_i16(waveform_name_or_handle, data) if use_named else self._write_binary16_waveform(waveform_name_or_handle, data)
            else:
                raise TypeError("Unsupported dtype. Is {}, expected {} or {}".format(data.typecode, 'd (double)', 'h (16 bit int)'))

        return self._write_named_waveform_f64(waveform_name_or_handle, data) if use_named else self._write_waveform(waveform_name_or_handle, data)

    def _error_message(self, error_code):
        r'''_error_message

        Converts a status code returned by an NI-FGEN method into a
        user-readable string.

        Args:
            error_code (int): Specifies the **status** parameter that is returned from any of the
                NI-FGEN methods.

                **Default Value**: 0 (VI_SUCCESS)


        Returns:
            error_message (str): Returns the error message string read from the instrument error message
                queue.

                You must pass a ViChar array with at least 256 bytes.

        '''
        error_message = self._interpreter.error_message(error_code)
        return error_message


class Session(_SessionBase):
    '''An NI-FGEN session to an NI signal generator.'''

    def __init__(self, resource_name, channel_name=None, reset_device=False, options={}, *, grpc_options=None):
        r'''An NI-FGEN session to an NI signal generator.

        Creates and returns a new NI-FGEN session to the specified channel of a
        waveform generator that is used in all subsequent NI-FGEN method
        calls.

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must ensure that the name you use matches the name in the
                IVI Configuration Store file exactly, without any variations in the case
                of the characters.

                | Specifies the resource name of the device to initialize.

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
                device name*, as shown in Example 3. This naming convention allows for
                the use of an NI-DAQmx device in an application that was originally
                designed for a Traditional NI-DAQ device. For example, if the
                application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
                MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

                If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
                exists with that same name, the NI-DAQmx device is matched first.

                You can also pass in the name of an IVI logical name or an IVI virtual
                name configured with the IVI Configuration utility, as shown in Example
                5. A logical name identifies a particular virtual instrument. A virtual
                name identifies a specific device and specifies the initial settings for
                the session.

                +-----------+--------------------------------------+------------------------+---------------------------------+
                | Example # | Device Type                          | Syntax                 | Variable                        |
                +===========+======================================+========================+=================================+
                | 1         | Traditional NI-DAQ device            | DAQ::\ *1*             | (*1* = device number)           |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 2         | NI-DAQmx device                      | *myDAQmxDevice*        | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 3         | NI-DAQmx device                      | DAQ::\ *myDAQmxDevice* | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 4         | NI-DAQmx device                      | DAQ::\ *2*             | (*2* = device name)             |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 5         | IVI logical name or IVI virtual name | *myLogicalName*        | (*myLogicalName* = name)        |
                +-----------+--------------------------------------+------------------------+---------------------------------+

            channel_name (str, list, range, tuple): Specifies the channel that this VI uses.

                **Default Value**: "0"

            reset_device (bool): Specifies whether you want to reset the device during the initialization
                procedure. True specifies that the device is reset and performs the
                same method as the Reset method.

                ****Defined Values****

                **Default Value**: False

                +-------+---------------------+
                | True  | Reset device        |
                +-------+---------------------+
                | False | Do not reset device |
                +-------+---------------------+

            options (dict): Specifies the initial value of certain properties for the session. The
                syntax for **options** is a dictionary of properties with an assigned
                value. For example:

                { 'simulate': False }

                You do not have to specify a value for all the properties. If you do not
                specify a value for a property, the default value is used.

                Advanced Example:
                { 'simulate': True, 'driver_setup': { 'Model': '<model number>',  'BoardType': '<type>' } }

                +-------------------------+---------+
                | Property                | Default |
                +=========================+=========+
                | range_check             | True    |
                +-------------------------+---------+
                | query_instrument_status | False   |
                +-------------------------+---------+
                | cache                   | True    |
                +-------------------------+---------+
                | simulate                | False   |
                +-------------------------+---------+
                | record_value_coersions  | False   |
                +-------------------------+---------+
                | driver_setup            | {}      |
                +-------------------------+---------+

            grpc_options (nifgen.grpc_session_options.GrpcSessionOptions): MeasurementLink gRPC session options


        Returns:
            session (nifgen.Session): A session object representing the device.

        '''
        if grpc_options:
            import nifgen._grpc_stub_interpreter as _grpc_stub_interpreter
            interpreter = _grpc_stub_interpreter.GrpcStubInterpreter(grpc_options)
        else:
            interpreter = _library_interpreter.LibraryInterpreter(encoding='windows-1251')

        # Initialize the superclass with default values first, populate them later
        super(Session, self).__init__(
            repeated_capability_list=[],
            interpreter=interpreter,
            freeze_it=False,
            all_channels_in_session=None
        )
        channel_name = _converters.convert_repeated_capabilities_without_prefix(channel_name)
        options = _converters.convert_init_with_options_dictionary(options)

        # Call specified init function
        # Note that _interpreter default-initializes the session handle in its constructor, so that
        # if _initialize_with_channels fails, the error handler can reference it.
        # And then here, once _initialize_with_channels succeeds, we call set_session_handle
        # with the actual session handle.
        self._interpreter.set_session_handle(self._initialize_with_channels(resource_name, channel_name, reset_device, options))

        # NI-TClk does not work over NI gRPC Device Server
        if not grpc_options:
            self.tclk = nitclk.SessionReference(self._interpreter.get_session_handle())

        # Store the parameter list for later printing in __repr__
        param_list = []
        param_list.append("resource_name=" + pp.pformat(resource_name))
        param_list.append("channel_name=" + pp.pformat(channel_name))
        param_list.append("reset_device=" + pp.pformat(reset_device))
        param_list.append("options=" + pp.pformat(options))
        self._param_list = ', '.join(param_list)

        # Store the list of channels in the Session which is needed by some nimi-python modules.
        # Use try/except because not all the modules support channels.
        # self.get_channel_names() and self.channel_count can only be called after the session
        # handle is set
        try:
            self._all_channels_in_session = self.get_channel_names(range(self.channel_count))
        except AttributeError:
            self._all_channels_in_session = None

        # Finally, set _is_frozen to True which is used to prevent clients from accidentally adding
        # members when trying to set a property with a typo.
        self._is_frozen = True

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._interpreter._close_on_exit:
            self.close()

    def initiate(self):
        '''initiate

        Initiates signal generation. If you want to abort signal generation,
        call the abort method. After the signal generation
        is aborted, you can call the initiate method to
        cause the signal generator to produce a signal again.

        Note:
        This method will return a Python context manager that will initiate on entering and abort on exit.
        '''
        return _Generation(self)

    def close(self):
        '''close

        Performs the following operations:

        -  Closes the instrument I/O session.
        -  Destroys the NI-FGEN session and all of its properties.
        -  Deallocates any memory resources NI-FGEN uses.

        Not all signal routes established by calling the ExportSignal
        and RouteSignalOut methods are released when the NI-FGEN
        session is closed. The following table shows what happens to a signal
        route on your device when you call the _close method.

        +--------------------+-------------------+------------------+
        | Routes To          | NI 5401/5411/5431 | Other Devices    |
        +====================+===================+==================+
        | Front Panel        | Remain connected  | Remain connected |
        +--------------------+-------------------+------------------+
        | RTSI/PXI Backplane | Remain connected  | Disconnected     |
        +--------------------+-------------------+------------------+

        Note:
        After calling _close, you cannot use NI-FGEN again until you
        call the init or InitWithOptions methods.

        Note:
        This method is not needed when using the session context manager
        '''
        try:
            self._close()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    @ivi_synchronized
    def abort(self):
        r'''abort

        Aborts any previously initiated signal generation. Call the
        initiate method to cause the signal generator to
        produce a signal again.
        '''
        self._interpreter.abort()

    @ivi_synchronized
    def clear_arb_memory(self):
        r'''clear_arb_memory

        Removes all previously created arbitrary waveforms, sequences, and
        scripts from the signal generator memory and invalidates all waveform
        handles, sequence handles, and waveform names.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.
        '''
        self._interpreter.clear_arb_memory()

    @ivi_synchronized
    def clear_arb_sequence(self, sequence_handle):
        r'''clear_arb_sequence

        Removes a previously created arbitrary sequence from the signal
        generator memory and invalidates the sequence handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            sequence_handle (int): Specifies the handle of the arbitrary sequence that you want the signal
                generator to remove. You can create an arbitrary sequence using the
                create_arb_sequence or create_advanced_arb_sequence method.
                These methods return a handle that you use to identify the sequence.

                | **Defined Value**:
                | NIFGEN_VAL_ALL_SEQUENCES—Remove all sequences from the signal
                  generator

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.clear_arb_sequence(sequence_handle)

    @ivi_synchronized
    def _clear_arb_waveform(self, waveform_handle):
        r'''_clear_arb_waveform

        Removes a previously created arbitrary waveform from the signal
        generator memory and invalidates the waveform handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            waveform_handle (int): Specifies the handle of the arbitrary waveform that you want the signal
                generator to remove.

                You can create multiple arbitrary waveforms using one of the following
                niFgen Create Waveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64

                **Defined Value**:

                NIFGEN_VAL_ALL_WAVEFORMS—Remove all waveforms from the signal
                generator.

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.clear_arb_waveform(waveform_handle)

    @ivi_synchronized
    def clear_freq_list(self, frequency_list_handle):
        r'''clear_freq_list

        Removes a previously created frequency list from the signal generator
        memory and invalidates the frequency list handle.

        Note:
        The signal generator must not be in the Generating state when you
        call this method.

        Args:
            frequency_list_handle (int): Specifies the handle of the frequency list you want the signal generator
                to remove. You create multiple frequency lists using
                create_freq_list. create_freq_list returns a handle that you
                use to identify each list. Specify a value of -1 to clear all frequency
                lists.

                **Defined Value**

                NIFGEN_VAL_ALL_FLISTS—Remove all frequency lists from the signal
                generator.

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.

        '''
        self._interpreter.clear_freq_list(frequency_list_handle)

    @ivi_synchronized
    def commit(self):
        r'''commit

        Causes a transition to the Committed state. This method verifies
        property values, reserves the device, and commits the property values
        to the device. If the property values are all valid, NI-FGEN sets the
        device hardware configuration to match the session configuration. This
        method does not support the NI 5401/5404/5411/5431 signal generators.

        In the Committed state, you can load waveforms, scripts, and sequences
        into memory. If any properties are changed, NI-FGEN implicitly
        transitions back to the Idle state, where you can program all session
        properties before applying them to the device. This method has no
        effect if the device is already in the Committed or Generating state and
        returns a successful status value.

        Calling this VI before the niFgen Initiate Generation VI is optional but
        has the following benefits:

        -  Routes are committed, so signals are exported or imported.
        -  Any Reference Clock and external clock circuits are phase-locked.
        -  A subsequent initiate method can run faster
           because the device is already configured.
        '''
        self._interpreter.commit()

    @ivi_synchronized
    def create_advanced_arb_sequence(self, waveform_handles_array, loop_counts_array, sample_counts_array=None, marker_location_array=None):
        r'''create_advanced_arb_sequence

        Creates an arbitrary sequence from an array of waveform handles and an
        array of corresponding loop counts. This method returns a handle that
        identifies the sequence. You pass this handle to the
        configure_arb_sequence method to specify what arbitrary sequence
        you want the signal generator to produce.

        The create_advanced_arb_sequence method extends on the
        create_arb_sequence method by adding the ability to set the
        number of samples in each sequence step and to set marker locations.

        An arbitrary sequence consists of multiple waveforms. For each waveform,
        you specify the number of times the signal generator produces the
        waveform before proceeding to the next waveform. The number of times to
        repeat a specific waveform is called the loop count.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.SEQ before calling this
        method.

        Args:
            waveform_handles_array (list of int): Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                allocate_waveform method or one of the following niFgen
                CreateWaveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64

                **Default Value**: None

            loop_counts_array (list of int): Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                query_arb_seq_capabilities method.

                **Default Value**: None

            sample_counts_array (list of int): Specifies the array of sample counts that you want to use to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value you specify in the **sequenceLength** parameter. Each
                **sampleCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates the subset, in samples, of the given waveform to
                generate. Each element of the **sampleCountsArray** must be larger than
                the minimum waveform size, a multiple of the waveform quantum and no
                larger than the number of samples in the corresponding waveform. You can
                obtain these values by calling the query_arb_wfm_capabilities
                method.

                **Default Value**: None

            marker_location_array (list of int): Specifies the array of marker locations to where you want a marker to be
                generated in the sequence. The array must have at least as many elements
                as the value you specify in the **sequenceLength** parameter. Each
                **markerLocationArray** element corresponds to a
                **waveformHandlesArray** element and indicates where in the waveform a
                marker is to generate. The marker location must be less than the size of
                the waveform the marker is in. The markers are coerced to the nearest
                marker quantum and the coerced values are returned in the
                **coercedMarkersArray** parameter.

                If you do not want a marker generated for a particular sequence stage,
                set this parameter to NIFGEN_VAL_NO_MARKER.

                **Defined Value**: NIFGEN_VAL_NO_MARKER

                **Default Value**: None

                Note:
                One or more of the referenced values are not in the Python API for this driver. Enums that only define values, or represent True/False, have been removed.


        Returns:
            coerced_markers_array (list of int): Returns an array of all given markers that are coerced (rounded) to the
                nearest marker quantum. Not all devices coerce markers.

                **Default Value**: None

            sequence_handle (int): Returns the handle that identifies the new arbitrary sequence. You can
                pass this handle to configure_arb_sequence to generate the
                arbitrary sequence.

        '''
        if loop_counts_array is not None and len(loop_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of loop_counts_array and waveform_handles_array parameters do not match.")  # case S160
        if sample_counts_array is not None and len(sample_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of sample_counts_array and waveform_handles_array parameters do not match.")  # case S160
        if marker_location_array is not None and len(marker_location_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of marker_location_array and waveform_handles_array parameters do not match.")  # case S160
        coerced_markers_array, sequence_handle = self._interpreter.create_advanced_arb_sequence(waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array)
        return coerced_markers_array, sequence_handle

    @ivi_synchronized
    def create_arb_sequence(self, waveform_handles_array, loop_counts_array):
        r'''create_arb_sequence

        Creates an arbitrary sequence from an array of waveform handles and an
        array of corresponding loop counts. This method returns a handle that
        identifies the sequence. You pass this handle to the
        configure_arb_sequence method to specify what arbitrary sequence
        you want the signal generator to produce.

        An arbitrary sequence consists of multiple waveforms. For each waveform,
        you can specify the number of times that the signal generator produces
        the waveform before proceeding to the next waveform. The number of times
        to repeat a specific waveform is called the loop count.

        Note:
        You must call the ConfigureOutputMode method to set the
        **outputMode** parameter to OutputMode.SEQ before calling this
        method.

        Args:
            waveform_handles_array (list of int): Specifies the array of waveform handles from which you want to create a
                new arbitrary sequence. The array must have at least as many elements as
                the value that you specify in **sequenceLength**. Each
                **waveformHandlesArray** element has a corresponding **loopCountsArray**
                element that indicates how many times that waveform is repeated. You
                obtain waveform handles when you create arbitrary waveforms with the
                allocate_waveform method or one of the following niFgen
                CreateWaveform methods:

                -  create_waveform
                -  create_waveform
                -  create_waveform_from_file_i16
                -  create_waveform_from_file_f64

                **Default Value**: None

            loop_counts_array (list of int): Specifies the array of loop counts you want to use to create a new
                arbitrary sequence. The array must have at least as many elements as the
                value that you specify in the **sequenceLength** parameter. Each
                **loopCountsArray** element corresponds to a **waveformHandlesArray**
                element and indicates how many times to repeat that waveform. Each
                element of the **loopCountsArray** must be less than or equal to the
                maximum number of loop counts that the signal generator allows. You can
                obtain the maximum loop count from **maximumLoopCount** in the
                query_arb_seq_capabilities method.

                **Default Value**: None


        Returns:
            sequence_handle (int): Returns the handle that identifies the new arbitrary sequence. You can
                pass this handle to configure_arb_sequence to generate the
                arbitrary sequence.

        '''
        if loop_counts_array is not None and len(loop_counts_array) != len(waveform_handles_array):  # case S160
            raise ValueError("Length of loop_counts_array and waveform_handles_array parameters do not match.")  # case S160
        sequence_handle = self._interpreter.create_arb_sequence(waveform_handles_array, loop_counts_array)
        return sequence_handle

    @ivi_synchronized
    def create_freq_list(self, waveform, frequency_array, duration_array):
        r'''create_freq_list

        Creates a frequency list from an array of frequencies
        (**frequencyArray**) and an array of durations (**durationArray**). The
        two arrays should have the same number of elements, and this value must
        also be the size of the **frequencyListLength**. The method returns a
        handle that identifies the frequency list (the **frequencyListHandle**).
        You can pass this handle to configure_freq_list to specify what
        frequency list you want the signal generator to produce.

        A frequency list consists of a list of frequencies and durations. The
        signal generator generates each frequency for the given amount of time
        and then proceeds to the next frequency. When the end of the list is
        reached, the signal generator starts over at the beginning of the list.

        Note:
        The signal generator must not be in the Generating state when you call
        this method.

        Args:
            waveform (enums.Waveform): Specifies the standard waveform that you want the signal generator to
                produce. NI-FGEN sets the func_waveform property to this
                value.

                ****Defined Values****

                **Default Value**: Waveform.SINE

                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SINE      | Specifies that the signal generator produces a sinusoid waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.SQUARE    | Specifies that the signal generator produces a square waveform.                                                                |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.TRIANGLE  | Specifies that the signal generator produces a triangle waveform.                                                              |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_UP   | Specifies that the signal generator produces a positive ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.RAMP_DOWN | Specifies that the signal generator produces a negative ramp waveform.                                                         |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.DC        | Specifies that the signal generator produces a constant voltage.                                                               |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.NOISE     | Specifies that the signal generator produces white noise.                                                                      |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+
                | Waveform.USER      | Specifies that the signal generator produces a user-defined waveform as defined with the define_user_standard_waveform method. |
                +--------------------+--------------------------------------------------------------------------------------------------------------------------------+

            frequency_array (list of float): Specifies the array of frequencies to form the frequency list. The array
                must have at least as many elements as the value you specify in
                **frequencyListLength**. Each **frequencyArray** element has a
                corresponding **durationArray** element that indicates how long that
                frequency is repeated.

                **Units**: hertz

                **Default Value**: None

            duration_array (list of float): Specifies the array of durations to form the frequency list. The array
                must have at least as many elements as the value that you specify in
                **frequencyListLength**. Each **durationArray** element has a
                corresponding **frequencyArray** element and indicates how long in
                seconds to generate the corresponding frequency.

                **Units**: seconds

                **Default Value**: None


        Returns:
            frequency_list_handle (int): Returns the handle that identifies the new frequency list. You can pass
                this handle to configure_freq_list to generate the arbitrary
                sequence.

        '''
        if type(waveform) is not enums.Waveform:
            raise TypeError('Parameter waveform must be of type ' + str(enums.Waveform))
        if duration_array is not None and len(duration_array) != len(frequency_array):  # case S160
            raise ValueError("Length of duration_array and frequency_array parameters do not match.")  # case S160
        frequency_list_handle = self._interpreter.create_freq_list(waveform, frequency_array, duration_array)
        return frequency_list_handle

    @ivi_synchronized
    def disable(self):
        r'''disable

        Places the instrument in a quiescent state where it has minimal or no
        impact on the system to which it is connected. The analog output and all
        exported signals are disabled.
        '''
        self._interpreter.disable()

    @ivi_synchronized
    def export_attribute_configuration_buffer(self):
        r'''export_attribute_configuration_buffer

        Exports the property configuration of the session to a configuration
        buffer.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑FGEN returns an
        error.

        Returns:
            configuration (bytes): Specifies the byte array buffer to be populated with the exported
                property configuration.

        '''
        configuration = self._interpreter.export_attribute_configuration_buffer()
        return _converters.convert_to_bytes(configuration)

    @ivi_synchronized
    def export_attribute_configuration_file(self, file_path):
        r'''export_attribute_configuration_file

        Exports the property configuration of the session to the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        This method verifies that the properties you have configured for the
        session are valid. If the configuration is invalid, NI‑FGEN returns an
        error.

        Args:
            file_path (str): Specifies the absolute path to the file to contain the exported
                property configuration. If you specify an empty or relative path, this
                method returns an error.
                **Default file extension:** .nifgenconfig

        '''
        self._interpreter.export_attribute_configuration_file(file_path)

    @ivi_synchronized
    def get_channel_name(self, index):
        r'''get_channel_name

        Returns the channel string that is in the channel table at an index you
        specify.

        Note:
        This method is included for compliance with the IviFgen Class
        Specification.

        Args:
            index (int): A 1-based index into the channel table.


        Returns:
            channel_string (str): Returns the channel string that is in the channel table at the index you
                specify. Do not modify the contents of the channel string.

        '''
        channel_string = self._interpreter.get_channel_name(index)
        return channel_string

    @ivi_synchronized
    def _get_ext_cal_last_date_and_time(self):
        r'''_get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration.
        The time returned is 24-hour (military) local time; for example, if the
        device was calibrated at 2:30 PM, this method returns 14 for the
        **hour** parameter and 30 for the **minute** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        '''
        year, month, day, hour, minute = self._interpreter.get_ext_cal_last_date_and_time()
        return year, month, day, hour, minute

    @ivi_synchronized
    def get_ext_cal_last_temp(self):
        r'''get_ext_cal_last_temp

        Returns the temperature at the last successful external calibration. The
        temperature is returned in degrees Celsius.

        Returns:
            temperature (float): Specifies the temperature at the last successful calibration in degrees
                Celsius.

        '''
        temperature = self._interpreter.get_ext_cal_last_temp()
        return temperature

    @ivi_synchronized
    def get_ext_cal_recommended_interval(self):
        r'''get_ext_cal_recommended_interval

        Returns the recommended interval between external calibrations in
        months.

        Returns:
            months (hightime.timedelta): Specifies the recommended interval between external calibrations in
                months.

        '''
        months = self._interpreter.get_ext_cal_recommended_interval()
        return _converters.convert_month_to_timedelta(months)

    @ivi_synchronized
    def get_hardware_state(self):
        r'''get_hardware_state

        Returns the current hardware state of the device and, if the device is
        in the hardware error state, the current hardware error.

        Note: Hardware states do not necessarily correspond to NI-FGEN states.

        Returns:
            state (enums.HardwareState): Returns the hardware state of the signal generator.

                **Defined Values**

                +-----------------------------------------+--------------------------------------------+
                | HardwareState.IDLE                      | The device is in the Idle state.           |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.WAITING_FOR_START_TRIGGER | The device is waiting for Start Trigger.   |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.RUNNING                   | The device is in the Running state.        |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.DONE                      | The generation has completed successfully. |
                +-----------------------------------------+--------------------------------------------+
                | HardwareState.HARDWARE_ERROR            | There is a hardware error.                 |
                +-----------------------------------------+--------------------------------------------+

        '''
        state = self._interpreter.get_hardware_state()
        return state

    @ivi_synchronized
    def get_ext_cal_last_date_and_time(self):
        '''get_ext_cal_last_date_and_time

        Returns the date and time of the last successful external calibration. The time returned is 24-hour (military) local time; for example, if the device was calibrated at 2:30 PM, this method returns 14 for the **hour** parameter and 30 for the **minute** parameter.

        Returns:
            last_cal_datetime (hightime.datetime): Indicates date and time of the last calibration.

        '''
        year, month, day, hour, minute = self._get_ext_cal_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def get_self_cal_last_date_and_time(self):
        '''get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        Returns:
            last_cal_datetime (hightime.datetime): Returns the date and time the device was last calibrated.

        '''
        year, month, day, hour, minute = self._get_self_cal_last_date_and_time()
        return hightime.datetime(year, month, day, hour, minute)

    @ivi_synchronized
    def _get_self_cal_last_date_and_time(self):
        r'''_get_self_cal_last_date_and_time

        Returns the date and time of the last successful self-calibration.

        All values are returned as separate parameters. Each parameter is
        returned as an integer, including the year, month, day, hour, minute,
        and second. For example, if the device is calibrated in September 2013,
        this method returns 9 for the **month** parameter and 2013 for the
        **year** parameter.

        The time returned is 24-hour (military) local time. For example, if the
        device was calibrated at 2:30 PM, this method returns 14 for the
        **hours** parameter and 30 for the **minutes** parameter.

        Returns:
            year (int): Specifies the year of the last successful calibration.

            month (int): Specifies the month of the last successful calibration.

            day (int): Specifies the day of the last successful calibration.

            hour (int): Specifies the hour of the last successful calibration.

            minute (int): Specifies the minute of the last successful calibration.

        '''
        year, month, day, hour, minute = self._interpreter.get_self_cal_last_date_and_time()
        return year, month, day, hour, minute

    @ivi_synchronized
    def get_self_cal_last_temp(self):
        r'''get_self_cal_last_temp

        Returns the temperature at the last successful self-calibration. The
        temperature is returned in degrees Celsius.

        Returns:
            temperature (float): Specifies the temperature at the last successful calibration in degrees
                Celsius.

        '''
        temperature = self._interpreter.get_self_cal_last_temp()
        return temperature

    @ivi_synchronized
    def get_self_cal_supported(self):
        r'''get_self_cal_supported

        Returns whether the device supports self–calibration.

        Returns:
            self_cal_supported (bool): Returns whether the device supports self-calibration.

                ****Defined Values****

                +-------+------------------------------------+
                | True  | Self–calibration is supported.     |
                +-------+------------------------------------+
                | False | Self–calibration is not supported. |
                +-------+------------------------------------+

        '''
        self_cal_supported = self._interpreter.get_self_cal_supported()
        return self_cal_supported

    @ivi_synchronized
    def import_attribute_configuration_buffer(self, configuration):
        r'''import_attribute_configuration_buffer

        Imports a property configuration to the session from the specified
        configuration buffer.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        Note:
        You cannot call this method while the session is in a running state,
        such as while generating a signal.

        Args:
            configuration (bytes): Specifies the byte array buffer that contains the property
                configuration to import.

        '''
        configuration = _converters.convert_to_bytes(configuration)
        self._interpreter.import_attribute_configuration_buffer(configuration)

    @ivi_synchronized
    def import_attribute_configuration_file(self, file_path):
        r'''import_attribute_configuration_file

        Imports a property configuration to the session from the specified
        file.

        You can export and import session property configurations only between
        devices with identical model numbers, channel counts, and onboard memory
        sizes.

        Note:
        You cannot call this method while the session is in a running state,
        such as while generating a signal.

        Args:
            file_path (str): Specifies the absolute path to the file containing the property
                configuration to import. If you specify an empty or relative path, this
                method returns an error.
                **Default File Extension:** .nifgenconfig

        '''
        self._interpreter.import_attribute_configuration_file(file_path)

    def _initialize_with_channels(self, resource_name, channel_name=None, reset_device=False, option_string=""):
        r'''_initialize_with_channels

        Creates and returns a new NI-FGEN session to the specified channel of a
        waveform generator that is used in all subsequent NI-FGEN method
        calls.

        Args:
            resource_name (str): Caution:
                Traditional NI-DAQ and NI-DAQmx device names are not case-sensitive.
                However, all IVI names, such as logical names, are case-sensitive. If
                you use logical names, driver session names, or virtual names in your
                program, you must ensure that the name you use matches the name in the
                IVI Configuration Store file exactly, without any variations in the case
                of the characters.

                | Specifies the resource name of the device to initialize.

                For Traditional NI-DAQ devices, the syntax is DAQ::\ *n*, where *n* is
                the device number assigned by MAX, as shown in Example 1.

                For NI-DAQmx devices, the syntax is just the device name specified in
                MAX, as shown in Example 2. Typical default names for NI-DAQmx devices
                in MAX are Dev1 or PXI1Slot1. You can rename an NI-DAQmx device by
                right-clicking on the name in MAX and entering a new name.

                An alternate syntax for NI-DAQmx devices consists of DAQ::\ *NI-DAQmx
                device name*, as shown in Example 3. This naming convention allows for
                the use of an NI-DAQmx device in an application that was originally
                designed for a Traditional NI-DAQ device. For example, if the
                application expects DAQ::1, you can rename the NI-DAQmx device to 1 in
                MAX and pass in DAQ::1 for the resource name, as shown in Example 4.

                If you use the DAQ::\ *n* syntax and an NI-DAQmx device name already
                exists with that same name, the NI-DAQmx device is matched first.

                You can also pass in the name of an IVI logical name or an IVI virtual
                name configured with the IVI Configuration utility, as shown in Example
                5. A logical name identifies a particular virtual instrument. A virtual
                name identifies a specific device and specifies the initial settings for
                the session.

                +-----------+--------------------------------------+------------------------+---------------------------------+
                | Example # | Device Type                          | Syntax                 | Variable                        |
                +===========+======================================+========================+=================================+
                | 1         | Traditional NI-DAQ device            | DAQ::\ *1*             | (*1* = device number)           |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 2         | NI-DAQmx device                      | *myDAQmxDevice*        | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 3         | NI-DAQmx device                      | DAQ::\ *myDAQmxDevice* | (*myDAQmxDevice* = device name) |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 4         | NI-DAQmx device                      | DAQ::\ *2*             | (*2* = device name)             |
                +-----------+--------------------------------------+------------------------+---------------------------------+
                | 5         | IVI logical name or IVI virtual name | *myLogicalName*        | (*myLogicalName* = name)        |
                +-----------+--------------------------------------+------------------------+---------------------------------+

            channel_name (str, list, range, tuple): Specifies the channel that this VI uses.

                **Default Value**: "0"

            reset_device (bool): Specifies whether you want to reset the device during the initialization
                procedure. True specifies that the device is reset and performs the
                same method as the Reset method.

                ****Defined Values****

                **Default Value**: False

                +-------+---------------------+
                | True  | Reset device        |
                +-------+---------------------+
                | False | Do not reset device |
                +-------+---------------------+

            option_string (dict): Sets the initial value of certain session properties.

                The syntax for **optionString** is

                <*attributeName*> = <*value*>

                where

                *attributeName* is the name of the property and *value* is the value to
                which the property is set

                To set multiple properties, separate them with a comma.

                If you pass NULL or an empty string for this parameter, the session uses
                the default values for these properties. You can override the default
                values by assigning a value explicitly in a string that you pass for
                this parameter.

                You do not have to specify all of the properties and may leave any of
                them out. However, if you do not specify one of the properties, its
                default value is used.

                If simulation is enabled (Simulate=1), you may specify the device that
                you want to simulate. To specify a device, enter the following syntax in
                **optionString**.

                DriverSetup=Model:<*driver model number*>;Channels:<*channel
                names*>;BoardType:<*module type*>;MemorySize:<*size of onboard memory in
                bytes*>

                **Syntax Examples**

                **Properties and **Defined Values****

                **Default Values**: "Simulate=0,RangeCheck=1,QueryInstrStatus=1,Cache=1"

                +------------------+-------------------------+-------------+
                | Property Name    | Property                | Values      |
                +==================+=========================+=============+
                | RangeCheck       | RANGE_CHECK             | True, False |
                +------------------+-------------------------+-------------+
                | QueryInstrStatus | QUERY_INSTRUMENT_STATUS | True, False |
                +------------------+-------------------------+-------------+
                | Cache            | CACHE                   | True, False |
                +------------------+-------------------------+-------------+
                | Simulate         | simulate                | True, False |
                +------------------+-------------------------+-------------+

                Note:
                One or more of the referenced properties are not in the Python API for this driver.


        Returns:
            vi (int): Returns a session handle that you can use to identify the device in all
                subsequent NI-FGEN method calls.

        '''
        channel_name = _converters.convert_repeated_capabilities_without_prefix(channel_name)
        option_string = _converters.convert_init_with_options_dictionary(option_string)
        vi = self._interpreter.initialize_with_channels(resource_name, channel_name, reset_device, option_string)
        return vi

    @ivi_synchronized
    def _initiate_generation(self):
        r'''_initiate_generation

        Initiates signal generation. If you want to abort signal generation,
        call the abort method. After the signal generation
        is aborted, you can call the initiate method to
        cause the signal generator to produce a signal again.
        '''
        self._interpreter.initiate_generation()

    @ivi_synchronized
    def is_done(self):
        r'''is_done

        Determines whether the current generation is complete. This method
        sets the **done** parameter to True if the session is in the Idle or
        Committed states.

        Note:
        NI-FGEN only reports the **done** parameter as True after the
        current generation is complete in Single trigger mode.

        Returns:
            done (bool): Returns information about the completion of waveform generation.

                **Defined Values**

                +-------+-----------------------------+
                | True  | Generation is complete.     |
                +-------+-----------------------------+
                | False | Generation is not complete. |
                +-------+-----------------------------+

        '''
        done = self._interpreter.is_done()
        return done

    @ivi_synchronized
    def query_arb_seq_capabilities(self):
        r'''query_arb_seq_capabilities

        Returns the properties of the signal generator that are related to
        creating arbitrary sequences (the max_num_sequences,
        min_sequence_length,
        max_sequence_length, and max_loop_count
        properties).

        Returns:
            maximum_number_of_sequences (int): Returns the maximum number of arbitrary waveform sequences that the
                signal generator allows. NI-FGEN obtains this value from the
                max_num_sequences property.

            minimum_sequence_length (int): Returns the minimum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                min_sequence_length property.

            maximum_sequence_length (int): Returns the maximum number of arbitrary waveforms the signal generator
                allows in a sequence. NI-FGEN obtains this value from the
                max_sequence_length property.

            maximum_loop_count (int): Returns the maximum number of times the signal generator can repeat an
                arbitrary waveform in a sequence. NI-FGEN obtains this value from the
                max_loop_count property.

        '''
        maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count = self._interpreter.query_arb_seq_capabilities()
        return maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count

    @ivi_synchronized
    def query_arb_wfm_capabilities(self):
        r'''query_arb_wfm_capabilities

        Returns the properties of the signal generator that are related to
        creating arbitrary waveforms. These properties are the maximum number of
        waveforms, waveform quantum, minimum waveform size, and maximum waveform
        size.

        Note:
        If you do not want to obtain the waveform quantum, pass a value of
        VI_NULL for this parameter.

        Returns:
            maximum_number_of_waveforms (int): Returns the maximum number of arbitrary waveforms that the signal
                generator allows. NI-FGEN obtains this value from the
                max_num_waveforms property.

            waveform_quantum (int): The size (number of points) of each waveform must be a multiple of a
                constant quantum value. This parameter obtains the quantum value that
                the signal generator uses. NI-FGEN returns this value from the
                waveform_quantum property.

                For example, when this property returns a value of 8, all waveform
                sizes must be a multiple of 8.

            minimum_waveform_size (int): Returns the minimum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                min_waveform_size property.

            maximum_waveform_size (int): Returns the maximum number of points that the signal generator allows in
                a waveform. NI-FGEN obtains this value from the
                max_waveform_size property.

        '''
        maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size = self._interpreter.query_arb_wfm_capabilities()
        return maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size

    @ivi_synchronized
    def query_freq_list_capabilities(self):
        r'''query_freq_list_capabilities

        Returns the properties of the signal generator that are related to
        creating frequency lists. These properties are
        max_num_freq_lists,
        min_freq_list_length,
        max_freq_list_length,
        min_freq_list_duration,
        max_freq_list_duration, and
        freq_list_duration_quantum.

        Returns:
            maximum_number_of_freq_lists (int): Returns the maximum number of frequency lists that the signal generator
                allows. NI-FGEN obtains this value from the
                max_num_freq_lists property.

            minimum_frequency_list_length (int): Returns the minimum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                min_freq_list_length property.

            maximum_frequency_list_length (int): Returns the maximum number of steps that the signal generator allows in
                a frequency list. NI-FGEN obtains this value from the
                max_freq_list_length property.

            minimum_frequency_list_duration (float): Returns the minimum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                min_freq_list_duration property.

            maximum_frequency_list_duration (float): Returns the maximum duration that the signal generator allows in a step
                of a frequency list. NI-FGEN obtains this value from the
                max_freq_list_duration property.

            frequency_list_duration_quantum (float): Returns the quantum of which all durations must be a multiple in a
                frequency list. NI-FGEN obtains this value from the
                freq_list_duration_quantum property.

        '''
        maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum = self._interpreter.query_freq_list_capabilities()
        return maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum

    @ivi_synchronized
    def read_current_temperature(self):
        r'''read_current_temperature

        Reads the current onboard temperature of the device. The temperature is
        returned in degrees Celsius.

        Returns:
            temperature (float): Returns the current temperature read from onboard temperature sensors,
                in degrees Celsius.

        '''
        temperature = self._interpreter.read_current_temperature()
        return temperature

    @ivi_synchronized
    def reset_device(self):
        r'''reset_device

        Performs a hard reset on the device. Generation is stopped, all routes
        are released, external bidirectional terminals are tristated, FPGAs are
        reset, hardware is configured to its default state, and all session
        properties are reset to their default states.
        '''
        self._interpreter.reset_device()

    @ivi_synchronized
    def reset_with_defaults(self):
        r'''reset_with_defaults

        Resets the instrument and reapplies initial user–specified settings from
        the logical name that was used to initialize the session. If the session
        was created without a logical name, this method is equivalent to the
        reset method.
        '''
        self._interpreter.reset_with_defaults()

    @ivi_synchronized
    def self_cal(self):
        r'''self_cal

        Performs a full internal self-calibration on the device. If the
        calibration is successful, new calibration data and constants are stored
        in the onboard EEPROM.
        '''
        self._interpreter.self_cal()

    @ivi_synchronized
    def wait_until_done(self, max_time=hightime.timedelta(seconds=10.0)):
        r'''wait_until_done

        Waits until the device is done generating or until the maximum time has
        expired.

        Args:
            max_time (hightime.timedelta, datetime.timedelta, or int in milliseconds): Specifies the timeout value in milliseconds.

        '''
        max_time = _converters.convert_timedelta_to_milliseconds_int32(max_time)
        self._interpreter.wait_until_done(max_time)

    def _close(self):
        r'''_close

        Performs the following operations:

        -  Closes the instrument I/O session.
        -  Destroys the NI-FGEN session and all of its properties.
        -  Deallocates any memory resources NI-FGEN uses.

        Not all signal routes established by calling the ExportSignal
        and RouteSignalOut methods are released when the NI-FGEN
        session is closed. The following table shows what happens to a signal
        route on your device when you call the _close method.

        +--------------------+-------------------+------------------+
        | Routes To          | NI 5401/5411/5431 | Other Devices    |
        +====================+===================+==================+
        | Front Panel        | Remain connected  | Remain connected |
        +--------------------+-------------------+------------------+
        | RTSI/PXI Backplane | Remain connected  | Disconnected     |
        +--------------------+-------------------+------------------+

        Note:
        After calling _close, you cannot use NI-FGEN again until you
        call the init or InitWithOptions methods.
        '''
        self._interpreter.close()

    @ivi_synchronized
    def self_test(self):
        '''self_test

        Runs the instrument self-test routine and returns the test result(s).

        Raises `SelfTestError` on self test failure. Properties on exception object:

        - code - failure code from driver
        - message - status message from driver

        +----------------+------------------+
        | Self-Test Code | Description      |
        +================+==================+
        | 0              | Passed self-test |
        +----------------+------------------+
        | 1              | Self-test failed |
        +----------------+------------------+

        Note:
        When used on some signal generators, the device is reset after the
        self_test method runs. If you use the self_test
        method, your device may not be in its previously configured state
        after the method runs.
        '''
        code, msg = self._self_test()
        if code:
            raise errors.SelfTestError(code, msg)
        return None

    @ivi_synchronized
    def reset(self):
        r'''reset

        Resets the instrument to a known state. This method aborts the
        generation, clears all routes, and resets session properties to the
        default values. This method does not, however, commit the session
        properties or configure the device hardware to its default state.

        Note:
        For the NI 5401/5404/5411/5431, this method exhibits the same
        behavior as the reset_device method.
        '''
        self._interpreter.reset()

    @ivi_synchronized
    def _self_test(self):
        r'''_self_test

        Runs the instrument self-test routine and returns the test result(s).

        Note:
        When used on some signal generators, the device is reset after the
        self_test method runs. If you use the self_test
        method, your device may not be in its previously configured state
        after the method runs.

        Returns:
            self_test_result (int): Contains the value returned from the instrument self-test. A value of 0
                indicates success.

                +----------------+------------------+
                | Self-Test Code | Description      |
                +================+==================+
                | 0              | Passed self-test |
                +----------------+------------------+
                | 1              | Self-test failed |
                +----------------+------------------+

            self_test_message (str): Returns the self-test response string from the instrument.

                You must pass a ViChar array with at least 256 bytes.

        '''
        self_test_result, self_test_message = self._interpreter.self_test()
        return self_test_result, self_test_message
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/unit_tests/_matchers.py sha256=cef57f0b06222a252aac030770f55ca6dd0e7d74a1c180016e75ade6283f92fc bytes=12199 -->
## FILE: generated/nifgen/nifgen/unit_tests/_matchers.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/unit_tests/_matchers.py`
- sha256: `cef57f0b06222a252aac030770f55ca6dd0e7d74a1c180016e75ade6283f92fc`
- bytes: 12199

````python
# -*- coding: utf-8 -*-
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
import nifgen._visatype as _visatype
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Base classes


class _ScalarMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("{}: Unexpected type. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_type, type(other)))
            return False
        if other.value != self.expected_value:
            print("{}: Unexpected value. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_value, other.value))
            return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class _PointerMatcher(object):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __eq__(self, other):
        if not isinstance(other, ctypes.POINTER(self.expected_type)):
            print("Unexpected type. Expected: {}. Received: {}".format(ctypes.POINTER(self.expected_type), type(other)))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_type))


class _BufferMatcher(object):
    def __init__(self, expected_element_type, expected_size_or_value):
        if isinstance(expected_size_or_value, int):
            # Were given the size of the buffer
            self.expected_value = None
            self.expected_size = expected_size_or_value
        else:
            # Were given a list or something that behaves like a list
            self.expected_value = expected_size_or_value
            self.expected_size = len(expected_size_or_value)
        self.expected_type = expected_element_type * self.expected_size
        # Store params for __repr__
        self._expected_element_type = expected_element_type
        self._expected_size_or_value = expected_size_or_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            # Because of object lifetimes, we may need to mock the other instance and provide lists instead of the actual array
            if not isinstance(other, self.expected_type) and not isinstance(other, list):
                print("Unexpected type. Expected: {} or {}. Received: {}".format(self.expected_type, list, type(other)))
                return False
        if self.expected_size != len(other):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(other)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for i in range(0, len(self.expected_value)):
                if self.expected_value[i] != other[i]:
                    print("Unexpected value at index {}. Expected: {}. Received: {}".format(i, self.expected_value[i], other[i]))
                    return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self._expected_element_type), pp.pformat(self._expected_size_or_value))

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type  = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_value = ' + str(self.expected_value) + '\n'
        ret_str += '    expected_size  = ' + str(self.expected_size) + '\n'
        return ret_str


# Strings


class ViStringMatcher(object):
    def __init__(self, expected_string_value):
        self.expected_string_value = expected_string_value

    def __eq__(self, other):
        if not isinstance(other, ctypes.Array):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            if not isinstance(other, ctypes.Array):
                print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(other)))
                return False
        if len(other) < len(self.expected_string_value) + 1:  # +1 for NULL terminating character
            print("Unexpected length in C string. Expected at least: {}. Received {}".format(len(other), len(self.expected_string_value) + 1))
            return False
        if not isinstance(other[0], bytes):
            print("Unexpected type. Not a string. Received: {}".format(type(other[0])))
            return False
        if other.value.decode("ascii") != self.expected_string_value:
            print("Unexpected value. Expected {}. Received: {}".format(self.expected_string_value, other.value.decode))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_string_value))


# Custom Type


def _compare_ctype_structs(expected, actual):
    # From https://stackoverflow.com/questions/20986330/print-all-fields-of-ctypes-structure-with-introspection
    for field in expected._fields_:
        field_name = field[0]
        expected_val = getattr(expected, field_name)
        actual_val = getattr(actual, field_name)
        if expected_val != actual_val:
            print("Unexpected value field {}. Expected: {}. Received: {}".format(field_name, expected_val, actual_val))
            return False
    return True


class CustomTypeMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        return _compare_ctype_structs(self.expected_value, actual)

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class CustomTypeBufferMatcher(object):
    def __init__(self, expected_element_type, expected_value):
        self.expected_value = expected_value
        self.expected_size = len(expected_value)
        self.expected_type = expected_element_type * self.expected_size
        self.expected_element_type = expected_element_type

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected array type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        if self.expected_size != len(actual):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(actual)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for a, e in zip(actual, self.expected_value):
                if not isinstance(a, self.expected_element_type):
                    print("Unexpected type. Expected: {}. Received: {}".format(self.expected_element_type, type(a)))
                    return False
                if not _compare_ctype_structs(e, a):
                    return False
        return True

    def __repr__(self):
        expected_val_repr = '[' + ', '.join([x.__repr__() for x in self.expected_value]) + ']'
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_element_type), expected_val_repr)

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_size = ' + str(self.expected_size) + '\n'
        return ret_str


# Scalars


class ViBooleanMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViBoolean, 1 if expected_value is True else 0)


class ViSessionMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViSession, expected_value)


class ViInt16Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt16, expected_value)


class ViInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt32, expected_value)


class ViUInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViUInt32, expected_value)


class ViAttrMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViAttr, expected_value)


class ViInt64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt64, expected_value)


class ViReal64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViReal64, expected_value)


# Pointers


class ViBooleanPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViBoolean)


class ViSessionPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViSession)


class ViInt16PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt16)


class ViInt32PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt32)


class ViInt64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt64)


class ViReal64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViReal64)


# Buffers


class ViBooleanBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViBoolean, expected_size_or_value)


class ViCharBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViChar, expected_size_or_value)


class ViInt8BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt8, expected_size_or_value)


class ViInt16BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt16, expected_size_or_value)


class ViInt32BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt32, expected_size_or_value)


class ViInt64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt64, expected_size_or_value)


class ViReal64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViReal64, expected_size_or_value)


class ViSessionBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViSession, expected_size_or_value)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/unit_tests/_mock_helper.py sha256=98d53868d35243891b0859a170a3dde6c42f5d2a9aafc47a0b36afcb6f0cf9cd bytes=65520 -->
## FILE: generated/nifgen/nifgen/unit_tests/_mock_helper.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/unit_tests/_mock_helper.py`
- sha256: `98d53868d35243891b0859a170a3dde6c42f5d2a9aafc47a0b36afcb6f0cf9cd`
- bytes: 65520

````python
# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['AbortGeneration'] = {}
        self._defaults['AbortGeneration']['return'] = 0
        self._defaults['AllocateNamedWaveform'] = {}
        self._defaults['AllocateNamedWaveform']['return'] = 0
        self._defaults['AllocateWaveform'] = {}
        self._defaults['AllocateWaveform']['return'] = 0
        self._defaults['AllocateWaveform']['waveformHandle'] = None
        self._defaults['ClearArbMemory'] = {}
        self._defaults['ClearArbMemory']['return'] = 0
        self._defaults['ClearArbSequence'] = {}
        self._defaults['ClearArbSequence']['return'] = 0
        self._defaults['ClearArbWaveform'] = {}
        self._defaults['ClearArbWaveform']['return'] = 0
        self._defaults['ClearFreqList'] = {}
        self._defaults['ClearFreqList']['return'] = 0
        self._defaults['ClearUserStandardWaveform'] = {}
        self._defaults['ClearUserStandardWaveform']['return'] = 0
        self._defaults['Commit'] = {}
        self._defaults['Commit']['return'] = 0
        self._defaults['ConfigureArbSequence'] = {}
        self._defaults['ConfigureArbSequence']['return'] = 0
        self._defaults['ConfigureArbWaveform'] = {}
        self._defaults['ConfigureArbWaveform']['return'] = 0
        self._defaults['ConfigureFreqList'] = {}
        self._defaults['ConfigureFreqList']['return'] = 0
        self._defaults['ConfigureStandardWaveform'] = {}
        self._defaults['ConfigureStandardWaveform']['return'] = 0
        self._defaults['CreateAdvancedArbSequence'] = {}
        self._defaults['CreateAdvancedArbSequence']['return'] = 0
        self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray'] = None
        self._defaults['CreateAdvancedArbSequence']['sequenceHandle'] = None
        self._defaults['CreateArbSequence'] = {}
        self._defaults['CreateArbSequence']['return'] = 0
        self._defaults['CreateArbSequence']['sequenceHandle'] = None
        self._defaults['CreateFreqList'] = {}
        self._defaults['CreateFreqList']['return'] = 0
        self._defaults['CreateFreqList']['frequencyListHandle'] = None
        self._defaults['CreateWaveformF64'] = {}
        self._defaults['CreateWaveformF64']['return'] = 0
        self._defaults['CreateWaveformF64']['waveformHandle'] = None
        self._defaults['CreateWaveformFromFileF64'] = {}
        self._defaults['CreateWaveformFromFileF64']['return'] = 0
        self._defaults['CreateWaveformFromFileF64']['waveformHandle'] = None
        self._defaults['CreateWaveformFromFileI16'] = {}
        self._defaults['CreateWaveformFromFileI16']['return'] = 0
        self._defaults['CreateWaveformFromFileI16']['waveformHandle'] = None
        self._defaults['CreateWaveformI16'] = {}
        self._defaults['CreateWaveformI16']['return'] = 0
        self._defaults['CreateWaveformI16']['waveformHandle'] = None
        self._defaults['DefineUserStandardWaveform'] = {}
        self._defaults['DefineUserStandardWaveform']['return'] = 0
        self._defaults['DeleteNamedWaveform'] = {}
        self._defaults['DeleteNamedWaveform']['return'] = 0
        self._defaults['DeleteScript'] = {}
        self._defaults['DeleteScript']['return'] = 0
        self._defaults['Disable'] = {}
        self._defaults['Disable']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer'] = {}
        self._defaults['ExportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ExportAttributeConfigurationBuffer']['configuration'] = None
        self._defaults['ExportAttributeConfigurationFile'] = {}
        self._defaults['ExportAttributeConfigurationFile']['return'] = 0
        self._defaults['GetAttributeViBoolean'] = {}
        self._defaults['GetAttributeViBoolean']['return'] = 0
        self._defaults['GetAttributeViBoolean']['attributeValue'] = None
        self._defaults['GetAttributeViInt32'] = {}
        self._defaults['GetAttributeViInt32']['return'] = 0
        self._defaults['GetAttributeViInt32']['attributeValue'] = None
        self._defaults['GetAttributeViReal64'] = {}
        self._defaults['GetAttributeViReal64']['return'] = 0
        self._defaults['GetAttributeViReal64']['attributeValue'] = None
        self._defaults['GetAttributeViString'] = {}
        self._defaults['GetAttributeViString']['return'] = 0
        self._defaults['GetAttributeViString']['attributeValue'] = None
        self._defaults['GetChannelName'] = {}
        self._defaults['GetChannelName']['return'] = 0
        self._defaults['GetChannelName']['channelString'] = None
        self._defaults['GetError'] = {}
        self._defaults['GetError']['return'] = 0
        self._defaults['GetError']['errorCode'] = None
        self._defaults['GetError']['errorDescription'] = None
        self._defaults['GetExtCalLastDateAndTime'] = {}
        self._defaults['GetExtCalLastDateAndTime']['return'] = 0
        self._defaults['GetExtCalLastDateAndTime']['year'] = None
        self._defaults['GetExtCalLastDateAndTime']['month'] = None
        self._defaults['GetExtCalLastDateAndTime']['day'] = None
        self._defaults['GetExtCalLastDateAndTime']['hour'] = None
        self._defaults['GetExtCalLastDateAndTime']['minute'] = None
        self._defaults['GetExtCalLastTemp'] = {}
        self._defaults['GetExtCalLastTemp']['return'] = 0
        self._defaults['GetExtCalLastTemp']['temperature'] = None
        self._defaults['GetExtCalRecommendedInterval'] = {}
        self._defaults['GetExtCalRecommendedInterval']['return'] = 0
        self._defaults['GetExtCalRecommendedInterval']['months'] = None
        self._defaults['GetHardwareState'] = {}
        self._defaults['GetHardwareState']['return'] = 0
        self._defaults['GetHardwareState']['state'] = None
        self._defaults['GetSelfCalLastDateAndTime'] = {}
        self._defaults['GetSelfCalLastDateAndTime']['return'] = 0
        self._defaults['GetSelfCalLastDateAndTime']['year'] = None
        self._defaults['GetSelfCalLastDateAndTime']['month'] = None
        self._defaults['GetSelfCalLastDateAndTime']['day'] = None
        self._defaults['GetSelfCalLastDateAndTime']['hour'] = None
        self._defaults['GetSelfCalLastDateAndTime']['minute'] = None
        self._defaults['GetSelfCalLastTemp'] = {}
        self._defaults['GetSelfCalLastTemp']['return'] = 0
        self._defaults['GetSelfCalLastTemp']['temperature'] = None
        self._defaults['GetSelfCalSupported'] = {}
        self._defaults['GetSelfCalSupported']['return'] = 0
        self._defaults['GetSelfCalSupported']['selfCalSupported'] = None
        self._defaults['ImportAttributeConfigurationBuffer'] = {}
        self._defaults['ImportAttributeConfigurationBuffer']['return'] = 0
        self._defaults['ImportAttributeConfigurationFile'] = {}
        self._defaults['ImportAttributeConfigurationFile']['return'] = 0
        self._defaults['InitializeWithChannels'] = {}
        self._defaults['InitializeWithChannels']['return'] = 0
        self._defaults['InitializeWithChannels']['vi'] = None
        self._defaults['InitiateGeneration'] = {}
        self._defaults['InitiateGeneration']['return'] = 0
        self._defaults['IsDone'] = {}
        self._defaults['IsDone']['return'] = 0
        self._defaults['IsDone']['done'] = None
        self._defaults['LockSession'] = {}
        self._defaults['LockSession']['return'] = 0
        self._defaults['LockSession']['callerHasLock'] = None
        self._defaults['QueryArbSeqCapabilities'] = {}
        self._defaults['QueryArbSeqCapabilities']['return'] = 0
        self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences'] = None
        self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength'] = None
        self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength'] = None
        self._defaults['QueryArbSeqCapabilities']['maximumLoopCount'] = None
        self._defaults['QueryArbWfmCapabilities'] = {}
        self._defaults['QueryArbWfmCapabilities']['return'] = 0
        self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms'] = None
        self._defaults['QueryArbWfmCapabilities']['waveformQuantum'] = None
        self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize'] = None
        self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize'] = None
        self._defaults['QueryFreqListCapabilities'] = {}
        self._defaults['QueryFreqListCapabilities']['return'] = 0
        self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists'] = None
        self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength'] = None
        self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength'] = None
        self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration'] = None
        self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration'] = None
        self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum'] = None
        self._defaults['ReadCurrentTemperature'] = {}
        self._defaults['ReadCurrentTemperature']['return'] = 0
        self._defaults['ReadCurrentTemperature']['temperature'] = None
        self._defaults['ResetDevice'] = {}
        self._defaults['ResetDevice']['return'] = 0
        self._defaults['ResetWithDefaults'] = {}
        self._defaults['ResetWithDefaults']['return'] = 0
        self._defaults['SelfCal'] = {}
        self._defaults['SelfCal']['return'] = 0
        self._defaults['SendSoftwareEdgeTrigger'] = {}
        self._defaults['SendSoftwareEdgeTrigger']['return'] = 0
        self._defaults['SetAttributeViBoolean'] = {}
        self._defaults['SetAttributeViBoolean']['return'] = 0
        self._defaults['SetAttributeViInt32'] = {}
        self._defaults['SetAttributeViInt32']['return'] = 0
        self._defaults['SetAttributeViReal64'] = {}
        self._defaults['SetAttributeViReal64']['return'] = 0
        self._defaults['SetAttributeViString'] = {}
        self._defaults['SetAttributeViString']['return'] = 0
        self._defaults['SetNamedWaveformNextWritePosition'] = {}
        self._defaults['SetNamedWaveformNextWritePosition']['return'] = 0
        self._defaults['SetRuntimeEnvironment'] = {}
        self._defaults['SetRuntimeEnvironment']['return'] = 0
        self._defaults['SetWaveformNextWritePosition'] = {}
        self._defaults['SetWaveformNextWritePosition']['return'] = 0
        self._defaults['UnlockSession'] = {}
        self._defaults['UnlockSession']['return'] = 0
        self._defaults['UnlockSession']['callerHasLock'] = None
        self._defaults['WaitUntilDone'] = {}
        self._defaults['WaitUntilDone']['return'] = 0
        self._defaults['WriteBinary16Waveform'] = {}
        self._defaults['WriteBinary16Waveform']['return'] = 0
        self._defaults['WriteNamedWaveformF64'] = {}
        self._defaults['WriteNamedWaveformF64']['return'] = 0
        self._defaults['WriteNamedWaveformI16'] = {}
        self._defaults['WriteNamedWaveformI16']['return'] = 0
        self._defaults['WriteScript'] = {}
        self._defaults['WriteScript']['return'] = 0
        self._defaults['WriteWaveform'] = {}
        self._defaults['WriteWaveform']['return'] = 0
        self._defaults['close'] = {}
        self._defaults['close']['return'] = 0
        self._defaults['error_message'] = {}
        self._defaults['error_message']['return'] = 0
        self._defaults['error_message']['errorMessage'] = None
        self._defaults['reset'] = {}
        self._defaults['reset']['return'] = 0
        self._defaults['self_test'] = {}
        self._defaults['self_test']['return'] = 0
        self._defaults['self_test']['selfTestResult'] = None
        self._defaults['self_test']['selfTestMessage'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niFgen_AbortGeneration(self, vi):  # noqa: N802
        if self._defaults['AbortGeneration']['return'] != 0:
            return self._defaults['AbortGeneration']['return']
        return self._defaults['AbortGeneration']['return']

    def niFgen_AllocateNamedWaveform(self, vi, channel_name, waveform_name, waveform_size):  # noqa: N802
        if self._defaults['AllocateNamedWaveform']['return'] != 0:
            return self._defaults['AllocateNamedWaveform']['return']
        return self._defaults['AllocateNamedWaveform']['return']

    def niFgen_AllocateWaveform(self, vi, channel_name, waveform_size, waveform_handle):  # noqa: N802
        if self._defaults['AllocateWaveform']['return'] != 0:
            return self._defaults['AllocateWaveform']['return']
        # waveform_handle
        if self._defaults['AllocateWaveform']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_AllocateWaveform", param='waveformHandle')
        if waveform_handle is not None:
            waveform_handle.contents.value = self._defaults['AllocateWaveform']['waveformHandle']
        return self._defaults['AllocateWaveform']['return']

    def niFgen_ClearArbMemory(self, vi):  # noqa: N802
        if self._defaults['ClearArbMemory']['return'] != 0:
            return self._defaults['ClearArbMemory']['return']
        return self._defaults['ClearArbMemory']['return']

    def niFgen_ClearArbSequence(self, vi, sequence_handle):  # noqa: N802
        if self._defaults['ClearArbSequence']['return'] != 0:
            return self._defaults['ClearArbSequence']['return']
        return self._defaults['ClearArbSequence']['return']

    def niFgen_ClearArbWaveform(self, vi, waveform_handle):  # noqa: N802
        if self._defaults['ClearArbWaveform']['return'] != 0:
            return self._defaults['ClearArbWaveform']['return']
        return self._defaults['ClearArbWaveform']['return']

    def niFgen_ClearFreqList(self, vi, frequency_list_handle):  # noqa: N802
        if self._defaults['ClearFreqList']['return'] != 0:
            return self._defaults['ClearFreqList']['return']
        return self._defaults['ClearFreqList']['return']

    def niFgen_ClearUserStandardWaveform(self, vi, channel_name):  # noqa: N802
        if self._defaults['ClearUserStandardWaveform']['return'] != 0:
            return self._defaults['ClearUserStandardWaveform']['return']
        return self._defaults['ClearUserStandardWaveform']['return']

    def niFgen_Commit(self, vi):  # noqa: N802
        if self._defaults['Commit']['return'] != 0:
            return self._defaults['Commit']['return']
        return self._defaults['Commit']['return']

    def niFgen_ConfigureArbSequence(self, vi, channel_name, sequence_handle, gain, offset):  # noqa: N802
        if self._defaults['ConfigureArbSequence']['return'] != 0:
            return self._defaults['ConfigureArbSequence']['return']
        return self._defaults['ConfigureArbSequence']['return']

    def niFgen_ConfigureArbWaveform(self, vi, channel_name, waveform_handle, gain, offset):  # noqa: N802
        if self._defaults['ConfigureArbWaveform']['return'] != 0:
            return self._defaults['ConfigureArbWaveform']['return']
        return self._defaults['ConfigureArbWaveform']['return']

    def niFgen_ConfigureFreqList(self, vi, channel_name, frequency_list_handle, amplitude, dc_offset, start_phase):  # noqa: N802
        if self._defaults['ConfigureFreqList']['return'] != 0:
            return self._defaults['ConfigureFreqList']['return']
        return self._defaults['ConfigureFreqList']['return']

    def niFgen_ConfigureStandardWaveform(self, vi, channel_name, waveform, amplitude, dc_offset, frequency, start_phase):  # noqa: N802
        if self._defaults['ConfigureStandardWaveform']['return'] != 0:
            return self._defaults['ConfigureStandardWaveform']['return']
        return self._defaults['ConfigureStandardWaveform']['return']

    def niFgen_CreateAdvancedArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sample_counts_array, marker_location_array, coerced_markers_array, sequence_handle):  # noqa: N802
        if self._defaults['CreateAdvancedArbSequence']['return'] != 0:
            return self._defaults['CreateAdvancedArbSequence']['return']
        # coerced_markers_array
        if self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray'] is None:
            raise MockFunctionCallError("niFgen_CreateAdvancedArbSequence", param='coercedMarkersArray')
        test_value = self._defaults['CreateAdvancedArbSequence']['coercedMarkersArray']
        try:
            coerced_markers_array_ref = coerced_markers_array.contents
        except AttributeError:
            coerced_markers_array_ref = coerced_markers_array
        assert len(coerced_markers_array_ref) >= len(test_value)
        for i in range(len(test_value)):
            coerced_markers_array_ref[i] = test_value[i]
        # sequence_handle
        if self._defaults['CreateAdvancedArbSequence']['sequenceHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateAdvancedArbSequence", param='sequenceHandle')
        if sequence_handle is not None:
            sequence_handle.contents.value = self._defaults['CreateAdvancedArbSequence']['sequenceHandle']
        return self._defaults['CreateAdvancedArbSequence']['return']

    def niFgen_CreateArbSequence(self, vi, sequence_length, waveform_handles_array, loop_counts_array, sequence_handle):  # noqa: N802
        if self._defaults['CreateArbSequence']['return'] != 0:
            return self._defaults['CreateArbSequence']['return']
        # sequence_handle
        if self._defaults['CreateArbSequence']['sequenceHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateArbSequence", param='sequenceHandle')
        if sequence_handle is not None:
            sequence_handle.contents.value = self._defaults['CreateArbSequence']['sequenceHandle']
        return self._defaults['CreateArbSequence']['return']

    def niFgen_CreateFreqList(self, vi, waveform, frequency_list_length, frequency_array, duration_array, frequency_list_handle):  # noqa: N802
        if self._defaults['CreateFreqList']['return'] != 0:
            return self._defaults['CreateFreqList']['return']
        # frequency_list_handle
        if self._defaults['CreateFreqList']['frequencyListHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateFreqList", param='frequencyListHandle')
        if frequency_list_handle is not None:
            frequency_list_handle.contents.value = self._defaults['CreateFreqList']['frequencyListHandle']
        return self._defaults['CreateFreqList']['return']

    def niFgen_CreateWaveformF64(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformF64']['return'] != 0:
            return self._defaults['CreateWaveformF64']['return']
        # waveform_handle
        if self._defaults['CreateWaveformF64']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformF64", param='waveformHandle')
        if waveform_handle is not None:
            waveform_handle.contents.value = self._defaults['CreateWaveformF64']['waveformHandle']
        return self._defaults['CreateWaveformF64']['return']

    def niFgen_CreateWaveformFromFileF64(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileF64']['return'] != 0:
            return self._defaults['CreateWaveformFromFileF64']['return']
        # waveform_handle
        if self._defaults['CreateWaveformFromFileF64']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileF64", param='waveformHandle')
        if waveform_handle is not None:
            waveform_handle.contents.value = self._defaults['CreateWaveformFromFileF64']['waveformHandle']
        return self._defaults['CreateWaveformFromFileF64']['return']

    def niFgen_CreateWaveformFromFileI16(self, vi, channel_name, file_name, byte_order, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformFromFileI16']['return'] != 0:
            return self._defaults['CreateWaveformFromFileI16']['return']
        # waveform_handle
        if self._defaults['CreateWaveformFromFileI16']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformFromFileI16", param='waveformHandle')
        if waveform_handle is not None:
            waveform_handle.contents.value = self._defaults['CreateWaveformFromFileI16']['waveformHandle']
        return self._defaults['CreateWaveformFromFileI16']['return']

    def niFgen_CreateWaveformI16(self, vi, channel_name, waveform_size, waveform_data_array, waveform_handle):  # noqa: N802
        if self._defaults['CreateWaveformI16']['return'] != 0:
            return self._defaults['CreateWaveformI16']['return']
        # waveform_handle
        if self._defaults['CreateWaveformI16']['waveformHandle'] is None:
            raise MockFunctionCallError("niFgen_CreateWaveformI16", param='waveformHandle')
        if waveform_handle is not None:
            waveform_handle.contents.value = self._defaults['CreateWaveformI16']['waveformHandle']
        return self._defaults['CreateWaveformI16']['return']

    def niFgen_DefineUserStandardWaveform(self, vi, channel_name, waveform_size, waveform_data_array):  # noqa: N802
        if self._defaults['DefineUserStandardWaveform']['return'] != 0:
            return self._defaults['DefineUserStandardWaveform']['return']
        return self._defaults['DefineUserStandardWaveform']['return']

    def niFgen_DeleteNamedWaveform(self, vi, channel_name, waveform_name):  # noqa: N802
        if self._defaults['DeleteNamedWaveform']['return'] != 0:
            return self._defaults['DeleteNamedWaveform']['return']
        return self._defaults['DeleteNamedWaveform']['return']

    def niFgen_DeleteScript(self, vi, channel_name, script_name):  # noqa: N802
        if self._defaults['DeleteScript']['return'] != 0:
            return self._defaults['DeleteScript']['return']
        return self._defaults['DeleteScript']['return']

    def niFgen_Disable(self, vi):  # noqa: N802
        if self._defaults['Disable']['return'] != 0:
            return self._defaults['Disable']['return']
        return self._defaults['Disable']['return']

    def niFgen_ExportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationBuffer']['return']
        # configuration
        if self._defaults['ExportAttributeConfigurationBuffer']['configuration'] is None:
            raise MockFunctionCallError("niFgen_ExportAttributeConfigurationBuffer", param='configuration')
        if size_in_bytes.value == 0:
            return len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])
        try:
            configuration_ref = configuration.contents
        except AttributeError:
            configuration_ref = configuration
        for i in range(len(self._defaults['ExportAttributeConfigurationBuffer']['configuration'])):
            configuration_ref[i] = self._defaults['ExportAttributeConfigurationBuffer']['configuration'][i]
        return self._defaults['ExportAttributeConfigurationBuffer']['return']

    def niFgen_ExportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ExportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ExportAttributeConfigurationFile']['return']
        return self._defaults['ExportAttributeConfigurationFile']['return']

    def niFgen_GetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViBoolean']['return'] != 0:
            return self._defaults['GetAttributeViBoolean']['return']
        # attribute_value
        if self._defaults['GetAttributeViBoolean']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViBoolean", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViBoolean']['attributeValue']
        return self._defaults['GetAttributeViBoolean']['return']

    def niFgen_GetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViInt32']['return'] != 0:
            return self._defaults['GetAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViInt32']['attributeValue']
        return self._defaults['GetAttributeViInt32']['return']

    def niFgen_GetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViReal64']['return'] != 0:
            return self._defaults['GetAttributeViReal64']['return']
        # attribute_value
        if self._defaults['GetAttributeViReal64']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViReal64", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetAttributeViReal64']['attributeValue']
        return self._defaults['GetAttributeViReal64']['return']

    def niFgen_GetAttributeViString(self, vi, channel_name, attribute_id, array_size, attribute_value):  # noqa: N802
        if self._defaults['GetAttributeViString']['return'] != 0:
            return self._defaults['GetAttributeViString']['return']
        # attribute_value
        if self._defaults['GetAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niFgen_GetAttributeViString", param='attributeValue')
        if array_size.value == 0:
            return len(self._defaults['GetAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetAttributeViString']['return']

    def niFgen_GetChannelName(self, vi, index, buffer_size, channel_string):  # noqa: N802
        if self._defaults['GetChannelName']['return'] != 0:
            return self._defaults['GetChannelName']['return']
        # channel_string
        if self._defaults['GetChannelName']['channelString'] is None:
            raise MockFunctionCallError("niFgen_GetChannelName", param='channelString')
        if buffer_size.value == 0:
            return len(self._defaults['GetChannelName']['channelString'])
        channel_string.value = self._defaults['GetChannelName']['channelString'].encode('ascii')
        return self._defaults['GetChannelName']['return']

    def niFgen_GetError(self, vi, error_code, error_description_buffer_size, error_description):  # noqa: N802
        if self._defaults['GetError']['return'] != 0:
            return self._defaults['GetError']['return']
        # error_code
        if self._defaults['GetError']['errorCode'] is None:
            raise MockFunctionCallError("niFgen_GetError", param='errorCode')
        if error_code is not None:
            error_code.contents.value = self._defaults['GetError']['errorCode']
        # error_description
        if self._defaults['GetError']['errorDescription'] is None:
            raise MockFunctionCallError("niFgen_GetError", param='errorDescription')
        if error_description_buffer_size.value == 0:
            return len(self._defaults['GetError']['errorDescription'])
        error_description.value = self._defaults['GetError']['errorDescription'].encode('ascii')
        return self._defaults['GetError']['return']

    def niFgen_GetExtCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetExtCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetExtCalLastDateAndTime']['return']
        # year
        if self._defaults['GetExtCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetExtCalLastDateAndTime']['year']
        # month
        if self._defaults['GetExtCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetExtCalLastDateAndTime']['month']
        # day
        if self._defaults['GetExtCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetExtCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetExtCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetExtCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetExtCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetExtCalLastDateAndTime']['minute']
        return self._defaults['GetExtCalLastDateAndTime']['return']

    def niFgen_GetExtCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetExtCalLastTemp']['return'] != 0:
            return self._defaults['GetExtCalLastTemp']['return']
        # temperature
        if self._defaults['GetExtCalLastTemp']['temperature'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalLastTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetExtCalLastTemp']['temperature']
        return self._defaults['GetExtCalLastTemp']['return']

    def niFgen_GetExtCalRecommendedInterval(self, vi, months):  # noqa: N802
        if self._defaults['GetExtCalRecommendedInterval']['return'] != 0:
            return self._defaults['GetExtCalRecommendedInterval']['return']
        # months
        if self._defaults['GetExtCalRecommendedInterval']['months'] is None:
            raise MockFunctionCallError("niFgen_GetExtCalRecommendedInterval", param='months')
        if months is not None:
            months.contents.value = self._defaults['GetExtCalRecommendedInterval']['months']
        return self._defaults['GetExtCalRecommendedInterval']['return']

    def niFgen_GetHardwareState(self, vi, state):  # noqa: N802
        if self._defaults['GetHardwareState']['return'] != 0:
            return self._defaults['GetHardwareState']['return']
        # state
        if self._defaults['GetHardwareState']['state'] is None:
            raise MockFunctionCallError("niFgen_GetHardwareState", param='state')
        if state is not None:
            state.contents.value = self._defaults['GetHardwareState']['state']
        return self._defaults['GetHardwareState']['return']

    def niFgen_GetSelfCalLastDateAndTime(self, vi, year, month, day, hour, minute):  # noqa: N802
        if self._defaults['GetSelfCalLastDateAndTime']['return'] != 0:
            return self._defaults['GetSelfCalLastDateAndTime']['return']
        # year
        if self._defaults['GetSelfCalLastDateAndTime']['year'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='year')
        if year is not None:
            year.contents.value = self._defaults['GetSelfCalLastDateAndTime']['year']
        # month
        if self._defaults['GetSelfCalLastDateAndTime']['month'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='month')
        if month is not None:
            month.contents.value = self._defaults['GetSelfCalLastDateAndTime']['month']
        # day
        if self._defaults['GetSelfCalLastDateAndTime']['day'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='day')
        if day is not None:
            day.contents.value = self._defaults['GetSelfCalLastDateAndTime']['day']
        # hour
        if self._defaults['GetSelfCalLastDateAndTime']['hour'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='hour')
        if hour is not None:
            hour.contents.value = self._defaults['GetSelfCalLastDateAndTime']['hour']
        # minute
        if self._defaults['GetSelfCalLastDateAndTime']['minute'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime", param='minute')
        if minute is not None:
            minute.contents.value = self._defaults['GetSelfCalLastDateAndTime']['minute']
        return self._defaults['GetSelfCalLastDateAndTime']['return']

    def niFgen_GetSelfCalLastTemp(self, vi, temperature):  # noqa: N802
        if self._defaults['GetSelfCalLastTemp']['return'] != 0:
            return self._defaults['GetSelfCalLastTemp']['return']
        # temperature
        if self._defaults['GetSelfCalLastTemp']['temperature'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalLastTemp", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['GetSelfCalLastTemp']['temperature']
        return self._defaults['GetSelfCalLastTemp']['return']

    def niFgen_GetSelfCalSupported(self, vi, self_cal_supported):  # noqa: N802
        if self._defaults['GetSelfCalSupported']['return'] != 0:
            return self._defaults['GetSelfCalSupported']['return']
        # self_cal_supported
        if self._defaults['GetSelfCalSupported']['selfCalSupported'] is None:
            raise MockFunctionCallError("niFgen_GetSelfCalSupported", param='selfCalSupported')
        if self_cal_supported is not None:
            self_cal_supported.contents.value = self._defaults['GetSelfCalSupported']['selfCalSupported']
        return self._defaults['GetSelfCalSupported']['return']

    def niFgen_ImportAttributeConfigurationBuffer(self, vi, size_in_bytes, configuration):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationBuffer']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationBuffer']['return']
        return self._defaults['ImportAttributeConfigurationBuffer']['return']

    def niFgen_ImportAttributeConfigurationFile(self, vi, file_path):  # noqa: N802
        if self._defaults['ImportAttributeConfigurationFile']['return'] != 0:
            return self._defaults['ImportAttributeConfigurationFile']['return']
        return self._defaults['ImportAttributeConfigurationFile']['return']

    def niFgen_InitializeWithChannels(self, resource_name, channel_name, reset_device, option_string, vi):  # noqa: N802
        if self._defaults['InitializeWithChannels']['return'] != 0:
            return self._defaults['InitializeWithChannels']['return']
        # vi
        if self._defaults['InitializeWithChannels']['vi'] is None:
            raise MockFunctionCallError("niFgen_InitializeWithChannels", param='vi')
        if vi is not None:
            vi.contents.value = self._defaults['InitializeWithChannels']['vi']
        return self._defaults['InitializeWithChannels']['return']

    def niFgen_InitiateGeneration(self, vi):  # noqa: N802
        if self._defaults['InitiateGeneration']['return'] != 0:
            return self._defaults['InitiateGeneration']['return']
        return self._defaults['InitiateGeneration']['return']

    def niFgen_IsDone(self, vi, done):  # noqa: N802
        if self._defaults['IsDone']['return'] != 0:
            return self._defaults['IsDone']['return']
        # done
        if self._defaults['IsDone']['done'] is None:
            raise MockFunctionCallError("niFgen_IsDone", param='done')
        if done is not None:
            done.contents.value = self._defaults['IsDone']['done']
        return self._defaults['IsDone']['return']

    def niFgen_LockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['LockSession']['return'] != 0:
            return self._defaults['LockSession']['return']
        # caller_has_lock
        if self._defaults['LockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niFgen_LockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['LockSession']['callerHasLock']
        return self._defaults['LockSession']['return']

    def niFgen_QueryArbSeqCapabilities(self, vi, maximum_number_of_sequences, minimum_sequence_length, maximum_sequence_length, maximum_loop_count):  # noqa: N802
        if self._defaults['QueryArbSeqCapabilities']['return'] != 0:
            return self._defaults['QueryArbSeqCapabilities']['return']
        # maximum_number_of_sequences
        if self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumNumberOfSequences')
        if maximum_number_of_sequences is not None:
            maximum_number_of_sequences.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumNumberOfSequences']
        # minimum_sequence_length
        if self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='minimumSequenceLength')
        if minimum_sequence_length is not None:
            minimum_sequence_length.contents.value = self._defaults['QueryArbSeqCapabilities']['minimumSequenceLength']
        # maximum_sequence_length
        if self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumSequenceLength')
        if maximum_sequence_length is not None:
            maximum_sequence_length.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumSequenceLength']
        # maximum_loop_count
        if self._defaults['QueryArbSeqCapabilities']['maximumLoopCount'] is None:
            raise MockFunctionCallError("niFgen_QueryArbSeqCapabilities", param='maximumLoopCount')
        if maximum_loop_count is not None:
            maximum_loop_count.contents.value = self._defaults['QueryArbSeqCapabilities']['maximumLoopCount']
        return self._defaults['QueryArbSeqCapabilities']['return']

    def niFgen_QueryArbWfmCapabilities(self, vi, maximum_number_of_waveforms, waveform_quantum, minimum_waveform_size, maximum_waveform_size):  # noqa: N802
        if self._defaults['QueryArbWfmCapabilities']['return'] != 0:
            return self._defaults['QueryArbWfmCapabilities']['return']
        # maximum_number_of_waveforms
        if self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='maximumNumberOfWaveforms')
        if maximum_number_of_waveforms is not None:
            maximum_number_of_waveforms.contents.value = self._defaults['QueryArbWfmCapabilities']['maximumNumberOfWaveforms']
        # waveform_quantum
        if self._defaults['QueryArbWfmCapabilities']['waveformQuantum'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='waveformQuantum')
        if waveform_quantum is not None:
            waveform_quantum.contents.value = self._defaults['QueryArbWfmCapabilities']['waveformQuantum']
        # minimum_waveform_size
        if self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='minimumWaveformSize')
        if minimum_waveform_size is not None:
            minimum_waveform_size.contents.value = self._defaults['QueryArbWfmCapabilities']['minimumWaveformSize']
        # maximum_waveform_size
        if self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize'] is None:
            raise MockFunctionCallError("niFgen_QueryArbWfmCapabilities", param='maximumWaveformSize')
        if maximum_waveform_size is not None:
            maximum_waveform_size.contents.value = self._defaults['QueryArbWfmCapabilities']['maximumWaveformSize']
        return self._defaults['QueryArbWfmCapabilities']['return']

    def niFgen_QueryFreqListCapabilities(self, vi, maximum_number_of_freq_lists, minimum_frequency_list_length, maximum_frequency_list_length, minimum_frequency_list_duration, maximum_frequency_list_duration, frequency_list_duration_quantum):  # noqa: N802
        if self._defaults['QueryFreqListCapabilities']['return'] != 0:
            return self._defaults['QueryFreqListCapabilities']['return']
        # maximum_number_of_freq_lists
        if self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumNumberOfFreqLists')
        if maximum_number_of_freq_lists is not None:
            maximum_number_of_freq_lists.contents.value = self._defaults['QueryFreqListCapabilities']['maximumNumberOfFreqLists']
        # minimum_frequency_list_length
        if self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='minimumFrequencyListLength')
        if minimum_frequency_list_length is not None:
            minimum_frequency_list_length.contents.value = self._defaults['QueryFreqListCapabilities']['minimumFrequencyListLength']
        # maximum_frequency_list_length
        if self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumFrequencyListLength')
        if maximum_frequency_list_length is not None:
            maximum_frequency_list_length.contents.value = self._defaults['QueryFreqListCapabilities']['maximumFrequencyListLength']
        # minimum_frequency_list_duration
        if self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='minimumFrequencyListDuration')
        if minimum_frequency_list_duration is not None:
            minimum_frequency_list_duration.contents.value = self._defaults['QueryFreqListCapabilities']['minimumFrequencyListDuration']
        # maximum_frequency_list_duration
        if self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='maximumFrequencyListDuration')
        if maximum_frequency_list_duration is not None:
            maximum_frequency_list_duration.contents.value = self._defaults['QueryFreqListCapabilities']['maximumFrequencyListDuration']
        # frequency_list_duration_quantum
        if self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum'] is None:
            raise MockFunctionCallError("niFgen_QueryFreqListCapabilities", param='frequencyListDurationQuantum')
        if frequency_list_duration_quantum is not None:
            frequency_list_duration_quantum.contents.value = self._defaults['QueryFreqListCapabilities']['frequencyListDurationQuantum']
        return self._defaults['QueryFreqListCapabilities']['return']

    def niFgen_ReadCurrentTemperature(self, vi, temperature):  # noqa: N802
        if self._defaults['ReadCurrentTemperature']['return'] != 0:
            return self._defaults['ReadCurrentTemperature']['return']
        # temperature
        if self._defaults['ReadCurrentTemperature']['temperature'] is None:
            raise MockFunctionCallError("niFgen_ReadCurrentTemperature", param='temperature')
        if temperature is not None:
            temperature.contents.value = self._defaults['ReadCurrentTemperature']['temperature']
        return self._defaults['ReadCurrentTemperature']['return']

    def niFgen_ResetDevice(self, vi):  # noqa: N802
        if self._defaults['ResetDevice']['return'] != 0:
            return self._defaults['ResetDevice']['return']
        return self._defaults['ResetDevice']['return']

    def niFgen_ResetWithDefaults(self, vi):  # noqa: N802
        if self._defaults['ResetWithDefaults']['return'] != 0:
            return self._defaults['ResetWithDefaults']['return']
        return self._defaults['ResetWithDefaults']['return']

    def niFgen_SelfCal(self, vi):  # noqa: N802
        if self._defaults['SelfCal']['return'] != 0:
            return self._defaults['SelfCal']['return']
        return self._defaults['SelfCal']['return']

    def niFgen_SendSoftwareEdgeTrigger(self, vi, trigger, trigger_id):  # noqa: N802
        if self._defaults['SendSoftwareEdgeTrigger']['return'] != 0:
            return self._defaults['SendSoftwareEdgeTrigger']['return']
        return self._defaults['SendSoftwareEdgeTrigger']['return']

    def niFgen_SetAttributeViBoolean(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViBoolean']['return'] != 0:
            return self._defaults['SetAttributeViBoolean']['return']
        return self._defaults['SetAttributeViBoolean']['return']

    def niFgen_SetAttributeViInt32(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViInt32']['return'] != 0:
            return self._defaults['SetAttributeViInt32']['return']
        return self._defaults['SetAttributeViInt32']['return']

    def niFgen_SetAttributeViReal64(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViReal64']['return'] != 0:
            return self._defaults['SetAttributeViReal64']['return']
        return self._defaults['SetAttributeViReal64']['return']

    def niFgen_SetAttributeViString(self, vi, channel_name, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['SetAttributeViString']['return'] != 0:
            return self._defaults['SetAttributeViString']['return']
        return self._defaults['SetAttributeViString']['return']

    def niFgen_SetNamedWaveformNextWritePosition(self, vi, channel_name, waveform_name, relative_to, offset):  # noqa: N802
        if self._defaults['SetNamedWaveformNextWritePosition']['return'] != 0:
            return self._defaults['SetNamedWaveformNextWritePosition']['return']
        return self._defaults['SetNamedWaveformNextWritePosition']['return']

    def niFgen_SetRuntimeEnvironment(self, environment, environment_version, reserved1, reserved2):  # noqa: N802
        if self._defaults['SetRuntimeEnvironment']['return'] != 0:
            return self._defaults['SetRuntimeEnvironment']['return']
        return self._defaults['SetRuntimeEnvironment']['return']

    def niFgen_SetWaveformNextWritePosition(self, vi, channel_name, waveform_handle, relative_to, offset):  # noqa: N802
        if self._defaults['SetWaveformNextWritePosition']['return'] != 0:
            return self._defaults['SetWaveformNextWritePosition']['return']
        return self._defaults['SetWaveformNextWritePosition']['return']

    def niFgen_UnlockSession(self, vi, caller_has_lock):  # noqa: N802
        if self._defaults['UnlockSession']['return'] != 0:
            return self._defaults['UnlockSession']['return']
        # caller_has_lock
        if self._defaults['UnlockSession']['callerHasLock'] is None:
            raise MockFunctionCallError("niFgen_UnlockSession", param='callerHasLock')
        if caller_has_lock is not None:
            caller_has_lock.contents.value = self._defaults['UnlockSession']['callerHasLock']
        return self._defaults['UnlockSession']['return']

    def niFgen_WaitUntilDone(self, vi, max_time):  # noqa: N802
        if self._defaults['WaitUntilDone']['return'] != 0:
            return self._defaults['WaitUntilDone']['return']
        return self._defaults['WaitUntilDone']['return']

    def niFgen_WriteBinary16Waveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        if self._defaults['WriteBinary16Waveform']['return'] != 0:
            return self._defaults['WriteBinary16Waveform']['return']
        return self._defaults['WriteBinary16Waveform']['return']

    def niFgen_WriteNamedWaveformF64(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        if self._defaults['WriteNamedWaveformF64']['return'] != 0:
            return self._defaults['WriteNamedWaveformF64']['return']
        return self._defaults['WriteNamedWaveformF64']['return']

    def niFgen_WriteNamedWaveformI16(self, vi, channel_name, waveform_name, size, data):  # noqa: N802
        if self._defaults['WriteNamedWaveformI16']['return'] != 0:
            return self._defaults['WriteNamedWaveformI16']['return']
        return self._defaults['WriteNamedWaveformI16']['return']

    def niFgen_WriteScript(self, vi, channel_name, script):  # noqa: N802
        if self._defaults['WriteScript']['return'] != 0:
            return self._defaults['WriteScript']['return']
        return self._defaults['WriteScript']['return']

    def niFgen_WriteWaveform(self, vi, channel_name, waveform_handle, size, data):  # noqa: N802
        if self._defaults['WriteWaveform']['return'] != 0:
            return self._defaults['WriteWaveform']['return']
        return self._defaults['WriteWaveform']['return']

    def niFgen_close(self, vi):  # noqa: N802
        if self._defaults['close']['return'] != 0:
            return self._defaults['close']['return']
        return self._defaults['close']['return']

    def niFgen_error_message(self, vi, error_code, error_message):  # noqa: N802
        if self._defaults['error_message']['return'] != 0:
            return self._defaults['error_message']['return']
        # error_message
        if self._defaults['error_message']['errorMessage'] is None:
            raise MockFunctionCallError("niFgen_error_message", param='errorMessage')
        test_value = self._defaults['error_message']['errorMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(error_message) >= len(test_value)
        for i in range(len(test_value)):
            error_message[i] = test_value[i]
        return self._defaults['error_message']['return']

    def niFgen_reset(self, vi):  # noqa: N802
        if self._defaults['reset']['return'] != 0:
            return self._defaults['reset']['return']
        return self._defaults['reset']['return']

    def niFgen_self_test(self, vi, self_test_result, self_test_message):  # noqa: N802
        if self._defaults['self_test']['return'] != 0:
            return self._defaults['self_test']['return']
        # self_test_result
        if self._defaults['self_test']['selfTestResult'] is None:
            raise MockFunctionCallError("niFgen_self_test", param='selfTestResult')
        if self_test_result is not None:
            self_test_result.contents.value = self._defaults['self_test']['selfTestResult']
        # self_test_message
        if self._defaults['self_test']['selfTestMessage'] is None:
            raise MockFunctionCallError("niFgen_self_test", param='selfTestMessage')
        test_value = self._defaults['self_test']['selfTestMessage']
        if type(test_value) is str:
            test_value = test_value.encode('ascii')
        assert len(self_test_message) >= len(test_value)
        for i in range(len(test_value)):
            self_test_message[i] = test_value[i]
        return self._defaults['self_test']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niFgen_AbortGeneration.side_effect = MockFunctionCallError("niFgen_AbortGeneration")
        mock_library.niFgen_AbortGeneration.return_value = 0
        mock_library.niFgen_AllocateNamedWaveform.side_effect = MockFunctionCallError("niFgen_AllocateNamedWaveform")
        mock_library.niFgen_AllocateNamedWaveform.return_value = 0
        mock_library.niFgen_AllocateWaveform.side_effect = MockFunctionCallError("niFgen_AllocateWaveform")
        mock_library.niFgen_AllocateWaveform.return_value = 0
        mock_library.niFgen_ClearArbMemory.side_effect = MockFunctionCallError("niFgen_ClearArbMemory")
        mock_library.niFgen_ClearArbMemory.return_value = 0
        mock_library.niFgen_ClearArbSequence.side_effect = MockFunctionCallError("niFgen_ClearArbSequence")
        mock_library.niFgen_ClearArbSequence.return_value = 0
        mock_library.niFgen_ClearArbWaveform.side_effect = MockFunctionCallError("niFgen_ClearArbWaveform")
        mock_library.niFgen_ClearArbWaveform.return_value = 0
        mock_library.niFgen_ClearFreqList.side_effect = MockFunctionCallError("niFgen_ClearFreqList")
        mock_library.niFgen_ClearFreqList.return_value = 0
        mock_library.niFgen_ClearUserStandardWaveform.side_effect = MockFunctionCallError("niFgen_ClearUserStandardWaveform")
        mock_library.niFgen_ClearUserStandardWaveform.return_value = 0
        mock_library.niFgen_Commit.side_effect = MockFunctionCallError("niFgen_Commit")
        mock_library.niFgen_Commit.return_value = 0
        mock_library.niFgen_ConfigureArbSequence.side_effect = MockFunctionCallError("niFgen_ConfigureArbSequence")
        mock_library.niFgen_ConfigureArbSequence.return_value = 0
        mock_library.niFgen_ConfigureArbWaveform.side_effect = MockFunctionCallError("niFgen_ConfigureArbWaveform")
        mock_library.niFgen_ConfigureArbWaveform.return_value = 0
        mock_library.niFgen_ConfigureFreqList.side_effect = MockFunctionCallError("niFgen_ConfigureFreqList")
        mock_library.niFgen_ConfigureFreqList.return_value = 0
        mock_library.niFgen_ConfigureStandardWaveform.side_effect = MockFunctionCallError("niFgen_ConfigureStandardWaveform")
        mock_library.niFgen_ConfigureStandardWaveform.return_value = 0
        mock_library.niFgen_CreateAdvancedArbSequence.side_effect = MockFunctionCallError("niFgen_CreateAdvancedArbSequence")
        mock_library.niFgen_CreateAdvancedArbSequence.return_value = 0
        mock_library.niFgen_CreateArbSequence.side_effect = MockFunctionCallError("niFgen_CreateArbSequence")
        mock_library.niFgen_CreateArbSequence.return_value = 0
        mock_library.niFgen_CreateFreqList.side_effect = MockFunctionCallError("niFgen_CreateFreqList")
        mock_library.niFgen_CreateFreqList.return_value = 0
        mock_library.niFgen_CreateWaveformF64.side_effect = MockFunctionCallError("niFgen_CreateWaveformF64")
        mock_library.niFgen_CreateWaveformF64.return_value = 0
        mock_library.niFgen_CreateWaveformFromFileF64.side_effect = MockFunctionCallError("niFgen_CreateWaveformFromFileF64")
        mock_library.niFgen_CreateWaveformFromFileF64.return_value = 0
        mock_library.niFgen_CreateWaveformFromFileI16.side_effect = MockFunctionCallError("niFgen_CreateWaveformFromFileI16")
        mock_library.niFgen_CreateWaveformFromFileI16.return_value = 0
        mock_library.niFgen_CreateWaveformI16.side_effect = MockFunctionCallError("niFgen_CreateWaveformI16")
        mock_library.niFgen_CreateWaveformI16.return_value = 0
        mock_library.niFgen_DefineUserStandardWaveform.side_effect = MockFunctionCallError("niFgen_DefineUserStandardWaveform")
        mock_library.niFgen_DefineUserStandardWaveform.return_value = 0
        mock_library.niFgen_DeleteNamedWaveform.side_effect = MockFunctionCallError("niFgen_DeleteNamedWaveform")
        mock_library.niFgen_DeleteNamedWaveform.return_value = 0
        mock_library.niFgen_DeleteScript.side_effect = MockFunctionCallError("niFgen_DeleteScript")
        mock_library.niFgen_DeleteScript.return_value = 0
        mock_library.niFgen_Disable.side_effect = MockFunctionCallError("niFgen_Disable")
        mock_library.niFgen_Disable.return_value = 0
        mock_library.niFgen_ExportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niFgen_ExportAttributeConfigurationBuffer")
        mock_library.niFgen_ExportAttributeConfigurationBuffer.return_value = 0
        mock_library.niFgen_ExportAttributeConfigurationFile.side_effect = MockFunctionCallError("niFgen_ExportAttributeConfigurationFile")
        mock_library.niFgen_ExportAttributeConfigurationFile.return_value = 0
        mock_library.niFgen_GetAttributeViBoolean.side_effect = MockFunctionCallError("niFgen_GetAttributeViBoolean")
        mock_library.niFgen_GetAttributeViBoolean.return_value = 0
        mock_library.niFgen_GetAttributeViInt32.side_effect = MockFunctionCallError("niFgen_GetAttributeViInt32")
        mock_library.niFgen_GetAttributeViInt32.return_value = 0
        mock_library.niFgen_GetAttributeViReal64.side_effect = MockFunctionCallError("niFgen_GetAttributeViReal64")
        mock_library.niFgen_GetAttributeViReal64.return_value = 0
        mock_library.niFgen_GetAttributeViString.side_effect = MockFunctionCallError("niFgen_GetAttributeViString")
        mock_library.niFgen_GetAttributeViString.return_value = 0
        mock_library.niFgen_GetChannelName.side_effect = MockFunctionCallError("niFgen_GetChannelName")
        mock_library.niFgen_GetChannelName.return_value = 0
        mock_library.niFgen_GetError.side_effect = MockFunctionCallError("niFgen_GetError")
        mock_library.niFgen_GetError.return_value = 0
        mock_library.niFgen_GetExtCalLastDateAndTime.side_effect = MockFunctionCallError("niFgen_GetExtCalLastDateAndTime")
        mock_library.niFgen_GetExtCalLastDateAndTime.return_value = 0
        mock_library.niFgen_GetExtCalLastTemp.side_effect = MockFunctionCallError("niFgen_GetExtCalLastTemp")
        mock_library.niFgen_GetExtCalLastTemp.return_value = 0
        mock_library.niFgen_GetExtCalRecommendedInterval.side_effect = MockFunctionCallError("niFgen_GetExtCalRecommendedInterval")
        mock_library.niFgen_GetExtCalRecommendedInterval.return_value = 0
        mock_library.niFgen_GetHardwareState.side_effect = MockFunctionCallError("niFgen_GetHardwareState")
        mock_library.niFgen_GetHardwareState.return_value = 0
        mock_library.niFgen_GetSelfCalLastDateAndTime.side_effect = MockFunctionCallError("niFgen_GetSelfCalLastDateAndTime")
        mock_library.niFgen_GetSelfCalLastDateAndTime.return_value = 0
        mock_library.niFgen_GetSelfCalLastTemp.side_effect = MockFunctionCallError("niFgen_GetSelfCalLastTemp")
        mock_library.niFgen_GetSelfCalLastTemp.return_value = 0
        mock_library.niFgen_GetSelfCalSupported.side_effect = MockFunctionCallError("niFgen_GetSelfCalSupported")
        mock_library.niFgen_GetSelfCalSupported.return_value = 0
        mock_library.niFgen_ImportAttributeConfigurationBuffer.side_effect = MockFunctionCallError("niFgen_ImportAttributeConfigurationBuffer")
        mock_library.niFgen_ImportAttributeConfigurationBuffer.return_value = 0
        mock_library.niFgen_ImportAttributeConfigurationFile.side_effect = MockFunctionCallError("niFgen_ImportAttributeConfigurationFile")
        mock_library.niFgen_ImportAttributeConfigurationFile.return_value = 0
        mock_library.niFgen_InitializeWithChannels.side_effect = MockFunctionCallError("niFgen_InitializeWithChannels")
        mock_library.niFgen_InitializeWithChannels.return_value = 0
        mock_library.niFgen_InitiateGeneration.side_effect = MockFunctionCallError("niFgen_InitiateGeneration")
        mock_library.niFgen_InitiateGeneration.return_value = 0
        mock_library.niFgen_IsDone.side_effect = MockFunctionCallError("niFgen_IsDone")
        mock_library.niFgen_IsDone.return_value = 0
        mock_library.niFgen_LockSession.side_effect = MockFunctionCallError("niFgen_LockSession")
        mock_library.niFgen_LockSession.return_value = 0
        mock_library.niFgen_QueryArbSeqCapabilities.side_effect = MockFunctionCallError("niFgen_QueryArbSeqCapabilities")
        mock_library.niFgen_QueryArbSeqCapabilities.return_value = 0
        mock_library.niFgen_QueryArbWfmCapabilities.side_effect = MockFunctionCallError("niFgen_QueryArbWfmCapabilities")
        mock_library.niFgen_QueryArbWfmCapabilities.return_value = 0
        mock_library.niFgen_QueryFreqListCapabilities.side_effect = MockFunctionCallError("niFgen_QueryFreqListCapabilities")
        mock_library.niFgen_QueryFreqListCapabilities.return_value = 0
        mock_library.niFgen_ReadCurrentTemperature.side_effect = MockFunctionCallError("niFgen_ReadCurrentTemperature")
        mock_library.niFgen_ReadCurrentTemperature.return_value = 0
        mock_library.niFgen_ResetDevice.side_effect = MockFunctionCallError("niFgen_ResetDevice")
        mock_library.niFgen_ResetDevice.return_value = 0
        mock_library.niFgen_ResetWithDefaults.side_effect = MockFunctionCallError("niFgen_ResetWithDefaults")
        mock_library.niFgen_ResetWithDefaults.return_value = 0
        mock_library.niFgen_SelfCal.side_effect = MockFunctionCallError("niFgen_SelfCal")
        mock_library.niFgen_SelfCal.return_value = 0
        mock_library.niFgen_SendSoftwareEdgeTrigger.side_effect = MockFunctionCallError("niFgen_SendSoftwareEdgeTrigger")
        mock_library.niFgen_SendSoftwareEdgeTrigger.return_value = 0
        mock_library.niFgen_SetAttributeViBoolean.side_effect = MockFunctionCallError("niFgen_SetAttributeViBoolean")
        mock_library.niFgen_SetAttributeViBoolean.return_value = 0
        mock_library.niFgen_SetAttributeViInt32.side_effect = MockFunctionCallError("niFgen_SetAttributeViInt32")
        mock_library.niFgen_SetAttributeViInt32.return_value = 0
        mock_library.niFgen_SetAttributeViReal64.side_effect = MockFunctionCallError("niFgen_SetAttributeViReal64")
        mock_library.niFgen_SetAttributeViReal64.return_value = 0
        mock_library.niFgen_SetAttributeViString.side_effect = MockFunctionCallError("niFgen_SetAttributeViString")
        mock_library.niFgen_SetAttributeViString.return_value = 0
        mock_library.niFgen_SetNamedWaveformNextWritePosition.side_effect = MockFunctionCallError("niFgen_SetNamedWaveformNextWritePosition")
        mock_library.niFgen_SetNamedWaveformNextWritePosition.return_value = 0
        mock_library.niFgen_SetRuntimeEnvironment.side_effect = MockFunctionCallError("niFgen_SetRuntimeEnvironment")
        mock_library.niFgen_SetRuntimeEnvironment.return_value = 0
        mock_library.niFgen_SetWaveformNextWritePosition.side_effect = MockFunctionCallError("niFgen_SetWaveformNextWritePosition")
        mock_library.niFgen_SetWaveformNextWritePosition.return_value = 0
        mock_library.niFgen_UnlockSession.side_effect = MockFunctionCallError("niFgen_UnlockSession")
        mock_library.niFgen_UnlockSession.return_value = 0
        mock_library.niFgen_WaitUntilDone.side_effect = MockFunctionCallError("niFgen_WaitUntilDone")
        mock_library.niFgen_WaitUntilDone.return_value = 0
        mock_library.niFgen_WriteBinary16Waveform.side_effect = MockFunctionCallError("niFgen_WriteBinary16Waveform")
        mock_library.niFgen_WriteBinary16Waveform.return_value = 0
        mock_library.niFgen_WriteNamedWaveformF64.side_effect = MockFunctionCallError("niFgen_WriteNamedWaveformF64")
        mock_library.niFgen_WriteNamedWaveformF64.return_value = 0
        mock_library.niFgen_WriteNamedWaveformI16.side_effect = MockFunctionCallError("niFgen_WriteNamedWaveformI16")
        mock_library.niFgen_WriteNamedWaveformI16.return_value = 0
        mock_library.niFgen_WriteScript.side_effect = MockFunctionCallError("niFgen_WriteScript")
        mock_library.niFgen_WriteScript.return_value = 0
        mock_library.niFgen_WriteWaveform.side_effect = MockFunctionCallError("niFgen_WriteWaveform")
        mock_library.niFgen_WriteWaveform.return_value = 0
        mock_library.niFgen_close.side_effect = MockFunctionCallError("niFgen_close")
        mock_library.niFgen_close.return_value = 0
        mock_library.niFgen_error_message.side_effect = MockFunctionCallError("niFgen_error_message")
        mock_library.niFgen_error_message.return_value = 0
        mock_library.niFgen_reset.side_effect = MockFunctionCallError("niFgen_reset")
        mock_library.niFgen_reset.return_value = 0
        mock_library.niFgen_self_test.side_effect = MockFunctionCallError("niFgen_self_test")
        mock_library.niFgen_self_test.return_value = 0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/nifgen/VERSION sha256=5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d bytes=13 -->
## FILE: generated/nifgen/nifgen/VERSION

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/nifgen/VERSION`
- sha256: `5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d`
- bytes: 13

````text
1.4.10.dev0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/README.rst sha256=0c22757ae1973b84a52c9ba9ed7a94fd0c60d9f536ffc1477e77de581bf8e138 bytes=6971 -->
## FILE: generated/nifgen/README.rst

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/README.rst`
- sha256: `0c22757ae1973b84a52c9ba9ed7a94fd0c60d9f536ffc1477e77de581bf8e138`
- bytes: 6971

````rst
Overall Status
--------------

+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| master branch status | |BuildStatus| |MITLicense| |CoverageStatus|                                                                                        |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+
| GitHub status        | |OpenIssues| |OpenPullRequests|                                                                                                    |
+----------------------+------------------------------------------------------------------------------------------------------------------------------------+

===========  ============================================================================================================================
Info         NI Modular Instrument driver APIs for Python.
Author       NI
===========  ============================================================================================================================

.. |BuildStatus| image:: https://api.travis-ci.com/ni/nimi-python.svg
    :alt: Build Status - master branch
    :target: https://travis-ci.org/ni/nimi-python

.. |MITLicense| image:: https://img.shields.io/badge/License-MIT-yellow.svg
    :alt: MIT License
    :target: https://opensource.org/licenses/MIT

.. |CoverageStatus| image:: https://codecov.io/github/ni/nimi-python/graph/badge.svg
    :alt: Test Coverage - master branch
    :target: https://codecov.io/github/ni/nimi-python

.. |OpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python.svg
    :alt: Open Issues + Pull Requests
    :target: https://github.com/ni/nimi-python/issues

.. |OpenPullRequests| image:: https://img.shields.io/github/issues-pr/ni/nimi-python.svg
    :alt: Open Pull Requests
    :target: https://github.com/ni/nimi-python/pulls


.. _about-section:

About
=====

The **nifgen** module provides a Python API for NI-FGEN. The code is maintained in the Open Source repository for `nimi-python <https://github.com/ni/nimi-python>`_.

Support Policy
--------------
**nifgen** supports all the Operating Systems supported by NI-FGEN.

It follows `Python Software Foundation <https://devguide.python.org/#status-of-python-branches>`_ support policy for different versions of CPython.

NI created and supports **nifgen**.


NI-FGEN Python API Status
-------------------------

+-------------------------------+-----------------------+
| NI-FGEN (nifgen)              |                       |
+===============================+=======================+
| Driver Version Tested Against | 2025 Q4               |
+-------------------------------+-----------------------+
| PyPI Version                  | |nifgenLatestVersion| |
+-------------------------------+-----------------------+
| Supported Python Version      | |nifgenPythonVersion| |
+-------------------------------+-----------------------+
| Documentation                 | |nifgenDocs|          |
+-------------------------------+-----------------------+
| Open Issues                   | |nifgenOpenIssues|    |
+-------------------------------+-----------------------+
| Open Pull Requests            | |nifgenOpenPRs|       |
+-------------------------------+-----------------------+


.. |nifgenLatestVersion| image:: http://img.shields.io/pypi/v/nifgen.svg
    :alt: Latest NI-FGEN Version
    :target: http://pypi.python.org/pypi/nifgen


.. |nifgenPythonVersion| image:: http://img.shields.io/pypi/pyversions/nifgen.svg
    :alt: NI-FGEN supported Python versions
    :target: http://pypi.python.org/pypi/nifgen


.. |nifgenDocs| image:: https://readthedocs.org/projects/nifgen/badge/?version=latest
    :alt: NI-FGEN Python API Documentation Status
    :target: https://nifgen.readthedocs.io/en/latest


.. |nifgenOpenIssues| image:: https://img.shields.io/github/issues/ni/nimi-python/nifgen.svg
    :alt: Open Issues + Pull Requests for NI-FGEN
    :target: https://github.com/ni/nimi-python/issues?q=is%3Aopen+is%3Aissue+label%3Anifgen


.. |nifgenOpenPRs| image:: https://img.shields.io/github/issues-pr/ni/nimi-python/nifgen.svg
    :alt: Pull Requests for NI-FGEN
    :target: https://github.com/ni/nimi-python/pulls?q=is%3Aopen+is%3Aissue+label%3Anifgen



.. _nifgen_installation-section:

Installation
------------

As a prerequisite to using the **nifgen** module, you must install the NI-FGEN runtime on your system. Visit `ni.com/downloads <http://www.ni.com/downloads/>`_ to download the driver runtime for your devices.

The nimi-python modules (i.e. for **NI-FGEN**) can be installed with `pip <http://pypi.python.org/pypi/pip>`_::

  $ python -m pip install nifgen


Contributing
============

We welcome contributions! You can clone the project repository, build it, and install it by `following these instructions <https://github.com/ni/nimi-python/blob/master/CONTRIBUTING.md>`_.

Usage
------

The following is a basic example of using the **nifgen** module to open a session to a Function Generator and generate a sine wave for 5 seconds.

.. code-block:: python

    import nifgen
    import time
    with nifgen.Session("Dev1") as session:
        session.output_mode = nifgen.OutputMode.FUNC
        session.configure_standard_waveform(waveform=nifgen.Waveform.SINE, amplitude=1.0, frequency=10000000, dc_offset=0.0, start_phase=0.0)
        with session.initiate():
            time.sleep(5)

`Other usage examples can be found on GitHub. <https://github.com/ni/nimi-python/tree/master/src/nifgen/examples>`_

.. _support-section:

Support / Feedback
==================

For support specific to the Python API, follow the processs in `Bugs / Feature Requests`_.
For support with hardware, the driver runtime or any other questions not specific to the Python API, please visit `NI Community Forums <https://forums.ni.com/>`_.

.. _bugs-section:

Bugs / Feature Requests
=======================

To report a bug or submit a feature request specific to Python API, please use the
`GitHub issues page <https://github.com/ni/nimi-python/issues>`_.

Fill in the issue template as completely as possible and we will respond as soon
as we can.


.. _documentation-section:

Documentation
=============

Documentation is available `here <http://nifgen.readthedocs.io>`_.


.. _license-section:

License
=======

**nimi-python** is licensed under an MIT-style license (`see
LICENSE <https://github.com/ni/nimi-python/blob/master/LICENSE>`_).
Other incorporated projects may be licensed under different licenses. All
licenses allow for non-commercial and commercial use.


**gRPC Features**

For driver APIs that support it, passing a GrpcSessionOptions instance as a parameter to Session.__init__() is
subject to the NI General Purpose EULA (`see NILICENSE <https://github.com/ni/nimi-python/blob/master/NILICENSE>`_).
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/setup.py sha256=6ee113ecb39112e748f546220624ec4833b3aee5f6d49b13e668e2eeec606515 bytes=1824 -->
## FILE: generated/nifgen/setup.py

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/setup.py`
- sha256: `6ee113ecb39112e748f546220624ec4833b3aee5f6d49b13e668e2eeec606515`
- bytes: 1824

````python
#!/usr/bin/python
# This file was generated


from setuptools import setup


pypi_name = 'nifgen'


def read_contents(file_to_read):
    with open(file_to_read, 'r') as f:
        return f.read()


setup(
    name=pypi_name,
    zip_safe=True,
    version='1.4.10.dev0',
    description='NI-FGEN Python API',
    long_description=read_contents('README.rst'),
    long_description_content_type='text/x-rst',
    author='NI',
    author_email="opensource@ni.com",
    url="https://github.com/ni/nimi-python",
    maintainer="NI",
    maintainer_email="opensource@ni.com",
    keywords=['nifgen'],
    license='MIT',
    include_package_data=True,
    packages=['nifgen'],
    python_requires='>=3.10',
    install_requires=[
        'hightime>=0.2.0',
        'nitclk',
    ],
    extras_require={
        'grpc': [
            'grpcio>=1.59.0,<2.0',
            'protobuf>=4.21.6',
            'ni.grpcdevice.v1.proto>=1.0.0'
        ],
    },
    classifiers=[
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
        "Topic :: Scientific/Engineering :: Instrument Drivers",
        "Topic :: System :: Hardware :: Hardware Drivers"
    ],
    package_data={pypi_name: ['VERSION']},
)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nifgen/tox-system_tests.ini sha256=fac7b6b05f06a9b04464bde3c3a2d52e61efe047ca9c2983724e9c0380b70e2f bytes=3058 -->
## FILE: generated/nifgen/tox-system_tests.ini

- repository: `ni/nimi-python`
- source_path: `generated/nifgen/tox-system_tests.ini`
- sha256: `fac7b6b05f06a9b04464bde3c3a2d52e61efe047ca9c2983724e9c0380b70e2f`
- bytes: 3058

````ini
# Tox (http://tox.testrun.org/) is a tool for running tests
# in multiple virtualenvs. This configuration file will run the
# test suite on all supported python versions. To use it, "pip install tox"
# and then run "tox -c tox-system_tests.ini" from the driver directory. (generated/nifgen)
[tox]
envlist = py{310,311,312,313,314}-nifgen-wheel_dep,py{310,311,312,313,314}-nifgen-system_tests, py314-nifgen-coverage
skip_missing_interpreters=True
ignore_basepython_conflict=True
# We put the .tox directory outside of the Jenkins workspace so that it isn't wiped with the rest of the repo
toxworkdir = ../../../.tox

[testenv]
description =
    nifgen-wheel_dep: Build the nitclk wheel because we use it in nifgen tests
    nifgen-system_tests: Run nifgen system tests (requires NI-FGEN runtime to be installed)
    nifgen-coverage: Prepare coverage report for upload to codecov.io  # upload handled by GitHub Actions

changedir =
    nifgen-wheel_dep: ../nitclk
    nifgen-system_tests: .
    nifgen-coverage: .

commands =
    nifgen-wheel_dep: python -m build --wheel

    # --disable-pip-version-check prevents pip from telling us we need to upgrade pip, since we are doing that now
    nifgen-system_tests: python -m pip install --disable-pip-version-check --upgrade pip
    nifgen-system_tests: python ../../tools/install_local_wheel.py --driver nitclk --start-path ../..
    nifgen-system_tests: python -c "import nifgen; nifgen.print_diagnostic_information()"
    nifgen-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nifgen --parallel-mode -m pytest ../../src/nifgen/examples --junitxml=../junit/junit-nifgen-{envname}-examples-{env:BITNESS:64}.xml {posargs}
    nifgen-system_tests: coverage run --rcfile=../../tools/coverage_system_tests.rc --source nifgen --parallel-mode -m pytest ../../src/nifgen/system_tests -c tox-system_tests.ini --junitxml=../junit/junit-nifgen-{envname}-{env:BITNESS:64}.xml --durations=5 {posargs}

    nifgen-coverage: coverage combine --rcfile=../../tools/coverage_system_tests.rc ./
    # Create the report to upload
    nifgen-coverage: coverage xml -i --rcfile=../../tools/coverage_system_tests.rc
    # Display the coverage results
    nifgen-coverage: coverage report --rcfile=../../tools/coverage_system_tests.rc

deps =
    nifgen-wheel_dep: build

    nifgen-system_tests: pytest
    nifgen-system_tests: coverage
    nifgen-system_tests: numpy
    nifgen-system_tests: hightime
    nifgen-system_tests: fasteners
    nifgen-system_tests: pytest-json
    nifgen-system_tests: .[grpc]

    nifgen-coverage: coverage

depends =
    nifgen-coverage: py{310,311,312,313,314}-nifgen-system_tests
    nifgen-system_tests: py{310,311,312,313,314}-nifgen-wheel_dep,

passenv =
    GIT_BRANCH
    GIT_COMMIT
    BUILD_URL
    BRANCH_NAME
    JENKINS_URL
    BUILD_NUMBER

[pytest]
addopts = --verbose
filterwarnings =
   error::pytest.PytestUnhandledThreadExceptionWarning
norecursedirs = .* build dist CVS _darcs {arch} *.egg venv
junit_suite_name = nimi-python
junit_family = xunit1
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/__init__.py sha256=38a6e3500bc9287d30a50f4e3a1e28176ae77b2cec7498e8fdaf48ff07419be5 bytes=3191 -->
## FILE: generated/nimodinst/nimodinst/__init__.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/__init__.py`
- sha256: `38a6e3500bc9287d30a50f4e3a1e28176ae77b2cec7498e8fdaf48ff07419be5`
- bytes: 3191

````python
# -*- coding: utf-8 -*-
# This file was generated


__version__ = '1.4.10.dev0'

from nimodinst.errors import DriverWarning  # noqa: F401
from nimodinst.errors import Error  # noqa: F401
from nimodinst.session import Session  # noqa: F401


def get_diagnostic_information():
    '''Get diagnostic information about the system state that is suitable for printing or logging

    returns: dict

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    import importlib.metadata
    import os
    import platform
    import struct
    import sys

    def is_python_64bit():
        return (struct.calcsize("P") == 8)

    def is_os_64bit():
        return platform.machine().endswith('64')

    def is_venv():
        return 'VIRTUAL_ENV' in os.environ

    info = {}
    info['os'] = {}
    info['python'] = {}
    info['driver'] = {}
    info['module'] = {}
    if platform.system() == 'Windows':
        try:
            import winreg as winreg
        except ImportError:
            import _winreg as winreg

        os_name = 'Windows'
        try:
            driver_version_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\National Instruments\NI-ModInst\CurrentVersion")
            driver_version = winreg.QueryValueEx(driver_version_key, "Version")[0]
        except WindowsError:
            driver_version = 'Unknown'
    elif platform.system() == 'Linux':
        os_name = 'Linux'
        driver_version = 'Unknown'
    else:
        raise SystemError('Unsupported platform: {}'.format(platform.system()))

    installed_packages_names = [
        name
        for name_list in importlib.metadata.packages_distributions().values()
        for name in name_list
    ]
    installed_packages_names = set(installed_packages_names)
    installed_packages_list = [
        {'name': name, 'version': importlib.metadata.distribution(name).version}
        for name in sorted(installed_packages_names)
    ]

    info['os']['name'] = os_name
    info['os']['version'] = platform.version()
    info['os']['bits'] = '64' if is_os_64bit() else '32'
    info['driver']['name'] = "NI-ModInst"
    info['driver']['version'] = driver_version
    info['module']['name'] = 'nimodinst'
    info['module']['version'] = "1.4.10.dev0"
    info['python']['version'] = sys.version
    info['python']['bits'] = '64' if is_python_64bit() else '32'
    info['python']['is_venv'] = is_venv()
    info['python']['packages'] = installed_packages_list

    return info


def print_diagnostic_information():
    '''Print diagnostic information in a format suitable for issue report

    note: Python bitness may be incorrect when running in a virtual environment
    '''
    info = get_diagnostic_information()

    row_format = '    {:<10} {}'
    for type in ['OS', 'Driver', 'Module', 'Python']:
        typename = type.lower()
        print(type + ':')
        for item in info[typename]:
            if item != 'packages':
                print(row_format.format(item.title() + ':', info[typename][item]))
    print('    Installed Packages:')
    for p in info['python']['packages']:
        print((' ' * 8) + p['name'] + '==' + p['version'])

    return info
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/_converters.py sha256=c3cd6cbd42ea1cc7c0813f64b6d2aab946950161a3e5f9d816ef33358ff79b9e bytes=14627 -->
## FILE: generated/nimodinst/nimodinst/_converters.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/_converters.py`
- sha256: `c3cd6cbd42ea1cc7c0813f64b6d2aab946950161a3e5f9d816ef33358ff79b9e`
- bytes: 14627

````python
# -*- coding: utf-8 -*-
# This file was generated
import nimodinst._visatype as _visatype
import nimodinst.errors as errors

import array
import collections
import hightime
import numbers

from functools import singledispatch


@singledispatch
def _convert_repeated_capabilities(arg, prefix):  # noqa: F811
    '''Base version that should not be called

    Overall purpose is to convert the repeated capabilities to a list of strings with prefix from what ever form

    Supported types:
    - str - List (comma delimited)
    - str - Range (using '-' or ':')
    - str - single item
    - int
    - tuple
    - range
    - slice

    Each instance should return a list of strings, without prefix
    - '0' --> ['0']
    - 0 --> ['0']
    - '0, 1' --> ['0', '1']
    - 'ScriptTrigger0, ScriptTrigger1' --> ['0', '1']
    - '0-1' --> ['0', '1']
    - '0:1' --> ['0', '1']
    - '0-1,4' --> ['0', '1', '4']
    - range(0, 2) --> ['0', '1']
    - slice(0, 2) --> ['0', '1']
    - (0, 1, 4) --> ['0', '1', '4']
    - ('0-1', 4) --> ['0', '1', '4']
    - (slice(0, 1), '2', [4, '5-6'], '7-9', '11:14', '16, 17') -->
        ['0', '2', '4', '5', '6', '7', '8', '9', '11', '12', '13', '14', '16', '17']
    '''
    raise errors.InvalidRepeatedCapabilityError('Invalid type', type(arg))


@_convert_repeated_capabilities.register(numbers.Integral)  # noqa: F811
def _(repeated_capability, prefix):
    '''Integer version'''
    return [str(repeated_capability)]


# This parsing function duplicate the parsing in the driver, so if changes to the allowed format are made there, they will need to be replicated here.
@_convert_repeated_capabilities.register(str)  # noqa: F811
def _(repeated_capability, prefix):
    '''String version (this is the most complex)

    We need to deal with a range ('0-3' or '0:3'), a list ('0,1,2,3') and a single item
    '''
    # First we deal with a list
    rep_cap_list = repeated_capability.split(',')
    if len(rep_cap_list) > 1:
        # We have a list so call ourselves again to let the iterable instance handle it
        return _convert_repeated_capabilities(rep_cap_list, prefix)

    # Now we deal with ranges
    # We remove any prefix and change ':' to '-'
    r = repeated_capability.strip().replace(prefix, '').replace(':', '-')
    rc = r.split('-')
    if len(rc) > 1:
        if len(rc) > 2:
            raise errors.InvalidRepeatedCapabilityError("Multiple '-' or ':'", repeated_capability)
        try:
            start = int(rc[0])
            end = int(rc[1])
        except ValueError:
            # This exception is raised when repeated_capability is of the form "dev/0-1". rc[0] == "dev/0" in this case.
            # Just return the repeated_capability string as-is in that case.
            pass
        else:
            if end < start:
                rng = range(start, end - 1, -1)
            else:
                rng = range(start, end + 1)
            return _convert_repeated_capabilities(rng, prefix)

    # If we made it here, it must be a simple item so we remove any prefix and return
    return [repeated_capability.replace(prefix, '').strip()]


# We cannot use collections.abc.Iterable here because strings are also iterable and then this
# instance is what gets called instead of the string one.
@_convert_repeated_capabilities.register(list)  # noqa: F811
@_convert_repeated_capabilities.register(range)  # noqa: F811
@_convert_repeated_capabilities.register(tuple)  # noqa: F811
def _(repeated_capability, prefix):
    '''Iterable version - can handle lists, ranges, and tuples'''
    rep_cap_list = []
    for r in repeated_capability:
        rep_cap_list += _convert_repeated_capabilities(r, prefix)
    return rep_cap_list


@_convert_repeated_capabilities.register(slice)  # noqa: F811
def _(repeated_capability, prefix):
    '''slice version'''
    def ifnone(a, b):
        return b if a is None else a
    # Turn the slice into a list and call ourselves again to let the iterable instance handle it
    rng = range(ifnone(repeated_capability.start, 0), repeated_capability.stop, ifnone(repeated_capability.step, 1))
    return _convert_repeated_capabilities(rng, prefix)


def convert_repeated_capabilities(repeated_capability, prefix=''):
    '''Convert a repeated capabilities object to a comma delimited list

    Args:
        repeated_capability (str, list, tuple, slice, None) -
        prefix (str) - common prefix for all strings

    Returns:
        rep_cap_list (list of str) - list of each repeated capability item with ranges expanded and prefix added
    '''
    # We need to explicitly handle None here. Everything else we can pass on to the singledispatch functions
    if repeated_capability is None:
        return []
    return [prefix + r for r in _convert_repeated_capabilities(repeated_capability, prefix)]


def convert_repeated_capabilities_without_prefix(repeated_capability):
    '''Convert a repeated capabilities object, without any prefix, to a comma delimited list

    Args:
        repeated_capability - Supported types:
            - str - list (comma-delimited)
            - str - range (using '-' or ':')
            - str - single item
            - int
            - list of str
            - tuple of str
            - range of str
            - slice of str
            - None

    Returns:
        rep_cap (str) - comma delimited string of each repeated capability item with ranges expanded
    '''
    return ','.join(convert_repeated_capabilities(repeated_capability, ''))


def expand_channel_string(channel_string, all_channels_in_session):
    '''Expands a channel_string to a list of individual channel names.

    The individual channel names may or may not be fully qualified channel names as applicable for
    the session. In other words, the individual channel names will be a subset of
    all_channels_in_session.

    Examples:
        - expand_channel_string('1', ['0', '1', '2', '3']) --> ['1']
        - expand_channel_string('4,1:2', ['1', '2', '4']) --> ['4', '1', '2']
        - expand_channel_string('2:3,0', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/2', 'Dev1/3', 'Dev1/0']
        - expand_channel_string('Dev1/1', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3'])
            --> ['Dev1/1']
        - expand_channel_string('4,Dev1/1:2', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/1', 'Dev1/2']
        - expand_channel_string('Dev1/4,Dev1/2,Dev1/3', ['Dev1/2', 'Dev1/3', 'Dev1/4'])
            --> ['Dev1/4', 'Dev1/2', 'Dev1/3']
        - expand_channel_string('Dev1/1,Dev2/2', ['Dev1/0', 'Dev1/1', 'Dev1/2', 'Dev1/3', 'Dev2/0', 'Dev2/1', 'Dev2/2', 'Dev2/3'])
            --> ['Dev1/1', 'Dev2/2']
        - expand_channel_string(' Dev1 / 1 : 2 , 4 ', ['Dev1/1', 'Dev1/2', 'Dev1/4'])
            --> ['Dev1/1', 'Dev1/2', 'Dev1/4']
        - expand_channel_string('DEV1/0-1    , Dev1/3', ['dev1/0', 'dev1/1', 'dev1/2', 'dev1/3'])
            --> ['dev1/0', 'dev1/1', 'dev1/3']

    Args:
        channel_string (str) - refer to _convert_repeated_capabilities() for the
            supported formats (this string is expected to be used as the index of session.channels)

        all_channels_in_session (list of str) - names of all the channels in the session as returned
            by get_channel_names()

    Returns:
        channel_names (list of str) - A list in which each element is the name of a single channel,
            with the exact capitalization used by the driver runtime.
    '''
    if channel_string.strip() == '':
        return all_channels_in_session

    # Rule 1: If all_channels_in_session is fully-qualified then returned channel names should be
    #         fully-qualified, otherwise returned channel names should not be fully-qualified.
    # Rule 2: If any channel in the input is not fully-qualified, but we need to return
    #         fully-qualified channels because of Rule 1, then use the channel qualifier obtained
    #         from all_channels_in_session. This can only happen on a single-instrument session,
    #         so all the channel qualifiers are the same and we pick the first one.

    instrument, separator, channel = all_channels_in_session[0].rpartition('/')
    default_channel_qualifier = instrument + separator

    expanded_channel_list = []
    for token in channel_string.split(','):
        instrument, separator, channel = token.rpartition('/')
        instrument = instrument.strip()
        channel_qualifier = instrument + separator if instrument else default_channel_qualifier
        expanded_channel_list.extend(
            convert_repeated_capabilities(channel.strip(), channel_qualifier)
        )

    # Convert the expanded channel names to their canonical form based on all_channels_in_session
    lowercase_channel_name_to_session_channel_name_dict = {
        channel_name.lower(): channel_name for channel_name in all_channels_in_session
    }
    return [
        lowercase_channel_name_to_session_channel_name_dict[channel_name.lower()]
        for channel_name in expanded_channel_list
    ]


def _convert_timedelta(value, library_type, scaling):
    try:
        # We first assume it is a timedelta object
        scaled_value = value.total_seconds() * scaling
    except AttributeError:
        # If that doesn't work, assume it is a value in seconds
        # cast to float so scaled_value is always a float. This allows `timeout=10` to work as expected
        scaled_value = float(value) * scaling

    # ctype integer types don't convert to int from float so we need to
    if library_type in [_visatype.ViInt64, _visatype.ViInt32, _visatype.ViUInt32, _visatype.ViInt16, _visatype.ViUInt16, _visatype.ViInt8]:
        scaled_value = int(scaled_value)

    return scaled_value


def convert_timedelta_to_seconds_real64(value):
    return _convert_timedelta(value, _visatype.ViReal64, 1)


def convert_timedelta_to_milliseconds_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1000)


def convert_timedeltas_to_seconds_real64(values):
    return [convert_timedelta_to_seconds_real64(i) for i in values]


def convert_seconds_real64_to_timedelta(value):
    return hightime.timedelta(seconds=value)


def convert_seconds_real64_to_timedeltas(values):
    return [convert_seconds_real64_to_timedelta(i) for i in values]


def convert_month_to_timedelta(months):
    return hightime.timedelta(days=(30.4167 * months))


# Scaling factor to apply on seconds to get months
# would be 1/(60 seconds * 60 minutes * 24 hours * 30.4167 days)
def convert_timedelta_to_months_int32(value):
    return _convert_timedelta(value, _visatype.ViInt32, 1.0 / (60 * 60 * 24 * 30.4167))


# This converter is not called from the normal codegen path for function. Instead it is
# call from init and is a special case.
def convert_init_with_options_dictionary(values):
    if type(values) is str:
        init_with_options_string = values
    else:
        good_keys = {
            'rangecheck': 'RangeCheck',
            'queryinstrstatus': 'QueryInstrStatus',
            'cache': 'Cache',
            'simulate': 'Simulate',
            'recordcoercions': 'RecordCoercions',
            'interchangecheck': 'InterchangeCheck',
            'driversetup': 'DriverSetup',
            'range_check': 'RangeCheck',
            'query_instr_status': 'QueryInstrStatus',
            'record_coercions': 'RecordCoercions',
            'interchange_check': 'InterchangeCheck',
            'driver_setup': 'DriverSetup',
        }
        init_with_options = []
        for k in sorted(values.keys()):
            value = None
            if k.lower() in good_keys and not good_keys[k.lower()] == 'DriverSetup':
                value = good_keys[k.lower()] + ('=1' if values[k] is True else '=0')
            elif k.lower() in good_keys and good_keys[k.lower()] == 'DriverSetup':
                if not isinstance(values[k], dict):
                    raise TypeError('DriverSetup must be a dictionary')
                value = 'DriverSetup=' + (';'.join([key + ':' + values[k][key] for key in sorted(values[k])]))
            else:
                value = k + ('=1' if values[k] is True else '=0')

            init_with_options.append(value)

        init_with_options_string = ','.join(init_with_options)

    return init_with_options_string


# convert value to bytes
@singledispatch
def _convert_to_bytes(value):  # noqa: F811
    pass


@_convert_to_bytes.register(list)  # noqa: F811
@_convert_to_bytes.register(bytes)  # noqa: F811
@_convert_to_bytes.register(bytearray)  # noqa: F811
@_convert_to_bytes.register(array.array)  # noqa: F811
def _(value):
    return value


@_convert_to_bytes.register(str)  # noqa: F811
def _(value):
    return value.encode()


def convert_to_bytes(value):  # noqa: F811
    return bytes(_convert_to_bytes(value))


def convert_comma_separated_string_to_list(comma_separated_string):
    return [x.strip() for x in comma_separated_string.split(',')]


def convert_list_to_comma_separated_string(list_of_strings):
    '''Convert a list or tuple of strings into a comma-separated string.

    Args:
        list_of_strings (list or tuple of str): List or tuple of strings.

    Returns:
        str: Comma-separated string.
    '''
    if not isinstance(list_of_strings, (list, tuple)) or not all(isinstance(item, str) for item in list_of_strings):
        raise TypeError('Input must be a list or tuple of str')
    return ','.join(list_of_strings)


def convert_chained_repeated_capability_to_parts(chained_repeated_capability):
    '''Convert a chained repeated capabilities string to a list of comma-delimited repeated capabilities string.

    Converter assumes that the input contains the full cartesian product of its parts.
    e.g. If chained_repeated_capability is 'site0/PinA,site0/PinB,site1/PinA,site1/PinB',
    ['site0,site1', 'PinA,PinB'] is returned.

    Args:
        chained_repeated_capability (str) - comma-delimited repeated capabilities string where each
        item is a chain of slash-delimited repeated capabilities

    Returns:
        rep_cap_list (list of str) - list of comma-delimited repeated capabilities string
    '''
    chained_repeated_capability_items = convert_comma_separated_string_to_list(chained_repeated_capability)
    repeated_capability_lists = [[] for _ in range(chained_repeated_capability_items[0].count('/') + 1)]
    for item in chained_repeated_capability_items:
        repeated_capability_lists = [x + [y] for x, y in zip(repeated_capability_lists, item.split('/'))]
    return [','.join(collections.OrderedDict.fromkeys(x)) for x in repeated_capability_lists]
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/_library.py sha256=addfd40210e62a0b82ba142dfa442c832c919f4e2ee08e7706bf7f64fdf299c9 bytes=4561 -->
## FILE: generated/nimodinst/nimodinst/_library.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/_library.py`
- sha256: `addfd40210e62a0b82ba142dfa442c832c919f4e2ee08e7706bf7f64fdf299c9`
- bytes: 4561

````python
# -*- coding: utf-8 -*-
# This file was generated

import ctypes
import nimodinst.errors as errors
import threading

from nimodinst._visatype import *  # noqa: F403,H303


class Library(object):
    '''Library

    Wrapper around driver library.
    Class will setup the correct ctypes information for every function on first call.
    '''

    def __init__(self, ctypes_library):
        self._func_lock = threading.Lock()
        self._library = ctypes_library
        # We cache the cfunc object from the ctypes.CDLL object
        self.niModInst_CloseInstalledDevicesSession_cfunc = None
        self.niModInst_GetExtendedErrorInfo_cfunc = None
        self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc = None
        self.niModInst_GetInstalledDeviceAttributeViString_cfunc = None
        self.niModInst_OpenInstalledDevicesSession_cfunc = None

    def _get_library_function(self, name):
        try:
            function = getattr(self._library, name)
        except AttributeError as e:
            raise errors.DriverTooOldError() from e
        return function

    def niModInst_CloseInstalledDevicesSession(self, handle):  # noqa: N802
        with self._func_lock:
            if self.niModInst_CloseInstalledDevicesSession_cfunc is None:
                self.niModInst_CloseInstalledDevicesSession_cfunc = self._get_library_function('niModInst_CloseInstalledDevicesSession')
                self.niModInst_CloseInstalledDevicesSession_cfunc.argtypes = [ViSession]  # noqa: F405
                self.niModInst_CloseInstalledDevicesSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_CloseInstalledDevicesSession_cfunc(handle)

    def niModInst_GetExtendedErrorInfo(self, error_info_buffer_size, error_info):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetExtendedErrorInfo_cfunc is None:
                self.niModInst_GetExtendedErrorInfo_cfunc = self._get_library_function('niModInst_GetExtendedErrorInfo')
                self.niModInst_GetExtendedErrorInfo_cfunc.argtypes = [ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niModInst_GetExtendedErrorInfo_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_GetExtendedErrorInfo_cfunc(error_info_buffer_size, error_info)

    def niModInst_GetInstalledDeviceAttributeViInt32(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc is None:
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc = self._get_library_function('niModInst_GetInstalledDeviceAttributeViInt32')
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_GetInstalledDeviceAttributeViInt32_cfunc(handle, index, attribute_id, attribute_value)

    def niModInst_GetInstalledDeviceAttributeViString(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        with self._func_lock:
            if self.niModInst_GetInstalledDeviceAttributeViString_cfunc is None:
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc = self._get_library_function('niModInst_GetInstalledDeviceAttributeViString')
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc.argtypes = [ViSession, ViInt32, ViInt32, ViInt32, ctypes.POINTER(ViChar)]  # noqa: F405
                self.niModInst_GetInstalledDeviceAttributeViString_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_GetInstalledDeviceAttributeViString_cfunc(handle, index, attribute_id, attribute_value_buffer_size, attribute_value)

    def niModInst_OpenInstalledDevicesSession(self, driver, handle, device_count):  # noqa: N802
        with self._func_lock:
            if self.niModInst_OpenInstalledDevicesSession_cfunc is None:
                self.niModInst_OpenInstalledDevicesSession_cfunc = self._get_library_function('niModInst_OpenInstalledDevicesSession')
                self.niModInst_OpenInstalledDevicesSession_cfunc.argtypes = [ctypes.POINTER(ViChar), ctypes.POINTER(ViSession), ctypes.POINTER(ViInt32)]  # noqa: F405
                self.niModInst_OpenInstalledDevicesSession_cfunc.restype = ViStatus  # noqa: F405
        return self.niModInst_OpenInstalledDevicesSession_cfunc(driver, handle, device_count)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/_library_interpreter.py sha256=d14bcd69c25b2daab6e919eeef2b9b24c5eb5379e26a3a3fec8e31b545ec53d0 bytes=7235 -->
## FILE: generated/nimodinst/nimodinst/_library_interpreter.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/_library_interpreter.py`
- sha256: `d14bcd69c25b2daab6e919eeef2b9b24c5eb5379e26a3a3fec8e31b545ec53d0`
- bytes: 7235

````python
# -*- coding: utf-8 -*-
# This file was generated

import array
import ctypes
import hightime  # noqa: F401
import nimodinst._library_singleton as _library_singleton
import nimodinst._visatype as _visatype
import nimodinst.errors as errors


# Helper functions for creating ctypes needed for calling into the driver DLL
def _get_ctypes_pointer_for_buffer(value=None, library_type=None, size=None):
    if isinstance(value, array.array):
        assert library_type is not None, 'library_type is required for array.array'
        addr, _ = value.buffer_info()
        return ctypes.cast(addr, ctypes.POINTER(library_type))
    elif str(type(value)).find("'numpy.ndarray'") != -1:
        import numpy
        return numpy.ctypeslib.as_ctypes(value)
    elif isinstance(value, bytes):
        return ctypes.cast(value, ctypes.POINTER(library_type))
    elif isinstance(value, list):
        assert library_type is not None, 'library_type is required for list'
        return (library_type * len(value))(*value)
    else:
        if library_type is not None and size is not None:
            return (library_type * size)()
        else:
            return None


def _convert_to_array(value, array_type):
    if value is not None:
        if isinstance(value, array.array):
            value_array = value
        else:
            value_array = array.array(array_type, value)
    else:
        value_array = None

    return value_array


class LibraryInterpreter(object):
    '''Library C<->Python interpreter.

    This class is responsible for interpreting the Library's C API. It is responsible for:
    * Converting ctypes to native Python types.
    * Dealing with string encoding.
    * Allocating memory.
    * Converting errors returned by Library into Python exceptions.
    '''

    def __init__(self, encoding):
        self._encoding = encoding
        self._library = _library_singleton.get()
        # Initialize _handle to 0 for now.
        # Session will directly update it once the driver runtime init function has been called and
        # we have a valid session handle.
        self.set_session_handle()

    def set_session_handle(self, value=0):
        self._handle = value

    def get_session_handle(self):
        return self._handle

    def get_error_description(self, error_code):
        '''get_error_description

        Returns the error description.
        '''
        # We hand-maintain the code that calls into the cfunc rather than leverage code-generation
        # because niModInst_GetExtendedErrorInfo() does not properly do the IVI-dance.
        # See https://github.com/ni/nimi-python/issues/166
        error_info_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_info_ctype = None  # case C050
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        if error_code <= 0:
            return 'Failed to retrieve error description.'
        error_info_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_info_ctype = (_visatype.ViChar * error_info_buffer_size_ctype.value)()  # case C060
        # Note we don't look at the return value. This is intentional as niModInst returns the
        # original error code rather than 0 (VI_SUCCESS).
        self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        return error_info_ctype.value.decode("ascii")

    def close_installed_devices_session(self):  # noqa: N802
        handle_ctype = _visatype.ViSession(self._handle)  # case S110
        error_code = self._library.niModInst_CloseInstalledDevicesSession(handle_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return

    def get_extended_error_info(self):  # noqa: N802
        error_info_buffer_size_ctype = _visatype.ViInt32()  # case S170
        error_info_ctype = None  # case C050
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=True)
        error_info_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        error_info_ctype = (_visatype.ViChar * error_info_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niModInst_GetExtendedErrorInfo(error_info_buffer_size_ctype, error_info_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=True)
        return error_info_ctype.value.decode(self._encoding)

    def get_installed_device_attribute_vi_int32(self, index, attribute_id):  # noqa: N802
        handle_ctype = _visatype.ViSession(self._handle)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        attribute_id_ctype = _visatype.ViInt32(attribute_id)  # case S150
        attribute_value_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViInt32(handle_ctype, index_ctype, attribute_id_ctype, None if attribute_value_ctype is None else (ctypes.pointer(attribute_value_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(attribute_value_ctype.value)

    def get_installed_device_attribute_vi_string(self, index, attribute_id):  # noqa: N802
        handle_ctype = _visatype.ViSession(self._handle)  # case S110
        index_ctype = _visatype.ViInt32(index)  # case S150
        attribute_id_ctype = _visatype.ViInt32(attribute_id)  # case S150
        attribute_value_buffer_size_ctype = _visatype.ViInt32()  # case S170
        attribute_value_ctype = None  # case C050
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViString(handle_ctype, index_ctype, attribute_id_ctype, attribute_value_buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=True, is_error_handling=False)
        attribute_value_buffer_size_ctype = _visatype.ViInt32(error_code)  # case S180
        attribute_value_ctype = (_visatype.ViChar * attribute_value_buffer_size_ctype.value)()  # case C060
        error_code = self._library.niModInst_GetInstalledDeviceAttributeViString(handle_ctype, index_ctype, attribute_id_ctype, attribute_value_buffer_size_ctype, attribute_value_ctype)
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return attribute_value_ctype.value.decode(self._encoding)

    def open_installed_devices_session(self, driver):  # noqa: N802
        driver_ctype = ctypes.create_string_buffer(driver.encode(self._encoding))  # case C020
        handle_ctype = _visatype.ViSession()  # case S220
        device_count_ctype = _visatype.ViInt32()  # case S220
        error_code = self._library.niModInst_OpenInstalledDevicesSession(driver_ctype, None if handle_ctype is None else (ctypes.pointer(handle_ctype)), None if device_count_ctype is None else (ctypes.pointer(device_count_ctype)))
        errors.handle_error(self, error_code, ignore_warnings=False, is_error_handling=False)
        return int(handle_ctype.value), int(device_count_ctype.value)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/_library_singleton.py sha256=4927de848d2ffd65d9cd61d220140efafdc85f92c27b1eb3bb1363c03c3a218b bytes=1708 -->
## FILE: generated/nimodinst/nimodinst/_library_singleton.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/_library_singleton.py`
- sha256: `4927de848d2ffd65d9cd61d220140efafdc85f92c27b1eb3bb1363c03c3a218b`
- bytes: 1708

````python
# -*- coding: utf-8 -*-
# This file was generated

import platform

import ctypes
import ctypes.util
import nimodinst._library as _library
import nimodinst.errors as errors
import threading


_instance = None
_instance_lock = threading.Lock()
_library_info = {'Linux': {'64bit': {'name': 'nimodinst', 'type': 'cdll'}},
                 'Windows': {'32bit': {'name': 'niModInst.dll', 'type': 'windll'},
                             '64bit': {'name': 'niModInst_64.dll', 'type': 'cdll'}}}


def _get_library_name():
    try:
        lib_name = ctypes.util.find_library(_library_info[platform.system()][platform.architecture()[0]]['name'])  # We find and return full path to the DLL
        if lib_name is None:
            raise errors.DriverNotInstalledError()
        return lib_name
    except KeyError:
        raise errors.UnsupportedConfigurationError


def _get_library_type():
    try:
        return _library_info[platform.system()][platform.architecture()[0]]['type']
    except KeyError:
        raise errors.UnsupportedConfigurationError


def get():
    '''get

    Returns the library.Library singleton for nimodinst.
    '''
    global _instance

    with _instance_lock:
        if _instance is None:
            try:
                library_type = _get_library_type()
                if library_type == 'windll':
                    ctypes_library = ctypes.WinDLL(_get_library_name())
                else:
                    assert library_type == 'cdll'
                    ctypes_library = ctypes.CDLL(_get_library_name())
            except OSError:
                raise errors.DriverNotInstalledError()
            _instance = _library.Library(ctypes_library)
        return _instance
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/_visatype.py sha256=ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92 bytes=662 -->
## FILE: generated/nimodinst/nimodinst/_visatype.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/_visatype.py`
- sha256: `ac436ae1613f5e807cd16d2df951c7a502f37996234e4d324c5412b3633e1c92`
- bytes: 662

````python
import ctypes


'''Definitions of the VISA types used by the C API of the driver runtime.
These are aliased directly to ctypes types so can be used directly to call into the library.
'''


ViChar = ctypes.c_char
ViInt8 = ctypes.c_int8
ViUInt8 = ctypes.c_uint8
ViInt16 = ctypes.c_int16
ViUInt16 = ctypes.c_uint16
ViInt32 = ctypes.c_int32
ViUInt32 = ctypes.c_uint32
ViInt64 = ctypes.c_int64
ViUInt64 = ctypes.c_uint64
ViString = ctypes.c_char_p
ViReal32 = ctypes.c_float
ViReal64 = ctypes.c_double

# Types that are based on other visatypes
ViBoolean = ViUInt16
ViStatus = ViInt32
ViSession = ViUInt32
ViAttr = ViUInt32
ViConstString = ViString
ViRsrc = ViString
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/errors.py sha256=39d2e47afe3313be33916b681f7aa316f82b9fd15c4351a7c0e0451bbff4bdaf bytes=3308 -->
## FILE: generated/nimodinst/nimodinst/errors.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/errors.py`
- sha256: `39d2e47afe3313be33916b681f7aa316f82b9fd15c4351a7c0e0451bbff4bdaf`
- bytes: 3308

````python
# -*- coding: utf-8 -*-
# This file was generated


import platform
import warnings


def _is_success(code):
    return (code == 0)


def _is_error(code):
    return (code < 0)


def _is_warning(code):
    return (code > 0)


class Error(Exception):
    '''Base error class for NI-ModInst'''

    def __init__(self, message):
        super(Error, self).__init__(message)


class DriverError(Error):
    '''An error originating from the NI-ModInst driver'''

    def __init__(self, code, description):
        assert _is_error(code), "Should not raise Error if code is not fatal."
        self.code = code
        self.description = description
        super(DriverError, self).__init__(str(self.code) + ": " + self.description)


class DriverWarning(Warning):
    '''A warning originating from the NI-ModInst driver'''

    def __init__(self, code, description):
        assert _is_warning(code), "Should not create Warning if code is not positive."
        super(DriverWarning, self).__init__('Warning {} occurred.\n\n{}'.format(code, description))


class UnsupportedConfigurationError(Error):
    '''An error due to using this module in an usupported platform.'''

    def __init__(self):
        super(UnsupportedConfigurationError, self).__init__('System configuration is unsupported: ' + platform.architecture()[0] + ' ' + platform.system())


class DriverNotInstalledError(Error):
    '''An error due to using this module without the driver runtime installed.'''

    def __init__(self):
        super(DriverNotInstalledError, self).__init__('The NI-ModInst runtime could not be loaded. Make sure it is installed and its bitness matches that of your Python interpreter. Please visit http://www.ni.com/downloads/drivers/ to download and install it.')


class DriverTooOldError(Error):
    '''An error due to using this module with an older version of the NI-ModInst driver runtime.'''

    def __init__(self):
        super(DriverTooOldError, self).__init__('A function was not found in the NI-ModInst runtime. Please visit http://www.ni.com/downloads/drivers/ to download a newer version and install it.')


class DriverTooNewError(Error):
    '''An error due to the NI-ModInst driver runtime being too new for this module.'''

    def __init__(self):
        super(DriverTooNewError, self).__init__('The NI-ModInst runtime returned an unexpected value. This can occur if it is too new for the nimodinst Python module. Upgrade the nimodinst Python module.')


def handle_error(library_interpreter, code, ignore_warnings, is_error_handling):
    '''handle_error

    Helper function for handling errors returned by nimodinst.Library.
    It calls back into the LibraryInterpreter to get the corresponding error
    description and raises if necessary.
    '''

    if _is_success(code) or (_is_warning(code) and ignore_warnings):
        return

    if is_error_handling:
        # The caller is in the midst of error handling and an error occurred.
        # Don't try to get the description or we'll start recursing until the stack overflows.
        description = ''
    else:
        description = library_interpreter.get_error_description(code)

    if _is_error(code):
        raise DriverError(code, description)

    assert _is_warning(code)
    warnings.warn(DriverWarning(code, description))
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/session.py sha256=27248ad0902649b3c2961aa2fbc7679fe11717e88f67e5002b46f65e5fc81638 bytes=14066 -->
## FILE: generated/nimodinst/nimodinst/session.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/session.py`
- sha256: `27248ad0902649b3c2961aa2fbc7679fe11717e88f67e5002b46f65e5fc81638`
- bytes: 14066

````python
# This file was generated

import nimodinst._library_interpreter as _library_interpreter
import nimodinst.errors as errors

# Used for __repr__ and __str__
import pprint

pp = pprint.PrettyPrinter(indent=4)


class AttributeViInt32(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_int32(self._index, self._attribute_id)


class AttributeViString(object):

    def __init__(self, owner, attribute_id, index):
        self._owner = owner
        self._index = index
        self._attribute_id = attribute_id

    def __getitem__(self, index):
        return self._owner._get_installed_device_attribute_vi_string(self._index, self._attribute_id)


class _Device(object):

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, owner, index):
        self._index = index
        self.bus_number = AttributeViInt32(owner, 12, index=index)
        '''
        The bus on which the device has been enumerated.
        '''
        self.chassis_number = AttributeViInt32(owner, 11, index=index)
        '''
        The number of the chassis in which the device is installed. This property can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
        '''
        self.device_model = AttributeViString(owner, 1, index=index)
        '''
        The model of the device (for example, NI PXI-5122)
        '''
        self.device_name = AttributeViString(owner, 0, index=index)
        '''
        The name of the device, which can be used to open an instrument driver session for that device
        '''
        self.max_pciexpress_link_width = AttributeViInt32(owner, 18, index=index)
        '''
        **MAX_PCIEXPRESS_LINK_WIDTH**
        '''
        self.pciexpress_link_width = AttributeViInt32(owner, 17, index=index)
        '''
        **PCIEXPRESS_LINK_WIDTH**
        '''
        self.serial_number = AttributeViString(owner, 2, index=index)
        '''
        The serial number of the device
        '''
        self.slot_number = AttributeViInt32(owner, 10, index=index)
        '''
        The slot (for example, in a PXI chassis) in which the device is installed. This property can only be queried for PXI devices installed in a chassis that has been properly identified in MAX.
        '''
        self.socket_number = AttributeViInt32(owner, 13, index=index)
        '''
        The socket number on which the device has been enumerated
        '''
        self._param_list = 'owner=' + pp.pformat(owner) + ', index=' + pp.pformat(index)
        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('nimodinst', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        ret_str += '    bus_number = ' + pp.pformat(self.bus_number) + '\n'
        ret_str += '    chassis_number = ' + pp.pformat(self.chassis_number) + '\n'
        ret_str += '    device_model = ' + pp.pformat(self.device_model) + '\n'
        ret_str += '    device_name = ' + pp.pformat(self.device_name) + '\n'
        ret_str += '    max_pciexpress_link_width = ' + pp.pformat(self.max_pciexpress_link_width) + '\n'
        ret_str += '    pciexpress_link_width = ' + pp.pformat(self.pciexpress_link_width) + '\n'
        ret_str += '    serial_number = ' + pp.pformat(self.serial_number) + '\n'
        ret_str += '    slot_number = ' + pp.pformat(self.slot_number) + '\n'
        ret_str += '    socket_number = ' + pp.pformat(self.socket_number) + '\n'
        return ret_str

    def __getattribute__(self, name):
        if name in ['_is_frozen', 'index', '_param_list', '__class__', '__name__', '__repr__', '__str__', '__setattr__', ]:
            return object.__getattribute__(self, name)
        else:
            return object.__getattribute__(self, name).__getitem__(None)

    def __setattr__(self, name, value):
        if self._is_frozen:
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, name, value)


class _DeviceIterable(object):
    def __init__(self, owner, count):
        self._current_index = 0
        self._owner = owner
        self._count = count
        self._param_list = 'owner=' + pp.pformat(owner) + ', count=' + pp.pformat(count)
        self._is_frozen = True

    def _get_next(self):
        if self._current_index + 1 > self._count:
            raise StopIteration
        else:
            dev = _Device(self._owner, self._current_index)
            self._current_index += 1
            return dev

    def next(self):
        return self._get_next()

    def __next__(self):
        return self._get_next()

    def __repr__(self):
        return '{0}.{1}({2})'.format('nimodinst', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        ret_str += '    current index = {0}'.format(self._current_index)
        return ret_str


class Session(object):
    '''A NI-ModInst session to get device information'''

    # This is needed during __init__. Without it, __setattr__ raises an exception
    _is_frozen = False

    def __init__(self, driver):
        self._item_count = 0
        self._current_item = 0
        self._interpreter = _library_interpreter.LibraryInterpreter('windows-1251')
        # Note that _library_interpreter clears the session handle in its constructor, so that if
        # _open_installed_devices_session fails, the error handler can reference it.
        # And then once _open_installed_devices_session succeeds, we can call this again with the
        # actual session handle.
        handle, self._item_count = self._open_installed_devices_session(driver)
        self._interpreter.set_session_handle(handle)
        self._param_list = "driver=" + pp.pformat(driver)

        self.devices = []
        for i in range(self._item_count):
            self.devices.append(_Device(self, i))

        self._is_frozen = True

    def __repr__(self):
        return '{0}.{1}({2})'.format('nimodinst', self.__class__.__name__, self._param_list)

    def __str__(self):
        ret_str = self.__repr__() + ':\n'
        for i in range(self._item_count):
            ret_str += str(_Device(self, i)) + '\n'
        return ret_str

    def __setattr__(self, key, value):
        if self._is_frozen and key not in dir(self):
            raise AttributeError("__setattr__ not supported.")
        object.__setattr__(self, key, value)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    # Iterator functions
    def __len__(self):
        return self._item_count

    def __iter__(self):
        return _DeviceIterable(self, self._item_count)

    def close(self):
        try:
            self._close_installed_devices_session()
        except errors.DriverError:
            self._interpreter.set_session_handle()
            raise
        self._interpreter.set_session_handle()

    ''' These are code-generated '''

    def _close_installed_devices_session(self):
        r'''_close_installed_devices_session

        Cleans up the NI-ModInst session created by a call to
        _open_installed_devices_session. Call this method when you are
        finished using the session handle and do not use this handle again.
        '''
        self._interpreter.close_installed_devices_session()

    def _get_installed_device_attribute_vi_int32(self, index, attribute_id):
        r'''_get_installed_device_attribute_vi_int32

        Returns an integer property specified by the attributeID parameter for
        a device specified by the handle and index parameters. The handle
        parameter is expected to be a valid handle returned by
        _open_installed_devices_session. It therefore acts as a handle to
        a list of installed devices. The index parameter specifies the device in
        the list for which you want the property.

        Args:
            index (int): A zero-based index that specifies the device for which you want the
                property. This index parameter should be between 0 and (deviceCount -
                1), inclusive, where deviceCount is the number of installed devices
                returned by _open_installed_devices_session.

            attribute_id (int): The ID of the integer property you want to query. Valid Values Slot
                Number--the slot (for example, in a PXI chassis) in which the device is
                installed. This property can only be queried for PXI devices installed
                in a chassis that has been properly identified in MAX. Chassis
                Number--the number of the chassis in which the device is installed. This
                property can only be queried for PXI devices installed in a chassis
                that has been properly identified in MAX. Bus Number--the bus on which
                the device has been enumerated. Socket Number--the socket number on
                which the device has been enumerated. Notes The bus number and socket
                number can be used to form a VISA resource string for this device, of
                the form "PXI::::INSTR". Traditional NI-DAQ devices do not support the
                chassis number, bus number, and socket number properties.


        Returns:
            attribute_value (int): A pointer to a signed 32-bit integer variable that receives the value of
                the requested property.

        '''
        attribute_value = self._interpreter.get_installed_device_attribute_vi_int32(index, attribute_id)
        return attribute_value

    def _get_installed_device_attribute_vi_string(self, index, attribute_id):
        r'''_get_installed_device_attribute_vi_string

        Returns a string property specified by the attributeID parameter for a
        device specified by the handle and index parameters. The handle
        parameter is expected to be a valid handle returned by
        _open_installed_devices_session. Therefore, it acts as a handle
        to a list of installed devices. The index parameter specifies for which
        device in the list you want the property. To find out the length of the
        device name string before you allocate a buffer for it, simply call this
        method and pass 0 as the attributeValueBufferSize parameter or NULL as
        the attributeValue parameter. When you do this, the method returns the
        size of the buffer required to hold the property value string as its
        return value. You can then allocate an appropriately sized character
        buffer and call this method again.

        Args:
            index (int): A zero-based index that specifies the device for which you want the
                property. This index parameter should be between 0 and (deviceCount -
                1), inclusive, where deviceCount is the number of installed devices
                returned by _open_installed_devices_session.

            attribute_id (int): The ID of the string property you want to query. Valid Values
                device_name--the name of the device, which can be used
                to open an instrument driver session for that device
                device_model--the model of the device (for example, NI
                PXI-5122) serial_number--the serial number of the
                device


        Returns:
            attribute_value (str): The character buffer into which the property value string is copied.

        '''
        attribute_value = self._interpreter.get_installed_device_attribute_vi_string(index, attribute_id)
        return attribute_value

    def _open_installed_devices_session(self, driver):
        r'''_open_installed_devices_session

        Creates a handle to a list of installed devices supported by the
        specified driver. Call this method and pass in the name of an NI
        instrument driver, such as "NI-SCOPE". This method
        searches the system and constructs a list of all the installed devices
        that are supported by that driver, and then returns both a handle to
        this list and the number of devices found. The handle is used with other
        methods to query for properties such as device name and model, and to
        safely discard the list when finished. Note This handle reflects the
        system state when the handle is created (that is, when you call this
        method. If you remove devices from the system or rename them in
        Measurement & Automation Explorer (MAX), this handle may not refer to an
        accurate list of devices. You should destroy the handle using
        _close_installed_devices_session and create a new handle using
        this method.

        Args:
            driver (str): A string specifying the driver whose supported devices you want to find.
                This string is not case-sensitive. Some examples are: NI-SCOPE niScope
                NI-FGEN niFgen NI-HSDIO niHSDIO NI-DMM niDMM NI-SWITCH niSwitch Note If
                you use the empty string for this parameter, NI-ModInst creates a list
                of all Modular Instruments devices installed in the system.


        Returns:
            handle (int): A pointer to a ViSession variable that receives the value of the
                NI-ModInst session handle. This value acts as a handle to the list of
                installed devices and is used in other NI-ModInst methods.

            device_count (int): A pointer to an integer variable that receives the number of devices
                found in the system that are supported by the driver specified in the
                driver parameter.

        '''
        handle, device_count = self._interpreter.open_installed_devices_session(driver)
        return handle, device_count
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/unit_tests/_matchers.py sha256=c5b5ab077ab6a4090f281983eaee095caf64ee97b8b8a4c6141c14f8361a7a77 bytes=12202 -->
## FILE: generated/nimodinst/nimodinst/unit_tests/_matchers.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/unit_tests/_matchers.py`
- sha256: `c5b5ab077ab6a4090f281983eaee095caf64ee97b8b8a4c6141c14f8361a7a77`
- bytes: 12202

````python
# -*- coding: utf-8 -*-
# This file was generated
'''Matcher classes used by unit tests in order to set mock expectations.
These work well with our visatype definitions.
'''

import ctypes
import nimodinst._visatype as _visatype
import pprint

pp = pprint.PrettyPrinter(indent=4)


# Base classes


class _ScalarMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            print("{}: Unexpected type. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_type, type(other)))
            return False
        if other.value != self.expected_value:
            print("{}: Unexpected value. Expected: {}. Received: {}".format(self.__class__.__name__, self.expected_value, other.value))
            return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class _PointerMatcher(object):
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __eq__(self, other):
        if not isinstance(other, ctypes.POINTER(self.expected_type)):
            print("Unexpected type. Expected: {}. Received: {}".format(ctypes.POINTER(self.expected_type), type(other)))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_type))


class _BufferMatcher(object):
    def __init__(self, expected_element_type, expected_size_or_value):
        if isinstance(expected_size_or_value, int):
            # Were given the size of the buffer
            self.expected_value = None
            self.expected_size = expected_size_or_value
        else:
            # Were given a list or something that behaves like a list
            self.expected_value = expected_size_or_value
            self.expected_size = len(expected_size_or_value)
        self.expected_type = expected_element_type * self.expected_size
        # Store params for __repr__
        self._expected_element_type = expected_element_type
        self._expected_size_or_value = expected_size_or_value

    def __eq__(self, other):
        if not isinstance(other, self.expected_type):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            # Because of object lifetimes, we may need to mock the other instance and provide lists instead of the actual array
            if not isinstance(other, self.expected_type) and not isinstance(other, list):
                print("Unexpected type. Expected: {} or {}. Received: {}".format(self.expected_type, list, type(other)))
                return False
        if self.expected_size != len(other):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(other)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for i in range(0, len(self.expected_value)):
                if self.expected_value[i] != other[i]:
                    print("Unexpected value at index {}. Expected: {}. Received: {}".format(i, self.expected_value[i], other[i]))
                    return False
        return True

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self._expected_element_type), pp.pformat(self._expected_size_or_value))

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type  = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_value = ' + str(self.expected_value) + '\n'
        ret_str += '    expected_size  = ' + str(self.expected_size) + '\n'
        return ret_str


# Strings


class ViStringMatcher(object):
    def __init__(self, expected_string_value):
        self.expected_string_value = expected_string_value

    def __eq__(self, other):
        if not isinstance(other, ctypes.Array):
            # We try to "dereference" this in case it is a pointer and then do the check again. Only then saying they don't match
            try:
                other = other.contents
            except AttributeError:
                pass

            if not isinstance(other, ctypes.Array):
                print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(other)))
                return False
        if len(other) < len(self.expected_string_value) + 1:  # +1 for NULL terminating character
            print("Unexpected length in C string. Expected at least: {}. Received {}".format(len(other), len(self.expected_string_value) + 1))
            return False
        if not isinstance(other[0], bytes):
            print("Unexpected type. Not a string. Received: {}".format(type(other[0])))
            return False
        if other.value.decode("ascii") != self.expected_string_value:
            print("Unexpected value. Expected {}. Received: {}".format(self.expected_string_value, other.value.decode))
            return False
        return True

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, pp.pformat(self.expected_string_value))


# Custom Type


def _compare_ctype_structs(expected, actual):
    # From https://stackoverflow.com/questions/20986330/print-all-fields-of-ctypes-structure-with-introspection
    for field in expected._fields_:
        field_name = field[0]
        expected_val = getattr(expected, field_name)
        actual_val = getattr(actual, field_name)
        if expected_val != actual_val:
            print("Unexpected value field {}. Expected: {}. Received: {}".format(field_name, expected_val, actual_val))
            return False
    return True


class CustomTypeMatcher(object):
    def __init__(self, expected_type, expected_value):
        self.expected_type = expected_type
        self.expected_value = expected_value

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        return _compare_ctype_structs(self.expected_value, actual)

    def __repr__(self):
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_type), pp.pformat(self.expected_value))


class CustomTypeBufferMatcher(object):
    def __init__(self, expected_element_type, expected_value):
        self.expected_value = expected_value
        self.expected_size = len(expected_value)
        self.expected_type = expected_element_type * self.expected_size
        self.expected_element_type = expected_element_type

    def __eq__(self, actual):
        if not isinstance(actual, self.expected_type):
            print("Unexpected array type. Expected: {}. Received: {}".format(self.expected_type, type(actual)))
            return False
        if self.expected_size != len(actual):
            print("Unexpected length. Expected: {}. Received: {}".format(self.expected_size, len(actual)))
            return False
        if self.expected_value is not None:
            # Can't compare the objects directly because they're different types (one is list, another is ctypes array).
            # Go element by element, which allows for reporting the first index where different values were found.
            for a, e in zip(actual, self.expected_value):
                if not isinstance(a, self.expected_element_type):
                    print("Unexpected type. Expected: {}. Received: {}".format(self.expected_element_type, type(a)))
                    return False
                if not _compare_ctype_structs(e, a):
                    return False
        return True

    def __repr__(self):
        expected_val_repr = '[' + ', '.join([x.__repr__() for x in self.expected_value]) + ']'
        return '{}({}, {})'.format(self.__class__.__name__, pp.pformat(self.expected_element_type), expected_val_repr)

    def __str__(self):
        ret_str = self.__repr__() + '\n'
        ret_str += '    expected_type = ' + str(self.expected_type) + '\n'
        ret_str += '    expected_size = ' + str(self.expected_size) + '\n'
        return ret_str


# Scalars


class ViBooleanMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViBoolean, 1 if expected_value is True else 0)


class ViSessionMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViSession, expected_value)


class ViInt16Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt16, expected_value)


class ViInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt32, expected_value)


class ViUInt32Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViUInt32, expected_value)


class ViAttrMatcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViAttr, expected_value)


class ViInt64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViInt64, expected_value)


class ViReal64Matcher(_ScalarMatcher):
    def __init__(self, expected_value):
        _ScalarMatcher.__init__(self, _visatype.ViReal64, expected_value)


# Pointers


class ViBooleanPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViBoolean)


class ViSessionPointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViSession)


class ViInt16PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt16)


class ViInt32PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt32)


class ViInt64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViInt64)


class ViReal64PointerMatcher(_PointerMatcher):
    def __init__(self):
        _PointerMatcher.__init__(self, _visatype.ViReal64)


# Buffers


class ViBooleanBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViBoolean, expected_size_or_value)


class ViCharBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViChar, expected_size_or_value)


class ViInt8BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt8, expected_size_or_value)


class ViInt16BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt16, expected_size_or_value)


class ViInt32BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt32, expected_size_or_value)


class ViInt64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViInt64, expected_size_or_value)


class ViReal64BufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViReal64, expected_size_or_value)


class ViSessionBufferMatcher(_BufferMatcher):
    def __init__(self, expected_size_or_value):
        _BufferMatcher.__init__(self, _visatype.ViSession, expected_size_or_value)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/unit_tests/_mock_helper.py sha256=0f861927f66e0ccd7035456a5bf230f30320b4faeab579295bdb00915fd42961 bytes=6619 -->
## FILE: generated/nimodinst/nimodinst/unit_tests/_mock_helper.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/unit_tests/_mock_helper.py`
- sha256: `0f861927f66e0ccd7035456a5bf230f30320b4faeab579295bdb00915fd42961`
- bytes: 6619

````python
# -*- coding: utf-8 -*-
# This file was generated
import sys  # noqa: F401   - Not all mock_helpers will need this


class MockFunctionCallError(Exception):
    def __init__(self, function, param=None):
        self.function = function
        self.param = param
        msg = "{0} called without setting side_effect".format(self.function)
        if param is not None:
            msg += " or setting the {0} parameter return value".format(self.param)
        super(Exception, self).__init__(msg)


class SideEffectsHelper(object):
    def __init__(self):
        self._defaults = {}
        self._defaults['CloseInstalledDevicesSession'] = {}
        self._defaults['CloseInstalledDevicesSession']['return'] = 0
        self._defaults['GetExtendedErrorInfo'] = {}
        self._defaults['GetExtendedErrorInfo']['return'] = 0
        self._defaults['GetExtendedErrorInfo']['errorInfo'] = None
        self._defaults['GetInstalledDeviceAttributeViInt32'] = {}
        self._defaults['GetInstalledDeviceAttributeViInt32']['return'] = 0
        self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue'] = None
        self._defaults['GetInstalledDeviceAttributeViString'] = {}
        self._defaults['GetInstalledDeviceAttributeViString']['return'] = 0
        self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'] = None
        self._defaults['OpenInstalledDevicesSession'] = {}
        self._defaults['OpenInstalledDevicesSession']['return'] = 0
        self._defaults['OpenInstalledDevicesSession']['handle'] = None
        self._defaults['OpenInstalledDevicesSession']['deviceCount'] = None

    def __getitem__(self, func):
        return self._defaults[func]

    def __setitem__(self, func, val):
        self._defaults[func] = val

    def niModInst_CloseInstalledDevicesSession(self, handle):  # noqa: N802
        if self._defaults['CloseInstalledDevicesSession']['return'] != 0:
            return self._defaults['CloseInstalledDevicesSession']['return']
        return self._defaults['CloseInstalledDevicesSession']['return']

    def niModInst_GetExtendedErrorInfo(self, error_info_buffer_size, error_info):  # noqa: N802
        if self._defaults['GetExtendedErrorInfo']['return'] != 0:
            return self._defaults['GetExtendedErrorInfo']['return']
        # error_info
        if self._defaults['GetExtendedErrorInfo']['errorInfo'] is None:
            raise MockFunctionCallError("niModInst_GetExtendedErrorInfo", param='errorInfo')
        if error_info_buffer_size.value == 0:
            return len(self._defaults['GetExtendedErrorInfo']['errorInfo'])
        error_info.value = self._defaults['GetExtendedErrorInfo']['errorInfo'].encode('ascii')
        return self._defaults['GetExtendedErrorInfo']['return']

    def niModInst_GetInstalledDeviceAttributeViInt32(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        if self._defaults['GetInstalledDeviceAttributeViInt32']['return'] != 0:
            return self._defaults['GetInstalledDeviceAttributeViInt32']['return']
        # attribute_value
        if self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue'] is None:
            raise MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViInt32", param='attributeValue')
        if attribute_value is not None:
            attribute_value.contents.value = self._defaults['GetInstalledDeviceAttributeViInt32']['attributeValue']
        return self._defaults['GetInstalledDeviceAttributeViInt32']['return']

    def niModInst_GetInstalledDeviceAttributeViString(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        if self._defaults['GetInstalledDeviceAttributeViString']['return'] != 0:
            return self._defaults['GetInstalledDeviceAttributeViString']['return']
        # attribute_value
        if self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'] is None:
            raise MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViString", param='attributeValue')
        if attribute_value_buffer_size.value == 0:
            return len(self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'])
        attribute_value.value = self._defaults['GetInstalledDeviceAttributeViString']['attributeValue'].encode('ascii')
        return self._defaults['GetInstalledDeviceAttributeViString']['return']

    def niModInst_OpenInstalledDevicesSession(self, driver, handle, device_count):  # noqa: N802
        if self._defaults['OpenInstalledDevicesSession']['return'] != 0:
            return self._defaults['OpenInstalledDevicesSession']['return']
        # handle
        if self._defaults['OpenInstalledDevicesSession']['handle'] is None:
            raise MockFunctionCallError("niModInst_OpenInstalledDevicesSession", param='handle')
        if handle is not None:
            handle.contents.value = self._defaults['OpenInstalledDevicesSession']['handle']
        # device_count
        if self._defaults['OpenInstalledDevicesSession']['deviceCount'] is None:
            raise MockFunctionCallError("niModInst_OpenInstalledDevicesSession", param='deviceCount')
        if device_count is not None:
            device_count.contents.value = self._defaults['OpenInstalledDevicesSession']['deviceCount']
        return self._defaults['OpenInstalledDevicesSession']['return']

    # Helper function to setup Mock object with default side effects and return values
    def set_side_effects_and_return_values(self, mock_library):
        mock_library.niModInst_CloseInstalledDevicesSession.side_effect = MockFunctionCallError("niModInst_CloseInstalledDevicesSession")
        mock_library.niModInst_CloseInstalledDevicesSession.return_value = 0
        mock_library.niModInst_GetExtendedErrorInfo.side_effect = MockFunctionCallError("niModInst_GetExtendedErrorInfo")
        mock_library.niModInst_GetExtendedErrorInfo.return_value = 0
        mock_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViInt32")
        mock_library.niModInst_GetInstalledDeviceAttributeViInt32.return_value = 0
        mock_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = MockFunctionCallError("niModInst_GetInstalledDeviceAttributeViString")
        mock_library.niModInst_GetInstalledDeviceAttributeViString.return_value = 0
        mock_library.niModInst_OpenInstalledDevicesSession.side_effect = MockFunctionCallError("niModInst_OpenInstalledDevicesSession")
        mock_library.niModInst_OpenInstalledDevicesSession.return_value = 0
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/unit_tests/test_modinst.py sha256=a0715b3738fed5dc867810fcd3c9f4cbef5a7067783cd73769795d82f6063f4c bytes=14928 -->
## FILE: generated/nimodinst/nimodinst/unit_tests/test_modinst.py

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/unit_tests/test_modinst.py`
- sha256: `a0715b3738fed5dc867810fcd3c9f4cbef5a7067783cd73769795d82f6063f4c`
- bytes: 14928

````python
import _matchers
import _mock_helper

import nimodinst
import warnings

from unittest.mock import MagicMock
from unittest.mock import patch

SESSION_NUM_FOR_TEST = 42


class TestSession:
    class PatchedLibrary(nimodinst._library.Library):
        def __init__(self, ctypes_library):
            super().__init__(ctypes_library)

            for f in dir(self):
                if f.startswith("niModInst_") and not f.endswith("_cfunc"):
                    setattr(self, f, MagicMock())

    def setup_method(self, method):
        self.patched_library = self.PatchedLibrary(None)
        self.patched_library_singleton_get = patch('nimodinst._library_interpreter._library_singleton.get', return_value=self.patched_library)
        self.patched_library_singleton_get.start()

        self.side_effects_helper = _mock_helper.SideEffectsHelper()
        self.side_effects_helper.set_side_effects_and_return_values(self.patched_library)
        self.patched_library.niModInst_OpenInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_OpenInstalledDevicesSession
        self.disallow_close = self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect
        self.patched_library.niModInst_CloseInstalledDevicesSession.side_effect = self.side_effects_helper.niModInst_CloseInstalledDevicesSession

        self.side_effects_helper['OpenInstalledDevicesSession']['handle'] = SESSION_NUM_FOR_TEST
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1

        self.iteration_device_looping = 0
        self.num_int_devices_looping = 3
        self.int_vals_device_looping = [123, 456, 789]
        self.num_string_devices_looping = 4
        self.string_vals_device_looping = ["Life", "liberty", "and", "happiness"]

    def teardown_method(self, method):
        self.patched_library_singleton_get.stop()

    # Helper function for mocking multiple devices
    def niModInst_GetInstalledDeviceAttributeViString_looping(self, handle, index, attribute_id, attribute_value_buffer_size, attribute_value):  # noqa: N802
        if attribute_value_buffer_size.value == 0:
            # TODO(marcoskirsch): What about the byte for the NULL character? Issue #526
            return (len(self.string_vals_device_looping[self.iteration_device_looping]))
        bytes_to_copy = self.string_vals_device_looping[self.iteration_device_looping].encode('ascii')
        for i in range(0, len(bytes_to_copy)):
            attribute_value[i] = bytes_to_copy[i]
        self.iteration_device_looping += 1
        return 0

    # Helper function for mocking multiple devices
    def niModInst_GetInstalledDeviceAttributeViInt32_looping(self, handle, index, attribute_id, attribute_value):  # noqa: N802
        attribute_value.contents.value = self.int_vals_device_looping[self.iteration_device_looping]
        self.iteration_device_looping += 1
        return 0

    # API Tests

    def test_open_and_close(self):
        session = nimodinst.Session('')
        self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(_matchers.ViStringMatcher(''), _matchers.ViSessionPointerMatcher(), _matchers.ViInt32PointerMatcher())
        session.close()
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_close(self):
        session = nimodinst.Session('')
        session.close()
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_context_manager(self):
        with nimodinst.Session('') as session:
            assert isinstance(session, nimodinst.Session)
            self.patched_library.niModInst_OpenInstalledDevicesSession.assert_called_once_with(_matchers.ViStringMatcher(''), _matchers.ViSessionPointerMatcher(), _matchers.ViInt32PointerMatcher())
        self.patched_library.niModInst_CloseInstalledDevicesSession.assert_called_once_with(_matchers.ViSessionMatcher(SESSION_NUM_FOR_TEST))

    def test_iterating_for(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 2
        with nimodinst.Session('') as session:
            assert len(session) == 2
            count = 0
            for d in session:
                count += 1
            assert count == len(session)

    def test_iterating_for_empty(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 0
        with nimodinst.Session('') as session:
            assert len(session) == 0
            count = 0
            for d in session:
                count += 1
            assert count == len(session)

    def test_get_extended_error_info(self):
        error_string = 'Error'
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            # Calling the internal function directly, as get_extended_error_info() functions differently than other IVI Dance functions.
            # As a result, it cannot be used directly during error handling.
            result = session._interpreter.get_extended_error_info()
            assert result == error_string

    def test_get_error_description_fails(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = -1
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['return'] = -2
        with nimodinst.Session('') as session:
            try:
                session.devices[0].chassis_number
            except nimodinst.Error as e:
                assert e.code == -1  # we want the original error code from getting the attribute.
                assert e.description == "Failed to retrieve error description."

    def test_get_attribute_session(self):
        val = 123
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = val
        with nimodinst.Session('') as session:
            attr_int = session.devices[0].chassis_number
            assert attr_int == val

    def test_get_attribute_vi_int32_for_loop_index(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.niModInst_GetInstalledDeviceAttributeViInt32_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_int_devices_looping
        index = 0
        with nimodinst.Session('') as session:
            attr_int = session.devices[index].chassis_number
            index += 1
            assert attr_int == self.int_vals_device_looping[self.iteration_device_looping - 1]  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_vi_string_for_loop_index(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.niModInst_GetInstalledDeviceAttributeViString_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_string_devices_looping
        index = 0
        with nimodinst.Session('') as session:
            attr_int = session.devices[index].device_name
            index += 1
            assert attr_int == self.string_vals_device_looping[self.iteration_device_looping - 1]  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_session_no_index(self):
        val = 123
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = val
        with nimodinst.Session('') as session:
            try:
                session.chassis_number
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'chassis_number'"

    def test_get_attribute_vi_int32_for_loop_multiple_devices(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.niModInst_GetInstalledDeviceAttributeViInt32_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_int_devices_looping
        with nimodinst.Session('') as session:
            for d in session:
                attr_int = d.chassis_number
                assert attr_int == self.int_vals_device_looping[self.iteration_device_looping - 1]  # Have to subtract once since it was already incremented in the callback function

    def test_get_attribute_vi_string_for_loop_multiple_devices(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.niModInst_GetInstalledDeviceAttributeViString_looping
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = self.num_string_devices_looping
        with nimodinst.Session('') as session:
            for d in session:
                attr_int = d.device_name
                assert attr_int == self.string_vals_device_looping[self.iteration_device_looping - 1]  # Have to subtract once since it was already incremented in the callback function

    # Error Tests
    def test_cannot_add_properties_to_session_set(self):
        with nimodinst.Session('') as session:
            try:
                session.non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "__setattr__ not supported."

    def test_cannot_add_properties_to_session_get(self):
        with nimodinst.Session('') as session:
            try:
                session.non_existent_property
                assert False
            except AttributeError as e:
                assert str(e) == "'Session' object has no attribute 'non_existent_property'"

    def test_cannot_add_properties_to_device_set(self):
        with nimodinst.Session('') as session:
            try:
                session.devices[0].non_existent_property = 5
                assert False
            except AttributeError as e:
                assert str(e) == "__setattr__ not supported."

    def test_cannot_add_properties_to_device_get(self):
        with nimodinst.Session('') as session:
            try:
                session.devices[0].non_existent_property
                assert False
            except AttributeError as e:
                assert str(e) == "'_Device' object has no attribute 'non_existent_property'"

    def test_vi_int32_attribute_read_only(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            try:
                session.devices[0].chassis_number = 5
                assert False
            except AttributeError as e:
                assert str(e) == "__setattr__ not supported."

    def test_vi_string_attribute_read_only(self):
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 1
        with nimodinst.Session('') as session:
            try:
                session.devices[0].device_name = "Not Possible"
                assert False
            except AttributeError as e:
                assert str(e) == "__setattr__ not supported."

    def test_int_attribute_error(self):
        error_code = -1234
        error_string = 'Error'
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = -1
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = error_code
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            try:
                session.devices[0].chassis_number
                assert False
            except nimodinst.Error as e:
                assert e.code == error_code
                assert e.description == error_string

    def test_int_attribute_warning(self):
        warning_code = 1234
        error_string = 'Error'
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = -1
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['return'] = warning_code
        self.patched_library.niModInst_GetExtendedErrorInfo.side_effect = self.side_effects_helper.niModInst_GetExtendedErrorInfo
        self.side_effects_helper['GetExtendedErrorInfo']['errorInfo'] = error_string
        with nimodinst.Session('') as session:
            with warnings.catch_warnings(record=True) as w:
                session.devices[0].chassis_number
                assert len(w) == 1
                assert issubclass(w[0].category, nimodinst.DriverWarning)
                assert error_string in str(w[0].message)

    def test_repr_and_str(self):
        self.patched_library.niModInst_GetInstalledDeviceAttributeViInt32.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViInt32
        self.patched_library.niModInst_GetInstalledDeviceAttributeViString.side_effect = self.side_effects_helper.niModInst_GetInstalledDeviceAttributeViString
        self.side_effects_helper['OpenInstalledDevicesSession']['deviceCount'] = 2
        self.side_effects_helper['GetInstalledDeviceAttributeViInt32']['attributeValue'] = 42
        self.side_effects_helper['GetInstalledDeviceAttributeViString']['attributeValue'] = 'fourty two'
        with nimodinst.Session('') as session:
            session
            print(session)
            for d in session:
                d
                print(d)


# not a session test per se
def test_diagnostic_information():
    info = nimodinst.print_diagnostic_information()
    assert isinstance(info, dict)
````

<!--NI_OSS_SOURCE repo=nimi-python path=generated/nimodinst/nimodinst/VERSION sha256=5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d bytes=13 -->
## FILE: generated/nimodinst/nimodinst/VERSION

- repository: `ni/nimi-python`
- source_path: `generated/nimodinst/nimodinst/VERSION`
- sha256: `5f2df6d86b73b1668c81b8c2b11cfa05ed74b6c42453c2bd4badfc93a2d47b0d`
- bytes: 13

````text
1.4.10.dev0
````
