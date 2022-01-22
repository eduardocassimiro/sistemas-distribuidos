# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import smart_portao_pb2 as smart__portao__pb2


class PortaoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.abrirPortao = channel.unary_unary(
                '/Portao/abrirPortao',
                request_serializer=smart__portao__pb2.PortaoStatus.SerializeToString,
                response_deserializer=smart__portao__pb2.PortaoStatus.FromString,
                )
        self.fecharPortao = channel.unary_unary(
                '/Portao/fecharPortao',
                request_serializer=smart__portao__pb2.PortaoStatus.SerializeToString,
                response_deserializer=smart__portao__pb2.PortaoStatus.FromString,
                )


class PortaoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def abrirPortao(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def fecharPortao(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PortaoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'abrirPortao': grpc.unary_unary_rpc_method_handler(
                    servicer.abrirPortao,
                    request_deserializer=smart__portao__pb2.PortaoStatus.FromString,
                    response_serializer=smart__portao__pb2.PortaoStatus.SerializeToString,
            ),
            'fecharPortao': grpc.unary_unary_rpc_method_handler(
                    servicer.fecharPortao,
                    request_deserializer=smart__portao__pb2.PortaoStatus.FromString,
                    response_serializer=smart__portao__pb2.PortaoStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Portao', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Portao(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def abrirPortao(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Portao/abrirPortao',
            smart__portao__pb2.PortaoStatus.SerializeToString,
            smart__portao__pb2.PortaoStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def fecharPortao(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Portao/fecharPortao',
            smart__portao__pb2.PortaoStatus.SerializeToString,
            smart__portao__pb2.PortaoStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
