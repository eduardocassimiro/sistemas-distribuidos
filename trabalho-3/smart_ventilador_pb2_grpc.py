# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import smart_ventilador_pb2 as smart__ventilador__pb2


class VentiladorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ligarVentilador = channel.unary_unary(
                '/Ventilador/ligarVentilador',
                request_serializer=smart__ventilador__pb2.VentiladorStatus.SerializeToString,
                response_deserializer=smart__ventilador__pb2.VentiladorStatus.FromString,
                )
        self.desligarVentilador = channel.unary_unary(
                '/Ventilador/desligarVentilador',
                request_serializer=smart__ventilador__pb2.VentiladorStatus.SerializeToString,
                response_deserializer=smart__ventilador__pb2.VentiladorStatus.FromString,
                )


class VentiladorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ligarVentilador(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def desligarVentilador(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VentiladorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ligarVentilador': grpc.unary_unary_rpc_method_handler(
                    servicer.ligarVentilador,
                    request_deserializer=smart__ventilador__pb2.VentiladorStatus.FromString,
                    response_serializer=smart__ventilador__pb2.VentiladorStatus.SerializeToString,
            ),
            'desligarVentilador': grpc.unary_unary_rpc_method_handler(
                    servicer.desligarVentilador,
                    request_deserializer=smart__ventilador__pb2.VentiladorStatus.FromString,
                    response_serializer=smart__ventilador__pb2.VentiladorStatus.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Ventilador', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Ventilador(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ligarVentilador(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ventilador/ligarVentilador',
            smart__ventilador__pb2.VentiladorStatus.SerializeToString,
            smart__ventilador__pb2.VentiladorStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def desligarVentilador(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Ventilador/desligarVentilador',
            smart__ventilador__pb2.VentiladorStatus.SerializeToString,
            smart__ventilador__pb2.VentiladorStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
