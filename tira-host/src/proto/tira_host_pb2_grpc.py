# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import proto.tira_host_pb2 as tira__host__pb2


class TiraHostServiceStub(object):
    """-----------------------------------------------------------------------------
    Definitions
    -----------------------------------------------------------------------------

    The service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.test = channel.unary_unary(
                '/tira.generated.TiraHostService/test',
                request_serializer=tira__host__pb2.Input.SerializeToString,
                response_deserializer=tira__host__pb2.Output.FromString,
                )
        self.vm_backup = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_backup',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_create = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_create',
                request_serializer=tira__host__pb2.RequestVmCreate.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_delete = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_delete',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_info = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_info',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.ResponseVmInfo.FromString,
                )
        self.vm_list = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_list',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_metrics = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_metrics',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_sandbox = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_sandbox',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_shutdown = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_shutdown',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_snapshot = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_snapshot',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_start = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_start',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_stop = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_stop',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.vm_unsandbox = channel.unary_unary(
                '/tira.generated.TiraHostService/vm_unsandbox',
                request_serializer=tira__host__pb2.RequestVmCommands.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.run_execute = channel.unary_unary(
                '/tira.generated.TiraHostService/run_execute',
                request_serializer=tira__host__pb2.RequestRunExecuteEval.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )
        self.run_eval = channel.unary_unary(
                '/tira.generated.TiraHostService/run_eval',
                request_serializer=tira__host__pb2.RequestRunExecuteEval.SerializeToString,
                response_deserializer=tira__host__pb2.Response.FromString,
                )


class TiraHostServiceServicer(object):
    """-----------------------------------------------------------------------------
    Definitions
    -----------------------------------------------------------------------------

    The service definition.
    """

    def test(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_backup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_list(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_metrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_sandbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_shutdown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_snapshot(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_start(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_stop(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vm_unsandbox(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def run_execute(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def run_eval(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TiraHostServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'test': grpc.unary_unary_rpc_method_handler(
                    servicer.test,
                    request_deserializer=tira__host__pb2.Input.FromString,
                    response_serializer=tira__host__pb2.Output.SerializeToString,
            ),
            'vm_backup': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_backup,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_create': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_create,
                    request_deserializer=tira__host__pb2.RequestVmCreate.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_delete': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_delete,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_info': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_info,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.ResponseVmInfo.SerializeToString,
            ),
            'vm_list': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_list,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_metrics': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_metrics,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_sandbox': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_sandbox,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_shutdown': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_shutdown,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_snapshot': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_snapshot,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_start': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_start,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_stop': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_stop,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'vm_unsandbox': grpc.unary_unary_rpc_method_handler(
                    servicer.vm_unsandbox,
                    request_deserializer=tira__host__pb2.RequestVmCommands.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'run_execute': grpc.unary_unary_rpc_method_handler(
                    servicer.run_execute,
                    request_deserializer=tira__host__pb2.RequestRunExecuteEval.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
            'run_eval': grpc.unary_unary_rpc_method_handler(
                    servicer.run_eval,
                    request_deserializer=tira__host__pb2.RequestRunExecuteEval.FromString,
                    response_serializer=tira__host__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'tira.generated.TiraHostService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TiraHostService(object):
    """-----------------------------------------------------------------------------
    Definitions
    -----------------------------------------------------------------------------

    The service definition.
    """

    @staticmethod
    def test(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/test',
            tira__host__pb2.Input.SerializeToString,
            tira__host__pb2.Output.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_backup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_backup',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_create',
            tira__host__pb2.RequestVmCreate.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_delete',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_info',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.ResponseVmInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_list',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_metrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_metrics',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_sandbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_sandbox',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_shutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_shutdown',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_snapshot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_snapshot',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_start(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_start',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_stop(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_stop',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vm_unsandbox(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/vm_unsandbox',
            tira__host__pb2.RequestVmCommands.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def run_execute(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/run_execute',
            tira__host__pb2.RequestRunExecuteEval.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def run_eval(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/tira.generated.TiraHostService/run_eval',
            tira__host__pb2.RequestRunExecuteEval.SerializeToString,
            tira__host__pb2.Response.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
