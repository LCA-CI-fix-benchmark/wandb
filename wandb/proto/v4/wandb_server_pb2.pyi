"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
import wandb.proto.wandb_base_pb2
import wandb.proto.wandb_internal_pb2
import wandb.proto.wandb_settings_pb2

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class ServerShutdownRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    _INFO_FIELD_NUMBER: builtins.int
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> None: ...

global___ServerShutdownRequest = ServerShutdownRequest

@typing_extensions.final
class ServerShutdownResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerShutdownResponse = ServerShutdownResponse

@typing_extensions.final
class ServerStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    _INFO_FIELD_NUMBER: builtins.int
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> None: ...

global___ServerStatusRequest = ServerStatusRequest

@typing_extensions.final
class ServerStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerStatusResponse = ServerStatusResponse

@typing_extensions.final
class ServerInformInitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SETTINGS_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    @property
    def settings(self) -> wandb.proto.wandb_settings_pb2.Settings: ...
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        settings: wandb.proto.wandb_settings_pb2.Settings | None = ...,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info", "settings", b"settings"]) -> None: ...

global___ServerInformInitRequest = ServerInformInitRequest

@typing_extensions.final
class ServerInformInitResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerInformInitResponse = ServerInformInitResponse

@typing_extensions.final
class ServerInformStartRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SETTINGS_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    @property
    def settings(self) -> wandb.proto.wandb_settings_pb2.Settings: ...
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        settings: wandb.proto.wandb_settings_pb2.Settings | None = ...,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info", "settings", b"settings"]) -> None: ...

global___ServerInformStartRequest = ServerInformStartRequest

@typing_extensions.final
class ServerInformStartResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerInformStartResponse = ServerInformStartResponse

@typing_extensions.final
class ServerInformFinishRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    _INFO_FIELD_NUMBER: builtins.int
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> None: ...

global___ServerInformFinishRequest = ServerInformFinishRequest

@typing_extensions.final
class ServerInformFinishResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerInformFinishResponse = ServerInformFinishResponse

@typing_extensions.final
class ServerInformAttachRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    _INFO_FIELD_NUMBER: builtins.int
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> None: ...

global___ServerInformAttachRequest = ServerInformAttachRequest

@typing_extensions.final
class ServerInformAttachResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SETTINGS_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    @property
    def settings(self) -> wandb.proto.wandb_settings_pb2.Settings: ...
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        settings: wandb.proto.wandb_settings_pb2.Settings | None = ...,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info", "settings", b"settings"]) -> None: ...

global___ServerInformAttachResponse = ServerInformAttachResponse

@typing_extensions.final
class ServerInformDetachRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    _INFO_FIELD_NUMBER: builtins.int
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> None: ...

global___ServerInformDetachRequest = ServerInformDetachRequest

@typing_extensions.final
class ServerInformDetachResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerInformDetachResponse = ServerInformDetachResponse

@typing_extensions.final
class ServerInformTeardownRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    EXIT_CODE_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    exit_code: builtins.int
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        exit_code: builtins.int = ...,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info", "exit_code", b"exit_code"]) -> None: ...

global___ServerInformTeardownRequest = ServerInformTeardownRequest

@typing_extensions.final
class ServerInformTeardownResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerInformTeardownResponse = ServerInformTeardownResponse

@typing_extensions.final
class ServerInformBroadcastRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSCRIPTION_KEY_FIELD_NUMBER: builtins.int
    RECORD_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    subscription_key: builtins.str
    @property
    def record(self) -> wandb.proto.wandb_internal_pb2.Record: ...
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        subscription_key: builtins.str = ...,
        record: wandb.proto.wandb_internal_pb2.Record | None = ...,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info", "record", b"record"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info", "record", b"record", "subscription_key", b"subscription_key"]) -> None: ...

global___ServerInformBroadcastRequest = ServerInformBroadcastRequest

@typing_extensions.final
class ServerInformBroadcastResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerInformBroadcastResponse = ServerInformBroadcastResponse

@typing_extensions.final
class ServerInformSubscribeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSCRIPTION_KEY_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    subscription_key: builtins.str
    run_id: builtins.str
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        subscription_key: builtins.str = ...,
        run_id: builtins.str = ...,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info", "run_id", b"run_id", "subscription_key", b"subscription_key"]) -> None: ...

global___ServerInformSubscribeRequest = ServerInformSubscribeRequest

@typing_extensions.final
class ServerInformSubscribeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerInformSubscribeResponse = ServerInformSubscribeResponse

@typing_extensions.final
class ServerInformUnsubscribeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBSCRIPTION_KEY_FIELD_NUMBER: builtins.int
    RUN_ID_FIELD_NUMBER: builtins.int
    _INFO_FIELD_NUMBER: builtins.int
    subscription_key: builtins.str
    run_id: builtins.str
    @property
    def _info(self) -> wandb.proto.wandb_base_pb2._RecordInfo: ...
    def __init__(
        self,
        *,
        subscription_key: builtins.str = ...,
        run_id: builtins.str = ...,
        _info: wandb.proto.wandb_base_pb2._RecordInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_info", b"_info"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_info", b"_info", "run_id", b"run_id", "subscription_key", b"subscription_key"]) -> None: ...

global___ServerInformUnsubscribeRequest = ServerInformUnsubscribeRequest

@typing_extensions.final
class ServerInformUnsubscribeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___ServerInformUnsubscribeResponse = ServerInformUnsubscribeResponse

@typing_extensions.final
class ServerRequest(google.protobuf.message.Message):
    """
    ServerRequest, ServerResponse: used in sock server
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RECORD_PUBLISH_FIELD_NUMBER: builtins.int
    RECORD_COMMUNICATE_FIELD_NUMBER: builtins.int
    INFORM_INIT_FIELD_NUMBER: builtins.int
    INFORM_FINISH_FIELD_NUMBER: builtins.int
    INFORM_ATTACH_FIELD_NUMBER: builtins.int
    INFORM_DETACH_FIELD_NUMBER: builtins.int
    INFORM_TEARDOWN_FIELD_NUMBER: builtins.int
    INFORM_START_FIELD_NUMBER: builtins.int
    INFORM_BROADCAST_FIELD_NUMBER: builtins.int
    INFORM_SUBSCRIBE_FIELD_NUMBER: builtins.int
    INFORM_UNSUBSCRIBE_FIELD_NUMBER: builtins.int
    @property
    def record_publish(self) -> wandb.proto.wandb_internal_pb2.Record: ...
    @property
    def record_communicate(self) -> wandb.proto.wandb_internal_pb2.Record: ...
    @property
    def inform_init(self) -> global___ServerInformInitRequest: ...
    @property
    def inform_finish(self) -> global___ServerInformFinishRequest: ...
    @property
    def inform_attach(self) -> global___ServerInformAttachRequest: ...
    @property
    def inform_detach(self) -> global___ServerInformDetachRequest: ...
    @property
    def inform_teardown(self) -> global___ServerInformTeardownRequest: ...
    @property
    def inform_start(self) -> global___ServerInformStartRequest: ...
    @property
    def inform_broadcast(self) -> global___ServerInformBroadcastRequest: ...
    @property
    def inform_subscribe(self) -> global___ServerInformSubscribeRequest: ...
    @property
    def inform_unsubscribe(self) -> global___ServerInformUnsubscribeRequest: ...
    def __init__(
        self,
        *,
        record_publish: wandb.proto.wandb_internal_pb2.Record | None = ...,
        record_communicate: wandb.proto.wandb_internal_pb2.Record | None = ...,
        inform_init: global___ServerInformInitRequest | None = ...,
        inform_finish: global___ServerInformFinishRequest | None = ...,
        inform_attach: global___ServerInformAttachRequest | None = ...,
        inform_detach: global___ServerInformDetachRequest | None = ...,
        inform_teardown: global___ServerInformTeardownRequest | None = ...,
        inform_start: global___ServerInformStartRequest | None = ...,
        inform_broadcast: global___ServerInformBroadcastRequest | None = ...,
        inform_subscribe: global___ServerInformSubscribeRequest | None = ...,
        inform_unsubscribe: global___ServerInformUnsubscribeRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["inform_attach", b"inform_attach", "inform_broadcast", b"inform_broadcast", "inform_detach", b"inform_detach", "inform_finish", b"inform_finish", "inform_init", b"inform_init", "inform_start", b"inform_start", "inform_subscribe", b"inform_subscribe", "inform_teardown", b"inform_teardown", "inform_unsubscribe", b"inform_unsubscribe", "record_communicate", b"record_communicate", "record_publish", b"record_publish", "server_request_type", b"server_request_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["inform_attach", b"inform_attach", "inform_broadcast", b"inform_broadcast", "inform_detach", b"inform_detach", "inform_finish", b"inform_finish", "inform_init", b"inform_init", "inform_start", b"inform_start", "inform_subscribe", b"inform_subscribe", "inform_teardown", b"inform_teardown", "inform_unsubscribe", b"inform_unsubscribe", "record_communicate", b"record_communicate", "record_publish", b"record_publish", "server_request_type", b"server_request_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["server_request_type", b"server_request_type"]) -> typing_extensions.Literal["record_publish", "record_communicate", "inform_init", "inform_finish", "inform_attach", "inform_detach", "inform_teardown", "inform_start", "inform_broadcast", "inform_subscribe", "inform_unsubscribe"] | None: ...

global___ServerRequest = ServerRequest

@typing_extensions.final
class ServerResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_COMMUNICATE_FIELD_NUMBER: builtins.int
    INFORM_INIT_RESPONSE_FIELD_NUMBER: builtins.int
    INFORM_FINISH_RESPONSE_FIELD_NUMBER: builtins.int
    INFORM_ATTACH_RESPONSE_FIELD_NUMBER: builtins.int
    INFORM_DETACH_RESPONSE_FIELD_NUMBER: builtins.int
    INFORM_TEARDOWN_RESPONSE_FIELD_NUMBER: builtins.int
    INFORM_START_RESPONSE_FIELD_NUMBER: builtins.int
    INFORM_BROADCAST_RESPONSE_FIELD_NUMBER: builtins.int
    INFORM_SUBSCRIBE_RESPONSE_FIELD_NUMBER: builtins.int
    INFORM_UNSUBSCRIBE_RESPONSE_FIELD_NUMBER: builtins.int
    @property
    def result_communicate(self) -> wandb.proto.wandb_internal_pb2.Result: ...
    @property
    def inform_init_response(self) -> global___ServerInformInitResponse: ...
    @property
    def inform_finish_response(self) -> global___ServerInformFinishResponse: ...
    @property
    def inform_attach_response(self) -> global___ServerInformAttachResponse: ...
    @property
    def inform_detach_response(self) -> global___ServerInformDetachResponse: ...
    @property
    def inform_teardown_response(self) -> global___ServerInformTeardownResponse: ...
    @property
    def inform_start_response(self) -> global___ServerInformStartResponse: ...
    @property
    def inform_broadcast_response(self) -> global___ServerInformBroadcastResponse: ...
    @property
    def inform_subscribe_response(self) -> global___ServerInformSubscribeResponse: ...
    @property
    def inform_unsubscribe_response(self) -> global___ServerInformUnsubscribeResponse: ...
    def __init__(
        self,
        *,
        result_communicate: wandb.proto.wandb_internal_pb2.Result | None = ...,
        inform_init_response: global___ServerInformInitResponse | None = ...,
        inform_finish_response: global___ServerInformFinishResponse | None = ...,
        inform_attach_response: global___ServerInformAttachResponse | None = ...,
        inform_detach_response: global___ServerInformDetachResponse | None = ...,
        inform_teardown_response: global___ServerInformTeardownResponse | None = ...,
        inform_start_response: global___ServerInformStartResponse | None = ...,
        inform_broadcast_response: global___ServerInformBroadcastResponse | None = ...,
        inform_subscribe_response: global___ServerInformSubscribeResponse | None = ...,
        inform_unsubscribe_response: global___ServerInformUnsubscribeResponse | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["inform_attach_response", b"inform_attach_response", "inform_broadcast_response", b"inform_broadcast_response", "inform_detach_response", b"inform_detach_response", "inform_finish_response", b"inform_finish_response", "inform_init_response", b"inform_init_response", "inform_start_response", b"inform_start_response", "inform_subscribe_response", b"inform_subscribe_response", "inform_teardown_response", b"inform_teardown_response", "inform_unsubscribe_response", b"inform_unsubscribe_response", "result_communicate", b"result_communicate", "server_response_type", b"server_response_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["inform_attach_response", b"inform_attach_response", "inform_broadcast_response", b"inform_broadcast_response", "inform_detach_response", b"inform_detach_response", "inform_finish_response", b"inform_finish_response", "inform_init_response", b"inform_init_response", "inform_start_response", b"inform_start_response", "inform_subscribe_response", b"inform_subscribe_response", "inform_teardown_response", b"inform_teardown_response", "inform_unsubscribe_response", b"inform_unsubscribe_response", "result_communicate", b"result_communicate", "server_response_type", b"server_response_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["server_response_type", b"server_response_type"]) -> typing_extensions.Literal["result_communicate", "inform_init_response", "inform_finish_response", "inform_attach_response", "inform_detach_response", "inform_teardown_response", "inform_start_response", "inform_broadcast_response", "inform_subscribe_response", "inform_unsubscribe_response"] | None: ...

global___ServerResponse = ServerResponse
